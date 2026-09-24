# Leistungspreis der aFRR im Herbst 2025

Eigene Auswertung vom 24.09.2026 zur Frage, warum der Leistungspreis der
positiven aFRR im September und Oktober 2025 beim Doppelten des übrigen
Jahres liegt, und warum der Leistungspreis der negativen aFRR von Februar
bis Mai steigt. Die Fragen sind in `ANFRAGE_AFRR_HERBST_2025.md` gestellt.

## Quellen

- regelleistung.net, Ergebnisübersicht des Leistungsmarkts (RESULT OVERVIEW
  CAPACITY MARKET aFRR), Jahresdateien 2024, 2025 und 2026 aus dem
  Datenbestand des Optimierungsmodells,
  `data/Regelleistung_regelleistung.net/aFRR_Leistung`. Eintrag
  `regelleistung_ausschreibungsdaten_2026`.
- regelleistung.net, Ergebnisübersicht des Arbeitsmarkts (RESULT OVERVIEW
  ENERGY MARKET aFRR), Jahresdateien 2024 und 2025, derselbe Eintrag.
- energy-charts.de, Viertelstundenreihen 2024 und 2025 mit Last, erneuerbarer
  und nicht erneuerbarer Erzeugung, Intradaypreis und Gaspreis,
  `data/Strompreise_energy-charts.de`. Eintrag `energy_charts_strompreise_2026`.

Die Jahresdatei 2025 enthält 4380 Zeitscheiben, nämlich 365 Tage mal sechs
Vier-Stunden-Produkte mal zwei Richtungen. Ausgewertet ist die Spalte
`GERMANY_AVERAGE_CAPACITY_PRICE`, dazu `GERMANY_MARGINAL_CAPACITY_PRICE`,
`GERMANY_SUM_OF_OFFERED_CAPACITY`, `GERMANY_ALLOCATED_VOLUME` und
`GERMANY_IMPORT(-)_EXPORT(+)`.

## Skripte

| Datei | Zweck |
|---|---|
| `auswertung.py` | Monatswerte je Richtung, Preis je Vier-Stunden-Produkt, angebotene Menge |
| `marktlage.py` | hält den Leistungspreis gegen Intradaypreis, Tagesspanne, Residuallast und Gaspreis, Tageskorrelationen |
| `ergebnis.txt` | Ausgabe von `auswertung.py` vom 24.09.2026 |

Beide Skripte lesen die xlsx-Dateien ohne openpyxl über
`../mfrr_leistungspreise/xlsx_lesen.py`.

```
python analysen/afrr_herbst_2025/auswertung.py
python analysen/afrr_herbst_2025/marktlage.py
```

Das Ergebnis steht in `BEFUND.md`.
