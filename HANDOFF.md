# Übergabe an die nächste Sitzung, Stand 22.09.2026

Diese Datei ersetzt die Fassung vom 19.09.2026 vollständig. Die alte Fassung
steht in der Git-Historie unter `e2fe683`.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3 und 7, dann `KAPITEL_4_AUFBAU.md`.
`ENTSCHEIDUNGSPROTOKOLL.md` hat über 13 000 Zeilen und wird nie ganz gelesen,
sondern nur angehängt und gezielt durchsucht (Einträge vom 20. und 21.09.2026
unter `chapter_1.tex`, `chapter_2.tex`, `literature.bib` und unter den
übergreifenden Entscheidungen).

---

## 1 Aufgabe der nächsten Sitzung: Kapitel 4

Die Kapitel 1 bis 3 sind mit dem Verfasser am PDF durchgegangen und stehen.
**Die nächste Sitzung schreibt Kapitel 4** nach `WORKFLOW.md` Abschnitt 3:
Stichpunkte liegen vor, es folgt je Abschnitt ein Absatzplan, den der Verfasser
freigibt, erst dann Fließtext. Der Verfasser diktiert dabei knapp und in
Tippschreibweise; er will Vorschläge, keine Rückfragen zu Dingen, die sich aus
dem Material ergeben. Seine Vorgabe vom 21.09.2026: **"Unsichere immer mit
deinem Vorschlag"**, also bei Unsicherheit die eigene Fassung umsetzen und sie
als Vorschlag kennzeichnen, nicht nachfragen.

**Arbeitsweise am Absatz: `WORKFLOW.md` Abschnitt 10**, am 22.09.2026 aus dem
Durchgang abgeleitet. Kurz: den ganzen Absatz mit Nachbarn lesen und seine
Kernaussage benennen, bevor ein Satz angefasst wird; jede Behauptung an der
Quelle prüfen; auf eine Verständnisfrage mit Befund, neuem Wortlaut und
Empfehlung antworten, höchstens zwei Fassungen; präzise statt vorsichtig
formulieren; nach der zweiten Iteration am selben Satz die Ebene wechseln
(Satz verschieben, Definition umsetzen, Absatz neu aufbauen, Anhang), statt
weiter am Wortlaut zu drehen. Der Verfasser hat bei früheren Sitzungen
schwammige Formulierungen und das Verharren an einer Stelle bemängelt.

### 1.1 Was für Kapitel 4 bereitliegt

- `chapters/chapter_4.tex`: Gerüst in Stichpunkten nach `KAPITEL_4_AUFBAU.md`
  (Gliederung Einleitung, 4.1 Preisniveau und Streuung mit Tabelle 4.1, 4.2
  Zeitliches Muster mit Abbildung 4.1, 4.3 Preis und Engpassbedarf mit
  Abbildung 4.2, 4.4 Zahlung bei vollständiger Bindung mit Abbildung 4.3, 4.5
  Sensitivitäten mit Abbildungen 4.4 bis 4.6, 4.6 Zusammenfassung). Der
  Dateikopf trägt den roten Faden, den Zielumfang von 16 Seiten und die
  Trennlinie zwischen Beschreiben und Bewerten. **Die Stichpunkte stammen vom
  17./18.09.2026 und nennen zum Teil noch Analysetage und alte Zahlen**, sie
  sind vor jedem Absatzplan gegen die Zahlen unter 1.2 zu lesen.
- **Alle sechs Abbildungen liegen als PDF in `figures/chapter_4/` und sind
  seit dem 21.09.2026 eingebunden**, die Platzhalter sind weg. Dazu vier
  Preisgitterseiten (`dispatch_preisgitter_2025-02-11`, `-02-22`, `-05-15`,
  `-08-26`), die noch in keiner `figure`-Umgebung stehen; sie beantworten die
  Frage, welche Märkte die Reservierung mit steigendem Preis verdrängt, und
  gehören nach der Anweisung des Analyse-Repositorys in Kapitel 4 (eine Seite
  je Tag, 455 mal 539 Punkte, passt mit Bildunterschrift auf eine Seite).
- `figures/chapter_3/fuellgrad_iterationen_2025.pdf` und
  `maximalpreis_iterationen_2025.pdf` sind aus Kapitel 4 nach Kapitel 3
  umgezogen (Verfahren, zweite Iteration: 86 bzw. 90 Prozent gegen 100
  Prozent Füllgrad) und dort **noch nicht eingebunden**.
