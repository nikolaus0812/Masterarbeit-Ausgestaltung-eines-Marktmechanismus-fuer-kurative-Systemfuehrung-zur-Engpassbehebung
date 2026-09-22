# Übergabe an die nächste Sitzung, Stand 22.09.2026, abends

Diese Datei ersetzt die Fassung vom 22.09.2026 morgens vollständig. Die alte
Fassung steht in der Git-Historie.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3, 7 und 10. `ENTSCHEIDUNGSPROTOKOLL.md` hat über
16 000 Zeilen und wird nie ganz gelesen, sondern nur angehängt und gezielt
durchsucht.

---

## 1 Stand des Dokuments

Build sauber, Biber ohne Warnung, **104 Seiten**. `python tools/pruefen.py
--alle` meldet allein den Altbefund in `chapters/chapter_5.tex` Zeile 91.
`main.tex` bindet die Kapitel 1 bis 4 ein, 5 und 6 sind auskommentiert; die
beiden Warnungen zu `ch:discussion` und `ch:conc` sind deshalb normal.

| Teil | Umfang |
|---|---|
| Kapitel 1 Einleitung | PDF-Seite 9 bis 13, fünf Seiten, **keine Reserve** |
| Kapitel 2 Grundlagen und Stand der Technik | PDF-Seite 14 bis 37 |
| Kapitel 3 Marktmechanismus und Modellierung | PDF-Seite 38 bis 56 |
| Kapitel 4 Exemplarische Anwendung | PDF-Seite 57 bis 69 |
| Anhänge A bis F | A Weber, B Überlastdauer, C Optimierungsproblem, D Ablauf, E Validierung je Markt, F Preisgitter |

Logische Seitenzahl ist PDF-Seite minus acht.

### 1.1 Kapitel 4 ist geschrieben

Am 22.09.2026 nach `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` aus dem
Analyse-Repository umgebaut. Das Stichpunktgerüst ist vollständig durch
Fließtext ersetzt. Gliederung:

| Abschnitt | Abbildung | Stand |
|---|---|---|
| Einleitung | keine, Modellierung und Güte als Text | geschrieben |
| 4.1 Verlauf des Dispatch und Verdrängung der Märkte | Verweis auf Anhang F | geschrieben |
| 4.2 Preise beider Iterationen und Erlöswirkung | Erlösvergleich | geschrieben |
| 4.3 Verteilung der Verdrängungspreise | Boxplot | geschrieben |
| 4.4 Zeitliches Muster | Heatmap, Zeitmuster | geschrieben |
| 4.5 Kurativer Reservierungspreis und Engpassbedarf | Jahreslauf Median und Mittel | geschrieben |
| 4.6 Sensitivitäten | | |
| 4.6.1 Modellierung der aFRR | aFRR Leistung, aFRR Energie | geschrieben |
| 4.6.2 Abrufdauer | Abrufdauer, 2. Iteration | geschrieben |
| 4.6.3 Handelsspanne am IDC | folgt | **leer, wartet auf `sensi8`** |
| 4.6.4 Zukünftig niedrigere Preise | folgt | **leer, wartet auf `sensi8`** |
| 4.7 Diskussion der Ergebnisse | keine | **leer, anschließend** |

Die drei leeren Abschnitte stehen im PDF als bloße Überschriften. Der frühere
Abschnitt *Zahlung bei vollständiger Bindung* ist gestrichen, sein Inhalt
steckt in 4.2. **Tabelle 4.1 ist ersatzlos entfallen**, die Verteilung trägt
jetzt der Boxplot. Kapitel 4 hat keine Tabelle mehr.

**Die Anweisung nennt die Sensitivitäten 4.7 und die Diskussion 4.8, streicht
aber zugleich 4.6.** Beides zugleich ginge nur mit einer Lücke in der
Nummerierung, deshalb zählt LaTeX hier fortlaufend. Die Marken tragen die
Sache und nicht die Nummer.

### 1.2 Alle Zahlen stammen aus dem Analyse-Repository

