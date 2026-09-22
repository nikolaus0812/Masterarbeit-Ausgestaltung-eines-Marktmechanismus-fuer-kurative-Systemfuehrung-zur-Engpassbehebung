# Workflow für Korrektur und Neufassung

Stand 14.09.2026. Er ersetzt die Fassung vom 07.09.2026 und das satzweise
Verfahren aus der alten `CLAUDE.md`. Er gilt für die Korrektur der Kapitel 1
und 2 nach den Betreuerkommentaren und für das Schreiben der Kapitel 3 bis 6.

---

## 1 Warum der Absatz und nicht der Satz

Das satzweise Verfahren hat drei Fassungen je Satz erzeugt und den Verfasser
wählen lassen. Es hat Sätze geliefert, die einzeln tragen, aber zusammen nicht.
Genau das bemängelt der Betreuer, nämlich Thesen ohne angebundene Begründung,
fehlende Übergänge, Pronomen ohne Bezug und Absätze ohne Konsequenz. Diese
Mängel entstehen zwischen den Sätzen und lassen sich nur beheben, wenn der
Absatz als Ganzes geplant und geschrieben wird.

Deshalb gilt seit dem 14.09.2026: Die Arbeitseinheit ist der Absatz. Ein Absatz
trägt eine Kernaussage, hat vier bis acht Sätze und entsteht in einem Zug aus
einem Absatzplan. Fassungen zur Wahl gibt es nur noch für den Aufbau eines
Absatzes, nicht für den Wortlaut einzelner Sätze. Wortlautvarianten liefert
Claude nur auf ausdrückliche Anfrage zu einem benannten Satz.

Die Stichpunktphase aus dem Vorgehen vom 09.09.2026 bleibt für neue Abschnitte
erhalten und geht dem Absatzplan voraus.

---

## 2 Der Absatzplan

Der Absatzplan ist die Freigabeeinheit. Ohne freigegebenen Plan entsteht kein
Fließtext. Er hat sechs Zeilen und passt auf einen Bildschirm.

```
Absatz:        2.1.1 Absatz 3, G 64 bis 72
Kernaussage:   Der praeventive Ansatz kostet aus drei Gruenden, naemlich ...
Aufbau:        These (Satz 1) -> Merkmal 1 mit Beleg -> Merkmal 2 mit Zeiten
               -> Merkmal 3 mit Beleg -> Konsequenz (Satz 7)
Anschluss:     knuepft an ... des Vorabsatzes an, fuehrt zu ... des Folgeabsatzes
Begriffe:      Planungshorizont, erstmals hier, Definition im Satz 3
Belege:        S2 sous_comparison_2025 (zu pruefen), S4 Mechanismus,
               S6 eigene Ableitung, vom Verfasser zu pruefen
Nicht sagen:   keine Behauptung, das Netz sei ohne kurativ nicht N-1-sicher
```

Bei der Korrektur eines bestehenden Absatzes kommen zwei Zeilen hinzu, nämlich
die **Befunde** mit den Kennungen aus `AENDERUNGEN_KAP1_2.md` und die
**Maßnahme**, also umbauen, kürzen, streichen oder verschieben.

Gibt es für den Aufbau zwei Wege, die sich in der Sache unterscheiden, etwa in
der Reihenfolge der Merkmale oder darin, ob eine Nebenaussage mitläuft, legt
Claude beide vor und sagt, woran sich die Wahl festmacht. Mehr als zwei Wege
gibt es selten. Wortlaut steht im Plan keiner.

---

## 3 Der Zyklus, je Abschnitt

Die Einheit des Zyklus ist ein Unterabschnitt, weil die Absätze eines
Unterabschnitts aneinander hängen und die Übergänge nur im Zusammenhang stimmen
können.

**Schritt 1, Vorlage.** Claude legt für jeden Absatz des Unterabschnitts den
Absatzplan vor, in der Reihenfolge des Textes, mit einem Satz zum Anschluss
zwischen den Absätzen. Bei einer Korrektur stammt der Ausgangspunkt aus
`AENDERUNGEN_KAP1_2.md`, bei einem neuen Abschnitt aus den gemeinsam
erarbeiteten Stichpunkten. Claude nennt dabei, welche Begriffe der Abschnitt
voraussetzt und wo sie definiert sind, welche Belege fehlen und welche
Entscheidung offen ist. Fehlt eine Entscheidung, endet der Zyklus hier.

