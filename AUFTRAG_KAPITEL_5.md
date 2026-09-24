# Auftrag: Kapitel 5, Bewertung und Diskussion

> **Teilweise erledigt am 24.09.2026.** Abschnitt 8 ist abgearbeitet:
> die vier Fragen sind dem Verfasser gestellt und beantwortet, die
> Gliederung steht in Fassung A mit acht Abschnitten, und die
> Stichpunkte aller 31 Absaetze stehen in `chapters/chapter_5.tex`.
> **Der dort vorgeschlagene Strukturvorschlag ist damit ueberholt.**
> Die Abschnitte 1 bis 7 bleiben die Lesekarte fuer die
> Ausformulierung, ebenso Abschnitt 9 mit den Dingen, die nicht zu
> tun sind. Der Stand steht im Protokoll unter `## chapter_5.tex`
> und in `HANDOFF.md` Abschnitt 7a.
>
> Zwei Annahmen dieser Datei haben sich als falsch erwiesen. Der
> Anforderungskatalog ist **keine** Dopplung zur Ergebnisdiskussion,
> denn Anforderung A7 liefert den schaerfsten Befund. Und die
> Saettigung des Marktes fuer FCR ist **belegt**, naemlich mit 810 MW
> praequalifizierter BESS-Leistung in Abschnitt 2.3 gegen 564 MW
> deutschem Bedarf in Abschnitt 2.2.3.

Angelegt am 23.09.2026 abends von der Sitzung, die Kapitel 4 geschrieben hat.
Adressat ist ein **neuer Chat**, der am 24.09.2026 mit dem Verfasser Kapitel 5
schreibt. Diese Datei ist die Lesekarte. Sie nennt jede Fundstelle, damit du
nicht suchen musst.

---

## 0 Das Wichtigste in zehn Zeilen

Die Arbeit bestimmt den **kurativen Reservierungspreis**, also den Betrag, den
ein Betreiber für die Vorhaltung mindestens fordern muss, um mit der
Reservierung genauso viel zu verdienen wie ohne sie. Kapitel 4 ist fertig und
mit dem Verfasser Absatz für Absatz durchgegangen. Kapitel 5 diskutiert diese
Ergebnisse. Der Verfasser will **alle** Ergebnisse diskutiert sehen, dazu
ihre Folgen für die Betriebsführung, mögliche Entwicklungen im
Engpassmanagement und am Markt, ein eigenes Kapitel zur Zukunft von
Batteriespeichern im Engpassmanagement und am Ende eine Diskussion der
kurativen Systemführung im Allgemeinen, aus der der weitere Forschungsbedarf
und der Erkenntnisbedarf aus Projekten folgt.

**Erste Handlung:** nicht schreiben, sondern lesen und nachvollziehen. Danach
legst du dem Verfasser einen Strukturvorschlag vor und fragst ihn gezielt.

---

## 1 Lesereihenfolge, mit Aufwandsschätzung

Lies in dieser Reihenfolge. Die Klammer nennt, wie viel du wirklich brauchst.

| Nr | Datei | was davon |
|---|---|---|
| 1 | `CLAUDE.md` | **ganz.** Rollen, Stilregeln 1 bis 17, gesperrte und verbindliche Begriffe, Prüfungen, Einheiten, Dateihandhabung. Bindet dich vollständig. |
| 2 | `HANDOFF.md` | **ganz.** Besonders Abschnitt 3 (bindende Entscheidungen), Abschnitt 6 (offene Punkte) und **Abschnitt 7, der die Sammlung der Diskussionspunkte aus Kapitel 4 ist**. |
| 3 | `WORKFLOW.md` | Abschnitte 3, 7 und 10. Absatzplan, Kommentardurchgang, Arbeitsweise am Absatz. |
| 4 | diese Datei | ganz |
| 5 | `chapters/chapter_4.tex` | **nur den Fließtext**, siehe Abschnitt 2. Die Datei hat gut 1100 Zeilen, davon ist etwa die Hälfte Kommentar mit zurückgenommenen Fassungen. |
| 6 | `chapters/chapter_5.tex` | **ganz**, 318 Zeilen. Der bestehende Gerüstzustand, siehe Abschnitt 5. |
| 7 | Anhänge | nur die in Abschnitt 3 genannten, und nur wenn du die Zahl brauchst. |
| 8 | Analyse-Repository | nur die in Abschnitt 4 genannten Stellen. **Lesend, niemals schreibend.** |

