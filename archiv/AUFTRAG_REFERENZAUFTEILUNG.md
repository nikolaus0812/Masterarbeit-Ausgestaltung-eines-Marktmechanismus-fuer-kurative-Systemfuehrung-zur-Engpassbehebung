# Auftrag: Aufteilung des Referenzerlöses in der Zukunftsvariante

**Stand 23.09.2026.** Absender ist die Schriftfassung, Adressat ist das
Analyse-Repository `bess_dispatch_optimization`.

Dies ist die Antwort auf den Vorbehalt am Ende von
`ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` Abschnitt 7.13: *„Sagt Bescheid, wenn sie
gebraucht wird."* Sie wird gebraucht.

---

## 1 Warum

Abschnitt 4.6.4 der Arbeit beschreibt, wie sich der Erlös der Bezugsanlage
verändert, wenn die Preise am \ac{IDC} und an der aFRR auf 80 und die der FCR
auf 90 Prozent sinken. Die Summen stehen im Text, nämlich 340,6 auf 281,4 und
420,0 auf 352,0 Tsd. €/(MW·a).

**Die Aussage über die Verschiebung zwischen den Märkten steht dagegen auf dem
Marktrest der ersten Iteration.** Das ist das, was eine Suche übrig lässt, von
der Abschnitt 4.2 belegt, dass sie gerade die teuren Stunden offen lässt. Als
Beleg für die Frage, wie sich die Erlösstruktur einer Anlage verschiebt, ist
das der falsche Gegenstand.

Die eigentliche Frage lautet: **Bleibt die Bezugsanlage in der Zukunftswelt
eine Regelleistungsanlage?** Heute tragen Leistung und Arbeit der aFRR 76,6
Prozent des Bruttoerlöses, und Abschnitt 4.2 stützt darauf die Aussage, die
Anlage halte im Referenzfall vor allem Regelleistung und handle daneben am
\ac{IDC}. Ob dieser Satz auch unter niedrigeren Preisen gilt, entscheidet die
Aufteilung des Referenzerlöses und nichts sonst.

---

## 2 Was gebraucht wird

**Die Aufteilung des Referenzerlöses der Zukunftsvariante nach Märkten**, im
selben Zuschnitt wie für das Jahr 2025 in Abschnitt 1 der Ergebnisdatei, also
aFRR-Leistung, \ac{IDC}, aFRR-Arbeit, Day-Ahead, FCR, Bruttoerlös, Degradation
und Nettoerlös, in Tsd. €/(MW·a) und in Anteilen am Bruttoerlös.

Nach Abschnitt 7.13 verlangt das eine eigene Rechnung von rund 25 Minuten,
weil `erloesaufteilung_jahr_2025.parquet` nur für den Basisfall vorliegt.
Dieser Aufwand ist aus Sicht der Schriftfassung gerechtfertigt.

### 2.1 Zur Abbildung

**Kein neues Bild.** Die Aufteilung gehört in die vorhandene Abbildung
`sensi_zukunft_erloes_2025.pdf`, deren beide Referenzbalken bisher ungeteilt
sind. Der Vorbehalt des Analyse-Repositorys war richtig: eine Teilung nur am
linken Balken lüde zu einem Vergleich ein, den die Abbildung nicht trägt.
Genau deshalb sind **beide** Referenzbalken zu teilen oder keiner.

Ob auch die beiden Balken der Vollverdrängung eine Teilung tragen, entscheidet
das Analyse-Repository. Dort ist der Markterlös in der zweiten Iteration null,
sodass eine Teilung dort vermutlich nichts zeigt.

Kapitel 4 trägt zwölf Abbildungen, eine dreizehnte ist unerwünscht.

### 2.2 Zu den Zahlen

In `ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md`, im Format des dortigen Abschnitts 1,
damit sich beide Welten nebeneinander lesen lassen. Zwei Zahlen sind für den
Text besonders von Belang:

1. **Der Anteil der aFRR am Bruttoerlös**, Leistung und Arbeit zusammen, in
   beiden Welten. Heute 76,6 Prozent.
2. **Der Anteil des Day-Ahead**, heute 7,3 Prozent. Steigt er in der
   Zukunftswelt deutlich, so verschiebt sich die Anlage vom Vorhalten zum
   Handeln, und das wäre ein Befund für die Diskussion.

---

## 3 Was nicht gebraucht wird

Keine Deutung der Verschiebung. Dass der Day-Ahead relativ stärker wird, weil
die übrigen Märkte gesenkt sind, ist eine Rechenfolge und steht im Text als
solche. Die Formulierung aus Abschnitt 7.13, der Day-Ahead gewinne, obwohl er
gar nicht verändert wurde, ist **nicht** in die Arbeit übernommen worden, weil
sie eine erwartbare Folge als Befund darstellt.

Interessant ist allein, **wie groß** die Verschiebung ausfällt, und ob sie den
Satz aus Abschnitt 4.2 über den Charakter der Anlage berührt.

---

## 4 Dringlichkeit

Nachrangig. Abschnitt 4.6.4 steht ohne die Aufteilung, und der Text nennt die
Verschiebung bereits mit den Zahlen des Marktrests. Die Lieferung würde den
Beleg von einem Nebenprodukt auf den Referenzfall stellen und die Aussage
damit tragfähig machen.