- `KAPITEL_4_AUFBAU.md` Abschnitt 7 nennt die offenen Entscheidungen N1 bis N5
  (Einheit des Preises, Kapiteltitel, Name *Abrufdauer*, Behandlung der ersten
  Iteration, Zahl der Tage 365 gegen 363). N3 ist durch die Abbildungslieferung
  faktisch entschieden: die Größe heißt **Abrufdauer**, sie setzt die Breite
  des Ladezustandsbandes, die Bindungsdauer bleibt eine Stunde.

### 1.2 Zahlen für Kapitel 4, Stand des Gesamtlaufs vom 17. bis 19.09.2026

Quelle: `analysen/code/schrift/ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` im
Analyse-Repository, Abschnitt 7, Stand 21.09.2026 16:14. Jede Zahl stammt aus
der Datendatei der jeweiligen Abbildung. Rückfragen dorthin, nicht nachrechnen.

- **4.1 Heatmap.** 8760 Stunden je Richtung, zweite Iteration. Median je
  Stunde: Entladereservierung höchstens 43,8 Euro je Megawatt und Stunde um 19
  Uhr, Ladereservierung 58,6 um 13 Uhr. Schwarz die zwei aus der Optimierung
  genommenen Stunden der Zeitumstellung, grau die Stunden ohne endlichen Preis.
- **4.2 Jahreslauf.** 365 Tage, zweite Iteration, je Tag Minimum, Median,
  Maximum. Die waagerechte Linie bei 101 Euro je Megawattstunde ist der
  **Arbeitspreis** des präventiven Redispatch 2025 (3,08 Milliarden Euro auf
  30,44 Terawattstunden), kein Leistungspreis. Korrelation Tagesmedian gegen
  Redispatchleistung r = minus 0,03 (Entlade-) und plus 0,11 (Ladereservierung).
  Die rechte Achse zeigt Redispatchleistung im Tagesmittel in Megawatt.
- **4.3 Erlösvergleich.** 363 Tage. Markterlös ohne Bindung 33,91 Millionen
  Euro; erste Iteration 40,82 kurativ plus 8,86 am Markt; zweite Iteration
  41,84 kurativ und 0,00 am Markt. Achse "Erlös in Mio. Euro", "netto nach
  Degradation" steht in der Bildunterschrift.
- **4.4 aFRR-Modellierung.** Sieben Jahresläufe (nicht mehr vier gepoolte
  Analysetage, die Streuung der alten Fassung war zu über 90 Prozent der
  Unterschied zwischen den Kalendertagen). Jahresmedian Entlade- /
  Ladereservierung in Euro je Megawatt und Stunde: Basisfall (pro rata,
  mittlerer Zuschlagspreis) 12,22 / 9,85; ganz ohne aFRR 3,47 / 4,25; Leistung
  zum Grenzpreis 14,19 / 11,47; ohne Energielieferung 12,62 / 5,47; Lieferung
  bis zur Reservierung 18,85 / 20,69; bis zum realen Abruf 20,60 / 20,88; bis
  zur Speicherleistung 20,61 / 21,33. Befund: der Sprung liegt zwischen pro
  rata und frei, nicht zwischen den freien Modi. Zwei Lesehilfen für die
  Bildunterschrift: "ganz ohne aFRR" trennt Leistung und Energie nicht (pro
  rata hängt die Energie an der Leistung); "bis 100 MW" heißt bis zur
  Speicherleistung in abgerufenen Slots.
- **4.5 Abrufdauer.** 8758 Stunden je Variante und Richtung. Von 1 h auf
  0,25 h sinkt der Median in der ersten Iteration um 18,8 (Entlade-) und 35,1
  Prozent (Ladereservierung), nach der zweiten Iteration nur noch um 4,0 und
  12,7 Prozent. Eingebunden ist `sensi_abrufdauer_2025_iterationen.pdf` mit
  vier Feldern (links erste, rechts zweite Iteration, oben Entlade-, unten
  Ladereservierung) als Vorschlag von Fable; die Zweifeldfassung
  `sensi_abrufdauer_2025.pdf` liegt daneben. **Entscheidung des Verfassers
  offen.**
- **4.6 IDC-Spread.** Fünf Beispieltage, Median der 24 Stundenpreise, **erste
  Iteration**, kein Jahresfeld (ein belastbares Jahresfeld bräuchte einen
  Jahreslauf mit Streckung 2, rund sieben Stunden; ob er stattfindet,
  entscheidet der Verfasser).
