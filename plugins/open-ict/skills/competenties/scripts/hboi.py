#!/usr/bin/env python3
"""
HBO-I Professional Tasks Query Tool

This module provides a command-line interface for querying professional tasks
from the Open-ICT competency framework for HBO-I (Higher Professional Education
in Information Technology). The framework organizes tasks by architecture layers,
activities, and proficiency levels.

The data structure follows a three-dimensional matrix:
- Architecture layers (e.g., Software, Infrastructure)
- Activities (e.g., Analyseren, Ontwerpen, Realiseren)
- Proficiency levels (1-4, representing increasing complexity)

Usage:
    python hboi.py [--layer LAYER] [--activity ACTIVITY] [--level LEVEL]

Exit Codes:
    0: Success
    1: Error (invalid input, missing data file, or no results found)
"""

import json
import sys
import argparse
from pathlib import Path

# Directory paths for locating data files relative to script location
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"

# Valid architecture layers as defined in the Open-ICT framework
# These represent different technical domains in ICT systems
VALID_LAYERS = [
    "Gebruikersinteractie",      # User interaction layer
    "Organisatieprocessen",      # Organizational processes layer
    "Infrastructuur",            # Infrastructure layer
    "Software",                  # Software layer
    "Hardwareinterfacing"        # Hardware interfacing layer
]

# Valid professional activities as defined in the Open-ICT framework
# These represent different phases of the development lifecycle
VALID_ACTIVITIES = [
    "Analyseren",                # Analysis phase
    "Adviseren",                 # Advisory phase
    "Ontwerpen",                 # Design phase
    "Realiseren",                # Implementation phase
    "Manage & Control"           # Management and control phase
]