Keine Zahl des Kapitels ist aus einer Abbildung abgelesen oder in der
Schriftfassung nachgerechnet. Quelle ist
`analysen/code/schrift/ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` Abschnitt 7 und
Abschnitt 4 der Anweisung. **Rückfragen dorthin, nicht nachrechnen.**

Neun Abbildungen liegen in `figures/chapter_4/`. Stand der drei zuletzt
geholten: Jahreslauf Median und Mittel vom 22.09. 12:05, Zeitmuster vom
22.09. 11:14. Das Zeitmuster zeigt seither Median **und** arithmetisches
Mittel mit einem Band dazwischen.

---

## 2 Dateiübersicht

Am 22.09.2026 aufgeräumt, weil das Wurzelverzeichnis unübersichtlich wurde.
**Im Wurzelverzeichnis liegen nur noch Dateien, die gelten.**

### Wurzelverzeichnis, sieben Dateien

| Datei | Rolle |
|---|---|
| `CLAUDE.md` | Auftrag, Stilregeln, Begriffe, Prüfungen. Claude ändert sie nicht, der Verfasser zieht selbst nach. |
| `HANDOFF.md` | diese Datei, Einstiegspunkt jeder Sitzung |
| `WORKFLOW.md` | Vorgehen: Absatzplan (3), Kommentardurchgang (7), Arbeitsweise am Absatz (10) |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen, nie ganz lesen |
| `DURCHSICHT_KAP1_3.md` | **offen**: Liste G, vierzehn Punkte aus Kapitel 3, nichts umgesetzt |
| `RUECKMELDUNG_AN_ANALYSE.md` | **offen**: Antwort an das Analyse-Repository, noch nicht abgesendet |
| `README.md` | Beschreibung des Repositorys |

### `archiv/`, elf Dateien, nur zum Nachschlagen

| Datei | war | abgelöst durch |
|---|---|---|
| `AENDERUNGEN_KAP1_2.md` | Änderungsliste Kapitel 1 und 2 | umgesetzt 15.09. |
| `AENDERUNGEN_KAP3.md` | Änderungsliste Kapitel 3 | umgesetzt 15.09. |
| `KUERZUNGEN_KAP1_2.md` | Kürzungsliste | umgesetzt 15.09. |
| `STRUKTUR.md` | Gliederung Kapitel 3 | umgesetzt |
| `ANWEISUNG_KOMMENTARE.md` | Anweisung für den Kommentardurchgang | `WORKFLOW.md` Abschnitt 7 |
| `KOMMENTARE_KAP3.md`, `KOMMENTARBESTAND_KAP3.md` | Kommentardurchgang Kapitel 3 | eingearbeitet |
| `KONTROLLAUFTRAG_FABLE.md`, `KONTROLLE_FABLE.md` | Kontrolldurchgang 17.09. | eingearbeitet |
| `KAPITEL_4_AUFBAU.md` | eigene Sortierung von Kapitel 4 vom 18.09. | **`AUFBAU_KAPITEL_4.md` im Analyse-Repository**, 22.09. |
| `quellencheck_bericht.md` | erzeugter Bericht vom 19.09. | nicht versioniert, kein Steuerdokument |

### Im Analyse-Repository, nur lesend

`analysen/code/schrift/` trägt `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` (das
Arbeitsdokument), `AUFBAU_KAPITEL_4.md` (roter Faden je Abschnitt),
`ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` (Herleitung, Abschnitt 7 alle Zahlen)
und `UEBERGABE_AN_SCHRIFTFASSUNG.md`. **Diese Dateien am Repository lesen und
nicht in einer Kopie**, sie ändern sich mehrmals täglich.

---

## 3 Entscheidungen, die beim Schreiben binden

Ausführlich im Protokoll. Kurz:

- **Betreiber gegen EIV.** Der *Betreiber* ist der wirtschaftliche Entscheider,
  der *EIV* verantwortet den Einsatz im Betrieb. Der *Anlagenbetreiber* steht
  nur, wo § 13a EnWG oder die Festlegung ihn nennen. Kapitel 4 spricht vom
  Betreiber.