**Schritt 2, Freigabe.** Der Verfasser gibt die Pläne frei, ändert sie oder
streicht Absätze. Änderungen am Plan schreibt er als Anmerkung, nicht als
Wortlaut. Will er einen Wortlaut vorgeben, kennzeichnet er ihn als wörtlich.

**Schritt 3, Text.** Claude schreibt die Absätze des Unterabschnitts als Ganzes
in die Datei. Ersetzter Fließtext bleibt als Kommentar über der neuen Fassung
erhalten, mit Datum, Grund und den Kennungen der Befunde. Marken und
Kommentare bleiben unberührt. Dazu liefert Claude den Belegzettel und den
Argumentzettel aus Abschnitt 5.

**Schritt 4, Prüfung.** Die Prüfsuite läuft, dann die Fremdleser-Prüfung aus
Abschnitt 4. Claude behebt die Befunde, bevor es übergibt, und berichtet, was
die Fremdleser-Prüfung nicht verstanden hat und wie es darauf reagiert hat.

**Schritt 5, Durchsicht.** Der Verfasser liest das gebaute PDF. Rückmeldungen
erfolgen satzweise, etwa *Absatz 3, Satz 4, Bezug unklar*. Eine
Korrekturrunde gehört zum Zyklus. Braucht ein Absatz eine zweite, war der Plan
zu dünn, und der Absatz geht zurück zu Schritt 1.

**Schritt 6, Protokoll.** Claude schreibt den Eintrag für
`ENTSCHEIDUNGSPROTOKOLL.md`, ein Eintrag je Unterabschnitt, mit den
Entscheidungen, den zurückgenommenen Formulierungen und den eigenständigen
Ableitungen. Danach gilt der Unterabschnitt als abgeschlossen.

Für neue Abschnitte steht vor Schritt 1 die Stichpunktphase, nämlich erst
gemeinsam die Fragen sammeln, die der Abschnitt beantworten muss, dann die
Stichpunkte in Blöcken anlegen, ein Stichpunkt je späterem Satz, und die Zahl
der Stichpunkte gegen das Seitenziel halten. Erst daraus entstehen die
Absatzpläne.

---

## 4 Die Fremdleser-Prüfung

Der Betreuer hat empfohlen, einen Absatz jemandem zu geben, der die kurative
Systemführung nicht kennt, und danach zu fragen, ob er verstanden wurde. Bis
ein Mensch liest, übernimmt das ein Subagent ohne Zugang zum übrigen Text.

Claude gibt dem Subagenten allein den neuen Unterabschnitt als gerenderten
Fließtext, ohne Kommentare, ohne Kapitelkontext, ohne diese Anleitung, und
stellt vier Fragen.

1. Was ist die Kernaussage jedes Absatzes, in einem Satz?
2. Welche Wörter, Abkürzungen oder Bezüge sind nicht erklärt oder nicht
   auflösbar?
3. Wo folgt auf eine Behauptung keine Begründung, oder auf eine Begründung
   keine Konsequenz?
4. Welcher Absatz lässt sich mit dem vorigen nicht verbinden?

Weicht die genannte Kernaussage vom Absatzplan ab, ist der Absatz nicht
gelungen. Was der Subagent nicht auflösen kann, wird im Text aufgelöst, auch
wenn der Begriff in einem früheren Kapitel definiert ist, denn der Betreuer
liest genauso.

---

## 5 Was Claude mit jedem Abschnitt liefert

**Die Datei.** Vollständig, Zeilenenden und UTF-8 unverändert, alle Kommentare
erhalten, alter Wortlaut als Kommentar.

**Der Belegzettel.** Je Absatz eine Zeile je Aussage mit Quelle oder mit dem
Vermerk Mechanismus, eigene Ableitung oder unbelegt. Unbelegte Aussagen stehen
nicht im Text, ohne dass der Verfasser sie gesehen hat.

**Der Argumentzettel.** Jedes Argument, das nicht aus den Stichpunkten oder aus
`AENDERUNGEN_KAP1_2.md` stammt, einzeln, als eigenständiges Argument
gekennzeichnet. Dazu zählen auch Hinweise des Betreuers, für die kein Beleg
vorliegt, etwa die Begrenzung des KuPilot-Einsatzes auf eine Stunde.

