# Übergabe an die nächste Sitzung, Stand 22.09.2026, abends

Diese Datei ersetzt die Fassung vom 22.09.2026 morgens vollständig. Die alte
Fassung steht in der Git-Historie.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3, 7 und 10. `ENTSCHEIDUNGSPROTOKOLL.md` hat über
16 000 Zeilen und wird nie ganz gelesen, sondern nur angehängt und gezielt
durchsucht.

---

## 1 Stand des Dokuments

Build sauber, Biber ohne Warnung, **106 Seiten**. `python tools/pruefen.py
--alle` meldet allein den Altbefund in `chapters/chapter_5.tex` Zeile 91.
`main.tex` bindet die Kapitel 1 bis 4 ein, 5 und 6 sind auskommentiert; die
beiden Warnungen zu `ch:discussion` und `ch:conc` sind deshalb normal.

| Teil | Umfang |
|---|---|
| Kapitel 1 Einleitung | PDF-Seite 9 bis 13, fünf Seiten, **keine Reserve** |
| Kapitel 2 Grundlagen und Stand der Technik | PDF-Seite 14 bis 37 |
| Kapitel 3 Marktmechanismus und Modellierung | PDF-Seite 38 bis 56 |
| Kapitel 4 Ergebnisse | PDF-Seite 57 bis 68 |
| Anhänge A bis G | A Weber, B Überlastdauer, C Optimierungsproblem, D Ablauf, E Validierung je Markt, F Preisgitter, G Jahreslauf im Median |

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

Neun Abbildungen liegen in `figures/chapter_4/`. Stand am 22.09.2026 abends
geprüft: alle neun sind deckungsgleich mit dem Lieferordner. Das Zeitmuster
zeigt die Summe als Hauptkurve, dazu Median und arithmetisches Mittel mit der
grauen Fläche dazwischen.

**Der Kapiteltitel lautet seit dem 22.09.2026 `Ergebnisse`**, Entscheidung des
Verfassers über das Analyse-Repository.

---

## 2 Dateiübersicht

Am 22.09.2026 aufgeräumt, weil das Wurzelverzeichnis unübersichtlich wurde.
**Im Wurzelverzeichnis liegen nur noch Dateien, die gelten.**

### Wurzelverzeichnis, fünf Dateien

| Datei | Rolle |
|---|---|
| `CLAUDE.md` | Auftrag, Stilregeln, Begriffe, Prüfungen. Claude ändert sie nicht, der Verfasser zieht selbst nach. |
| `HANDOFF.md` | diese Datei, Einstiegspunkt jeder Sitzung |
| `WORKFLOW.md` | Vorgehen: Absatzplan (3), Kommentardurchgang (7), Arbeitsweise am Absatz (10) |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen, nie ganz lesen |
| `README.md` | Beschreibung des Repositorys |

### `archiv/`, fünfzehn Dateien, nur zum Nachschlagen

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
| `DURCHSICHT_KAP1_3.md` | Durchsicht Kapitel 1 bis 3 vom 15.09. | Listen A bis F umgesetzt, Reste der Liste G stehen unten in Abschnitt 6 |
| `RUECKMELDUNG_AN_ANALYSE.md` | Rückmeldung an das Analyse-Repository | abgesendet, beantwortet in `ANTWORT_AN_SCHRIFTFASSUNG.md` |
| `AUFTRAG_ABBILDUNGSSTIL.md` | Auftrag zum Abbildungsstil vom 22.09. | mit Update 3 des Analyse-Repositorys erledigt |
| `AUFTRAG_ANALYSETAGE.md` | Auftrag zu den Analysetagen vom 22.09. | mit Update 4 des Analyse-Repositorys erledigt |

### Im Analyse-Repository, nur lesend