`ENTSCHEIDUNGSPROTOKOLL.md` hat über 19 000 Zeilen und wird **nie ganz
gelesen**. Suche gezielt mit `grep -n`, wenn du wissen willst, warum eine
Formulierung so steht.

### So liest du Kapitel 4 ohne Ballast

```
grep -v "^%" chapters/chapter_4.tex | grep . > /tmp/kap4.txt
```

Das ergibt etwa 200 Zeilen reinen Fließtext samt Gleitumgebungen. Jede Zeile
ist genau ein Satz. **Lies das vollständig**, es ist der Gegenstand deiner
Diskussion. Danach kennst du jede Aussage, die zu diskutieren ist.

---

## 2 Was Kapitel 4 sagt, Abschnitt für Abschnitt

Diese Übersicht ist zur Orientierung. **Sie ersetzt das Lesen nicht**, denn du
sollst jede Aussage selbst nachvollziehen.

| Abschnitt | Gegenstand | Abbildungen |
|---|---|---|
| Kapiteleinleitung | Fragestellung, Einheitenkonvention: Preise in €/(MW·h), Erlöse in Tsd. €/(MW·a) | — |
| 4.1 Verlauf des Dispatch und Verdrängung der Märkte | fünf Analysetage unter zehn vorgegebenen Preisen von null bis 200 €/(MW·h); welche Vermarktung wann weicht | Fahrpläne in Anhang F |
| 4.2 Preise beider Iterationen und Erlöswirkung | Aufteilung des Referenzerlöses nach Märkten; erste gegen zweite Iteration; Füllgrad je Tagesstunde | 4.1, 4.2 |
| 4.3 Verteilung der Verdrängungspreise | Rechtsschiefe, Median gegen arithmetisches Mittel, Quartile, Quantile, Maxima | 4.3 |
| 4.4 Zeitliches Muster | Heatmap je Stunde und Kalendertag, Tages- und Jahresgang, Ursachen | 4.4, 4.5 |
| 4.5 Kurativer Reservierungspreis und Engpassbedarf | Preis gegen Engpassmanagementbedarf über Tag und Jahr, Bezugslinie 101 €/MWh | 4.6, Anhang H |
| 4.6 Sensitivitäten | 4.6.1 Modellierung der aFRR, 4.6.2 Abrufdauer, 4.6.3 Handelsspanne am IDC, 4.6.4 Zukünftig niedrigere Preise | 4.7 bis 4.11 |

**Die tragenden Zahlen des Basisfalls**, damit du sie beim Lesen erkennst:
Median des kurativen Reservierungspreises 12,22 €/(MW·h) entladend und
9,85 €/(MW·h) ladend, arithmetisches Mittel 23,64 und 24,33 €/(MW·h), Maxima
1008 und 510 €/(MW·h). Referenzerlös 340,6 Tsd. €/(MW·a), Zahlung bei
vollständiger Verdrängung 420,0 Tsd. €/(MW·a).

**Der einheitliche Erklärungsmechanismus des Kapitels**, in der Bearbeitung
entstanden und mehrfach geprüft: der **Leistungspreis der aFRR bestimmt das
Niveau**, denn er entfällt mit der reservierten Stunde vollständig, weil die
aFRR ein Blockprodukt ist. Die **Arbitrage an den Energiemärkten ist dagegen
zwischen den Stunden eines Tages verschiebbar**, solange der Tag eine tiefe
Staffel gleichwertiger Spannen trägt. Der Energiemarkt setzt den Preis nur
dort, wo diese Staffel einbricht, nämlich an jedem zwanzigsten Tag des Jahres.
Dieser Mechanismus erklärt die wechselnde Verdrängungsreihenfolge in 4.1, die
offenen Stunden in 4.2 und die Maxima in 4.3 mit einer Ursache. **Er ist der
rote Faden, an dem die Diskussion ansetzen kann.**

