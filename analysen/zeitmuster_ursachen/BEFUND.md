# Ursachen der teuren Perioden im Zeitmuster 2025

Eigene Auswertung vom 23.09.2026, Quelle `jahr_slots_2025.parquet`.
Preise der Reservierung in Euro je Megawatt und Stunde, Marktpreise
des Day-Ahead und des Intraday in Euro je Megawattstunde, der
aFRR-Leistungspreis in Euro je Megawatt und Stunde.

## 1 Ladereservierung mittags, 10 bis 15 Uhr

| Zeitraum | Reservierung | aFRR-Leistung | IDC-Preis | IDC-Minimum | Anteil negativ in % | aFRR MW | IDC MW |
|---|---|---|---|---|---|---|---|
| Anfang April | 69.4 | 48.8 | -11.1 | -128.4 | 57.5 | 83.6 | 8.0 |
| Ende April | 85.1 | 70.3 | 33.6 | -7.5 | 30.0 | 89.1 | 3.5 |
| Anfang Mai | 62.1 | 53.5 | 15.7 | -38.0 | 38.8 | 86.5 | 7.2 |
| Mitte Mai | 137.5 | 136.8 | 0.2 | -35.4 | 60.8 | 86.4 | 1.6 |
| Ende Juni | 103.0 | 86.2 | 4.4 | -59.7 | 58.8 | 91.0 | 5.1 |
| **ganzes Jahr** | 49.8 | 37.5 | 57.9 | 21.8 | 23.7 | 83.3 | 4.9 |

## 2 Entladereservierung abends, 17 bis 20 Uhr

| Zeitraum | Reservierung | aFRR-Leistung | IDC-Preis | IDC-Maximum | DA-Preis | aFRR MW | IDC MW |
|---|---|---|---|---|---|---|---|
| September | 71.5 | 49.0 | 154.2 | 289.6 | 143.9 | 56.3 | 10.9 |
| Oktober | 57.0 | 47.7 | 123.2 | 207.3 | 126.1 | 67.5 | 6.5 |
| **ganzes Jahr** | 41.3 | 25.8 | 122.3 | 205.8 | 123.5 | 63.4 | 9.2 |

## 3 Woran der Preis haengt, ueber alle 365 Tage

Rangkorrelation nach Spearman zwischen dem Reservierungspreis im
Fenster und den moeglichen Treibern.

**Ladereservierung mittags**

| Treiber | Rangkorrelation |
|---|---|
| afrr_cap | +0.90 |
| afrr_ene | -0.40 |
| idc | -0.65 |
| idc_min | -0.67 |
| neg_anteil | +0.63 |
| da | -0.73 |

**Entladereservierung abends**

| Treiber | Rangkorrelation |
|---|---|
| afrr_cap | +0.74 |
| afrr_ene | +0.38 |
| idc | +0.36 |
| idc_max | +0.60 |
| da | +0.34 |

## 4 Die 15 teuersten Mittage der Ladereservierung

| Tag | preis | afrr_cap | idc | idc_min | neg_anteil |
|---|---|---|---|---|---|
| 15.05. | 307.0 | 309.8 | -2.9 | -34.5 | 83.3 |
| 29.04. | 273.0 | 230.6 | 0.6 | -45.0 | 62.5 |
| 25.06. | 210.8 | 104.9 | 67.9 | 3.5 | 0.0 |
| 06.03. | 188.9 | 38.8 | 16.6 | -17.8 | 50.0 |
| 22.03. | 182.7 | 55.4 | -32.2 | -85.5 | 100.0 |
| 26.08. | 176.8 | 83.3 | 49.8 | 16.3 | 0.0 |
| 12.05. | 176.3 | 185.9 | 6.6 | -13.2 | 50.0 |
| 14.06. | 174.5 | 59.8 | -26.5 | -80.0 | 83.3 |
| 23.06. | 174.0 | 184.1 | -1.1 | -7.4 | 75.0 |
| 30.04. | 170.1 | 164.6 | 3.1 | -41.2 | 54.2 |
| 16.05. | 159.5 | 162.7 | 15.9 | -10.2 | 29.2 |
| 01.07. | 151.4 | 73.7 | 89.1 | 66.9 | 0.0 |
| 16.09. | 146.5 | 84.3 | 0.3 | -2.6 | 41.7 |
| 17.05. | 143.7 | 133.4 | -1.6 | -7.9 | 79.2 |
| 24.09. | 131.4 | 103.7 | 58.0 | 4.5 | 0.0 |

## 5 Die 15 teuersten Abende der Entladereservierung

| Tag | preis | afrr_cap | idc | idc_max | da |
|---|---|---|---|---|---|
| 08.09. | 244.8 | 60.1 | 713.9 | 1196.5 | 260.8 |
| 06.03. | 170.8 | 18.5 | 416.3 | 1443.5 | 147.3 |
| 26.08. | 163.5 | 33.9 | 422.3 | 1620.0 | 153.3 |
| 30.04. | 152.7 | 23.3 | 106.9 | 163.6 | 121.7 |
| 21.01. | 130.0 | 63.1 | 481.9 | 798.3 | 232.7 |
| 06.04. | 126.3 | 15.0 | 77.0 | 132.7 | 94.7 |
| 01.07. | 122.2 | 39.8 | 235.6 | 587.8 | 259.4 |
| 08.10. | 121.7 | 92.1 | 230.3 | 364.1 | 168.5 |
| 14.10. | 113.8 | 85.8 | 247.6 | 430.7 | 314.2 |
| 20.01. | 110.5 | 43.8 | 270.6 | 399.3 | 393.1 |
| 15.01. | 109.7 | 107.3 | 183.8 | 228.4 | 288.6 |
| 01.10. | 109.6 | 102.1 | 121.6 | 182.2 | 220.2 |
| 03.12. | 107.3 | 63.9 | 282.7 | 638.7 | 195.6 |
| 04.09. | 99.8 | 66.9 | 283.4 | 552.2 | 217.4 |
| 22.10. | 98.5 | 77.6 | 258.2 | 482.4 | 239.9 |

## 6 Monatsmittel der Treiber

| Monat | Lad-Res | aFRR neg | IDC mittags | neg. Anteil | Ent-Res | aFRR pos | IDC abends |
|---|---|---|---|---|---|---|---|
| 01 | 18.0 | 3.0 | 110.1 | 3% | 33.7 | 22.5 | 144.3 |
| 02 | 18.9 | 4.8 | 110.0 | 1% | 29.2 | 22.6 | 152.7 |
| 03 | 54.2 | 31.7 | 42.3 | 34% | 45.7 | 21.1 | 146.7 |
| 04 | 69.1 | 55.1 | 21.1 | 36% | 49.6 | 19.5 | 108.8 |
| 05 | 87.5 | 82.2 | 9.2 | 53% | 47.7 | 22.8 | 100.8 |
| 06 | 82.8 | 67.4 | 6.1 | 58% | 42.8 | 22.0 | 99.3 |
| 07 | 47.3 | 41.6 | 51.6 | 19% | 26.9 | 17.7 | 100.8 |
| 08 | 58.5 | 50.8 | 28.2 | 34% | 37.4 | 19.6 | 114.4 |
| 09 | 79.2 | 61.0 | 43.3 | 30% | 71.5 | 49.0 | 154.2 |
| 10 | 49.1 | 35.7 | 70.2 | 14% | 57.0 | 47.7 | 123.2 |
| 11 | 23.0 | 11.9 | 104.5 | 0% | 31.6 | 27.7 | 117.6 |
| 12 | 8.4 | 2.6 | 100.9 | 0% | 21.8 | 17.5 | 107.8 |

