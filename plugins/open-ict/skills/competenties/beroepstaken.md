# HBO-I Beroepstaken

## Overview

Deze sectie beschrijft hoe je HBO-I beroepstaken uit het Open-ICT competentiekader kunt ophalen. Het framework organiseert professionele taken in een drie-dimensionale matrix van architectuurlagen, activiteiten en niveaus.

## Data Structuur

Het HBO-I competentiekader organiseert professionele taken volgens:

- **Architectuurlagen**: Verschillende technische domeinen in ICT systemen
- **Activiteiten**: Verschillende fasen van de ontwikkelingslevenscyclus
- **Niveaus**: Oplopende complexiteit en zelfstandigheid (1-4)

## Beschikbare Architectuurlagen

De volgende vijf architectuurlagen zijn beschikbaar:

1. **Gebruikersinteractie**: User interaction layer
2. **Organisatieprocessen**: Organizational processes layer
3. **Infrastructuur**: Infrastructure layer
4. **Software**: Software layer
5. **Hardwareinterfacing**: Hardware interfacing layer

## Beschikbare Activiteiten

De volgende vijf activiteiten zijn beschikbaar:

1. **Analyseren**: Analysis phase
2. **Adviseren**: Advisory phase
3. **Ontwerpen**: Design phase
4. **Realiseren**: Implementation phase
5. **Manage & Control**: Management and control phase

## Beschikbare Niveaus

Alle beroepstaken hebben vier niveaus (1-4) die oplopende complexiteit en zelfstandigheid representeren.

## Workflow Scenarios

### Scenario 1: Overzicht en Onderzoek (VERPLICHT: Alle Beroepstaken Ophalen)

**Wanneer te gebruiken:**

- Wanneer het nog niet duidelijk is aan welke beroepstaak er wordt gewerkt
- Wanneer de gebruiker wilt weten welke beroepstaken relevant zijn voor een bepaald bewijsstuk
- Wanneer je een overzicht nodig hebt van alle beschikbare beroepstaken en hun niveaus
- Bij het analyseren van bewijsstukken om te bepalen welke beroepstaken van toepassing zijn
- Wanneer je moet bepalen welke architectuurlagen of activiteiten relevant zijn

**VERPLICHTE WORKFLOW:**

1. **VOER UIT**: `python scripts/hboi.py` (zonder enige argumenten of filters)
2. **GEBRUIK ALLEEN**: De data die wordt gereturned door het script
3. **VERBODEN**: Het is **NIET TOEGESTAAN** om zelf criteria voor beroepstaken in te vullen of te verzinnen
4. **VERBODEN**: Het is **NIET TOEGESTAAN** om alleen een subset van beroepstaken op te halen in dit scenario
5. **ANALYSEER**: Gebruik de volledige dataset om te bepalen welke beroepstaken relevant zijn

**Voorbeeld gebruik:**

```bash
python scripts/hboi.py
```

**Resultaat**: JSON object met alle vijf architectuurlagen, elk met alle vijf activiteiten, elk met alle vier niveaus. Gebruik deze volledige dataset om te analyseren welke beroepstaken relevant zijn.

### Scenario 2: Specifieke Beroepstaak Bekend

**Wanneer te gebruiken:**

- Wanneer er al duidelijk is aan welke specifieke architectuurlaag en/of activiteit wordt gewerkt
- Wanneer de gebruiker expliciet vraagt naar een specifieke architectuurlaag of activiteit
- Wanneer je alleen informatie nodig hebt over één of meerdere specifieke beroepstaken

**WORKFLOW:**

#### 2a. Één Specifieke Combinatie (Laag + Activiteit)

**Wanneer**: Er is één specifieke architectuurlaag EN één specifieke activiteit bekend

**VOER UIT**:

```bash
python scripts/hboi.py --layer "Architectuurlaag" --activity "Activiteit"
```

**BELANGRIJK**:

- Gebruik de exacte namen zoals vermeld in de lijsten hierboven
- Voeg **GEEN** `--level` filter toe tenzij expliciet gevraagd naar een specifiek niveau
- Haal alle niveaus op voor de combinatie, tenzij expliciet anders gevraagd

**Voorbeeld:**