- **Dispatch-Modelle nach der EBGL:** *dezentrales* und *zentrales
  Dispatch-Modell*, nie Selbstdispatch.
- **Arbitrage** ist in 2.2.1 am Ende des IDC-Absatzes definiert.
- **Regelleistung.** Leistungspreis aFRR und mFRR im Gebotspreisverfahren, FCR
  im Grenzpreisverfahren; Regelarbeit nach Merit-Order zum Grenzpreis. Das Wort
  *Anreizkomponente* ist gestrichen, es stand in keiner Quelle.
- **Indifferenzprinzip**, nicht Indifferenzgebot, definiert in 2.3.1.
- **Inc-Dec** hängt daran, dass der Akteur den Eingriff mit dem Fahrplan
  herbeiführen kann. Die Abrufvergütung bleibt offen und wird nur als getrennt
  zu betrachten genannt.
- **Abrufdauer**, nicht Vorhaltedauer und nicht Bindungsdauer. Sie setzt die
  Breite des Ladezustandsbandes, die Bindungsdauer bleibt eine Stunde.
- **Dopplungen.** Kapitel 1 darf als Motivation wiederholen, ein Zwischenfazit
  darf zusammenfassen. Kritisch ist die Wiederholung in einem Absatz, der sie
  für seine Erklärung nicht braucht. Der Maßstab gilt für Kapitel 4 gegenüber
  Kapitel 3.
- **Redispatch heute:** 16,5 TWh in beiden Richtungen 2025, 98 Prozent auf 206
  Einheiten ab 100 MW.
- **Bezugslinie des präventiven Redispatch**, entschieden am 22.09.2026: 101
  Euro je bewegter Megawattstunde, gemittelt über beide Richtungen. Der Nenner
  enthält beide Richtungen und **wird nicht halbiert**, weil die Reihe nicht
  symmetrisch ist. Näheres in 4.5 und im Protokoll.
- Die Entscheidungen vom 18. und 19.09.2026 gelten unverändert: Stilregel 1
  mit mindestens einer halben Seite je Absatz, Trendjahr 2032, Aktenzeichen
  `BK8-22-001-A`, KuPilot erprobt die Höherauslastung, technologieoffener
  Mechanismus, keine Fußnoten in Kapitel 2.

---

## 4 Arbeitstechnik, die sich bewährt hat

- Änderungen an Kapiteldateien **immer über ein Python-Skript**, das die Datei
  mit `open(pfad, encoding="utf-8", newline="")` liest und mit CRLF
  zurückschreibt. Anker müssen genau einmal greifen, ersetzter Fließtext bleibt
  als Kommentar mit Datum und Grund über der neuen Fassung. **Skripte nur über
  das Write-Werkzeug anlegen**, Bash-Heredocs verstümmeln Backslashes.
- **Streichungen vor Einfügungen** im selben Skript, sonst greifen Anker
  doppelt. Gegenprobe über die Differenz der Fließtextzeilen.
- Protokolleinträge als Liste einzelner Zeilen anhängen, nicht als
  mehrzeiligen String, sonst entstehen einsame LF. Die Protokolldatei ist als
  einzige Markdown-Datei CRLF; die übrigen sind LF.
- Nach jeder Änderung: `python tools/pruefen.py <datei>`, Build (`pdflatex;
  biber; pdflatex; pdflatex`), Seitenlage prüfen, die neue Passage im Chat
  zeigen. Committen **nur** auf „commite", pushen nur auf ausdrückliche
  Anweisung (über plink, siehe Gedächtnisnotiz).
- Abbildungen: Größe wird im Erzeugungsskript gesetzt,
  `\includegraphics[width=\textwidth]` ohne weitere Skalierung. Sichtprüfung
  mit `pdftoppm -png -r 70` und dem Read-Werkzeug. Vor dem Holen die
  Zeitstempel vergleichen, das Analyse-Repository liefert mehrmals täglich neu.
- **Subagenten nur nach Rückfrage**, mit Zweck und Anzahl.
- Nicht jede Quelle ist maschinell lesbar. `pdffonts` prüfen, bevor man einem
  leeren `pdftotext` traut.

