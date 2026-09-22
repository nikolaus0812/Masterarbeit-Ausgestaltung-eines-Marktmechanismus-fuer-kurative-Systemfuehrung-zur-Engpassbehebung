# Rückmeldung an den Chat des Analyse-Repositorys

**Stand 22.09.2026, abends.** Gegenstück zu
`UEBERGABE_AN_SCHRIFTFASSUNG.md`. Der Nachtrag zur Bezugslinie des präventiven
Redispatch ist eingearbeitet, zwei der Rückfragen sind damit erledigt. Der
Abschnitt *Der Text zum Kopieren* ist zum Hineinkopieren in den anderen Chat
gedacht. Geschrieben wurde ausschließlich in der Schriftfassung; im
Analyse-Repository ist nur gelesen worden.

---

## Der Text zum Kopieren

Die Anweisung vom 22.09.2026 ist umgesetzt. Kapitel 4 trägt die neue
Gliederung, alle neun Abbildungen sind eingebunden, der Fließtext ist
geschrieben. Build ohne Fehler, 104 Seiten, Kapitel 4 auf PDF-Seite 57 bis 69.
Keine Zahl ist aus einer Abbildung abgelesen.

**Offen geblieben, wie verlangt:** 4.6.3 Handelsspanne am IDC, 4.6.4 Zukünftig
niedrigere Preise und die Diskussion. Sie stehen als bloße Überschriften im
PDF und warten auf `sensi8`.

### 0 Der Nachtrag zur Bezugslinie ist eingearbeitet

Abschnitt 4.5 trägt jetzt den Nenner mit beiden Richtungen, nämlich
12,15 TWh Erhöhung und 18,30 TWh Absenkung, und daraus 101 Euro **je
bewegter Megawattstunde, gemittelt über beide Richtungen**. Dazu stehen im
Text: dass der Nenner nicht halbiert wird, weil die Reihe nicht symmetrisch
ist; die vier denkbaren Nenner mit 101, 168, 202 und 253 Euro je
Megawattstunde; die Zuordnung des Unterschieds von 6,15 TWh (erneuerbare
Anlagen 9,50 auf der Absenkungsseite, konventionelle Anlagen und Speicher netto
3,35 hochfahrend, Countertrading mit 2,50 ohne Gegenposten an der dänischen
Grenze, Redispatch im engeren Sinn mit 1,17 nahezu ausgeglichen); und die
Einschränkung, dass eine Aufteilung nach Richtung nicht möglich ist, weil die
Mengen je Richtung, die Kosten aber nur als Summe vorliegen. Der verbleibende
Anteil ist dem Einspeisemanagement zugeschrieben und **ausdrücklich als
Vermutung gekennzeichnet**.

**Zur Korrektur aus dem Nachtrag:** Die Aussage, der Überhang sei die
EE-Abregelung von 9,4 TWh, ist nie in die Arbeit gelangt. Weder Kapitel 4
noch das Entscheidungsprotokoll noch diese Rückmeldung haben sie je enthalten,
es ist dort also nichts zurückzunehmen.

**Abbildungen nachgeholt:** Jahreslauf Median und Mittel vom 22.09. 12:05 und
Zeitmuster vom 22.09. 11:14. Das Zeitmuster zeigt jetzt Median und
arithmetisches Mittel mit Band; die Bildunterschrift ist entsprechend neu
gefasst, und der Satz über die „dritte Kurve“ im Text ist berichtigt.

### 1 Sechs Stellen, an denen ich anders entschieden habe

Jeweils: was die Anweisung sagt, was in der Arbeit steht, warum.

**1.1 Abschnittsnummern: 4.6 und 4.7 statt 4.7 und 4.8.**
Die Anweisung streicht in Abschnitt 1 den bisherigen Abschnitt 4.6 und nennt
zugleich die Sensitivitäten 4.7 und die Diskussion 4.8. Beides zusammen ginge
nur mit einer Lücke in der Nummerierung, und eine übersprungene Nummer liest
sich in einer Prüfungsarbeit als Fehler. LaTeX zählt deshalb fortlaufend: die
Sensitivitäten sind 4.6, die Diskussion ist 4.7. Die Marken tragen die Sache
und nicht die Nummer (`sec:sensitivities`, `sec:sensi_afrr`,
`sec:sensi_abrufdauer`, `sec:sensi_idc`, `sec:sensi_zukunft`,
`sec:results_discussion`), sodass spätere Verweise stabil bleiben. **Wenn die
Nummern 4.7 und 4.8 gewollt sind, bitte melden** — dann bräuchte es einen
Grund für die Lücke.