```bash
python scripts/hboi.py --layer "Software" --activity "Realiseren"
```

**Resultaat**: JSON object met alleen de "Software" laag en "Realiseren" activiteit, inclusief alle vier niveaus.

#### 2b. Één Specifieke Architectuurlaag

**Wanneer**: Er is één specifieke architectuurlaag bekend, maar geen specifieke activiteit

**VOER UIT**:

```bash
python scripts/hboi.py --layer "Architectuurlaag"
```

**BELANGRIJK**:

- Haal alle activiteiten op voor deze laag
- Voeg **GEEN** `--level` filter toe tenzij expliciet gevraagd

**Voorbeeld:**

```bash
python scripts/hboi.py --layer "Software"
```

**Resultaat**: JSON object met alleen de "Software" laag, inclusief alle vijf activiteiten en alle vier niveaus.

#### 2c. Één Specifieke Activiteit

**Wanneer**: Er is één specifieke activiteit bekend, maar geen specifieke architectuurlaag

**VOER UIT**:

```bash
python scripts/hboi.py --activity "Activiteit"
```

**BELANGRIJK**:

- Haal alle architectuurlagen op voor deze activiteit
- Voeg **GEEN** `--level` filter toe tenzij expliciet gevraagd

**Voorbeeld:**

```bash
python scripts/hboi.py --activity "Ontwerpen"
```

**Resultaat**: JSON object met alle vijf architectuurlagen, maar alleen de "Ontwerpen" activiteit voor elke laag, inclusief alle vier niveaus.

#### 2d. Meerdere Specifieke Combinaties

**Wanneer**: Er zijn meerdere specifieke combinaties van architectuurlagen en/of activiteiten bekend

**VERPLICHTE WORKFLOW:**

1. **VOER MEERDERE REQUESTS UIT**: Maak voor elke combinatie een aparte request naar het Python script
2. **GEEN COMBINATIE**: Je kunt niet meerdere combinaties in één request ophalen
3. **VOOR ELKE COMBINATIE**: Voer het juiste commando uit op basis van wat bekend is

**Voorbeelden:**

**Twee specifieke lagen:**

```bash
python scripts/hboi.py --layer "Software"
python scripts/hboi.py --layer "Infrastructuur"
```

**Twee specifieke activiteiten:**

```bash
python scripts/hboi.py --activity "Ontwerpen"
python scripts/hboi.py --activity "Realiseren"
```

**Twee specifieke combinaties:**

```bash
python scripts/hboi.py --layer "Software" --activity "Realiseren"
python scripts/hboi.py --layer "Gebruikersinteractie" --activity "Ontwerpen"
```

**Resultaat**: Meerdere aparte JSON objecten, één voor elke combinatie met alle relevante niveaus.

#### 2e. Specifiek Niveau (Alleen Wanneer Expliciet Gevraagd)

**Wanneer**: De gebruiker vraagt expliciet naar een specifiek niveau (bijv. "niveau 2", "level 3")

**VERPLICHTE WORKFLOW:**

1. **GEBRUIK `--level` FILTER**: Voeg `--level` toe aan de command alleen wanneer expliciet gevraagd
2. **COMBINEER MET ANDERE FILTERS**: Als er ook een specifieke laag en/of activiteit bekend is, combineer de filters
3. **GEEN NIVEAU FILTER**: Als er geen specifiek niveau wordt genoemd, haal alle niveaus op

**Voorbeelden:**

```bash
# Specifieke combinatie op specifiek niveau (expliciet gevraagd)
python scripts/hboi.py --layer "Software" --activity "Realiseren" --level 2

# Specifieke laag op specifiek niveau (expliciet gevraagd)
python scripts/hboi.py --layer "Software" --level 3

# Specifieke activiteit op specifiek niveau (expliciet gevraagd)
python scripts/hboi.py --activity "Ontwerpen" --level 4

# Alle beroepstaken op specifiek niveau (expliciet gevraagd)
python scripts/hboi.py --level 2

# Specifieke combinatie zonder niveau (geen niveau genoemd)
python scripts/hboi.py --layer "Software" --activity "Realiseren"
```

## Kritieke Regels

