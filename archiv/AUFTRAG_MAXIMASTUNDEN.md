# Auftrag: woher die Maxima des kurativen Reservierungspreises kommen

**Stand 23.09.2026.** Absender ist die Schriftfassung, Adressat ist das
Analyse-Repository `bess_dispatch_optimization`.

---

## 1 Warum

Abschnitt 4.3 beschreibt die Verteilung des kurativen Reservierungspreises und
sagt bisher nur, **dass** sie rechtsschief ist. Die Maxima von 1008 €/(MW·h)
entladend und 510 €/(MW·h) ladend stehen als Einzelwerte da, ohne Erklärung.

Vorgabe des Verfassers vom 23.09.2026: *„haben wir zudem mal geguckt woran das
liegt und welcher markt immer als letzter verdrängt wird für die maxima stunden,
damit wir es auch begründen können"*.

Der Text soll die Spitze der Verteilung also nicht nur zeigen, sondern
zurückführen. Ohne diese Zurückführung bleibt die Aussage beschreibend, und
genau das ist bei den Ausreißern bisher der Fall. Vergleichbares steht in
`ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` Abschnitt 8 offen, dort für den
Grenzpreis-Ausreißer von 4687 €/(MW·h).

---

## 2 Was gebraucht wird

Betrachtet werden die teuersten Stunden des Jahres 2025 unter der zweiten
Iteration, je Richtung. Vorschlag für den Zuschnitt: die 20 teuersten Stunden
je Richtung, mindestens aber alle Stunden oberhalb des 99-Prozent-Quantils von
173 €/(MW·h) entladend und 161 €/(MW·h) ladend.

1. **Welcher Markt hält in diesen Stunden die Leistung?** Also die Aufteilung
   der Leistung auf aFRR-Leistung, FCR, aFRR-Arbeit, Day-Ahead und IDC im
   Referenzfall dieser Stunden, gemittelt über die betrachteten Stunden und
   verglichen mit dem Jahresmittel.
2. **Welcher Markt weicht in diesen Stunden zuletzt?** Die Frage entspricht
   Abschnitt 2.1 der Ergebnisdatei, nur nicht über Analysetage, sondern über
   die teuersten Stunden.
3. **Woran liegt die Höhe?** Erwartbar sind zwei Ursachen, nämlich ein
   ungewöhnlich hoher Preis eines einzelnen Marktes in dieser Stunde oder eine
   Kopplung über das Ladezustandsband, bei der die Reservierung einer Stunde
   Geschäfte in benachbarten Stunden verhindert. Falls die Daten zwischen
   beiden unterscheiden lassen, bitte sagen, welche der beiden trägt.
4. **Wann liegen diese Stunden?** Datum und Tagesstunde der zehn teuersten
   Stunden je Richtung, damit sich der Befund gegen das Zeitmuster aus
   Abschnitt 4.4 halten lässt.

Keine Abbildung nötig. Eine Tabelle und drei bis fünf Sätze in
`ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` reichen, denn der Befund soll in den
Fließtext des Abschnitts 4.3 und nicht in ein eigenes Bild.

---

## 3 Was nicht gebraucht wird

Keine neue Rechnung, wenn die Antwort nicht aus den vorhandenen Zeitreihen
fällt. Sollte ein neuer Lauf nötig sein, bitte zuerst den Aufwand melden.
Vorrang hat weiterhin `sensi8_spanne_und_niveau`, auf das die Abschnitte 4.6.3
und 4.6.4 warten.

---

## 4 Antwort auf Update 5, Abschnitt 5

Zur gehandelten Energie ist **Weg 1 gewählt**, also getrennte Blöcke für
gehandelte Arbeit (Day-Ahead, IDC, aFRR-Arbeit) und vorgehaltene Leistung
(aFRR-Leistung, FCR, kurativ) in einer Tabelle mit zwei Überschriften.

Der Grund ist derselbe, aus dem die Arbeit an anderer Stelle Leistungspreis und
Arbeitspreis auseinanderhält: in Abschnitt 4.5 steht ausdrücklich, dass der
Arbeitspreis des präventiven Redispatch und der kurative Reservierungspreis
dimensionsgleich sind, aber nicht dasselbe meinen, und dass die Abbildung sie
deshalb nebeneinanderstellt, statt sie gegeneinander aufzurechnen. Eine Spalte,
die vorgehaltene und gehandelte Energie vermischt, würde diese Trennung wieder
einreißen.

---

## 5 Erledigt und übernommen

- Die Füllgradabbildung liegt in `figures/chapter_4/` und steht als
  Abbildung 4.2 im Text, mit dem Hinweis auf die abgeschnittene Ordinate in der
  Bildunterschrift.
- Die berichtigten Füllgrade 85,94 und 89,60 Prozent stehen im Text, ebenso die
  25,9 und 23,1 Prozent nicht voll reservierter Stunden. Die zweite Iteration
  ist als *bis auf die Stunde der Zeitumstellung voll reserviert* beschrieben.
- Der Rechenaufwand steht als Verhältnis im Text, nämlich gut das Dreifache
  aus 432 zu 136 Läufen im Median. Abschnitt 3.2.4 bleibt unverändert, denn
  die dortigen 84 bis 167 Läufe liegen innerhalb der gemessenen 83 bis 194.
- Die Berichtigung in Abschnitt 2.3 ist zur Kenntnis genommen. Der Text nennt
  an der betroffenen Stelle weiterhin den 26.08.2025.