**1.2 Der Arbeitspreis des präventiven Redispatch steht mit 3071 Mio. Euro
im Text, nicht mit 3,08 Mrd. Euro.**
Die Anweisung nennt in Abschnitt 4.5 Kosten von 3,08 Mrd. Euro. Die Quelle,
die die Arbeit dafür führt, ist die Mitteilung der Bundesnetzagentur zum
Netzengpassmanagement 2025; sie weist **3071 Mio. Euro** als vorläufige
Gesamtkosten aus, also 3,07 Mrd. Eine Zahl, die die zitierte Quelle nicht
trägt, darf nicht mit ihr belegt werden, deshalb folgt der Text der Quelle.
Der ausgewiesene Arbeitspreis von 101 Euro je Megawattstunde ist in beiden
Lesarten derselbe, die Aussage ändert sich also nicht.

**1.3 Der Saisonbefund steht beschreibend statt wertend.**
Die Anweisung und `AUFBAU_KAPITEL_4.md` formulieren ihn als „dort liegt das
Einsparpotenzial". Kapitel 4 beschreibt und bewertet nicht; die Bewertung
gehört nach Kapitel 5, weil sie den Nutzen der Maßnahme voraussetzt, den
Kapitel 4 nicht bestimmt. Im Text steht deshalb: die Jahreszeit mit dem
größten Engpassmanagementbedarf ist zugleich die Jahreszeit mit der
günstigsten Reservierung. Die Zahlen dahinter sind unverändert übernommen
(Winter 14,55 gegen Herbst 33,70 Euro je Megawatt und Stunde, Redispatch hoch
2314 gegen 1767 MW).

**1.4 Die einteilige Jahreslauffassung ist gelöscht, obwohl sie in Abschnitt 3
nicht genannt ist.**
`jahreslauf_reservierungspreis_redispatch_2025.pdf` steht in keiner der vier
Löschgruppen. Abschnitt 2 weist die beiden neuen Fassungen `_median` und
`_mittel` aber ausdrücklich als Ersatz der einteiligen Fassung aus, und eine
unbenutzte Datei im Abbildungsordner wäre eine Fehlerquelle. Sie ist deshalb
mit entfernt.

**1.5 Tabelle 4.1 entfällt ersatzlos.**
Die bisherige Kennzahlentabelle des Reservierungspreises ist in der neuen
Gliederung gegenstandslos, weil `verteilung_reservierungspreis_2025.pdf` genau
diese Kennzahlen trägt. Die Anweisung sagt das nicht ausdrücklich, es folgt
aber aus Abschnitt 4.3. Damit hat Kapitel 4 keine Tabelle mehr.

**1.6 Der Kapiteltitel ist unverändert geblieben.**
Er lautet weiter *Exemplarische Anwendung und Ergebnisse*. Die Anweisung
äußert sich nicht dazu. Das Wort *exemplarisch* trifft nicht mehr, weil das
ganze Jahr 2025 gerechnet ist und das Exemplarische inzwischen in Kapitel 3
steht. Geändert habe ich es nicht, weil der Titel eine Entscheidung des
Verfassers ist. **Vorschlag: *Der kurative Reservierungspreis*.**

### 2 Vier Punkte der Anweisung, die nicht mehr zum Bestand passten

Die Anweisung ist gegen einen etwas älteren Stand der Schriftfassung
geschrieben. Für die nächste Lieferung zur Kenntnis:

1. **Abschnitt 3b** nennt `sensi_afrr_modellierung.pdf` und
   `sensi_afrr_modellierung_alle.pdf` zur Löschung. Beide Vier-Tage-Fassungen
   lagen in der Schriftfassung nie.
2. **Abschnitt 3d** verlangt, `fuellgrad_iterationen_2025.pdf` und
   `maximalpreis_iterationen_2025.pdf` aus `figures/chapter_4/` nach
   `figures/chapter_3/` zu verschieben. Das ist am 21.09.2026 bereits
   geschehen. Beide liegen dort, sind aber **weiterhin in keiner
   figure-Umgebung** — sie werden also nirgends gezeigt. Das deckt sich mit
   Abschnitt 3d, wonach der Füllgradvergleich im Ergebnisteil nicht erscheint.
   Falls einer der beiden als Anhangbeleg gewünscht ist, bitte sagen.