- **Kapitel 3, 3.3.2** ist am 21.09.2026 auf den aktuellen Lauf gesetzt:
  Revenue-Index 260,0, Optimierungsmodell 340,7 Tausend Euro je Megawatt und
  Jahr, Faktor im Median 1,31, Spanne 1,04 bis 1,50, Korrelation 0,974, alle
  zwölf Monate über dem Index, Einzelmärkte FCR 1,24, aFRR 1,51, DA 0,85,
  Intraday 0,89.

### 1.3 Befund an das Analyse-Repository

In `jahreslauf_reservierungspreis_redispatch_2025.pdf` (Abbildung 4.2) ist der
Legendeneintrag "präventiver Redispatch, 101 Euro/MWh (Arbeitspreis ...)" am
rechten Rand der Seite abgeschnitten. Die Datei ist so eingebunden und muss
dort neu erzeugt werden. Aus dem Analyse-Repository heraus wird nichts in die
Schriftfassung geschrieben, das Kopieren macht dieser Chat (Vergleich über den
Inhalt ohne CreationDate, ModDate, ID und xref, Skript im alten
Sitzungsverzeichnis `abb_vergleich.py`, leicht neu zu schreiben).

---

## 2 Stand des Dokuments

Letzter Commit `6256cfd` (21.09.2026). **Uncommitted** liegen die Bereinigung
des Literaturverzeichnisses (`literature/literature.bib`, `extras/header.tex`)
und der Protokolleintrag dazu; der Verfasser hat sie noch nicht mit "commite"
freigegeben. Build sauber, Biber ohne Warnung, **95 Seiten**.

| Teil | Umfang |
|---|---|
| Kapitel 1 Einleitung | PDF-Seite 9 bis 13, fünf Seiten, **keine Reserve** |
| Kapitel 2 Grundlagen und Stand der Technik | PDF-Seite 14 bis 37, endet auf Seite 29 mit drei freien Zeilen |
| Kapitel 3 Marktmechanismus und Modellierung | PDF-Seite 38 bis 56 |
| Kapitel 4 Exemplarische Anwendung | ab PDF-Seite 57, Gerüst mit echten Abbildungen |
| Anhänge A bis E | A Weber-Ansatz, B Überlastdauer, C Optimierungsproblem, D Ablauf Reservierungspreis, E Validierung je Markt |

Logische Seitenzahl ist PDF-Seite minus acht. `main.tex` bindet die Kapitel 1
bis 4 ein, 5 und 6 sind auskommentiert (Warnungen zu `ch:discussion` und
`ch:conc` sind normal). `python tools/pruefen.py --alle` meldet einen Altbefund
in `chapters/chapter_5.tex` Zeile 91.

**Der Anhang "Fahrplan ohne die Mindestgröße" ist am 21.09.2026 stillgelegt**
(`extras/attachment_dispatch.tex` vollständig auskommentiert, in `main.tex`
nicht mehr eingebunden), weil die 25-MW-Schranke am 11.02.2025 bei 5 Euro nach
der Korrektur der Kausalitätsbedingung nicht bindet. Nicht wiederbeleben; der
Unterschied wäre erst bei 15 Euro je Megawatt und Stunde sichtbar.

**Layoutregeln, die der Verfasser am 21.09.2026 durchgesetzt hat.** Abbildungen
stehen vor dem Absatz, der sie auswertet, mit Option `[H]`; erzeugt ein `[H]`
eine halbleere Seite, wird der folgende Absatz vor die Abbildung gezogen (so
bei Abbildung 2.3). Kürzungen vor einer `[H]`-Abbildung vergrößern nur den
Weißraum, Kürzungen dahinter holen Seiten. Kapitel 1 muss auf fünf Seiten
bleiben.

---

## 3 Entscheidungen des 20. und 21.09.2026, die beim Schreiben binden

Ausführlich im Protokoll. Kurz:

- **Betreiber gegen EIV.** Der *Betreiber* ist der wirtschaftliche Entscheider
  (Preis, Erlös, Gebot, Aufwand, Vermarktung, Reservierung in der
  Fahrplanbildung), der *EIV* (Einsatzverantwortlicher, Akronym seit
  20.09.2026, eingeführt in 1.1) verantwortet den Einsatz im Betrieb, meldet
  den Fahrplan, gibt die Zusage und ist Adressat einer Anordnung. Der
  *Anlagenbetreiber* steht nur, wo § 13a EnWG oder die Festlegung ihn nennen.
  Das Optimierungsmodell rechnet aus der Sicht des Betreibers. Kapitel 4
  spricht also vom Betreiber.
