# Tagesmuster des Redispatch je Richtung

Eigene Auswertung vom 23.09.2026 aus 19.369 Einzelmassnahmen von
netztransparenz.net. Jede Massnahme ist mit ihrer mittleren Leistung
anteilig auf die beruehrten Stunden verteilt. Der Reservierungspreis
ist der Median der zweiten Iteration.

**Die Zuordnung der Richtungen.** Soll die Einspeisung reduziert werden,
so kann ein Speicher statt einer Abregelung laden; das entspricht der
Ladereservierung. Soll sie erhoeht werden, so kann er entladen; das
entspricht der Entladereservierung.

| Stunde | Redispatch reduzieren | Ladereservierung | Redispatch erhoehen | Entladereservierung |
|---|---|---|---|---|
| 00 | 793 | 3.1 | 1236 | 3.2 |
| 01 | 852 | 5.9 | 1304 | 4.2 |
| 02 | 891 | 7.5 | 1349 | 4.4 |
| 03 | 921 | 9.8 | 1374 | 4.8 |
| 04 | 950 | 7.2 | 1433 | 2.2 |
| 05 | 1031 | 5.9 | 1507 | 7.8 |
| 06 | 1218 | 4.5 | 1607 | 12.8 |
| 07 | 1311 | 4.5 | 1674 | 20.6 |
| 08 | 1366 | 4.9 | 1699 | 17.7 |
| 09 | 1520 | 18.0 | 1762 | 18.6 |
| 10 | 1634 | 29.1 | 1788 | 20.5 |
| 11 | 1690 | 40.0 | 1749 | 23.5 |
| 12 | 1701 | 45.0 | 1721 | 6.5 |
| 13 | 1683 | 58.6 | 1677 | 12.4 |
| 14 | 1615 | 56.9 | 1627 | 15.5 |
| 15 | 1493 | 47.4 | 1577 | 18.5 |
| 16 | 1341 | 25.6 | 1555 | 6.7 |
| 17 | 1270 | 12.9 | 1529 | 18.5 |
| 18 | 1158 | 4.5 | 1503 | 32.2 |
| 19 | 1120 | 4.1 | 1483 | 43.8 |
| 20 | 1054 | 2.2 | 1407 | 27.2 |
| 21 | 1008 | 4.6 | 1350 | 18.7 |
| 22 | 957 | 6.7 | 1306 | 11.9 |
| 23 | 882 | 13.0 | 1237 | 4.7 |

## 1 Wann der Bedarf am groessten ist

| Richtung | Maximum | Minimum | Verhaeltnis |
|---|---|---|---|
| Reduzieren | 1701 MW um 12 Uhr | 793 MW um 0 Uhr | 2.14 |
| Erhoehen | 1788 MW um 10 Uhr | 1236 MW um 0 Uhr | 1.45 |
| beide zusammen | 3440 MW um 11 Uhr | 2029 MW um 0 Uhr | 1.70 |

## 2 Faellt der Bedarf mit dem hohen Preis zusammen?

| Paarung | Rangkorrelation ueber die 24 Tagesstunden |
|---|---|
| Reduzieren gegen Ladereservierung | +0.59 |
| Erhoehen gegen Entladereservierung | +0.46 |
| Reduzieren gegen Entladereservierung | +0.50 |
| Erhoehen gegen Ladereservierung | +0.49 |

## 3 Die sechs teuersten Stunden je Richtung

**Ladereservierung**, teuerste Stunden 10, 11, 12, 13, 14, 15.

In diesen sechs Stunden faellt 33 Prozent des Bedarfs der Richtung
an, gegenueber 25 Prozent bei gleichmaessiger Verteilung.

**Entladereservierung**, teuerste Stunden 7, 10, 11, 18, 19, 20.

In diesen sechs Stunden faellt 26 Prozent des Bedarfs der Richtung
an, gegenueber 25 Prozent bei gleichmaessiger Verteilung.