---

## 3 Anhänge

| Anhang | Inhalt | wann du ihn brauchst |
|---|---|---|
| A | modifizierter Weber-Ansatz, Abbildung A.1; letzter Absatz trägt den Konsultationsbefund | 5.1, Verhältnis zur Festlegung |
| B | zulässige Überlastdauer einer Freileitung | wenn du über Reaktionszeit und Bindungsdauer argumentierst |
| C | vollständiges Optimierungsproblem | kritische Würdigung der Modellannahmen |
| D | Ablauf der zwei Iterationen, Abbildung D.1 | Zeitscheibenproblem |
| E | Validierung je Markt gegen den Revenue-Index | Belastbarkeit des Modells |
| F | Fahrpläne der fünf Analysetage | 4.1 nachvollziehen |
| G | Jahreslauf mit dem Median statt dem Mittel | 4.5 nachvollziehen |
| H | Zeitmuster des Redispatch, aggregiert aus 19 369 Einzelmaßnahmen | 4.5 nachvollziehen |

---

## 4 Zahlen belegen, ohne das Analyse-Repository zu belasten

Das Analyse-Repository liegt unter
`C:/GIT-HUB/bess_dispatch_optimization`. **Vor jedem Zugriff `git status`
lesen, fremde Änderungen nicht anfassen, nichts dorthin schreiben.** Dort
arbeitet parallel eine eigene Sitzung.

| Frage | Fundstelle |
|---|---|
| jede Kennzahl von Kapitel 4 | `analysen/code/schrift/ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md`, Abschnitt 4 trägt die vollständigen Verteilungen aller Sensitivitätsstufen, Abschnitt 7 die Zahlen je Abbildung |
| roter Faden je Abschnitt | `analysen/code/schrift/AUFBAU_KAPITEL_4.md` |
| Ursachen der teuren Perioden | im **Schriftrepository**: `analysen/zeitmuster_ursachen/`, dort `BEFUND*.md`. **Warnung in dessen `README.md` beachten:** alle Berichte außer `BEFUND_NEUBERECHNUNG.md` beruhen auf der ersten Iteration |
| Monatswerte auf der Ebene der Abbildung 4.6 | `analysen/zeitmuster_ursachen/BEFUND_MONATE_TAG.md` |
| Tagesmuster des Redispatch | `analysen/redispatch_tagesmuster/BEFUND*.md` |
| Abruf der aFRR-Arbeit | `analysen/afrr_abruf/BEFUND.md`: im Mittel 51 MW positiv und 53 MW negativ gegen bezuschlagte 2010 und 1820 MW, also 2,5 und 2,9 Prozent; in 92 Prozent der Viertelstunden unter einem Zehntel der Vorhaltung |

**Harte Regel:** keine Zahl aus einer Abbildung ablesen. Jede Zahl stammt aus
einer Tabelle, einem Bericht oder einer eigenen nachvollziehbaren Rechnung.

---

## 5 Der Zustand von `chapters/chapter_5.tex`

Die Datei ist ein **Gerüst aus Stichpunkten**, keine Prosa. 318 Zeilen, davon
der größte Teil Kommentar. Aufbau des Gerüsts:

```
5.1 Einordnung in den regulatorischen Rahmen   Punkte B1 bis B7
5.2 Bewertung anhand des Anforderungskatalogs  Punkte C...
5.3 Uebertragbarkeit auf Systemebene           Punkte D...
5.4 Kritische Wuerdigung der Modellannahmen    Punkte E...
5.5 Handlungsempfehlungen                      Punkte F...
```

