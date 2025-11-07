# Studentvaardigheden

## Overview

Deze sectie beschrijft hoe je studentvaardigheden uit het Open-ICT competentiekader kunt ophalen. Het framework bevat tien kernvaardigheden die worden beoordeeld in het Open-ICT curriculum, elk met vier niveaus die oplopende complexiteit en zelfstandigheid representeren.

## Beschikbare Vaardigheden

De volgende tien vaardigheden zijn beschikbaar:

1. **Juiste kennis ontwikkelen**: Het vermogen om relevante kennis te identificeren, te verwerven en toe te passen
2. **Kwalitatief product maken**: Het vermogen om producten te maken die voldoen aan kwaliteitscriteria
3. **Overzicht creëren**: Het vermogen om informatie te verzamelen en overzichtelijk weer te geven
4. **Kritisch oordelen**: Het vermogen om verkregen informatie te verwerken en onderbouwde conclusies te trekken
5. **Samenwerken**: Het vermogen om effectief samen te werken in teams
6. **Boodschap delen**: Het vermogen om informatie en ideeën duidelijk te communiceren
7. **Plannen**: Het vermogen om activiteiten te plannen en te organiseren
8. **Flexibel opstellen**: Het vermogen om flexibel te reageren op veranderende omstandigheden
9. **Pro-actief handelen**: Het vermogen om proactief te handelen en initiatief te nemen
10. **Reflecteren**: Het vermogen om te reflecteren op eigen handelen en leerproces

## Workflow Scenarios

### Scenario 1: Overzicht en Onderzoek (VERPLICHT: Alle Vaardigheden Ophalen)

**Wanneer te gebruiken:**

- Wanneer het nog niet duidelijk is aan welke vaardigheid er wordt gewerkt
- Wanneer de gebruiker wilt weten welke vaardigheden relevant zijn voor een bepaald bewijsstuk
- Wanneer je een overzicht nodig hebt van alle beschikbare vaardigheden en hun niveaus
- Bij het analyseren van bewijsstukken om te bepalen welke vaardigheden van toepassing zijn

**VERPLICHTE WORKFLOW:**

1. **VOER UIT**: `python scripts/vaardigheden.py` (zonder enige argumenten of filters)
2. **GEBRUIK ALLEEN**: De data die wordt gereturned door het script
3. **VERBODEN**: Het is **NIET TOEGESTAAN** om zelf criteria voor vaardigheden in te vullen of te verzinnen
4. **VERBODEN**: Het is **NIET TOEGESTAAN** om alleen een subset van vaardigheden op te halen in dit scenario
5. **ANALYSEER**: Gebruik de volledige dataset om te bepalen welke vaardigheden relevant zijn

**Voorbeeld gebruik:**

```bash
python scripts/vaardigheden.py
```

**Resultaat**: JSON object met alle tien vaardigheden, elk met alle vier niveaus (1-4). Gebruik deze volledige dataset om te analyseren welke vaardigheden relevant zijn.

### Scenario 2: Specifieke Vaardigheid Bekend

**Wanneer te gebruiken:**

- Wanneer er al duidelijk is aan welke specifieke vaardigheid wordt gewerkt
- Wanneer de gebruiker expliciet vraagt naar een specifieke vaardigheid
- Wanneer je alleen informatie nodig hebt over één of meerdere specifieke vaardigheden

**WORKFLOW:**

#### 2a. Één Specifieke Vaardigheid

**Wanneer**: Er is één specifieke vaardigheid bekend

**VOER UIT**:

```bash
python scripts/vaardigheden.py --skill "Vaardigheidsnaam"
```

**BELANGRIJK**:

- Gebruik de exacte vaardigheidsnaam zoals vermeld in de lijst hierboven
- Voeg **GEEN** `--level` filter toe tenzij expliciet gevraagd naar een specifiek niveau
- Haal alle niveaus op voor de vaardigheid, tenzij expliciet anders gevraagd

**Voorbeeld:**

```bash
python scripts/vaardigheden.py --skill "Samenwerken"
```

**Resultaat**: JSON object met alleen de "Samenwerken" vaardigheid, inclusief alle vier niveaus.

#### 2b. Meerdere Specifieke Vaardigheden

