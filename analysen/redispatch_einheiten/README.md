# Redispatch-Maßnahmen der ÜNB im Jahr 2025 je Einheit

Beleg für den Satz in Abschnitt 1.1, dass sich der Redispatch bisher auf
wenige große Anlagen stützt. Stand 21.09.2026.

## Quelle

Netztransparenz, Liste der Redispatch-Maßnahmen des Jahres 2025 mit jeder
einzelnen Maßnahme, Eintrag `netztransparenz_regelenergie_2026`. Die Rohdaten
liegen im Modellrepository unter
`data/processed/Redispatch_netztransparnez.net/2025_Redispatchmaßnahmen.parquet`
und nicht in diesem Repository. `auswertung.py` liest sie mit dem Interpreter
des Modellrepositorys und schreibt `redispatch_einheiten_2025.csv` (eine Zeile
je Einheit) und `ergebnis.txt`.

Spalten der Quelle: Beginn und Ende, Grund der Maßnahme, Richtung, mittlere und
maximale Leistung in MW, gesamte Arbeit in MWh, anweisender und anfordernder
ÜNB, betroffene Anlage, Primärenergieart.

## Abgrenzung

Ausgewertet sind allein die Maßnahmen, deren Grund *Redispatch* enthält, also
ohne Countertrading (Sammelposition *Börse* und Countertrade DE-DK), ohne
Probe- und Testfahrten. Die Liste enthält nur die von den ÜNB angewiesenen
Maßnahmen; die Abregelungen im Verteilnetz, die der SMARD-Jahreswert von
30,3 TWh einschließt, fehlen. Die maximale Leistung ist die größte im Jahr
angewiesene Leistung der Einheit, nicht ihre Anschlussleistung; bei den
Sammelpositionen der Offshore-Netzverknüpfungspunkte (etwa *UW Büttel*,
*OWP UW Dörpen-West*) ist es die Leistung des Verknüpfungspunkts.

## Ergebnis

19.369 Maßnahmen und 381 Einheiten insgesamt. Nur Redispatch: 16.893
Maßnahmen, 16,5 TWh (8,4 TWh Absenken, 8,1 TWh Erhöhen), 356 Einheiten,
davon 10,4 TWh konventionell, 5,6 TWh erneuerbar, 0,5 TWh sonstige.

| Einheiten mit maximaler Leistung | Anzahl | Anteil an der Arbeit |
|---|---|---|
| mindestens 100 MW | 206 | 98,0 % |
| mindestens 300 MW | 117 | 91,2 % |
| mindestens 500 MW | 54 | 64,5 % |

Die 20 größten Einheiten tragen die Hälfte der Arbeit, die 58 größten 80 %,
die 83 größten 90 %.

Verwendet in 1.1: 98 % auf 206 Einheiten mit mindestens 100 MW, Entscheidung
des Verfassers vom 21.09.2026.