**Der Prüfbericht.** Ergebnis der Prüfsuite und der Fremdleser-Prüfung, mit
dem, was behoben ist und was offen bleibt.

---

## 6 Korrektur der Kapitel 1 und 2

Die Reihenfolge steht in `AENDERUNGEN_KAP1_2.md` Abschnitt 5. Drei Regeln
kommen bei der Korrektur hinzu.

- **Erst die Entscheidungen.** V1 bis V13 aus der Änderungsliste binden mehrere
  Absätze. Die Rückfragen an den Betreuer laufen parallel, die übrigen
  entscheidet der Verfasser vor dem ersten Zyklus.
- **Kürzung und Kommentar zusammen.** Ein Absatz wird nur einmal angefasst. Die
  Kürzungen aus `KUERZUNGEN_KAP1_2.md` und die Betreuerkommentare gehen in
  denselben Absatzplan.
- **Definitionen wandern nach vorn.** Wird ein Begriff nach Abschnitt 5 der
  `CLAUDE.md` an seinem Ort definiert, prüft Claude alle späteren Fundstellen
  auf abweichende Erklärungen und meldet sie.

Nach jedem Kapitel wird gebaut und der Seitenstand gegen die Ziele in
`STRUKTUR.md` gehalten, nämlich fünf Seiten für Kapitel 1, 25 für Kapitel 2
und 14 für Kapitel 3.

---

## 7 Neue Kapitel

Kapitel 4 bis 6 entstehen nach demselben Zyklus. Zwei Dinge sind anders.

- Vor dem ersten Absatzplan steht die Stichpunktphase aus Abschnitt 3.
- Die Zeile *Nicht sagen* im Absatzplan ist Pflicht, weil die Kapitel 1 und 2
  mehrfach Ergebnisse vorweggenommen haben, die erst Kapitel 4 trägt.

Kapitel 4 wartet auf die Rechenläufe für das Jahr 2025. Kapitel 5 trägt die
beiden Aussagen, die aus 3.1.1 dorthin verschoben sind, siehe `STRUKTUR.md`.

---

## 8 Zeit

Bis zur Abgabe am 15.10.2026 bleiben vier Wochen und drei Tage.

| Zeitraum | Schreiben | Parallel |
|---|---|---|
| 14.09. bis 18.09. | Entscheidungen V1 bis V13, Kapitel 1, Abschnitt 2.1 | Rückfragen an den Betreuer |
| 19.09. bis 23.09. | Abschnitte 2.2 bis 2.4 mit A1 und A3, Kapitel 3 auf 14 Seiten | Rechenläufe Jahr 2025 |
| 24.09. bis 30.09. | Kapitel 4 | Abbildungen erzeugen |
| 01.10. bis 06.10. | Kapitel 5 | Folgeänderungen aus dem Protokoll |
| 07.10. bis 11.10. | Kapitel 6, Kurzfassung, Verzeichnisse, Gesamtdurchsicht | Literaturdatei bereinigen |
| 12.10. | Kolloquium | |
| 13.10. bis 15.10. | Puffer und Abgabe | |

Die Woche für Kapitel 5 ist knapp. Wenn Zeit fehlt, fehlt sie dort.

---

## 9 Wiederkehrende Fehlerbilder

Die Betreuerkommentare haben zu den fünf Mustern vom 07.09.2026 vier weitere
ergeben. Der Zyklus fängt sie an bestimmten Stellen ab.

| Muster | Abgefangen durch |
|---|---|
| Ergebnisse werden vorweggenommen | Zeile *Nicht sagen* im Absatzplan, Frage in Schritt 5 |
| Eine Quelle trägt weniger als der Satz | Belegzettel |
| Ein Begriff wird vor seiner Definition verwendet | Zeile *Begriffe* im Absatzplan, Liste in `CLAUDE.md` Abschnitt 5 |
| Eine zurückgenommene Formulierung kehrt zurück | alter Wortlaut als Kommentar in der Datei |
| Zwei Stellen sagen dasselbe | Schritt 1 liest die Nachbarabschnitte mit |
| These ohne angebundene Begründung | Zeile *Aufbau* im Absatzplan, Frage 3 der Fremdleser-Prüfung |
| Absatz ohne Konsequenz | Zeile *Aufbau* endet mit der Konsequenz, Frage 3 der Fremdleser-Prüfung |
| Pronomen und unbestimmte Nominalphrasen ohne Bezug | Frage 2 der Fremdleser-Prüfung, Suchmuster U3 und U4 |
| Fachliche Pauschalisierung | Zeile *Nicht sagen*, Stilregel 9 |

