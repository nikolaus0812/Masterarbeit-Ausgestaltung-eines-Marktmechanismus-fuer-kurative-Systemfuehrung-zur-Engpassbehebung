# Die zehn ertragreichsten Arbitragepaare je Tag

Eigene Auswertung vom 23.09.2026. Alle Preise in Euro je Megawattstunde,
die Reservierungspreise in Euro je Megawatt und Stunde.

## 1 Wie schnell die Spannen abfallen

| Groesse | Median | unteres Quartil | oberes Quartil |
|---|---|---|---|
| Spanne des ersten Paares | 178.96 | 121.14 | 269.63 |
| Spanne des zehnten Paares | 112.76 | 75.06 | 146.37 |
| Verhaeltnis zehntes zu erstem Paar | 0.62 | 0.48 | 0.72 |

Das zehnte Paar traegt im Median noch 62 Prozent der Spanne des ersten.

## 2 Liegt die Reservierung teuer, wo die Paare liegen

Mittlerer Reservierungspreis in den Stunden, die zu den zehn Paaren
gehoeren, gegen die uebrigen Stunden desselben Tages.

| Richtung | in den Paarstunden | in den uebrigen Stunden | Faktor |
|---|---|---|---|
| Entladereservierung | 34.8 | 20.6 | 1.68 |
| Ladereservierung | 40.3 | 24.4 | 1.65 |

Deckung: Anteil der sechs teuersten Reservierungsstunden eines Tages,
die zugleich zu den zehn Paaren gehoeren.

| Richtung | Median | Mittel |
|---|---|---|
| Entladen gegen Absatzstunden | 50 % | 48 % |
| Laden gegen Bezugsstunden | 50 % | 50 % |

## 3 Woran der Tagespreis haengt, erstes oder zehntes Paar

Rangkorrelation nach Spearman ueber alle 365 Tage.

| | Spanne des ersten Paares | Spanne des zehnten Paares | Abfall |
|---|---|---|---|
| Entladereservierung | +0.71 | +0.67 | -0.32 |
| Ladereservierung | +0.78 | +0.74 | -0.32 |

## 4 Monatsbild

| Monat | Spanne Paar 1 | Spanne Paar 10 | Abfall | Deckung entladen | Deckung laden |
|---|---|---|---|---|---|
| 01 | 221.8 | 106.1 | 59 % | 54 % | 42 % |
| 02 | 158.4 | 91.8 | 62 % | 46 % | 42 % |
| 03 | 276.6 | 133.3 | 59 % | 55 % | 55 % |
| 04 | 290.4 | 149.0 | 57 % | 41 % | 57 % |
| 05 | 306.8 | 149.7 | 58 % | 47 % | 56 % |
| 06 | 394.7 | 174.5 | 56 % | 44 % | 54 % |
| 07 | 207.4 | 108.0 | 64 % | 38 % | 59 % |
| 08 | 246.7 | 124.3 | 64 % | 44 % | 58 % |
| 09 | 315.2 | 153.2 | 51 % | 42 % | 53 % |
| 10 | 211.7 | 102.4 | 56 % | 53 % | 39 % |
| 11 | 152.4 | 80.2 | 61 % | 58 % | 38 % |
| 12 | 114.7 | 65.9 | 63 % | 58 % | 44 % |

## 5 Die zehn Tage mit der flachsten und der steilsten Staffel

**Flachste Staffel, das zehnte Paar traegt fast so viel wie das erste**

| Tag | Paar 1 | Paar 10 | Abfall | Reservierung entladen | Reservierung laden |
|---|---|---|---|---|---|
| 12.07. | 140.0 | 128.8 | 92 % | 20.6 | 22.0 |
| 01.06. | 127.3 | 115.9 | 91 % | 17.2 | 31.0 |
| 03.08. | 115.1 | 102.7 | 89 % | 11.6 | 20.2 |
| 05.08. | 119.2 | 106.2 | 89 % | 16.3 | 23.2 |
| 07.01. | 118.2 | 104.5 | 88 % | 12.5 | 13.9 |
| 01.08. | 133.7 | 117.9 | 88 % | 14.1 | 15.2 |
| 13.11. | 136.9 | 120.4 | 88 % | 21.1 | 22.1 |
| 10.12. | 130.4 | 114.4 | 88 % | 13.1 | 13.3 |
| 19.12. | 124.2 | 108.7 | 87 % | 10.1 | 11.7 |
| 08.12. | 121.1 | 104.7 | 86 % | 13.3 | 14.7 |

**Steilste Staffel, die Spanne bricht nach dem ersten Paar ein**

| Tag | Paar 1 | Paar 10 | Abfall | Reservierung entladen | Reservierung laden |
|---|---|---|---|---|---|
| 29.11. | 680.9 | 41.0 | 6 % | 13.9 | 34.5 |
| 26.08. | 1603.7 | 165.0 | 10 % | 61.3 | 125.4 |
| 15.05. | 1330.6 | 148.1 | 11 % | 104.6 | 165.9 |
| 22.01. | 754.7 | 92.8 | 12 % | 41.6 | 62.0 |
| 06.03. | 1461.3 | 202.8 | 14 % | 61.9 | 117.1 |
| 09.01. | 687.6 | 110.1 | 16 % | 27.6 | 51.9 |
| 03.10. | 735.5 | 127.6 | 17 % | 33.7 | 42.8 |
| 12.09. | 664.2 | 137.5 | 21 % | 28.7 | 64.3 |
| 25.04. | 560.5 | 117.3 | 21 % | 23.7 | 27.3 |
| 25.06. | 1159.6 | 245.2 | 21 % | 61.3 | 151.7 |

