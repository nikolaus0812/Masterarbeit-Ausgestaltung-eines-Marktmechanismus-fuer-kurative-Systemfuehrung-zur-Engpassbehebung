# Auftrag: Füllgrad über die Tagesstunden, eine neue Abbildung für 4.2

**Stand 23.09.2026.** Absender ist die Schriftfassung
`Masterarbeit-Ausgestaltung-eines-Marktmechanismus-fuer-kurative-Systemfuehrung-zur-Engpassbehebung`,
Adressat ist das Analyse-Repository `bess_dispatch_optimization`.

Aus dem Analyse-Repository heraus wird nichts in die Schriftfassung
geschrieben. Die Lieferung erfolgt wie bisher nach
`analysen/12_schrift/kapitel_4/`, das Kopieren macht die Schriftfassung.

---

## 1 Warum

Abschnitt 4.2 der Arbeit leitet seit dem 23.09.2026 von der tageweisen
Betrachtung des Abschnitts 4.1 in die Jahresbetrachtung über. Der zweite
Absatz stellt die erste Iteration der Preissuche als das teurere Verfahren
dar, nämlich 409,8 Tsd. €/(MW·a) Zahlung des ÜNB bei 88,6 Tsd. €/(MW·a)
verbliebenem Markterlös, insgesamt 46,3 Prozent über dem Referenzerlös.

Der Absatz sagt bisher **nicht**, *welche* Stunden die erste Iteration offen
lässt. Genau das ist der Punkt, an dem die Ineffizienz der ersten Iteration
sichtbar würde: sie bindet einen erheblichen Teil der Leistung, lässt aber
regelmäßig dieselben Stunden frei, und in diesen Stunden verdient die
Bezugsanlage weiter an den übrigen Märkten.

Vorgabe des Verfassers vom 23.09.2026: *„vlt wäre hier ein diagramm ganz
interessant welche tagesstunden noch offen bleiben. also füllgrad gemittelt
über die tagestunden."*

---

## 2 Was gebraucht wird

### 2.1 Die Abbildung

| Merkmal | Soll |
|---|---|
| Dateiname, Vorschlag | `fuellgrad_tagesstunden_2025.pdf` |
| Label in der Arbeit | `fig:fuellgrad_tagesstunden` |
| Abszisse | die 24 Tagesstunden, 0 bis 23 |
| Ordinate | Füllgrad der kurativen Reservierung in Prozent, 0 bis 100 |
| Kurven | erste Iteration je Richtung, zweite Iteration je Richtung als Vergleich |
| Grundgesamtheit | alle 365 Tage des Jahres 2025 |

**Füllgrad** heißt hier die kurativ reservierte Leistung geteilt durch die
Nennleistung der Bezugsanlage, je Stunde und Richtung. Gemittelt wird über
alle Tage des Jahres, getrennt je Tagesstunde. Sollte im Modell eine andere
Bezugsgröße naheliegen, etwa die in der jeweiligen Stunde überhaupt
reservierbare Leistung, dann bitte diese verwenden und die Wahl in einem Satz
begründen.

Ob beide Iterationen in ein Feld gehören oder ob zwei Felder nebeneinander
besser lesbar sind, entscheidet das Analyse-Repository. Die zweite Iteration
liegt erwartungsgemäß nahe an 100 Prozent und ist als Bezugslinie gedacht.

### 2.2 Die Zahlen dazu, als Text

Keine Zahl der Arbeit wird aus einer Abbildung abgelesen. In
`ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` werden deshalb gebraucht:

1. Mittlerer Füllgrad über das Jahr 2025, je Richtung und je Iteration.
2. Anteil der Stunden des Jahres, die unter den Preisen der ersten Iteration
   **nicht** voll reserviert sind, je Richtung.
3. Die drei Tagesstunden mit dem niedrigsten und die drei mit dem höchsten
   mittleren Füllgrad unter der ersten Iteration, je Richtung, mit Wert.