- **Dispatch-Modelle nach der EBGL:** *dezentrales Dispatch-Modell* und
  *zentrales Dispatch-Modell* (Art. 2 Nr. 17 und 18), nie mehr Selbstdispatch
  oder Dispatchmodell.
- **Arbitrage** ist seit dem 20.09.2026 in 2.2.1 am Ende des IDC-Absatzes
  definiert, nicht mehr in 2.3.5.
- **Regelleistung.** Leistungspreis aFRR/mFRR im Gebotspreisverfahren, FCR im
  Grenzpreisverfahren; Regelarbeit nach Merit-Order-Liste abgerufen und zum
  Grenzpreis vergütet; jede präqualifizierte Anlage darf Arbeit anbieten, die
  Bezuschlagten müssen (2.2.2 und 2.3.4). Das Wort *Anreizkomponente* ist
  gestrichen, es stand in keiner Quelle; die PQ-Bedingungen tragen nur die
  Pflicht zur kontinuierlichen Verfügbarkeit und Besicherung.
- **Indifferenzprinzip** (nicht Indifferenzgebot), definiert in 2.3.1.
- **Inc-Dec** hängt nicht an der Vergütung des Eingriffs, sondern daran, dass
  der Akteur den Eingriff mit dem Fahrplan herbeiführen kann; die kurative
  Vorhaltung entgeht dem Einwand nur durch den Produktzuschnitt (2.3.3). Die
  Abrufvergütung bleibt nach Entscheidung 14 offen und wird nur als getrennt
  zu betrachten genannt.
- **Dopplungen.** Kapitel 1 darf als Motivation wiederholen, was Kapitel 2
  ausführt. Innerhalb von Kapitel 2 sind Wiederholungen nur dort geblieben, wo
  der Absatz sie für seine eigene Erklärung braucht; das Zwischenfazit 2.4 darf
  zusammenfassen. Dieser Maßstab gilt auch für Kapitel 4 gegenüber Kapitel 3.
- **Redispatch heute:** 16,5 TWh in beiden Richtungen 2025, 98 Prozent auf 206
  Einheiten ab 100 MW (eigene Auswertung `analysen/redispatch_einheiten`,
  Beleg Netztransparenz). Der Redispatch ist das Mittel für strukturelle und
  stationäre Engpässe, das neue Instrument soll möglichst viele Anlagen an den
  Knoten der Höchst- und Hochspannung einbeziehen (1.1).
- Die Entscheidungen vom 18. und 19.09.2026 gelten unverändert (Stilregel 1:
  mindestens eine halbe Seite je Absatz, Umbruch nur bei Wechsel der
  Kernaussage, nie in einer Aufzählung; Trendjahr 2032; Aktenzeichen
  `BK8-22-001-A`; KuPilot erprobt die Höherauslastung; technologieoffener
  Mechanismus; keine Fußnoten in Kapitel 2).

---

## 4 Arbeitstechnik, die sich bewährt hat

- Änderungen an Kapiteldateien **immer über ein Python-Skript**, das die Datei
  mit `open(pfad, encoding="utf-8", newline="")` liest und mit CRLF
  zurückschreibt; Anker müssen genau einmal greifen, ersetzter Fließtext bleibt
  als Kommentar mit Datum und Grund über der neuen Fassung. **Skripte nur über
  das Write-Werkzeug anlegen**, Bash-Heredocs und `python -` verstümmeln
  Backslashes (`\c`, `\{`, `\r`), das ist am 21.09.2026 dreimal passiert.
- **Streichungen vor Einfügungen** im selben Skript, sonst greifen Anker
  doppelt. Gegenprobe über die Differenz der Fließtextzeilen vor und nach der
  Änderung.
- Protokolleinträge als Liste einzelner Zeilen anhängen, nicht als
  mehrzeiligen String, sonst entstehen einsame LF in der CRLF-Datei. Vor dem
  Commit `file ENTSCHEIDUNGSPROTOKOLL.md` prüfen.
- Nach jeder Änderung: `python tools/pruefen.py <datei>`, Build (`pdflatex;
  biber; pdflatex; pdflatex`), Seitenlage prüfen (`pdfinfo`, `pdftotext -f n
  -l n`), die neue Passage im Chat zeigen. Committen **nur** auf "commite",
  pushen nur auf ausdrückliche Anweisung (am 21.09.2026 einmal auf "pushe"
  über plink, siehe Gedächtnisnotiz).