### VERPLICHT: Gebruik Alleen Gereturned Data

**KRITIEK**: Je MOET alleen de data gebruiken die wordt gereturned door het Python script.

**VERBODEN:**

- ❌ Het verzinnen of invullen van criteria voor beroepstaken
- ❌ Het gebruik van kennis over beroepstaken die niet in de gereturned data staat
- ❌ Het aannemen van wat een beroepstaak zou moeten zijn zonder de data te raadplegen

**VERPLICHT:**

- ✅ Gebruik alleen de `title` velden uit de gereturned JSON
- ✅ Baseer alle analyses en conclusies op de daadwerkelijke data
- ✅ Raadpleeg altijd de volledige dataset wanneer onzekerheid bestaat

### VERPLICHT: Scenario 1 bij Onzekerheid

**KRITIEK**: Wanneer het niet duidelijk is welke beroepstaak relevant is, MOET je Scenario 1 gebruiken (alle beroepstaken ophalen).

**VERBODEN:**

- ❌ Het gissen naar welke beroepstaak relevant zou kunnen zijn
- ❌ Het ophalen van alleen een subset van beroepstaken "omdat je denkt dat die relevant zijn"
- ❌ Het overslaan van het ophalen van alle data bij onzekerheid

**VERPLICHT:**

- ✅ Bij twijfel: gebruik altijd Scenario 1
- ✅ Haal alle beroepstaken op wanneer je moet bepalen welke relevant zijn
- ✅ Analyseer de volledige dataset om te bepalen welke beroepstaken van toepassing zijn

### VERPLICHT: Meerdere Requests voor Meerdere Combinaties

**KRITIEK**: Wanneer je meerdere specifieke combinaties nodig hebt, maak je meerdere aparte requests.

**VERBODEN:**

- ❌ Het proberen om meerdere combinaties in één request te combineren
- ❌ Het ophalen van alle beroepstaken wanneer je alleen specifieke nodig hebt (tenzij Scenario 1 van toepassing is)

**VERPLICHT:**

- ✅ Maak voor elke combinatie een aparte request
- ✅ Voer elk script commando apart uit
- ✅ Verwerk de resultaten van elke request afzonderlijk

### VERPLICHT: Niveau Filter Alleen bij Expliciete Vraag

**KRITIEK**: Gebruik de `--level` filter alleen wanneer de gebruiker expliciet vraagt naar een specifiek niveau.

**VERBODEN:**

- ❌ Het toevoegen van `--level` "omdat je denkt dat het handig is"
- ❌ Het filteren op niveau zonder expliciete vraag van de gebruiker
- ❌ Het aannemen van een niveau zonder dat dit wordt genoemd

**VERPLICHT:**

- ✅ Gebruik `--level` alleen wanneer expliciet gevraagd (bijv. "niveau 2", "level 3", "op niveau 4")
- ✅ Haal standaard alle niveaus op voor de geselecteerde combinatie(s)
- ✅ Laat de gebruiker alle niveaus zien tenzij specifiek anders gevraagd

## Script Gebruik

### Basis Commando

Het Python script `scripts/hboi.py` wordt gebruikt om beroepstaken op te halen:

```bash
python scripts/hboi.py [--layer LAYER] [--activity ACTIVITY] [--level LEVEL]
```

### Opties

Alle opties zijn optioneel en kunnen gecombineerd worden:

- `--layer LAYER`: Filter op architectuurlaag

  - Als niet opgegeven: haalt alle lagen op
  - Moet exact overeenkomen met een van de vijf geldige lagen
  - Hoofdlettergevoelig

- `--activity ACTIVITY`: Filter op activiteit

  - Als niet opgegeven: haalt alle activiteiten op
  - Moet exact overeenkomen met een van de vijf geldige activiteiten
  - Hoofdlettergevoelig

- `--level LEVEL`: Filter op niveau (1, 2, 3, of 4)

  - **ALLEEN gebruiken wanneer expliciet gevraagd naar een specifiek niveau**
  - Als niet opgegeven: haalt alle niveaus op

- `-h` of `--help`: Toont gebruiksinformatie en sluit af

### Response Formaat

**Scenario 1 - Alle beroepstaken (zonder filters):**

