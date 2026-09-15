# Leistungspreise der mFRR und der aFRR im Jahr 2025

Beleg für die Abgrenzung der mFRR in Abschnitt 2.2.3 und für den Satz in
Abschnitt 3.2.1, dass das Modell die mFRR nicht führt. Stand 15.09.2026.

## Quelle

regelleistung.net, Ergebnisübersicht des Leistungsmarkts (RESULT OVERVIEW
CAPACITY MARKET), Eintrag `regelleistung_ausschreibungsdaten_2026`.

- mFRR: 365 Tagesdateien für 2025, am 15.09.2026 mit `download.py` über den
  Exportendpunkt der Datenplattform abgerufen. Die Tagesdateien liegen nicht
  im Repository, die daraus gelesenen Werte stehen in
  `mfrr_afrr_leistungspreise_2025.csv`.
- aFRR: Jahresdatei 2025 aus dem Modellrepository
  (`data/Regelleistung_regelleistung.net/aFRR_Leistung`).

Je Tag und Produkt sechs Vier-Stunden-Zeitscheiben je Richtung, also 2190
Zeitscheiben je Richtung und Jahr. Ausgewertet ist die Spalte
GERMANY_AVERAGE_CAPACITY_PRICE, der mengengewichtete Durchschnitt der
Zuschläge in Deutschland in Euro je Megawatt und Stunde, dazu
GERMANY_MARGINAL_CAPACITY_PRICE als höchster Zuschlag.

## Ergebnis

| Produkt, Richtung | Mittel des Durchschnittspreises | Median | Mittel des höchsten Zuschlags |
|---|---|---|---|
| mFRR positiv | 5,17 | 1,88 | 7,57 |
| mFRR negativ | 11,28 | 2,13 | 15,08 |
| aFRR positiv | 17,96 | 12,32 | 27,80 |
| aFRR negativ | 15,65 | 4,42 | 24,90 |

Alle Werte in Euro je Megawatt und Stunde. Im Mittel beider Richtungen liegt
der Leistungspreis der mFRR bei rund der Hälfte der aFRR, im Median bei einem
Fünftel bis der Hälfte. Der Text in 2.2.3 nennt die gerundeten Mittelwerte 5
und 11 gegen 18 und 16 Euro je Megawatt und Stunde.