- `tools/extract_alle.py` schreibt die Kapitel 1 bis 3 mit nummerierten
  Absätzen nach `%TEMP%\kap{n}_text.txt`; das ist der schnellste Weg, ein
  ganzes Kapitel zu lesen oder Dopplungen zu suchen.
- Abbildungen aus dem Analyse-Repository: Größe wird im Erzeugungsskript
  gesetzt, `\includegraphics[width=\textwidth]` ohne weitere Skalierung.
  Sichtprüfung mit `pdftoppm -png -r 60` und dem Read-Werkzeug.
- **Subagenten nur nach Rückfrage**, mit Zweck und Anzahl.
- Nicht jede Quelle ist maschinell lesbar (TenneT-Mitteilung zu KuPilot,
  FfE-Sägezahn, FAQ Stromspeicher, Sous 2022). `pdffonts` prüfen, bevor man
  einem leeren `pdftotext` traut.

---

## 5 CLAUDE.md ist überholt, der Verfasser zieht selbst nach

Claude ändert `CLAUDE.md` nicht. Offen sind neben den sechs Punkten aus der
Übergabe vom 19.09.2026 (Stilregel 1, Ort der PATL/TATL-Definition,
Aktenzeichen erledigt, Abgrenzung "kein Marktdesign", Trendjahr 2032,
Dateiliste):

7. **Abschnitt 5, Begriffe.** EIV als verbindliches Akronym; Betreiber gegen
   EIV gegen Anlagenbetreiber nach Abschnitt 3 dieser Datei; *dezentrales* und
   *zentrales Dispatch-Modell*; *Indifferenzprinzip*; *Abrufdauer* als Name der
   Sensitivität. Ort der Arbitrage-Definition ist 2.2.1, nicht 2.3.5.
8. **Abschnitt 1, Dateiliste.** `extras/attachment_dispatch.tex` ist
   stillgelegt, `extras/attachment_ablauf.tex` (Anhang D) fehlt in der Liste,
   `HANDOFF.md` trägt das Datum 22.09.2026, `figures/chapter_4/` ist gefüllt.
9. **Abschnitt 7, Entscheidung 3.** Die Mindestgröße von 25 MW ist als
   Sensitivität nur noch mit dem Hinweis sinnvoll, dass sie am Beispieltag bei
   5 Euro nicht bindet.

---

## 6 Offene Punkte

**Aus dem 21.09.2026**

- Wahl der Abbildung 4.5 (zwei oder vier Felder), siehe 1.2.
- Abgeschnittene Legende in Abbildung 4.2, siehe 1.3.
- Füllgrad und Maximalpreis in Kapitel 3 einbinden, Preisgitterseiten in
  Kapitel 4 einbinden.
- Modellbeschränkung auf FCR und aFRR (Kapitel 3) und die Zonenaufteilung
  stehen nirgends ausdrücklich; zu prüfen beim Schreiben von Kapitel 4.
- Gate-Closure-Zeiten 9 und 10 Uhr sowie Gebots- und Grenzpreisverfahren
  tragen allein regelleistung.net, das lokal nicht vorliegt; pRD3 bis pRD5
  sind als Nummern unbelegt; die Sanktion bei Nichtvorhaltung (MfRRA) fehlt
  als Quelle.
- `literature.bib`: Sous 2022 ohne Tagung (vermutlich 17. Symposium
  Energieinnovation 2022), FAQ Stromspeicher ohne URL; zwei verwaiste Einträge
  (`bundesnetzagentur_beschluss_2019`,
  `bundesministerium_der_justiz_netzausbaubeschleunigungsgesetz_2025`).
- Im Zwischenfazit 2.4 stehen vier fast wörtliche Übernahmen aus 2.2.2, 2.3.3
  und 2.3.4 (Abs. 67 S. 1, 5–6, 11; Abs. 69 S. 3), bewusst belassen.
- Der Überleitungssatz am Ende von 2.1.1 nennt die Bindungsdauer vor ihrer
  Definition in 2.1.2.
- Kapitel 4 nennt "Vergütungslogik des Redispatch" (1.2, Abruf) gegen
  "Vergütungslogik des Engpassmanagements" in 2.3; beim Schreiben einheitlich
  halten.

**Ältere Punkte, unverändert**