Jeder Stichpunkt trägt über sich einen Kommentar mit **Kennung und
Belegstand**, nämlich `[belegt]` mit Fundstelle, `[eigen]` für in der
Bearbeitung entstandene Argumentation und `[daten]` für eine eigene
Auswertung. Die Kennungen verweisen auf eine Sammlungsdatei, die **nicht mehr
im Repository liegt**; die Kennungen sind vor der Abgabe zu entfernen.

**Das Gerüst ist älter als Kapitel 4** und kennt die Ergebnisse noch nicht. Es
ist eine Materialsammlung, kein Gliederungsbeschluss. Der Zielumfang stand bei
zwölf Seiten. `main.tex` hat Kapitel 5 und 6 auskommentiert, Zeile 43 und 44.

**Zwei Dinge sind daran zu prüfen, bevor du etwas vorschlägst:**

1. Welche der Stichpunkte tragen nach Kapitel 4 noch, welche sind überholt.
2. Der Altbefund `chapters/chapter_5.tex:91`, den `tools/pruefen.py` seit
   Tagen meldet: das Wort *Batteriespeicher* steht dort ausgeschrieben statt
   als Akronym. Behebe das beiläufig, wenn du die Zeile ohnehin anfasst.

---

## 6 Was der Verfasser inhaltlich verlangt

Wörtlich, Vorgabe vom 23.09.2026 abends:

> Ich möchte alle Ergebnisse diskutieren und ihre Folgen auf die
> Betriebsführung, und eventuelle Entwicklungen im Engpassmanagement und am
> Markt auch ansprechen. Wichtig ist, dass am Ende ich noch mal unter den
> diskutierten Gesichtspunkten auch kurative Systemführung im Allgemeinen
> diskutiere, daraus auch schon Forschungsbedarf ableite, der noch folgen
> muss, beziehungsweise welche Erkenntnisse auch aus Projekten noch gewonnen
> werden müssen. Ein Kapitel würde ich auch gerne der Zukunft von BESS im
> Engpassmanagement widmen.

Daraus folgen fünf Pflichtbestandteile:

1. **Jedes Ergebnis von Kapitel 4 wird diskutiert.** Nicht nur die Höhe des
   Preises, sondern auch die Verteilung, das zeitliche Muster, das Verhältnis
   zum Engpassmanagementbedarf und jede Sensitivität.
2. **Folgen für die Betriebsführung.** Was bedeutet das Ergebnis für den
   Betreiber einer Anlage und für den ÜNB, der die Vorhaltung beschafft.
3. **Entwicklungen im Engpassmanagement und am Markt.** Was verändert sich, und
   wie hält das Ergebnis dieser Veränderung stand. Abschnitt 4.6.4 liefert die
   gerechnete Zukunftsvariante, der Regimebruch vom 01.10.2025 den
   beobachteten Fall.
4. **Ein eigener Abschnitt zur Zukunft von Batteriespeichern im
   Engpassmanagement.**
5. **Am Ende die kurative Systemführung im Allgemeinen**, und daraus
   abgeleitet der **weitere Forschungsbedarf** und der **Erkenntnisbedarf aus
   Projekten**.

---

## 7 Das Material für die Diskussion liegt bereit

`HANDOFF.md` Abschnitt 7 trägt die Sammlung. **Lies sie vollständig**, sie ist
die halbe Arbeit. Die tragenden Punkte, damit du sie erkennst:

**Regulatorisch**
- Anlage 1 der Festlegung, Seite 13: die PSKW-Vorgaben sind auf
  Batteriespeicher „auch ohne weitere Anpassungen" anwendbar. Und: § 13a
  Abs. 2 EnWG gibt kostenbasierten Redispatch vor, ein marktbasierter
  Redispatch ist gesetzlich nicht möglich. **Das ist der Kern von 5.1.**
- Die Vergütungsstruktur der Festlegung lautet Erzeugungsauslagen zuzüglich
  des Maximums aus anteiligem Werteverbrauch und Opportunität. Sie ist **nicht
  additiv**, sodass der Optionswert für ein BESS gar nicht in die Zahlung
  eingehen kann, wenn der Werteverbrauch größer ist.
