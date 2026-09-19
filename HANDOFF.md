# Übergabe an die nächste Sitzung, Stand 19.09.2026

Diese Datei ersetzt die Fassung vom 17.09.2026 vollständig. Die alte Fassung
steht in der Git-Historie unter `db08ed2`.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitt 7. `ENTSCHEIDUNGSPROTOKOLL.md` hat über 10 000 Zeilen
und wird nie ganz gelesen, sondern nur angehängt und gezielt durchsucht.

---

## 1 Was in dieser Sitzung zu tun ist

Der Verfasser geht das gesetzte PDF durch und veranlasst Änderungen. Der Ablauf
ist seit dem 16.09.2026 eingespielt und hat sich bewährt:

1. Der Verfasser zitiert eine Stelle aus dem PDF, meist mit den
   Trennzeichen des Umbruchs, und schreibt dahinter, was daran nicht stimmt.
   Die Anweisung ist oft knapp und in Tippschreibweise, etwa *"streichen und
   einfach im Text die Zitate setzen"* oder *"das steht völlig aus dem
   Kontext"*.
2. Du suchst die Stelle in der Kapiteldatei, nicht im PDF, prüfst den
   Zusammenhang des ganzen Absatzes und setzt die Änderung um.
3. Danach: `python tools/pruefen.py <datei>`, Build, und du zeigst die neue
   Fassung im Chat, nicht das ganze Kapitel.
4. Committet wird **nur**, wenn der Verfasser *"commite"* schreibt. Nie
   pushen.

**Die Kommentare des Verfassers haben Vorrang** vor allen offenen Vorschlägen
in `DURCHSICHT_KAP1_3.md`.

Kapitel 1 und die Einleitung von Kapitel 2 sind am 18. und 19.09.2026 auf
diesem Weg überarbeitet worden. Der Verfasser war zuletzt in Abschnitt 2.1.1.

---

## 2 Stand des Dokuments

Letzter Commit `3679ed7`. Build sauber, **94 Seiten**.

| Teil | PDF-Seiten | Umfang |
|---|---|---|
| Kapitel 1 Einleitung | 9 bis 13 | 5 Seiten, letzte Seite **randvoll** |
| Kapitel 2 Grundlagen und Stand der Technik | 14 bis 36 | 23 Seiten |
| Kapitel 3 Marktmechanismus und Modellierung | 37 bis 55 | 19 Seiten |
| Kapitel 4 Exemplarische Anwendung und Ergebnisse | 56 bis 63 | 8 Seiten, Gerüst |
| Anhänge A bis F | 74 bis 94 | |

Logische Seitenzahl ist PDF-Seite minus acht.

`main.tex` bindet die Kapitel 1 bis 4 ein, die Kapitel 5 und 6 sind
auskommentiert. Die beiden Warnungen zu `ch:discussion` und `ch:conc` sind
deshalb normal und kein Befund. `python tools/pruefen.py --alle` meldet einen
Altbefund in `chapters/chapter_5.tex` Zeile 91, der zum auskommentierten
Kapitel gehört.

**Kapitel 1 hat keine Reserve mehr.** Die fünfte Seite trägt 40 Zeilen, jeder
zusätzliche Satz kippt das Kapitel auf eine sechste Seite. Sieben nicht
umgesetzte Kürzungsvorschläge mit zusammen rund fünf Zeilen stehen im Protokoll
unter dem Eintrag vom 18.09.2026 zur Kürzung.

---

## 3 Entscheidungen der letzten beiden Tage, die beim Schreiben binden

Ausführlich im Protokoll unter `chapter_1.tex` und `chapter_2.tex`, Einträge
vom 18. und 19.09.2026.

- **Zeitlicher Rahmen ist das Trendjahr 2032 des NEP**, nicht mehr das Jahr
  2030. Belegt mit Kapitel 2.8 des zweiten Entwurfs NEP 2037/2045, Version
  2025: 260 GW Photovoltaik, 115 GW Windenergie an Land, etwa 90 % der
  Stromnachfrage aus erneuerbaren Energien, 41,1 GW Großbatteriespeicher,
  Engpassmanagementbedarf 14,8 TWh. Gerechnet wird weiterhin mit den
  beobachteten Preisen des Jahres 2025.
- **Die drei Teilfragen sind gestrichen** und sollen nirgends wieder
  auftauchen. Die Leitfrage trägt allein der Satz in 1.2, der prüft, ob die
  marktlich beschaffte Vorhaltung mit dem präventiven Redispatch mithält. In
  `chapters/chapter_6.tex` steht ein Hinweis, dass die dortige Gliederung der
  Zusammenfassung neu zu fassen ist.
- **Begriffe stehen als Nebensatz oder Apposition im laufenden Text**, nicht in
  einem eigenen Definitionsabsatz. Der Verfasser hat einen solchen Absatz in
  1.2 als "nimmt zu viel vorweg" verworfen.
- **Kein Absatz beginnt mit einem Literaturanker.** Der Auftakt von 2.1.1 mit
  InnoSys 2030 ist gestrichen, weil "damit zu starten holprig ist". Was ein
  Projekt erarbeitet hat, steht dort, wo davon erzählt wird.