3. **Abschnitt 3c** nennt `dispatch_festpreis_2025-02-11_p5_ohne_mindestgebot.pdf`.
   Die Datei liegt nicht vor, und der zugehörige Anhang ist am 21.09.2026
   stillgelegt. Nichts zu tun.
4. **Die Legende der Jahreslauf-Abbildung ist repariert.** Der am 21.09.2026
   gemeldete Befund (abgeschnittener Eintrag „präventiver Redispatch,
   101 €/MWh (Arbeitspreis …)") tritt in den beiden neuen Fassungen nicht mehr
   auf. Erledigt.

### 3 Rückfragen

1. **Fehlende Zahlen zu 4.5.** `AUFBAU_KAPITEL_4.md` führt unter 4.5 als noch
   zu rechnen: „Anteil der Tage **und Stunden** unter 101 €/MWh, je Richtung
   **und je Jahreszeit**". `ERGEBNISSE…md` Abschnitt 7.4 liefert die Tage
   (365/365 im Median, 362/365 und 364/365 im Mittel). Die **Stunden** unter
   der Linie und die **Aufteilung je Jahreszeit** fehlen. Im Text stehen
   deshalb nur die Tageszahlen. Werden die beiden anderen Größen nachgeliefert?
2. ~~Beleg der bewegten Menge.~~ **Erledigt durch den Nachtrag.** Der Text
   nennt jetzt 12,15 und 18,30 TWh je Richtung statt der Summe von 30,44.
   Offen bleibt allein, ob die beiden Richtungsmengen eigens zu belegen sind;
   die zitierte Mitteilung der Bundesnetzagentur führt für 2025 ein
   Maßnahmenvolumen von 30.319 GWh und keine Aufteilung nach Richtung.
3. ~~Das Zeitmuster ist nach der Anweisung noch einmal geändert worden.~~
   **Erledigt.** Die Fassung vom 22.09. 11:14 ist geholt, die Bildunterschrift
   nennt jetzt Median, arithmetisches Mittel und das Band dazwischen. Der Text
   selbst arbeitet weiter allein mit den Medianen aus `ERGEBNISSE…md`
   Abschnitt 7.2. **Falls die Mittelwerte je Stunde und je Monat im Text
   stehen sollen, fehlen sie in Abschnitt 7.** Alle neun Abbildungen des
   Kapitels sind jetzt größengleich mit dem Lieferordner.
4. **Nummerierung**, siehe 1.1.
5. **Kapiteltitel**, siehe 1.6.

### 4 Was sonst noch geschrieben wurde

**Abschnitt 3.3.2** ist nach Abschnitt 7 der Anweisung nachgezogen. Die Werte
vom 21.09.2026 gelten unverändert (340,7; Faktor 1,31; Spanne 1,04 bis 1,50;
Korrelation 0,974; alle zwölf Monate; FCR 1,24; aFRR 1,51; DA 0,85). Neu ist
die Aufteilung des Intraday-Handels in **ID1 0,97** und **IDC 0,89**; bisher
stand dort ein einzelner Wert. Ergänzt ist der Revenue-Index mit 260,0, damit
sich das Verhältnis von 1,31 nachrechnen lässt.

**Die Preisgitterseiten** stehen seit dem 22.09.2026 als eigener Anhang in der
Arbeit, und Abschnitt 4.1 verweist an genau einer Stelle darauf, wie
`ERGEBNISSE…md` Abschnitt 6 es vorsieht. Die Aussagen aus Abschnitt 2.3 stehen
im Fließtext und nicht in der Bildunterschrift.

**Übernommen sind auch die Vorbehalte** aus `ERGEBNISSE…md` Abschnitt 8: dass
der FCR-Befund nur die vier gerechneten Tage trägt, dass die
Verdrängungsreihenfolge an allen vier Tagen gleich ist und sich allein die
Schwellenpreise um den Faktor zehn unterscheiden, dass der Grenzpreis-Ausreißer
von 4687 Euro je Megawatt und Stunde ein nicht untersuchter Einzelwert ist und
dass „ohne aFRR" Leistung und Arbeit nicht trennt.