- Consentec-Befund zu KuPilot (Vergütung teilweise nicht in der
  Kostenerstattungssystematik abbildbar) vorgemerkt, nicht verwendet.
- Satz, wonach die Arbeit den Preis **eines Anbieters** bestimmt und nicht den
  Zuschnitt des Produkts, noch nicht gesetzt.
- Abgrenzung, dass der eingesparte Engpassmanagementbedarf nicht Gegenstand ist
  (Netzmodell nötig), steht seit dem 18.09.2026 nirgends; Vorschlag 3.2.1 oder
  Kapitel 5.
- Der angekündigte Vergleich der marktlich beschafften Vorhaltung mit dem
  präventiven Redispatch (1.2, letzter Satz des Zielabsatzes) ist in Kapitel 4
  nur über Abbildung 4.2 (Arbeitspreis 101 Euro je Megawattstunde) eingeplant.
- `DURCHSICHT_KAP1_3.md` Liste G, vierzehn Punkte aus Kapitel 3, nichts
  umgesetzt (G5 Degradationskosten 8 Euro je Megawattstunde ohne Quelle, G7
  aFRR-Menge 2000 MW ohne Beleg, G13 Mitteilung der Beschlusskammer zu
  Batteriespeichern vor Abgabe prüfen).
- Preisreihen in Kapitel 3 zitieren noch SMARD, Umstellung auf energy-charts
  oder EPEX offen.
- **Eine Zahlenprüfung für Kapitel 3 steht aus.** In 3.3.2 sind die
  Einzelmarkt-Erlöse des Revenue-Index (107,4; 221,3; 89,2; 134,1), die 133,0
  für ein Megawatt zum FCR-Preis mit 81 und 100 Prozent und die 81 / 72 MW
  mittlere aFRR-Vorhaltung nicht gegen den aktuellen Lauf geprüft.
- Näheprüfung Abbildung gegen Verweis als elfte Prüfung in `tools/pruefen.py`
  nicht aufgenommen.

---

## 7 Für Kapitel 5 vorgemerkt

- Anlage 1 der Festlegung, Seite 13: Anwendung der PSKW-Vorgaben auf
  Batteriespeicher "auch ohne weitere Anpassungen" zulässig; und: § 13a Abs. 2
  EnWG gibt kostenbasierten Redispatch vor, marktbasierter Redispatch ist
  gesetzlich nicht möglich.
- Der Konsultationsbefund (Volllaststunden-Einwand unbeantwortet) steht seit
  dem 21.09.2026 in Anhang A, letzter Absatz, und kann in Kapitel 5 aufgegriffen
  werden.
- Auftraggeber des Weber-Gutachtens in den Quellen widersprüchlich (EnBW gegen
  BDEW), bib folgt dem Deckblatt.
- Preissenkung der aFRR (`SZENARIO_AKTIV = "afrr_runter"`) als mögliche
  Sättigungsaussage, erst nach Kapitel 4 und 5 entscheiden
  (`KAPITEL_4_AUFBAU.md` 6.2).

---

## 8 Modellrepository

`C:/GIT-HUB/bess_dispatch_optimization`, Interpreter mit matplotlib:
`C:/ProgramData/anaconda3/envs/venv_mode/python.exe`. Dort arbeitet parallel
eine eigene Sitzung; vor jedem Zugriff `git status` lesen, fremde Änderungen
nicht anfassen, und **die Anweisungsdatei
`analysen/code/schrift/ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` im Repository lesen,
nicht die vom Verfasser in den Chat kopierte Fassung**: am 21.09.2026 war die
Datei zwischen Kopie und Umsetzung noch einmal geändert worden (Preisgitter
nach Kapitel 4).

Fertige Abbildungen liegen dort unter `analysen/12_schrift/kapitel_N/` in
Satzbreite (455,24 pt); Zuordnung `kapitel_N` nach `figures/chapter_N`,
`kapitel_anhang` nach `figures/anhang`. Eigene Auswertungen der
Schriftfassung: `analysen/mastr_speicher`, `analysen/mfrr_leistungspreise`,
`analysen/vollreservierung_pruefung`, `analysen/redispatch_einheiten` (liest
`data/processed/Redispatch_netztransparnez.net/2025_Redispatchmaßnahmen.parquet`
aus dem Modellrepository). Der Quelltext des Erlösindex der ISEA Battery Charts
liegt lokal unter `C:/GIT-HUB/battery_revenue_index-main`.