---

## 7 Kommentardurchgang des Verfassers, seit 16.09.2026

Nach der Neufassung eines Kapitels liest der Verfasser den Text selbst und
kommentiert ihn. Dafuer erzeugt Claude eine Kommentardatei je Kapitel, fuer
Kapitel 3 `KOMMENTARE_KAP3.md`, mit dem gerenderten Text als nummerierte
Absaetze und Saetze und einem Feld *Kommentar* unter jedem Absatz. Die Datei
ersetzt die Aenderungslisten aus `archiv/` als Vorlage.

Ablauf:

1. Der Verfasser traegt seine Kommentare in die Felder ein, in freier Form:
   Streichungen, neue Saetze, Verbindungen, inhaltliche Hinweise und die
   Entscheidungen zu den offenen Vorschlaegen aus `DURCHSICHT_KAP1_3.md`
   (Kennung und ja oder nein). Absaetze ohne Aenderung bleiben leer.
2. Claude liest allein die Kommentardatei und arbeitet Absatz fuer Absatz
   ein. Kommentare des Verfassers haben Vorrang vor den Vorschlaegen der
   Durchsicht. Trifft ein Kommentar einen Absatz, zu dem ein offener
   Vorschlag steht, gilt der Kommentar, und der Vorschlag entfaellt, sofern
   der Verfasser ihn nicht ausdruecklich annimmt.
3. Inhaltliche Hinweise ohne Wortlaut formuliert Claude nach den Stilregeln
   und legt den neuen Absatz im Sammelmodus vor, bevor er in die Datei geht.
   Wortlaut des Verfassers geht unveraendert in die Datei, nur gegen die
   Pruefsuite geprueft.
4. Nach jedem Unterabschnitt Pruefsuite, Build und Protokolleintrag, Commit
   je Kapitel. Keine Subagenten in diesem Schritt, die Fremdleser-Pruefung
   entfaellt, weil der Verfasser selbst liest.
5. Die Kommentardatei wird nach der Einarbeitung nach `archiv/` verschoben,
   die Kommentare stehen dann im Protokoll.

---

## 10 Arbeitsweise am Absatz, aus dem Durchgang vom 20. bis 22.09.2026

Diese Regeln sind aus dem Durchgang durch die Kapitel 1 bis 3 mit dem
Verfasser abgeleitet und gelten für jede Sitzung, unabhängig vom Modell. Sie
sollen zwei Schwächen abfangen, die der Verfasser bei früheren Sitzungen
beobachtet hat: schwammige, wenig präzise Formulierungen und das Verharren an
einer Stelle über mehrere Iterationen, ohne den Absatz als Ganzes neu zu
denken.

### 10.1 Bevor ein Satz geändert wird

1. **Den Absatz als Ganzes lesen, mit Vor- und Folgeabsatz.** Der schnellste
   Weg ist `python tools/extract_alle.py`, das die Kapitel 1 bis 3 als
   nummerierte Absätze nach `%TEMP%\kap{n}_text.txt` schreibt. Vor der
   Änderung in einem Satz benennen, welche Kernaussage der Absatz trägt und
   welche Sätze er dafür braucht. Was er nicht braucht, ist ein
   Streichkandidat, auch wenn der Verfasser nur einen einzelnen Satz
   beanstandet hat.
2. **Jede Behauptung an der Quelle prüfen, bevor sie steht oder bleibt.**
   `pdftotext` auf die PDF in `literature/PDFs`, dann `grep` nach dem
   Begriff. Steht der Begriff oder die Zahl in keiner Quelle, wird das gesagt
   und der Satz auf das gestützt, was die Quelle trägt. Am 21.09.2026 stand
   eine "Anreizkomponente" mit Zitat im Text, die in keiner Quelle vorkam.
