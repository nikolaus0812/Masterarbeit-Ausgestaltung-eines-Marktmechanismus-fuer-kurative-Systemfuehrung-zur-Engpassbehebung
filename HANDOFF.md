# Übergabe an die nächste Sitzung, Stand 17.09.2026

Diese Datei übergibt den Stand der Fable-Sitzung vom 16. und 17.09.2026 an
einen Opus-Chat, weil das Wochenkontingent des Verfassers für Fable erschöpft
ist. Zuerst `CLAUDE.md` lesen, dann diese Datei, dann `WORKFLOW.md`
Abschnitt 7. Das Protokoll `ENTSCHEIDUNGSPROTOKOLL.md` nur anhängen, nie ganz
lesen, es hat über 9000 Zeilen.

## 1 Was gerade läuft

Der Verfasser geht Kapitel 3 Abschnitt für Abschnitt durch und gibt seine
Kommentare direkt im Chat, meist als Zitat des Satzes aus dem PDF plus
Anweisung. Claude setzt jeden Kommentar sofort um, baut das PDF, fährt
`tools/pruefen.py` und committet nur, wenn der Verfasser "commite" sagt.
Die Kommentare des Verfassers haben Vorrang vor den offenen Vorschlägen in
`DURCHSICHT_KAP1_3.md`. `KOMMENTARE_KAP3.md` wird nicht genutzt.

Stand des Durchgangs: Kapiteleinleitung, 3.1, 3.1.1, 3.1.2, 3.2 Einleitung,
3.2.1, 3.2.2, 3.2.3 und der größte Teil von 3.2.4 sind kommentiert und
umgesetzt. Der Verfasser war zuletzt im Problemabsatz von 3.2.4 (Bisektion
reicht nicht aus). Noch nicht kommentiert sind der Rest von 3.2.4 (zweite
Iteration, Schleifenabsatz) und 3.3 in der neuen Gliederung 3.3.1 bis 3.3.3.
Letzter Commit: a22bd5b.

## 2 Entscheidungen vom 16. und 17.09.2026, die beim Schreiben binden

Alle stehen ausführlich im Protokoll unter chapter_3.tex und in `CLAUDE.md`
Abschnitt 5 und 7. Kurz:

- **Vorgegebener Reservierungspreis** ist der Preis je Stunde und Richtung,
  den die Suche dem Tagesmodell vorgibt, eingeführt in der Einleitung von
  3.2. **Kurativer Reservierungspreis** bleibt die gesuchte Größe, nämlich der
  kleinste vorgegebene Reservierungspreis, bei dem die Stunde voll reserviert
  ist. **Gebotspreis** für den Preis eines Gebots in der Ausschreibung. Nie
  nur "Preis" schreiben, wenn eine dieser drei Größen gemeint ist.
- **Kurative Bindung** für Leistungsband plus Ladezustandsband, definiert in
  2.1.2. **Referenzfahrplan** und **Referenzerlös** für den Lauf ohne kurative
  Reservierung, nicht "ungebundener Fahrplan".
- **Abruf wird gesondert vergütet** (Energie und Nachlaufpflicht je MW), die
  Preise dafür werden nicht festgelegt. Entscheidung 14 in `CLAUDE.md`.
- Weber-Abgrenzung in 3.2.4 gestrichen, der Vergleich mit der Festlegung
  gehört nach Kapitel 5 (offener Punkt).
- "halbieren" statt "bisektieren", kein "Vektor" in 3.2.4, Preisachse der
  Bisektionsabbildung ist logarithmisch.
- Erlösindex der Battery Charts: Bezugsanlage 2 h Energieinhalt je Leistung
  und 2 Zyklen je Tag, vom Verfasser am 17.09.2026 bestätigt. Quelltext des
  Index liegt lokal unter `C:/GIT-HUB/battery_revenue_index-main`, die
  Parameter stehen im Protokolleintrag vom 17.09.2026 zu 3.3.1.
- Energieinhalt je Leistung aus dem Marktstammdatenregister
  (`analysen/mastr_speicher`), mFRR-Ausschluss mit Preisen 2025
  (`analysen/mfrr_leistungspreise`).

## 3 Arbeitstechnik, die sich bewährt hat

- Änderungen an Kapiteldateien immer über ein Python-Skript, das die Datei
  mit `newline=""` liest und mit CRLF zurückschreibt. Alter Satz bleibt als
  Kommentar mit Datum und Grund über der neuen Fassung. Prüfen, dass jeder
  Anker genau einmal greift.
- **Skripte mit Backslashes nur über das Write-Werkzeug anlegen und dann
  ausführen.** Bash-Heredocs verstümmeln `\a`, `\t`, `\u` und haben schon
  Steuerzeichen in chapter_3.tex geschrieben.
- `tools/kap3_durchsicht_lib.py` bietet die Klasse `Datei` mit `idx`,
  `satz`, `verbinde`, `verschiebe`, `absatz_vor` und `speichere`. `DATUM`
  dort vor Gebrauch auf das Tagesdatum setzen.
- `tools/extract_alle.py` rendert Kapitel 1 bis 3 als Text mit nummerierten
  Absätzen in das Temp-Verzeichnis, nützlich für Dopplungs- und
  Anschlussprüfungen ohne PDF.
- Layoutprüfung: `pdftotext -layout main.pdf`, Seite im PDF minus 8 ist die
  logische Seite. Der Text kommt in cp1252 an, beim Lesen in Python
  `encoding="cp1252", errors="replace"` setzen.
- Build: `pdflatex; biber; pdflatex; pdflatex`. Die drei Warnungen zu
  `ch:results`, `ch:discussion`, `ch:conc` sind normal, die Kapitel sind
  auskommentiert. `python tools/pruefen.py --alle` meldet zwei Altbefunde in
  den auskommentierten Kapiteln 4 und 5, Kapitel 1 bis 3 sind ohne Befund.
- **Subagenten nur nach Rückfrage**, mit Zweck und Anzahl.
- Committen nur auf "commite" des Verfassers, nie pushen.

## 4 Modellrepository

`C:/GIT-HUB/bess_dispatch_optimization`, Interpreter mit matplotlib:
`C:/ProgramData/anaconda3/envs/venv_mode/python.exe`. Der Verfasser hat dort
eigene ungesicherte Änderungen in mehreren Dateien (festlegung.py,
pp_bilder.py, README und reservierungspreis_bisektion.py in
09_reservierungspreis_verfahren, ANWEISUNG_ABBILDUNGEN.md, DIAGRAMME.md,
erloesaufteilung.py). Diese Dateien nicht anfassen und nicht committen.
Abbildungen für Kapitel 3 entstehen unter `analysen/code/schrift/`, zuletzt
`16_dispatch_festpreis/dispatch_festpreis.py` für Abbildung 3.6, und werden
nach `figures/chapter_3/` kopiert.

## 5 Offen

- Rest des Kommentardurchgangs, siehe Abschnitt 1.
- `DURCHSICHT_KAP1_3.md`: Dopplungen F4, F5, F11, F12, F13, F18, F19, F21,
  F23 bis F25 und die Listen B3 und C3 für Kapitel 1 und 2 warten auf
  Entscheidung des Verfassers, jede einzeln mit Wortlaut vorlegen.
- Vergleich mit der Festlegung in Kapitel 5 (Protokoll, offene Punkte).
- Preisreihen in Kapitel 3 zitieren noch SMARD, Umstellung auf energy-charts
  oder EPEX wartet auf Entscheidung (Protokoll unter literature.bib).
