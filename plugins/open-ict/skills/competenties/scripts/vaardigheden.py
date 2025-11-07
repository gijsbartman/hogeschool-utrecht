#!/usr/bin/env python3
"""
Student Skills Query Tool

This module provides a command-line interface for querying student skills
from the Open-ICT competency framework. The framework organizes skills by
skill name and proficiency levels, representing different competencies that
students should develop during their ICT education.

The data structure follows a two-dimensional matrix:
- Skill names (e.g., "Samenwerken", "Kritisch oordelen")
- Proficiency levels (1-4, representing increasing complexity)

Usage:
    python vaardigheden.py [--skill SKILL] [--level LEVEL]

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

# Valid skill names as defined in the Open-ICT framework
# These represent core competencies that ICT students should develop
VALID_SKILLS = [
    "Juiste kennis ontwikkelen",    # Developing appropriate knowledge
    "Kwalitatief product maken",    # Creating quality products
    "Overzicht creëren",            # Creating overview
    "Kritisch oordelen",            # Critical judgment
    "Samenwerken",                  # Collaboration
    "Boodschap delen",              # Sharing messages
    "Plannen",                      # Planning
    "Flexibel opstellen",           # Being flexible
    "Pro-actief handelen",          # Proactive action
    "Reflecteren"                   # Reflection
]

def load_data():
    """
    Load student skills data from the JSON data file.
    
    Reads the vaardigheden-nl.json file containing the complete student skills
    competency framework data. The file is expected to be in the data directory
    relative to this script's location.
    
    Returns:
        dict: Nested dictionary structure containing student skills organized by:
              {skill_name: {level: skill_description}}
    
    Raises:
        SystemExit: If the data file is not found, contains invalid JSON,
                   or cannot be read for any other reason.
    
    Note:
        All errors are written to stderr before exiting with status code 1.
    """
    data_file = DATA_DIR / "vaardigheden-nl.json"
    
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

def filter_skills(data, skill_name=None, level=None):
    """
    Filter student skills based on specified criteria.
    
    Applies one or more filters to the competency framework data to narrow down
    the results. Filters can be combined and are applied in the following order:
    1. Skill name (reduces dataset to single skill)
    2. Level (filters specific proficiency levels within remaining skills)
    
    Args:
        data (dict): Complete competency framework data structure
        skill_name (str, optional): Skill name to filter by (e.g., "Samenwerken")
        level (str, optional): Proficiency level to filter by ("1", "2", "3", or "4")
    
    Returns:
        dict: Filtered data structure maintaining the same nested format as input,
              but containing only entries matching all specified filters
    
    Raises:
        SystemExit: If the specified skill name is not found in the data, or if
                   no skills match the specified filter combination
    
    Note:
        When no filters are specified, returns the complete dataset unchanged.
    """
    result = {}
    
    # First-level filter: narrow down to specific skill if requested
    if skill_name:
        if skill_name not in data:
            print(f"Error: Skill '{skill_name}' not found", file=sys.stderr)
            print(f"Valid skills: {', '.join(VALID_SKILLS)}", file=sys.stderr)
            sys.exit(1)
        # Reduce dataset to only the requested skill
        data = {skill_name: data[skill_name]}
    
    # Second-level filter: apply level filter if specified
    if level:
        # Iterate through all skills in the dataset (may be filtered or complete)
        for skill, levels in data.items():
            # Use dictionary comprehension to filter levels efficiently
            filtered_levels = {lvl: content for lvl, content in levels.items() if lvl == level}
            # Only include skill if it has matching levels
            if filtered_levels:
                result[skill] = filtered_levels
    else:
        # No level filter: include all skills and levels
        result = data
    
    # Validate that at least one skill matches the filter criteria
    if not result:
        print("No skills found with the specified filters", file=sys.stderr)
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
        description="Retrieve student skills from the Open-ICT competency framework.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Valid skills:
  {chr(10).join('  - ' + skill for skill in VALID_SKILLS)}

Examples:
  %(prog)s
  %(prog)s --skill "Samenwerken"
  %(prog)s --skill "Samenwerken" --level 2
  %(prog)s --level 3
        """
    )
    
    # Define command-line arguments
    # All arguments are optional, allowing flexible querying
    parser.add_argument(
        '--skill',
        help='Filter by skill name'
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
    
    # Additional validation: validate skill name against our constants
    # This provides better error messages than relying on filter_skills()
    if args.skill and args.skill not in VALID_SKILLS:
        print(f"Error: Invalid skill: {args.skill}", file=sys.stderr)
        print(f"Valid skills: {', '.join(VALID_SKILLS)}", file=sys.stderr)
        sys.exit(1)
    
    # Execute the main workflow: load data, apply filters, output results
    data = load_data()
    result = filter_skills(data, args.skill, args.level)
    
    # Output filtered results as formatted JSON
    # ensure_ascii=False preserves Dutch characters (e.g., é, ë)
    # indent=2 provides human-readable formatting for debugging
    print(json.dumps(result, ensure_ascii=False, indent=2))

# Entry point: only execute main() when script is run directly (not when imported)
if __name__ == "__main__":
    main()