**Wanneer**: Er zijn meerdere specifieke vaardigheden bekend

**VERPLICHTE WORKFLOW:**

1. **VOER MEERDERE REQUESTS UIT**: Maak voor elke vaardigheid een aparte request naar het Python script
2. **GEEN COMBINATIE**: Je kunt niet meerdere vaardigheden in één request ophalen
3. **VOOR ELKE VAARDIGHEID**: Voer `python scripts/vaardigheden.py --skill "Vaardigheidsnaam"` uit

**Voorbeeld bij 3 vaardigheden:**

```bash
python scripts/vaardigheden.py --skill "Samenwerken"
python scripts/vaardigheden.py --skill "Kritisch oordelen"
python scripts/vaardigheden.py --skill "Reflecteren"
```

**Resultaat**: Drie aparte JSON objecten, één voor elke vaardigheid met alle vier niveaus.

#### 2c. Specifiek Niveau (Alleen Wanneer Expliciet Gevraagd)

**Wanneer**: De gebruiker vraagt expliciet naar een specifiek niveau (bijv. "niveau 2", "level 3")

**VERPLICHTE WORKFLOW:**

1. **GEBRUIK `--level` FILTER**: Voeg `--level` toe aan de command alleen wanneer expliciet gevraagd
2. **COMBINEER MET `--skill`**: Als er ook een specifieke vaardigheid bekend is, combineer beide filters
3. **GEEN NIVEAU FILTER**: Als er geen specifiek niveau wordt genoemd, haal alle niveaus op

**Voorbeelden:**

```bash
# Specifieke vaardigheid op specifiek niveau (expliciet gevraagd)
python scripts/vaardigheden.py --skill "Reflecteren" --level 3

# Alle vaardigheden op specifiek niveau (expliciet gevraagd)
python scripts/vaardigheden.py --level 2

# Specifieke vaardigheid zonder niveau (geen niveau genoemd)
python scripts/vaardigheden.py --skill "Samenwerken"
```

## Kritieke Regels

### VERPLICHT: Gebruik Alleen Gereturned Data

**KRITIEK**: Je MOET alleen de data gebruiken die wordt gereturned door het Python script.

**VERBODEN:**

- ❌ Het verzinnen of invullen van criteria voor vaardigheden
- ❌ Het gebruik van kennis over vaardigheden die niet in de gereturned data staat
- ❌ Het aannemen van wat een vaardigheid zou moeten zijn zonder de data te raadplegen

**VERPLICHT:**

- ✅ Gebruik alleen de `title` en `info` velden uit de gereturned JSON
- ✅ Baseer alle analyses en conclusies op de daadwerkelijke data
- ✅ Raadpleeg altijd de volledige dataset wanneer onzekerheid bestaat

### VERPLICHT: Scenario 1 bij Onzekerheid

**KRITIEK**: Wanneer het niet duidelijk is welke vaardigheid relevant is, MOET je Scenario 1 gebruiken (alle vaardigheden ophalen).

**VERBODEN:**

- ❌ Het gissen naar welke vaardigheid relevant zou kunnen zijn
- ❌ Het ophalen van alleen een subset van vaardigheden "omdat je denkt dat die relevant zijn"
- ❌ Het overslaan van het ophalen van alle data bij onzekerheid

**VERPLICHT:**

- ✅ Bij twijfel: gebruik altijd Scenario 1
- ✅ Haal alle vaardigheden op wanneer je moet bepalen welke relevant zijn
- ✅ Analyseer de volledige dataset om te bepalen welke vaardigheden van toepassing zijn

### VERPLICHT: Meerdere Requests voor Meerdere Vaardigheden

**KRITIEK**: Wanneer je meerdere specifieke vaardigheden nodig hebt, maak je meerdere aparte requests.

**VERBODEN:**

- ❌ Het proberen om meerdere vaardigheden in één request te combineren
- ❌ Het ophalen van alle vaardigheden wanneer je alleen specifieke nodig hebt (tenzij Scenario 1 van toepassing is)

**VERPLICHT:**

- ✅ Maak voor elke vaardigheid een aparte request
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
- ✅ Haal standaard alle niveaus op voor de geselecteerde vaardigheid(en)
- ✅ Laat de gebruiker alle niveaus zien tenzij specifiek anders gevraagd