```json
{
  "Gebruikersinteractie": {
    "Analyseren": {
      "1": { "title": "Identificeren van de kernelementen..." },
      "2": { "title": "Benchmarken van functionaliteit..." },
      "3": { "title": "Analyseren van de eindgebruiker..." },
      "4": { "title": "Analyseren van maatschappelijke..." }
    },
    "Adviseren": {
      "1": { "title": "..." },
      "2": { "title": "..." },
      "3": { "title": "..." },
      "4": { "title": "..." }
    },
    ...
  },
  "Organisatieprocessen": {
    ...
  },
  ...
}
```

**Scenario 2a - Specifieke combinatie (zonder niveau filter):**

```json
{
  "Software": {
    "Realiseren": {
      "1": { "title": "..." },
      "2": { "title": "..." },
      "3": { "title": "..." },
      "4": { "title": "..." }
    }
  }
}
```

**Scenario 2b - Specifieke laag (zonder niveau filter):**

```json
{
  "Software": {
    "Analyseren": {
      "1": { "title": "..." },
      "2": { "title": "..." },
      "3": { "title": "..." },
      "4": { "title": "..." }
    },
    "Adviseren": {
      "1": { "title": "..." },
      ...
    },
    ...
  }
}
```

**Scenario 2e - Specifieke combinatie op specifiek niveau:**

```json
{
  "Software": {
    "Realiseren": {
      "3": {
        "title": "..."
      }
    }
  }
}
```

## Filter Logica

Filters worden in de volgende volgorde toegepast:

1. **Architectuurlaag filter**: Reduceert de dataset tot alleen de opgegeven laag
2. **Activiteit filter**: Filtert activiteiten binnen de overgebleven lagen
3. **Niveau filter**: Filtert niveaus binnen de overgebleven activiteiten

Filters zijn **additief**: alle opgegeven filters moeten worden voldaan voor een entry om in het resultaat te verschijnen.

## Validatie en Foutafhandeling

### Validatie

Het script valideert automatisch:

1. **Architectuurlaag**: Controleert of de opgegeven laag exact overeenkomt met een van de vijf geldige lagen
2. **Activiteit**: Controleert of de activiteit exact overeenkomt met een van de vijf geldige activiteiten
3. **Niveau**: Controleert of het niveau een geldige waarde is (1, 2, 3, of 4)
4. **Data bestand**: Controleert of het benodigde JSON bestand bestaat

### Foutmeldingen

**Ongeldige architectuurlaag:**

```
Error: Invalid architecture layer: Ongeldige Laag
Valid options: Gebruikersinteractie, Organisatieprocessen, Infrastructuur, Software, Hardwareinterfacing
```

**Ongeldige activiteit:**

```
Error: Invalid activity: Ongeldige Activiteit
Valid options: Analyseren, Adviseren, Ontwerpen, Realiseren, Manage & Control
```

**Ongeldig niveau:**

```
Error: Invalid level: 5 (must be 1-4)
```

**Ontbrekend data bestand:**

```
Error: Data file not found: /path/to/hboi-nl.json
```

**Geen resultaten:**

```
No professional tasks found with the specified filters
```

Alle foutmeldingen worden naar stderr geschreven. Het script eindigt met exit code 1 bij fouten.

## Exit Codes

- `0`: Succesvol uitgevoerd
- `1`: Fout opgetreden (ongeldige input, ontbrekend bestand, geen resultaten)

## Best Practices Samenvatting

1. **Bij onzekerheid**: Gebruik altijd Scenario 1 (alle beroepstaken ophalen)
2. **Gebruik alleen gereturned data**: Verzin geen criteria, gebruik alleen wat het script retourneert
3. **Meerdere combinaties**: Maak meerdere aparte requests
4. **Niveau filter**: Alleen gebruiken wanneer expliciet gevraagd
5. **Exacte namen**: Laag- en activiteitsnamen zijn hoofdlettergevoelig en moeten exact overeenkomen
6. **Alle niveaus**: Haal standaard alle niveaus op tenzij expliciet anders gevraagd
7. **Specifieke combinaties**: Gebruik `--layer` en `--activity` samen wanneer beide bekend zijn