- Die Beschlusskammer 8 hat die Behandlung von Batteriespeichern einem
  späteren Hinweis vorbehalten. Die Forschungslücke ist damit ein
  dokumentierter offener Punkt.
- **G1, Entscheidung des Verfassers vom 22.09.2026:** der kapazitätsbasierte
  Redispatch beschafft im Kern dieselbe Größe wie eine kurative Vorhaltung und
  unterscheidet sich nur in Auslöser und Reaktionszeit.

**Aus den Ergebnissen**
- Der Preis ist ein Preis **gegen die Regelleistung**, nicht gegen den
  Energiehandel. Die aFRR trägt drei Viertel des Referenzerlöses.
- Die **Granularität des Produkts bestimmt die Zahlung**. Die erste Iteration
  gibt allen Stunden eines Tages denselben Preis und ist deshalb ineffizient:
  der ÜNB zahlt beinahe den vollen Preis und bindet gerade die wertvollsten
  Stunden nicht. Hier ist das **Zeitscheibenproblem** noch einmal aufzunehmen.
- **Günstig genau dann, wenn viel gebraucht wird.** Im Dezember ist die
  Reservierung in beiden Richtungen am günstigsten, und von den zehn Tagen mit
  dem größten Engpassmanagementbedarf fallen sieben beziehungsweise neun auf
  den Winter. Das ist der stärkste positive Befund der Arbeit.
- **Die Ausnahme ist der Mittag**, wo der größte Bedarf an Reduzierung der
  Einspeisung auf die teuerste Ladereservierung trifft.
- Die kurative Reservierung gibt dem Speicher eine Möglichkeit, seinen Erlös
  **allein durch eine klügere Verteilung auf die Märkte** zu steigern, sofern
  er die richtigen Preise setzt.
- Die **teuersten Stunden sind schwer zu prognostizieren** und werden selten
  erreicht. Die Wahrscheinlichkeit ihres Eintretens schlägt sich gleichwohl im
  Preis nieder.
- Der ermittelte Preis ist **nur der opportunitätskostenbasierte Teil des
  Gebots**. Ein Betreiber nimmt darauf einen Aufschlag für Unsicherheit und für
  den eigenen Aufwand des Anbietens.
- Ein BESS wird eher zum **Entladen als bilanzieller Ausgleich** für
  erneuerbare Erzeugung eingeplant. Gekoppelt mit regelbarer Photovoltaik
  lohnen deshalb die Mittagsstunden am meisten, saisonal eher der Winter mit
  dominierender Winderzeugung. Die Abendstunden sind dagegen oft teuer.
- Die beiden Tage mit der **steilsten Staffel der Arbitragespannen**, nämlich
  der 26.08.2025 mit 10 und der 15.05.2025 mit 11 Prozent, sind genau die
  beiden Tage, an denen die Verdrängung nach 4.1 auch bei 200 €/(MW·h)
  unvollständig bleibt. Der Zusammenhang erklärt einen Befund aus 4.1.
- **Aus 4.6.1:** der Abrechnungspreis der Kapazitätsauktion bestimmt die
  teuren Stunden, der Liefermodus die typische Stunde. Der Abruf der
  aFRR-Arbeit ist ungewiss, im Mittel nur 2,5 und 2,9 Prozent der
  vorgehaltenen Leistung. Die Annahme freier Lieferung ist für eine einzelne
  Anlage nicht zu erwarten.
- **Aus 4.6.2:** eine halbe Stunde Abrufdauer kostet fast dasselbe wie eine
  Viertelstunde und verschafft dem ÜNB die doppelte Zeit für eine Ablösung der
  Maßnahme. Der Schritt auf die volle Stunde kostet 0,30 €/(MW·h) entladend und
  1,28 €/(MW·h) ladend. **Das ist ein unmittelbarer Vorschlag für den
  Produktzuschnitt.**
- **Aus 4.6.4:** niedrigere Marktpreise machen die kurative Bindung nicht
  günstiger als der heutige Stand, denn der Preis sinkt mit der Opportunität,
  und das Verhältnis beider bleibt bestehen.