def load_data():
    """
    Load professional tasks data from the JSON data file.
    
    Reads the hboi-nl.json file containing the complete HBO-I competency
    framework data. The file is expected to be in the data directory relative
    to this script's location.
    
    Returns:
        dict: Nested dictionary structure containing professional tasks organized by:
              {layer: {activity: {level: task_description}}}
    
    Raises:
        SystemExit: If the data file is not found, contains invalid JSON,
                   or cannot be read for any other reason.
    
    Note:
        All errors are written to stderr before exiting with status code 1.
    """
    data_file = DATA_DIR / "hboi-nl.json"
    
    # Verify data file exists before attempting to read
    if not data_file.exists():
        print(f"Error: Data file not found: {data_file}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Open with explicit UTF-8 encoding to handle Dutch characters
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        # Provide specific error for malformed JSON
        print(f"Error: Invalid JSON in data file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch-all for other file reading errors (permissions, I/O, etc.)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def filter_tasks(data, layer=None, activity=None, level=None):
    """
    Filter professional tasks based on specified criteria.
    
    Applies one or more filters to the competency framework data to narrow down
    the results. Filters can be combined and are applied in the following order:
    1. Architecture layer (reduces dataset to single layer)
    2. Activity (filters activities within remaining layers)
    3. Level (filters specific proficiency levels within remaining activities)
    
    Args:
        data (dict): Complete competency framework data structure
        layer (str, optional): Architecture layer to filter by (e.g., "Software")
        activity (str, optional): Activity type to filter by (e.g., "Ontwerpen")
        level (str, optional): Proficiency level to filter by ("1", "2", "3", or "4")
    
    Returns:
        dict: Filtered data structure maintaining the same nested format as input,
              but containing only entries matching all specified filters
    
    Raises:
        SystemExit: If the specified layer is not found in the data, or if no
                   tasks match the specified filter combination
    
    Note:
        When no filters are specified, returns the complete dataset unchanged.
    """
    result = {}
    
    # First-level filter: narrow down to specific architecture layer if requested
    if layer:
        if layer not in data:
            print(f"Error: Architecture layer '{layer}' not found", file=sys.stderr)
            print(f"Valid layers: {', '.join(VALID_LAYERS)}", file=sys.stderr)
            sys.exit(1)
        # Reduce dataset to only the requested layer
        data = {layer: data[layer]}
    
    # Second and third level filters: iterate through remaining layers
    # and apply activity and/or level filters
    for layer_name, activities in data.items():
        filtered_activities = {}
        
        for activity_name, levels in activities.items():
            # Skip activities that don't match the activity filter
            if activity and activity_name != activity:
                continue
            
            # Apply level filter if specified
            if level:
                # Use dictionary comprehension to filter levels efficiently
                filtered_levels = {lvl: content for lvl, content in levels.items() if lvl == level}
                # Only include activity if it has matching levels
                if filtered_levels:
                    filtered_activities[activity_name] = filtered_levels
            else:
                # No level filter: include all levels for this activity
                filtered_activities[activity_name] = levels
        
        # Only include layer if it has matching activities after filtering
        if filtered_activities:
            result[layer_name] = filtered_activities
    
    # Validate that at least one task matches the filter criteria
    if not result:
        print("No professional tasks found with the specified filters", file=sys.stderr)
        sys.exit(1)
    
    return result

def main():
    """
    Main entry point for the command-line interface.
    
    Parses command-line arguments, validates user input, loads the competency
    framework data, applies filters, and outputs the results as formatted JSON.
    
    The function handles all user interaction and orchestrates the data loading
    and filtering pipeline. All errors are reported to stderr with helpful
    messages, and the program exits with appropriate status codes.
    
    Returns:
        None: Outputs results to stdout and exits with status code 0 on success,
              or exits with status code 1 on error
    
    Side Effects:
        - Reads from data file system
        - Writes to stdout (JSON results)
        - Writes to stderr (error messages)
        - Calls sys.exit() on errors or successful completion
    """
    # Configure argument parser with detailed help text
    # RawDescriptionHelpFormatter preserves formatting in epilog
    parser = argparse.ArgumentParser(
        description="Retrieve HBO-I professional tasks from the Open-ICT competency framework.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Architecture layers:
  {chr(10).join('  - ' + layer for layer in VALID_LAYERS)}

Activities:
  {chr(10).join('  - ' + activity for activity in VALID_ACTIVITIES)}

Examples:
  %(prog)s
  %(prog)s --layer "Software"
  %(prog)s --activity "Ontwerpen"
  %(prog)s --layer "Software" --activity "Realiseren"
  %(prog)s --layer "Software" --level 2
  %(prog)s --level 3
        """
    )
    
    # Define command-line arguments
    # All arguments are optional, allowing flexible querying
    parser.add_argument(
        '--layer',
        help='Filter by architecture layer'
    )
    
    parser.add_argument(
        '--activity',
        help='Filter by activity'
    )
    
    # Level argument uses choices to restrict valid values at parse time
    parser.add_argument(
        '--level',
        type=str,
        choices=['1', '2', '3', '4'],
        help='Filter by level (1-4)'
    )
    
    # Parse command-line arguments (exits with error message if invalid)
    args = parser.parse_args()
    
    # Additional validation: argparse handles level choices, but we validate
    # layer and activity against our constants to ensure consistency
    # This provides better error messages than relying on filter_tasks()
    if args.layer and args.layer not in VALID_LAYERS:
        print(f"Error: Invalid architecture layer: {args.layer}", file=sys.stderr)
        print(f"Valid layers: {', '.join(VALID_LAYERS)}", file=sys.stderr)
        sys.exit(1)
    
    if args.activity and args.activity not in VALID_ACTIVITIES:
        print(f"Error: Invalid activity: {args.activity}", file=sys.stderr)
        print(f"Valid activities: {', '.join(VALID_ACTIVITIES)}", file=sys.stderr)
        sys.exit(1)
    
    # Execute the main workflow: load data, apply filters, output results
    data = load_data()
    result = filter_tasks(data, args.layer, args.activity, args.level)
    
    # Output filtered results as formatted JSON
    # ensure_ascii=False preserves Dutch characters (e.g., é, ë)
    # indent=2 provides human-readable formatting for debugging
    print(json.dumps(result, ensure_ascii=False, indent=2))

# Entry point: only execute main() when script is run directly (not when imported)
if __name__ == "__main__":
    main()