`analysen/code/schrift/` trägt `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` (das
Arbeitsdokument), `AUFBAU_KAPITEL_4.md` (roter Faden je Abschnitt),
`ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` (Herleitung, Abschnitt 7 alle Zahlen),
`UEBERGABE_AN_SCHRIFTFASSUNG.md`, `ANTWORT_AN_SCHRIFTFASSUNG.md` (Antwort auf
die Rückmeldung, 22.09. 12:04) und `UPDATE_02_AN_SCHRIFTFASSUNG.md` (Nachtrag
zur Bezugslinie, 22.09. 12:27). **Diese Dateien am Repository lesen und nicht
in einer Kopie**, sie ändern sich mehrmals täglich. Alles aus der Antwort und
aus Update 2 ist am 22.09.2026 eingearbeitet.

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
  Euro je bewegter Megawattstunde, gemittelt über beide Richtungen. Kosten und
  Menge stammen aus derselben Mitteilung der Bundesnetzagentur, nämlich
  3071 Millionen Euro auf 30 319 GWh. Der Nenner enthält beide Richtungen und
  **wird nicht halbiert**, weil die Reihe nicht symmetrisch ist. Näheres in 4.5
  und im Protokoll.
- **Kapiteltitel `Ergebnisse`**, entschieden am 22.09.2026.
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

- ~~Analysetage~~ **erledigt am 22.09.2026.** Fünf Tage, Anhang F hat fünf
  Seiten, Abschnitt 4.1 ist neu geschrieben. **Zwei der vier bisher belegten
  Aussagen sind dabei widerlegt worden:** die FCR wird am 06.05.2025 sehr wohl
  verdrängt (16 von 96 Zeitscheiben, weg bei 10 Euro je Megawatt und Stunde),
  und am 20.01.2025 weicht der Day-Ahead als letzter Markt statt als erster.
  Die tragfähige Aussage lautet jetzt, dass die Reihenfolge der Preisstruktur
  des Tages folgt und nicht einer festen Rangordnung der Märkte.
- **Offen und im Text gekennzeichnet:** dass die FCR an den übrigen Tagen bei
  null bleibt, steht auf fünf Tagen; wie häufig welche Verdrängungsreihenfolge
  über das Jahr eintritt, ist nicht geprüft; und die Umschichtung in den
  Day-Ahead ist an einem Tag und einem Preispunkt beobachtet.
- ~~Abbildungsstil~~ **erledigt am 22.09.2026.** Alle 28 Abbildungen tragen
  NimbusSanL mit 8,00 und 9,00 pt in voller Breite, keine Stauchung. Das
  Analyse-Repository hat die Ursache an der Wurzel behoben, nämlich ein
  `matplotlib.use` beim Import, das den LaTeX-Weg lautlos zurücksetzte, und
  führt jetzt `abbildungen_pruefen.py` als Wächter. Stellen unter 8 pt sind
  ausnahmslos Computer Modern in Skriptgröße, also Indizes des Formelsatzes,
  und bleiben.
- **4.6.3 und 4.6.4 sind leer** und warten auf `sensi8_spanne_und_niveau` aus
  dem Analyse-Repository. Nicht mit den Einzeltagsfassungen füllen.
- **Für 4.6.4 vorgemerkt (G3), Entscheidung des Verfassers vom 22.09.2026:**
  Die niedrigeren \ac{aFRR}-Preise der Zukunftsvariante lassen sich damit
  begründen, dass der Bestand an \ac{BESS} wächst, während der Bedarf an
  Regelleistung aus der Dimensionierung des Systems folgt und nicht mitwächst.
  Hilfsweise gehört das Argument in die Diskussion.
- **4.7 Diskussion ist leer** und folgt nach den beiden Sensitivitäten.
- `ERGEBNISSE…md` Abschnitt 7.4 liefert die **Tage** unter 101 Euro je
  Megawattstunde, nicht aber die **Stunden** und nicht die Aufteilung je
  Jahreszeit. `AUFBAU_KAPITEL_4.md` führt beides als noch zu rechnen. Im Text
  stehen deshalb nur die Tageszahlen.
- Die Herkunft des Unterschieds von 6,15 TWh zwischen Erhöhung und Absenkung
  ist in 4.5 zum Teil zugeordnet. Der verbleibende Anteil ist dem
  Einspeisemanagement zugeschrieben und **ausdrücklich als Vermutung
  gekennzeichnet**.