**Noch nicht belegt, vor Verwendung klären**
- Die Aussage, der **FCR-Markt sei gesättigt**, steht in den Kapiteln 1 bis 4
  nirgends im Fließtext. Kapitel 5 kann sich nicht darauf stützen, solange sie
  nicht belegt irgendwo steht. Frage den Verfasser.
- Der Auftraggeber des Weber-Gutachtens ist in den Quellen widersprüchlich,
  EnBW gegen BDEW; die Literaturdatei folgt dem Deckblatt.
- Der Consentec-Befund zu KuPilot ist vorgemerkt und nicht verwendet.

---

## 8 Dein Vorgehen am 24.09.2026

1. **Lesen und nachvollziehen**, nach Abschnitt 1. Melde dem Verfasser jeden
   Widerspruch und jede Zahl, die du nicht wiederfindest. Das ist ausdrücklich
   erwünscht und hat in dieser Sitzung mehrfach Fehler gefunden.
2. **Einen eigenen Strukturvorschlag ausarbeiten**, bevor du fragst. Der
   Verfasser will nicht nach der Struktur gefragt werden, ohne einen Vorschlag
   zu sehen. Vorgabe des Verfassers vom 22.09.2026: eigener Vorschlag statt
   Rückfrage, höchstens zwei Fassungen, nach zwei Iterationen den Absatz neu
   denken.
3. **Dann gezielt fragen**, und zwar zur Struktur. Nutze dafür ein
   Auswahlwerkzeug mit wenigen klaren Alternativen und nicht eine offene Frage.
4. **Erst nach Freigabe des Absatzplans schreiben.** Die Arbeitseinheit ist der
   Absatz, nicht der Satz.

### Ein Strukturvorschlag als Ausgangspunkt

Nicht als Beschluss, sondern damit du nicht bei null anfängst. Er nimmt die
fünf Pflichtbestandteile aus Abschnitt 6 auf und ordnet sie so, dass jede
Diskussion auf der vorigen aufbaut.

```
5.1  Einordnung des Ergebnisses
     Was der ermittelte Preis ist und was er nicht ist. Preis gegen die
     Regelleistung, opportunitaetskostenbasierter Teil des Gebots, Aufschlag
     des Betreibers. Hoehe und Verteilung gegen die Bezugslinie des
     praeventiven Redispatch.
5.2  Einordnung in den regulatorischen Rahmen
     Paragraf 13a EnWG, die nicht additive Verguetungsstruktur der
     Festlegung, der offengehaltene Regelungsbedarf fuer Batteriespeicher,
     das Verhaeltnis zu Redispatch 2.0 und zum kapazitaetsbasierten
     Redispatch.
5.3  Folgen fuer die Betriebsfuehrung
     Was der Befund fuer den Betreiber bedeutet und was fuer den UENB. Der
     Zuschnitt des Produkts: Granularitaet der Zeitscheibe, Abrufdauer,
     Mindestgroesse, beidseitige gegen einseitige Reservierung.
5.4  Belastbarkeit des Ergebnisses
     Die Sensitivitaeten als Antwort auf die Frage, welche Annahme das
     Ergebnis traegt. Die kritische Wuerdigung der Modellannahmen gehoert
     hierher, nicht in einen eigenen spaeten Abschnitt.
5.5  Entwicklungen im Engpassmanagement und am Markt
     Der Regimebruch vom 01.10.2025 als beobachteter Fall, die
     Zukunftsvariante als gerechneter Fall, der wachsende Bestand an BESS
     gegen den nicht mitwachsenden Regelleistungsbedarf.
5.6  Zukunft der Batteriespeicher im Engpassmanagement
     Der eigene Abschnitt, den der Verfasser verlangt. Warum ein BESS fuer
     die kurative Vorhaltung besonders geeignet ist, wo seine Grenze liegt,
     und wie sich das mit dem Bestand veraendert.
5.7  Kurative Systemfuehrung im Allgemeinen
     Was aus dem Ergebnis fuer die kurative Systemfuehrung jenseits des
     Speichers folgt. Daraus der weitere Forschungsbedarf und der
     Erkenntnisbedarf aus Projekten.
```