- **Ein Absatz beginnt mit seiner Folgerung**, wenn er sonst zu weit ausholt.
  So ist der Absatz zum Fünf-Zustands-Modell in 2.1.1 umgestellt worden.
- **Fußnoten werden aufgelöst**, die Belege stehen im Fließtext und jeweils bei
  dem Satz, den sie tragen. Kapitel 2 hat keine Fußnote mehr.
- Verbindliche Begriffe und gesperrte Ausdrücke stehen unverändert in
  `CLAUDE.md` Abschnitt 5. Die Stilregeln in Abschnitt 4 gelten
  uneingeschränkt, besonders Regel 1 (vier bis acht Sätze je Absatz), Regel 5
  (keine Pronomen über die Satzgrenze), Regel 15 (keine strukturellen Vor- und
  Rückverweise) und Regel 17 (ein Hauptsatz, höchstens ein Nebensatz).

---

## 4 Arbeitstechnik, die sich bewährt hat

- Änderungen an Kapiteldateien **immer über ein Python-Skript**, das die Datei
  mit `open(pfad, encoding="utf-8", newline="")` liest und mit CRLF
  zurückschreibt. Das Skript bricht ab, wenn ein Anker nicht genau einmal
  greift. Ersetzter Fließtext bleibt als Kommentar mit Datum und Grund über der
  neuen Fassung stehen, so verlangt es `CLAUDE.md` Abschnitt 10.
- **Skripte mit Backslashes oder Umlauten nur über das Write-Werkzeug anlegen**
  und dann ausführen. Bash-Heredocs und `python -c` verstümmeln `\c`, `\a`,
  `\t` und `\u`. Das ist in dieser Sitzung mehrfach passiert.
- Für kurze, eindeutige Ersetzungen genügt das Edit-Werkzeug, es erhält die
  Zeilenenden.
- Markdown-Dateien im Arbeitsverzeichnis haben **CRLF**, obwohl `CLAUDE.md`
  Abschnitt 6 von LF spricht. `core.autocrlf` ist auf dieser Maschine `true`
  und `.gitattributes` normiert auf LF im Repository. Wer an
  `ENTSCHEIDUNGSPROTOKOLL.md` anhängt, schreibt die neuen Zeilen mit CRLF.
- Layoutprüfung ohne PDF-Betrachter: `pdftotext -layout main.pdf -` und die
  Ausgabe an `\f` in Seiten teilen. So lässt sich zählen, wie voll eine Seite
  ist und wo ein Kapitel endet.
- Build: `pdflatex main; biber main; pdflatex main; pdflatex main`. `biber` nur
  nötig, wenn sich Zitate geändert haben.
- **Subagenten nur nach Rückfrage**, mit Zweck und Anzahl. Vorgabe des
  Verfassers vom 16.09.2026.
- Zu jedem Abschnitt, an dem gearbeitet wurde, gehört ein Protokolleintrag nach
  `CLAUDE.md` Abschnitt 9, mit den zurückgenommenen Formulierungen im Wortlaut
  und mit jeder eigenständigen Ableitung als solcher gekennzeichnet.

---

## 5 Dateien im Repository

Aktiv im Wurzelverzeichnis:

| Datei | Zweck |
|---|---|
| `CLAUDE.md` | bindender Auftrag, zuerst lesen |
| `WORKFLOW.md` | Ablauf für Korrektur, Neufassung und Kommentardurchgang |
| `HANDOFF.md` | diese Datei |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen |
| `DURCHSICHT_KAP1_3.md` | offene Vorschläge, allein Liste G ist noch aktuell |
| `KAPITEL_4_AUFBAU.md` | Vorlage für Kapitel 4, gehört der parallelen Sitzung |
| `README.md` | Kurzbeschreibung des Repositorys |

Am 19.09.2026 nach `archiv/` verschoben, weil abgearbeitet:
`KOMMENTARE_KAP3.md` (nie genutzt, der Verfasser kommentiert im Chat),
`KONTROLLAUFTRAG_FABLE.md` und `KONTROLLE_FABLE.md` (alle 75 Absatzbefunde und
22 Streichkandidaten sind entschieden und umgesetzt). Im Archiv liegen
außerdem `AENDERUNGEN_KAP1_2.md`, `AENDERUNGEN_KAP3.md`, `ANWEISUNG_KOMMENTARE.md`,
`KOMMENTARBESTAND_KAP3.md`, `KUERZUNGEN_KAP1_2.md` und `STRUKTUR.md`. Das
Archiv ist Nachschlagewerk und wird nicht mehr fortgeschrieben.

`quellencheck_bericht.md` erzeugt `tools/quellencheck.py` bei jedem Lauf neu,
die Datei ist in `.gitignore` und darf jederzeit gelöscht werden.

---

## 6 CLAUDE.md ist an vier Stellen überholt

Der Verfasser zieht `CLAUDE.md` selbst nach, Claude ändert die Datei nicht
stellvertretend. Offen sind:

1. **Abschnitt 1, Dateiliste.** `KOMMENTARE_KAP3.md` steht dort noch im
   Wurzelverzeichnis, liegt aber seit dem 19.09.2026 in `archiv/`.
2. **Abschnitt 5, Begriffe.** Die Abgrenzung "kein Marktdesign mit
   prognostizierten Preisen" bezieht sich auf einen Satz, der am 18.09.2026 aus
   1.2 gestrichen ist.
3. **Abschnitt 7, Entscheidung 4.** Dort steht das Jahr 2030 als qualitativer
   Rahmen. Der Rahmen ist seit dem 18.09.2026 das Trendjahr 2032 des NEP.
4. **Abschnitt 10, Dateihandhabung.** Für `chapters/chapter_3.tex` gilt seit dem
   17.09.2026 die Ausnahme, dass die Datei kommentarfrei bleibt. Ersetzter Text
   wandert dort in die Markdown-Dateien und nicht in einen Kommentar. Für alle
   übrigen Kapiteldateien gilt die Regel unverändert.

---

## 7 Offene Punkte

**Inhaltlich, mit Entscheidungsbedarf des Verfassers**

- Die Abgrenzung "wie viel Engpassmanagement die kurative Systemführung
  einspart, ist nicht Gegenstand, dafür wäre ein Netzmodell nötig" ist am
  18.09.2026 aus 1.2 gestrichen worden und steht seither nirgends mehr. Sie trug
  auch die Streichung in 3.2 (Streichkandidat S-11). Vorschlag: 3.2.1 oder
  Kapitel 5.
- Der Absatz zu den Vergütungslogiken in 1.2 hat rund vierzehn Sätze.
  Umbruchvorschlag vor *"Was die Vorhaltung den Betreiber kostet"*.
- Der Zielabsatz in 1.2 hat neun Sätze, Stilregel 1 lässt acht zu.
- `KAPITEL_4_AUFBAU.md` stützt sich in Abschnitt 1.1 auf die drei Teilfragen aus
  1.2, die es nicht mehr gibt. Die Datei gehört der parallelen Sitzung.
- Der angekündigte Vergleich der marktlich beschafften Vorhaltung mit dem
  präventiven Redispatch ist in den Kapiteln 4 und 5 noch nicht eingeplant.
- Der Ausdruck "kurative Verfügbarkeit" steht noch in 2.4 und ist durch
  "kurative Vorhaltung" zu ersetzen.
- Die Ankündigung von Kapitel 4 in 1.2 folgt der Sortierung aus
  `KAPITEL_4_AUFBAU.md`. Verschiebt die parallele Sitzung die Reihenfolge, ist
  der Satz nachzuziehen.

**Listen und Belege**

- `DURCHSICHT_KAP1_3.md` Liste G, vierzehn Punkte aus den Kommentaren von
  Kapitel 3, nichts davon umgesetzt. Darunter G2 (drei ungeprüfte Belege), G5
  (Degradationskosten von 8 Euro je Megawattstunde ohne Quelle), G7
  (ausgeschriebene aFRR-Menge von 2000 MW ohne Beleg), G13 (vor Abgabe prüfen,
  ob eine Mitteilung der Beschlusskammer zu Batteriespeichern ergangen ist).
- Die Listen A bis F derselben Datei stammen vom 15.09.2026 und sind durch die
  seitherigen Überarbeitungen teilweise überholt. Vor Gebrauch am PDF prüfen.
- Preisreihen in Kapitel 3 zitieren noch SMARD, die Umstellung auf
  energy-charts oder EPEX wartet auf eine Entscheidung.
- Ein Vorrang des Redispatch im Engpassmanagement ist in 2.1 zurückhaltend
  formuliert, weil die Daten der Bundesnetzagentur das Maßnahmenvolumen des
  gesamten Netzengpassmanagements ausweisen. Wird der Anteil belegt, ist der
  Satz zu beziffern.

---

## 8 Modellrepository

`C:/GIT-HUB/bess_dispatch_optimization`, Interpreter mit matplotlib:
`C:/ProgramData/anaconda3/envs/venv_mode/python.exe`.

Der Verfasser hat dort eigene ungesicherte Änderungen in mehreren Dateien.
Vor jedem Zugriff `git status` lesen und fremde Änderungen nicht anfassen.

**Abbildungen.** Größe und Seitenverhältnis werden **im Erzeugungsskript**
gesetzt, über `ts.subplots(breitenanteil=..., seitenverhaeltnis=...)` mit
`TEXTWIDTH = 16 cm`, und **niemals** über `\includegraphics` skaliert. Eine
Skalierung in LaTeX verkleinert die Schrift der Abbildung gegenüber dem
Fließtext. Die Skripte liegen unter `analysen/code/schrift/`, die fertigen PDF
werden nach `figures/chapter_<n>/` kopiert.

Der Quelltext des Erlösindex der ISEA Battery Charts liegt lokal unter
`C:/GIT-HUB/battery_revenue_index-main`. Seine Parameter und die Abgrenzung
seiner marktübergreifenden Leistungsaufteilung stehen im Protokoll unter dem
Eintrag vom 17.09.2026 zu 3.3.1.