---

## 5 CLAUDE.md ist überholt, der Verfasser zieht selbst nach

Claude ändert `CLAUDE.md` nicht. Offen:

1. **Abschnitt 1, Dateiliste.** Sie nennt `KAPITEL_4_AUFBAU.md`,
   `KOMMENTARE_KAP3.md` und `quellencheck_bericht.md` im Wurzelverzeichnis;
   alle drei liegen jetzt in `archiv/`. `extras/attachment_ablauf.tex` (Anhang
   D) und `extras/attachment_preisgitter.tex` (Anhang F) fehlen,
   `extras/attachment_dispatch.tex` ist stillgelegt.
2. **Abschnitt 5, Begriffe.** EIV als verbindliches Akronym; Betreiber gegen
   EIV gegen Anlagenbetreiber; *dezentrales* und *zentrales Dispatch-Modell*;
   *Indifferenzprinzip*; *Abrufdauer*. Ort der Arbitrage-Definition ist 2.2.1.
3. **Abschnitt 7, Entscheidung 3.** Die Mindestgröße von 25 MW ist als
   Sensitivität nur noch mit dem Hinweis sinnvoll, dass sie am Beispieltag bei
   5 Euro nicht bindet.
4. Die sechs Punkte aus der Übergabe vom 19.09.2026 gelten weiter: Stilregel 1,
   Ort der PATL- und TATL-Definition, Abgrenzung „kein Marktdesign",
   Trendjahr 2032.

---

## 6 Offene Punkte

**Aus Kapitel 4**

- **4.6.3 und 4.6.4 sind leer** und warten auf `sensi8_spanne_und_niveau` aus
  dem Analyse-Repository. Nicht mit den Einzeltagsfassungen füllen.
- **4.7 Diskussion ist leer** und folgt nach den beiden Sensitivitäten.
- `ERGEBNISSE…md` Abschnitt 7.4 liefert die **Tage** unter 101 Euro je
  Megawattstunde, nicht aber die **Stunden** und nicht die Aufteilung je
  Jahreszeit. `AUFBAU_KAPITEL_4.md` führt beides als noch zu rechnen. Im Text
  stehen deshalb nur die Tageszahlen.
- Die Herkunft des Unterschieds von 6,15 TWh zwischen Erhöhung und Absenkung
  ist in 4.5 zum Teil zugeordnet. Der verbleibende Anteil ist dem
  Einspeisemanagement zugeschrieben und **ausdrücklich als Vermutung
  gekennzeichnet**.
- **Kapiteltitel.** *Exemplarische Anwendung und Ergebnisse* trifft nicht mehr,
  weil das ganze Jahr gerechnet ist. Vorschlag: *Der kurative
  Reservierungspreis*. Entscheidung des Verfassers.
- **Abschnitt 1.2** beschreibt im letzten Satz des Zielabsatzes noch die alte
  Sortierung von Kapitel 4 und nennt die neuen Abschnitte 4.1 und 4.2 nicht.
- `fuellgrad_iterationen_2025.pdf` und `maximalpreis_iterationen_2025.pdf`
  liegen in `figures/chapter_3/`, stehen aber in keiner `figure`-Umgebung. Das
  deckt sich mit der Anweisung, wonach der Füllgradvergleich im Ergebnisteil
  nicht erscheint. Falls einer als Anhangbeleg gewünscht ist, ist er
  einzubinden.
- Der Revenue-Index mit 260,0 steht jetzt in 3.3.1 und in 3.3.2. Die
  Wiederholung macht das Verhältnis 1,31 nachrechenbar, lässt sich aber
  streichen.

**Ältere Punkte, unverändert**

- `DURCHSICHT_KAP1_3.md` Liste G, vierzehn Punkte aus Kapitel 3, nichts
  umgesetzt (G5 Degradationskosten 8 Euro je Megawattstunde ohne Quelle, G7
  aFRR-Menge 2000 MW ohne Beleg, G13 Mitteilung der Beschlusskammer zu
  Batteriespeichern vor Abgabe prüfen).