3. **Begriffe auf ihre erste Verwendung prüfen** (`grep -n` über die
   Kapiteldatei ohne Kommentarzeilen). Ein Begriff vor seiner Definition ist
   ein Befund, auch wenn er nicht Gegenstand der Anweisung war.
4. **Anweisungen aus dem Modellrepository an der Datei dort lesen**, nicht an
   der Kopie im Chat; die Datei kann zwischen Kopie und Umsetzung geändert
   worden sein.

### 10.2 Wie geantwortet wird

5. **Befund, dann Wortlaut, dann Empfehlung.** Auf "verstehe ich nicht" oder
   "was heißt das" folgt die Sache in zwei bis drei Sätzen und sofort der neue
   Wortlaut des Absatzes oder Satzes. Höchstens zwei Fassungen, die empfohlene
   zuerst, mit dem Grund in einem Satz. Nie drei Varianten, nie eine Frage
   ohne Vorschlag.
6. **Präzise statt vorsichtig.** Kein *in gewisser Weise*, *unter Umständen*,
   *kann dazu beitragen*, *tendenziell*. Wo eine Aussage abgeschwächt werden
   muss, wird gesagt, warum (fehlende Quelle, Randbedingung), und die
   Abschwächung steht in einem Wort (*dürfte*, *nach Angabe von*), nicht in
   einer Wolke. Zahlen tragen Bezugsgröße und Einheit. Ein Satz hat einen
   Hauptsatz und höchstens einen Nebensatz.
7. **Die Vorgabe des Verfassers in Tippschreibweise wird in einem Satz
   wiederholt**, wenn sie mehrdeutig ist, und im selben Zug umgesetzt.
   Rückfragen nur, wenn die Entscheidung tatsächlich seine ist (Streichen
   oder Umformulieren, Wahl zwischen zwei Abbildungen). Alles andere nach
   seiner Vorgabe vom 21.09.2026: "Unsichere immer mit deinem Vorschlag."
8. **Widerspricht seine Vorgabe der Quelle, zuerst die Quelle zeigen**, mit
   Fundstelle, und dann umsetzen, was er entscheidet. Die Einordnung steht im
   Protokoll.

### 10.3 Wenn eine Stelle nicht besser wird

9. **Nach der zweiten Iteration am selben Satz die Ebene wechseln.** Der
   Fehler liegt dann fast nie im Satz, sondern im Aufbau: Der Satz gehört in
   einen anderen Absatz, die Definition steht am falschen Ort, der Absatz
   erzählt in der falschen Reihenfolge, oder die Aussage gehört in den Anhang.
   Beispiele vom 21.09.2026: Das Fünf-Zustands-Modell in 2.1.1 ließ sich nicht
   kürzen, bis der Punkt (präventiv hält den PATL, kurativ den TATL, beide im
   Normalzustand) als zwei Sätze an die Abbildung 2.1 wanderte, wo beide
   Grenzwerte definiert sind. Die Regelleistungsvergütung in 2.3.4 wurde erst
   klar, als der Absatz entlang der Staffelung (Zuschlag der Leistung, dann
   Regelarbeitsmarkt, Merit-Order, Grenzpreis) neu aufgebaut wurde. Der
   Konsultationsbefund in 2.3.3 war nicht zu retten und ging nach Anhang A.
10. **Eine Dopplung wird an der Stelle aufgelöst, die sie für ihre Erklärung
    nicht braucht**, nicht an der ersten Fundstelle. Kapitel 1 darf als
    Motivation wiederholen, ein Zwischenfazit darf zusammenfassen; kritisch ist
    die Wiederholung in einem Absatz, der sie nicht braucht.
11. **Ein Satz, der zwei Dinge sagen soll, wird geteilt oder gestrichen.**
    Am 21.09.2026 fielen zwei Sätze zur Inc-Dec-Abgrenzung, weil ihr Gegensatz
    (Eingriff gegen Vorhaltung) das Argument nicht trug; der Satz davor trug
    die Anforderung bereits.

### 10.4 Nach der Änderung

12. Differenz der Fließtextzeilen vor und nach der Änderung ausgeben,
    Prüfsuite, Build, Seitenlage (`pdfinfo`, Anfang von Kapitel 1, 2 und 3),
    die neue Passage im Chat zeigen, Protokolleintrag mit dem gestrichenen
    Wortlaut. Committen nur auf "commite".
