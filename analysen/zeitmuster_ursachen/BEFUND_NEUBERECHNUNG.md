# Neuberechnung mit der zweiten Iteration

Eigene Auswertung vom 23.09.2026. Reservierungspreis aus
`be_full_pos` und `be_full_neg`, also der zweiten Iteration.

## 0 Gegenprobe gegen ERGEBNISSE Abschnitt 7.1

| Richtung | Median | Mittel | Maximum |
|---|---|---|---|
| Entladen | 12.22 | 23.64 | 1008.00 |
| Laden | 9.85 | 24.33 | 510.48 |

ERGEBNISSE nennt 12,22 / 23,64 / 1008,00 und 9,85 / 24,33 / 510,48.

## 1 Struktur der teuren Stunden, fuer Abschnitt 4.4

**Entladereservierung**, 90-Prozent-Quantil 52.3 Euro je Megawatt und Stunde

| Groesse | Wert |
|---|---|
| teure Stunden | 874 |
| Kalendertage | 223 |
| Stunden je betroffenem Tag | 3.9 |
| Anteil in den sechs staerksten Tagesstunden | 58 Prozent |
| diese Tagesstunden | 9, 11, 17, 18, 19, 20 |
| Anteil Maerz bis Oktober | 79 Prozent |

**Ladereservierung**, 90-Prozent-Quantil 72.5 Euro je Megawatt und Stunde

| Groesse | Wert |
|---|---|
| teure Stunden | 876 |
| Kalendertage | 176 |
| Stunden je betroffenem Tag | 5.0 |
| Anteil in den sechs staerksten Tagesstunden | 80 Prozent |
| diese Tagesstunden | 11, 12, 13, 14, 15, 16 |
| Anteil Maerz bis Oktober | 99 Prozent |

## 2 Woran der Preis haengt, fuer Abschnitt 4.1

| Fenster | Rangkorrelation mit dem aFRR-Leistungspreis |
|---|---|
| Ladereservierung 10 bis 15 Uhr | +0.92 |
| Entladereservierung 17 bis 20 Uhr | +0.74 |

Mittlerer aFRR-Leistungspreis der Mittagsstunden im Mai 82.2 gegen 37.5
im Jahresmittel derselben Stunden, also das 2.2-Fache.

## 3 Tages- und Jahresgang der Summe

| Groesse | Wert |
|---|---|
| Median der Summe, groesste Tagesstunde | 79.3 um 14 Uhr |
| Median der Summe, kleinste Tagesstunde | 9.6 um 0 Uhr |
| Verhaeltnis ueber den Tag | 8.28 |
| Median der Summe, groesster Monat | 56.9 im Monat 9 |
| Median der Summe, kleinster Monat | 13.5 im Monat 12 |
| Verhaeltnis ueber das Jahr | 4.23 |

Verhaeltnis der beiden Richtungen je Tagesstunde, Median:

| Stunde | entladen | ladend | Verhaeltnis |
|---|---|---|---|
| 07 | 20.6 | 4.5 | 4.6-fach |
| 13 | 12.4 | 58.6 | 4.7-fach |
| 14 | 15.5 | 56.9 | 3.7-fach |
| 19 | 43.8 | 4.1 | 10.7-fach |