4. Der Markterlös dieser offenen Stunden, wenn er sich ohne großen Aufwand
   aus dem vorhandenen Lauf ziehen lässt: von den 88,6 Tsd. €/(MW·a) der
   ersten Iteration wäre der Anteil der Tagesstunden interessant, an denen
   der Füllgrad am niedrigsten ist. Nachrangig, nur falls ohne neuen Lauf
   möglich.

### 2.3 Satzstandard

Unverändert nach `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` Abschnitt 0, nämlich
NimbusSanL, 8,0 pt Grundbeschriftung, 9,0 pt Achsentitel, 453,5 pt Breite,
Einbindung mit `width=\textwidth`, keine Stauchung.

---

## 3 Zwei Rückfragen zu vorhandenen Zahlen

### 3.1 Gelten die Füllgrade von 84,5 und 89,0 Prozent noch?

`ANWEISUNG_ABBILDUNGEN.md` nennt als mittleren Füllgrad 84,5 Prozent (POS)
und 89,0 Prozent (NEG) für die erste sowie 99,04 und 99,78 Prozent für die
zweite Iteration. Diese Werte stehen dort unmittelbar neben den Erlöszahlen
+45,1 und +21,9 Prozent, die inzwischen durch +46,3 und +23,3 Prozent ersetzt
sind, und sie beziehen sich auf 363 statt auf 365 Tage.

**Frage:** Sind die vier Füllgrade auf demselben Stand wie der
Erlösvergleich vom 22.09.2026, oder stammen sie noch aus dem Lauf vom
13.09.2026? Bis zur Antwort steht keiner der vier Werte in der Arbeit.

### 3.2 Gelten die Laufzahlen 84 bis 167 auch für die Jahresläufe?

Abschnitt 3.2.4 der Arbeit nennt für die erste Iteration 84 bis 167 Läufe des
Optimierungsmodells je Tag und für die zweite einige hundert, jeweils
belegt an den ausgewerteten Tagen. Abschnitt 4.2 verwendet diese Spanne
seit dem 23.09.2026 als Angabe zum Rechenaufwand.

**Frage:** Trifft die Spanne auch auf die Jahresläufe zu, aus denen Kapitel 4
rechnet, oder liegt sie dort anders? Falls für das Jahr eine eigene Zahl
vorliegt, bitte Minimum, Median und Maximum der Läufe je Tag und Iteration.

---

## 4 Zwei Nebenpunkte, die ohnehin offen sind

### 4.1 Widerspruch in `ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md`

Abschnitt 2.3 jener Datei nennt den 11.02.2025 als den Tag, an dem der
Day-Ahead zuerst weicht. Abschnitt 2.1 derselben Datei zeigt für diesen Tag
das Gegenteil, nämlich die Halbierung der aFRR bei 10 und die von Day-Ahead
und IDC erst bei 15 €/(MW·h). Die Schriftfassung folgt der Tabelle aus
Abschnitt 2.1 und nennt an dieser Stelle den 26.08.2025. **Bitte prüfen und
eine der beiden Stellen berichtigen.**

### 4.2 Gehandelte Energie je Markt und Tag

Der Verfasser hält die gehandelte Energie für aussagekräftiger als die
Leistungs-Tagesmittel in MW, die Abschnitt 4.1 und Anhang F derzeit tragen:
*„die gehandelte energie wäre noch interessanter und aussagekräftiger"*.
Diese Größe steht bisher in keiner gelieferten Auswertung.

Gebraucht würde die gehandelte oder vorgehaltene Energie je Markt, Tag und
Preisstufe des Preisgitters, für dieselben fünf Analysetage, in MWh. Sollte
das einen neuen Lauf erfordern, bitte zuerst den Aufwand melden und nicht
ungefragt rechnen. Bis dahin bleiben die MW-Werte im Text.

---

## 5 Dringlichkeit

Die Abbildung aus Abschnitt 2 hält den Durchgang durch 4.2 nicht auf, denn
der Absatz steht ohne sie. Sie ergänzt ihn um die Aussage, welche Stunden
offen bleiben. Nachrangig gegenüber `sensi8_spanne_und_niveau`, auf das die
Abschnitte 4.6.3 und 4.6.4 warten.