**Die Fragen, die du dem Verfasser stellen solltest**, jeweils mit deinem
eigenen Vorschlag daneben:

1. Bleibt die alte Gliederung mit fünf Abschnitten und dem
   Anforderungskatalog, oder tritt eine Gliederung nach den Ergebnissen an
   ihre Stelle. **Der Anforderungskatalog ist der Punkt, der zu klären ist:**
   das alte Gerüst prüft den Mechanismus gegen einen Katalog, die neue Vorgabe
   diskutiert die Ergebnisse. Beides zusammen wäre doppelt.
2. Wie viele Seiten. Der alte Zielumfang war zwölf.
3. Ob die kritische Würdigung der Modellannahmen ein eigener Abschnitt bleibt
   oder in die Diskussion der Sensitivitäten wandert.
4. Ob die Handlungsempfehlungen ein eigener Abschnitt bleiben oder als
   Konsequenz an das Ende jedes Abschnitts treten. Die Stilregel 4 verlangt
   ohnehin, dass jede Aussage zu Ende geführt wird.

---

## 9 Was du nicht tun darfst

Diese Punkte haben in der Sitzung vom 23.09.2026 Schaden angerichtet oder
beinahe angerichtet. Sie stehen hier, damit du sie nicht wiederholst.

- **Kein `git checkout` auf eine Datei mit ungesicherten Änderungen.** Das hat
  am 23.09.2026 die Arbeit eines halben Abends gekostet. Vor jedem Eingriff
  `git status` lesen.
- **Anker beim Ersetzen an den Zeilenanfang binden oder Kommentarzeilen
  überspringen.** Die Kapiteldateien tragen die zurückgenommenen Fassungen als
  Kommentar über der neuen. Ein `str.index` auf einen Satz trifft deshalb
  zuerst die alte Fassung. Auch das hat einen Absatz gekostet.
- **Skripte nur über das Write-Werkzeug anlegen.** Bash-Heredocs verstümmeln
  Backslashes, und LaTeX besteht aus Backslashes.
- **Zeilenenden:** `.tex`, `ENTSCHEIDUNGSPROTOKOLL.md` und `HANDOFF.md` liegen
  mit CRLF vor, alle anderen Markdown- und Python-Dateien mit LF. Prüfung 1
  meldet einen Verstoß.
- **Ersetzter Fließtext wird nicht gelöscht**, sondern als Kommentar mit Datum
  und Grund über der neuen Fassung erhalten.
- **Committen nur auf das Wort „commite", pushen nur auf ausdrückliche
  Anweisung.** `origin/main` ist derzeit hinter `main`.
- **Subagenten nur nach Rückfrage.** Nenne vorher Zweck und Zahl.
- **Keine Zahl aus einer Abbildung ablesen.**
- **Die Dateiliste in `tools/pruefen.py` ist fest verdrahtet.** Ein neuer
  Anhang wird sonst nicht geprüft. Bei jedem weiteren Anhang nachziehen.
- **Zu jedem Zeitpunkt arbeitet nur eine Seite an einer Datei.**

---

## 10 Bauen und prüfen

```
python tools/pruefen.py --alle
pdflatex main
biber main
pdflatex main
pdflatex main
```

Stand 23.09.2026 abends: **111 Seiten**, Prüfsuite meldet allein den Altbefund
`chapters/chapter_5.tex:91`. Die Warnungen zu `ch:discussion` und `ch:conc`
sind normal, solange Kapitel 5 und 6 in `main.tex` auskommentiert sind. Sobald
du Kapitel 5 einbindest, verschwinden sie.

Ein Interpreter mit pandas steht unter
`C:/ProgramData/anaconda3/python.exe`. Der Standard-Python dieser Maschine hat
pandas nicht.