## Script Gebruik

### Basis Commando

Het Python script `scripts/vaardigheden.py` wordt gebruikt om vaardigheden op te halen:

```bash
python scripts/vaardigheden.py [--skill SKILL] [--level LEVEL]
```

### Argumenten en Opties

- `--skill SKILL`: De naam van een specifieke vaardigheid om op te halen

  - Als niet opgegeven: haalt alle vaardigheden op (Scenario 1)
  - Moet exact overeenkomen met een van de tien geldige vaardigheidsnamen
  - Hoofdlettergevoelig

- `--level LEVEL`: Filter op specifiek niveau (1, 2, 3, of 4)

  - **ALLEEN gebruiken wanneer expliciet gevraagd naar een specifiek niveau**
  - Optioneel: kan gecombineerd worden met `--skill`
  - Als niet opgegeven: haalt alle niveaus op voor de geselecteerde vaardigheid(en)

- `-h` of `--help`: Toont gebruiksinformatie en sluit af

### Response Formaat

**Scenario 1 - Alle vaardigheden (zonder argumenten):**

```json
{
  "Juiste kennis ontwikkelen": {
    "1": {
      "title": "Student bepaalt welke kennis..."
    },
    "2": {
      "title": "niveau 1 + \n\nStudent kijkt naar gangbare..."
    },
    "3": {
      "title": "niveau 2 + \n\nStudent kijkt zelfstandig..."
    },
    "4": {
      "title": "niveau 3 + \n\nStudent laat zien..."
    }
  },
  "Kwalitatief product maken": {
    "1": { "title": "..." },
    "2": { "title": "..." },
    "3": { "title": "..." },
    "4": { "title": "..." }
  },
  ...
}
```

**Scenario 2a - Specifieke vaardigheid (zonder niveau filter):**

```json
{
  "Samenwerken": {
    "1": { "title": "..." },
    "2": { "title": "..." },
    "3": { "title": "..." },
    "4": { "title": "..." }
  }
}
```

**Scenario 2c - Specifieke vaardigheid op specifiek niveau:**

```json
{
  "Reflecteren": {
    "3": {
      "title": "..."
    }
  }
}
```

Sommige niveaus kunnen ook een `info` veld bevatten met aanvullende informatie, links naar bronnen, of voorbeelden.

## Validatie en Foutafhandeling

### Validatie

Het script valideert automatisch:

1. **Vaardigheidsnaam**: Controleert of de opgegeven naam exact overeenkomt met een van de tien geldige vaardigheden
2. **Niveau**: Controleert of het niveau een geldige waarde is (1, 2, 3, of 4)
3. **Data bestand**: Controleert of het benodigde JSON bestand bestaat

### Foutmeldingen

**Ongeldige vaardigheidsnaam:**

```
Error: Invalid skill: Ongeldige naam
Valid skills: Juiste kennis ontwikkelen, Kwalitatief product maken, ...
```

**Ongeldig niveau:**

```
Error: Invalid level: 5 (must be 1-4)
```

**Ontbrekend data bestand:**

```
Error: Data file not found: /path/to/vaardigheden-nl.json
```

**Geen resultaten:**

```
No skills found with the specified filters
```

Alle foutmeldingen worden naar stderr geschreven. Het script eindigt met exit code 1 bij fouten.

## Exit Codes

- `0`: Succesvol uitgevoerd
- `1`: Fout opgetreden (ongeldige input, ontbrekend bestand, geen resultaten)

## Best Practices Samenvatting

1. **Bij onzekerheid**: Gebruik altijd Scenario 1 (alle vaardigheden ophalen)
2. **Gebruik alleen gereturned data**: Verzin geen criteria, gebruik alleen wat het script retourneert
3. **Meerdere vaardigheden**: Maak meerdere aparte requests
4. **Niveau filter**: Alleen gebruiken wanneer expliciet gevraagd
5. **Exacte namen**: Vaardigheidsnamen zijn hoofdlettergevoelig en moeten exact overeenkomen
6. **Alle niveaus**: Haal standaard alle niveaus op tenzij expliciet anders gevraagd