- Gate-Closure-Zeiten 9 und 10 Uhr sowie Gebots- und Grenzpreisverfahren
  tragen allein regelleistung.net, das lokal nicht vorliegt; pRD3 bis pRD5
  sind als Nummern unbelegt; die Sanktion bei Nichtvorhaltung fehlt als Quelle.
- `literature.bib`: Sous 2022 ohne Tagung, FAQ Stromspeicher ohne URL; zwei
  verwaiste Einträge.
- Im Zwischenfazit 2.4 stehen vier fast wörtliche Übernahmen aus 2.2.2, 2.3.3
  und 2.3.4, bewusst belassen.
- Der Überleitungssatz am Ende von 2.1.1 nennt die Bindungsdauer vor ihrer
  Definition in 2.1.2.
- Satz, wonach die Arbeit den Preis **eines Anbieters** bestimmt und nicht den
  Zuschnitt des Produkts, noch nicht gesetzt.
- Abgrenzung, dass der eingesparte Engpassmanagementbedarf nicht Gegenstand ist
  (Netzmodell nötig), steht nirgends; Vorschlag 3.2.1 oder Kapitel 5.
- Preisreihen in Kapitel 3 zitieren noch SMARD, Umstellung auf energy-charts
  oder EPEX offen.
- **Eine Zahlenprüfung für Kapitel 3 steht aus.** In 3.3.2 sind die
  Einzelmarkt-Erlöse des Revenue-Index (107,4; 221,3; 89,2; 134,1), die 133,0
  für ein Megawatt zum FCR-Preis und die 81 und 72 MW mittlere aFRR-Vorhaltung
  nicht gegen den aktuellen Lauf geprüft.
- Näheprüfung Abbildung gegen Verweis als elfte Prüfung in `tools/pruefen.py`
  nicht aufgenommen.

---

## 7 Für Kapitel 5 vorgemerkt

- Anlage 1 der Festlegung, Seite 13: Anwendung der PSKW-Vorgaben auf
  Batteriespeicher „auch ohne weitere Anpassungen" zulässig; und: § 13a Abs. 2
  EnWG gibt kostenbasierten Redispatch vor, marktbasierter Redispatch ist
  gesetzlich nicht möglich.
- Der Konsultationsbefund (Volllaststunden-Einwand unbeantwortet) steht in
  Anhang A, letzter Absatz.
- Auftraggeber des Weber-Gutachtens in den Quellen widersprüchlich (EnBW gegen
  BDEW), bib folgt dem Deckblatt.
- Consentec-Befund zu KuPilot vorgemerkt, nicht verwendet.
- **Aus Kapitel 4:** der Preis ist ein Preis gegen die Regelleistung; die
  Granularität des Produkts bestimmt die Zahlung; günstig genau dann, wenn viel
  gebraucht wird (Winter); die teuren Stunden liegen im Abendmaximum.

---

## 8 Modellrepository

`C:/GIT-HUB/bess_dispatch_optimization`, Interpreter mit matplotlib:
`C:/ProgramData/anaconda3/envs/venv_mode/python.exe`. Dort arbeitet parallel
eine eigene Sitzung. **Vor jedem Zugriff `git status` lesen, fremde Änderungen
nicht anfassen, und nichts dorthin schreiben.** Das Repository ist für die
Schriftfassung lesend.

Fertige Abbildungen liegen unter `analysen/12_schrift/kapitel_N/` in Satzbreite
(455,24 pt); Zuordnung `kapitel_N` nach `figures/chapter_N`, `kapitel_anhang`
nach `figures/anhang`. Beim Abgleich die PDF-Felder `CreationDate`, `ModDate`
und `ID` ausnehmen.

Eigene Auswertungen der Schriftfassung: `analysen/mastr_speicher`,
`analysen/mfrr_leistungspreise`, `analysen/vollreservierung_pruefung`,
`analysen/redispatch_einheiten`. Der Quelltext des Erlösindex der ISEA Battery
Charts liegt lokal unter `C:/GIT-HUB/battery_revenue_index-main`.