- **Beleg der Richtungsmengen in 4.5.** Der Quotient von 101 Euro je
  Megawattstunde ist belegt, denn Kosten und Menge stehen in derselben
  Mitteilung der Bundesnetzagentur. Die Aufteilung nach Richtung im Absatz zur
  Asymmetrie, nämlich 12,15 gegen 18,30 TWh, stammt dagegen aus energy-charts
  und trägt keinen Eintrag in `literature.bib`. Die zitierte Mitteilung führt
  eigene Richtungszahlen, nämlich 15 549 GWh Absenkung gegen 7732 GWh Erhöhung
  am Markt und 1302 GWh aus Reservekraftwerken; die Asymmetrie zeigt sich dort
  ebenso, die Zahlen unterscheiden sich aber, weil die Abgrenzungen andere
  sind. **Zu entscheiden:** entweder einen Eintrag für energy-charts anlegen
  oder den Absatz auf die Zahlen der Bundesnetzagentur umstellen.
- ~~Abschnitt 1.2 beschreibt noch die alte Sortierung von Kapitel 4.~~
  **Erledigt am 22.09.2026**, der Zielabsatz nennt jetzt die verdrängte
  Vermarktung und die Kosten der vollständigen Verdrängung.
- `fuellgrad_iterationen_2025.pdf` und `maximalpreis_iterationen_2025.pdf`
  liegen in `figures/chapter_3/`, stehen aber in keiner `figure`-Umgebung. Das
  deckt sich mit der Anweisung, wonach der Füllgradvergleich im Ergebnisteil
  nicht erscheint. Falls einer als Anhangbeleg gewünscht ist, ist er
  einzubinden.
- ~~Revenue-Index 260,0 in 3.3.1 und 3.3.2.~~ **Entschieden am 22.09.2026:
  bleibt.** Abschnitt 3.3.1 führt den Maßstab ein, Abschnitt 3.3.2 braucht ihn
  für das Verhältnis von 1,31; die Wiederholung steht in einem Absatz, der sie
  für seine eigene Rechnung braucht.

**Ältere Punkte, unverändert**

- **Reste der Liste G aus `archiv/DURCHSICHT_KAP1_3.md`**, am 22.09.2026
  gegen den Text geprüft. Erledigt sind G2 (die drei ungeprüften Belege stehen
  nicht mehr in Kapitel 3), G6 (vom Verfasser entschieden), G11 (3.2 heißt
  *Optimierung des Speicherbetriebs*), G12 (`isea_methodik_2026` ist
  eingetragen und zitiert) und G14 (kein Verweis auf `sec:model_critique` mehr
  im laufenden Text). G5 und G7 betreffen den Text nicht, denn weder die 8 Euro
  je Megawattstunde Degradationskosten noch die 2000 MW ausgeschriebene
  aFRR-Menge stehen in Kapitel 3. Offen bleiben:
    - ~~G1~~ und ~~G3~~ sind am 22.09.2026 vom Verfasser verortet, siehe
      Abschnitt 7 und den Vermerk zu 4.6.4 weiter oben.
    - **G13**, vor Abgabe zu prüfen, ob eine Mitteilung der Beschlusskammer zu
      Batteriespeichern ergangen ist. Recherchestand August 2026: keine.
    - **G4 und G9** gehören nach Kapitel 5, siehe Abschnitt 7.
    - **G8 und G10** sind modellseitig, nämlich das Ladezustandsband der
      Regelleistung je Vier-Stunden-Zeitscheibe gegen das kurative Band je
      Viertelstunde sowie die nicht nachgemessene Rechenzeit.
- In `chapters/chapter_3.tex` stehen zwei verwaiste Marken ohne zugehörige
  Überschrift, nämlich `sec:market_design_comparison` und `sec:product_design`.
  Sie sind Reste des geparkten Unterabschnitts aus G1. Die Prüfsuite meldet sie
  nicht, weil Prüfung 8 nur `fig:` und `tab:` gegen Verweise hält.
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
- **G1, Entscheidung des Verfassers vom 22.09.2026:** Der kapazitätsbasierte
  Redispatch beschafft im Kern dieselbe Größe wie eine kurative Vorhaltung und
  unterscheidet sich nur in Auslöser und Reaktionszeit. Das Argument gehört in
  die Diskussion. Die beiden verwaisten Marken in `chapter_3.tex` sind deshalb
  am selben Tag entfernt worden.

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
