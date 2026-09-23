# Auftrag: Zeitmuster des Redispatch im Format der Abbildung 4.5

**Stand 23.09.2026.** Absender ist die Schriftfassung, Adressat ist das
Analyse-Repository `bess_dispatch_optimization`.

---

## 1 Was gebraucht wird

Eine Abbildung, die den **Redispatchbedarf** des Jahres 2025 über den Tag und
über das Jahr zeigt, **im selben Format wie
`reservierungspreis_zeitmuster_2025.pdf`**. Damit lassen sich beide
Abbildungen unmittelbar nebeneinanderlegen.

| Merkmal | Soll |
|---|---|
| Dateiname, Vorschlag | `redispatch_zeitmuster_2025.pdf` |
| Ablage | `analysen/12_schrift/kapitel_anhang/` |
| Label in der Arbeit | `fig:redispatch_zeitmuster` |
| Linkes Feld | Stunde des Tages, 0 bis 23 |
| Rechtes Feld | Monat, Januar bis Dezember |
| Ordinate | Redispatchleistung in MW |

Die drei Kurven entsprechen denen der Abbildung 4.5:

| Abbildung 4.5 | hier |
|---|---|
| Entladereservierung | Redispatch **Wirkleistungseinspeisung erhöhen** |
| Ladereservierung | Redispatch **Wirkleistungseinspeisung reduzieren** |
| Summe beider Richtungen | Summe beider Richtungen |

Ebenso zu übernehmen sind Median durchgezogen, arithmetisches Mittel
gestrichelt und die graue Fläche zwischen beiden Maßen für die Summe. Der
Abstand beider Maße trägt hier dieselbe Aussage wie beim Preis, denn auch die
Redispatchleistung dürfte rechtsschief verteilt sein.

**Die Zuordnung der Richtungen ist nicht willkürlich.** Soll die Einspeisung
reduziert werden, so kann ein Speicher statt einer Abregelung laden; das
entspricht der Ladereservierung. Soll sie erhöht werden, so kann er entladen;
das entspricht der Entladereservierung. Die Farben sollten deshalb denen der
Abbildung 4.5 folgen, damit die Paarung optisch erkennbar bleibt.

---

## 2 Datenquelle und Verfahren

Quelle ist
`data/processed/Redispatch_netztransparnez.net/2025_Redispatchmaßnahmen.parquet`
im Analyse-Repository, also die Einzelmaßnahmen von netztransparenz.net. Die
Datei führt 19 369 Maßnahmen mit `BEGINN_DATUM`, `BEGINN_UHRZEIT`,
`ENDE_DATUM`, `ENDE_UHRZEIT`, `RICHTUNG` und `MITTLERE_LEISTUNG_MW`. Alle
19 369 Einträge tragen vollständige Angaben.

Verfahren: jede Maßnahme wird mit ihrer mittleren Leistung auf die Stunden
verteilt, die sie berührt, anteilig nach der Überlappung. Daraus entsteht eine
Stundenreihe über das Jahr, aus der sich Median und Mittel je Tagesstunde und
je Monat bilden lassen.

**Die Schriftfassung hat das bereits gerechnet.** Das Skript liegt als
`analysen/redispatch_tagesmuster/richtungen.py` im Repository der
Schriftfassung. Bitte unabhängig nachrechnen und melden, falls die Werte
abweichen; ein Abgleich ist wertvoller als eine Übernahme.

Zur Gegenprobe die eigenen Ergebnisse, mittlere Leistung je Tagesstunde über
das ganze Jahr:

| Richtung | Maximum | Minimum | Verhältnis |
|---|---|---|---|
| reduzieren | 1701 MW um 12 Uhr | 793 MW um 0 Uhr | 2,14 |
| erhöhen | 1788 MW um 10 Uhr | 1236 MW um 0 Uhr | 1,45 |
| beide zusammen | 3440 MW um 11 Uhr | 2029 MW um 0 Uhr | 1,70 |

Und je Monat, beide Richtungen zusammen: Januar 5010 MW als größter und August
1037 MW als kleinster Wert, Verhältnis 4,83.

---

## 3 Wofür die Abbildung gebraucht wird

Abschnitt 4.5 hält den kurativen Reservierungspreis gegen den
Engpassmanagementbedarf. Der Jahresgang steht bereits in Abbildung 4.6. Was
fehlt, ist das **Tagesmuster** des Bedarfs, und es trägt einen Befund:

- Über den Tag schwankt der Bedarf um den Faktor 1,70, der Reservierungspreis
  dagegen um 8,28. Die Tageszeit ist damit die Dimension des Preises und nicht
  die des Bedarfs.
- Die Richtungen verhalten sich aber verschieden. Der Bedarf an **Reduzierung**
  hat sein Maximum um 12 Uhr, und dort ist die Ladereservierung am teuersten.
  In den sechs teuersten Ladestunden fallen 33 Prozent dieses Bedarfs an,
  gegenüber 25 Prozent bei gleichmäßiger Verteilung.
- Der Bedarf an **Erhöhung** ist mit dem Faktor 1,45 nahezu flach, und die
  teuren Abendstunden der Entladereservierung treffen ihn nicht: dort sind es
  26 gegen 25 Prozent.

Die Abbildung soll voraussichtlich in den Anhang, weil der Fließtext die
Aussage in wenigen Sätzen trägt und Kapitel 4 bereits zwölf Abbildungen führt.
Die endgültige Entscheidung trifft der Verfasser.

---

## 4 Satzstandard

Unverändert nach `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` Abschnitt 0, nämlich
NimbusSanL, 8,0 pt Grundbeschriftung, 9,0 pt Achsentitel, 453,5 pt Breite,
Einbindung mit `width=\textwidth`, keine Stauchung. Die Höhe sollte der
Abbildung 4.5 entsprechen, damit beide sich vergleichen lassen.

**Die Bildunterschrift schreibt die Schriftfassung**, sie hat höchstens zwei
gesetzte Zeilen. Gebraucht wird aus dem Analyse-Repository allein der Hinweis,
falls die Abbildung eine Eigenheit trägt, die der Leser sonst falsch deutet,
etwa eine abgeschnittene Achse.

---

## 5 Die Zahlen bitte in die Ergebnisdatei

Wie gewohnt in `ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md`, damit keine Zahl aus der
Abbildung abgelesen werden muss: Median und Mittel je Tagesstunde und je Monat,
je Richtung und für die Summe.

---

## 6 Dringlichkeit

Nachrangig. Abschnitt 4.5 steht ohne die Abbildung, denn die Zahlen liegen vor.
Die Abbildung würde den Vergleich sichtbar machen, den der Text sonst nur
behauptet.
