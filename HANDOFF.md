# Übergabe an die nächste Sitzung, Stand 23.09.2026

Diese Datei ersetzt die Fassung vom 22.09.2026 nachts vollständig. Die alte
Fassung steht in der Git-Historie.

> **Zuerst lesen: es liegen ungesicherte Änderungen im Arbeitsverzeichnis.**
> Geändert und **nicht committet** sind `chapters/chapter_4.tex`, diese Datei
> und `ENTSCHEIDUNGSPROTOKOLL.md`, dazu liegt
> `AUFTRAG_FUELLGRAD_TAGESSTUNDEN.md` als neue und noch nicht versionierte
> Datei im Wurzelverzeichnis. Der Stand ist gebaut und geprüft, er ist nur
> nicht festgeschrieben. Committet wird allein auf das Wort „commite".
> Vor der ersten eigenen Änderung `git diff` lesen und den Verfasser fragen,
> ob der Stand zuerst committet werden soll.
> Der letzte Commit ist `13fdbef` vom 23.09.2026, `origin/main` steht auf
> `b2c5792` und ist damit einen Commit zurück.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3, 7 und 10. `ENTSCHEIDUNGSPROTOKOLL.md` hat über
16 000 Zeilen und wird nie ganz gelesen, sondern nur angehängt und gezielt
durchsucht.

---

## 1 Stand des Dokuments

Build sauber, Biber ohne Warnung, **104 Seiten**, Stand 23.09.2026. `python tools/pruefen.py
--alle` meldet allein den Altbefund in `chapters/chapter_5.tex` Zeile 91.
`main.tex` bindet die Kapitel 1 bis 4 ein, 5 und 6 sind auskommentiert; die
beiden Warnungen zu `ch:discussion` und `ch:conc` sind deshalb normal.

| Teil | Umfang |
|---|---|
| Kapitel 1 Einleitung | PDF-Seite 9 bis 13, fünf Seiten, **keine Reserve** |
| Kapitel 2 Grundlagen und Stand der Technik | PDF-Seite 14 bis 37 |
| Kapitel 3 Marktmechanismus und Modellierung | PDF-Seite 38 bis 56 |
| Kapitel 4 Ergebnisse | PDF-Seite 57 bis 68, logisch 49 bis 60 |
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

Zehn Abbildungen liegen in `figures/chapter_4/`, die zehnte seit dem
23.09.2026. Stand am 22.09.2026 abends
geprüft: alle neun sind deckungsgleich mit dem Lieferordner. Das Zeitmuster
zeigt die Summe als Hauptkurve, dazu Median und arithmetisches Mittel mit der
grauen Fläche dazwischen.

**Der Kapiteltitel lautet seit dem 22.09.2026 `Ergebnisse`**, Entscheidung des
Verfassers über das Analyse-Repository.

### 1.3 Der Durchgang Absatz für Absatz läuft, 4.1 ist fertig

Seit dem 22.09.2026 abends geht der Verfasser das geschriebene Kapitel 4
**Absatz für Absatz mit Claude durch**. Der Text wird nicht mehr einseitig
verfasst, sondern gemeinsam formuliert. Vorgabe des Verfassers: *„ich will
gerne mit dir formulieren"*.

| Abschnitt | Durchgang |
|---|---|
| Kapiteleinleitung | **durch**, in der Nacht vom 22.09. neu gefasst |
| 4.1 Verlauf des Dispatch | **durch**, drei Umbauten |
| 4.2 Preise beider Iterationen | **durch** am 23.09., drei Absätze, Füllgradabbildung eingebaut |
| 4.3 Verteilung der Verdrängungspreise | **durch** am 23.09., drei Absätze und Schlussfolgerungen |
| 4.4 bis 4.6.2 | geschrieben, noch nicht durchgegangen, **als nächstes 4.4** |
| 4.6.3, 4.6.4, 4.7 | leer, warten auf `sensi8` |

**4.1 trägt jetzt vier Absätze**, nämlich Aufbau und Mechanik, einen
tagesvergleichenden, einen allgemeinen und die Schlussfolgerungen. Der
tagesvergleichende Absatz beginnt mit *„Im Vergleich der fünf Tage fällt
Folgendes auf."* Die Zwischenstände sind im Text als Kommentar mit Datum und
Grund erhalten, die zurückgenommenen Fassungen stehen auskommentiert darüber.

**In der Nacht vom 22.09. sind neun Änderungen an 4.1 eingearbeitet**, alle
vom Verfasser diktiert: *Kachelfolgen* heißt jetzt *Fahrpläne*; die Einheit
der genannten Leistungen ist einmal erklärt; der 20.01. weicht
*erwartungsgemäß* als letzter und trägt den Abstand zum IDC; am 11.02. ist ab
50 Euro je Megawatt und Stunde die volle Leistung von 200 MW über alle
24 Stunden reserviert; der IDC-Satz kommt ohne Vorgriff auf die
Erlösaufteilung des Abschnitts 4.2 aus; der Satz über die fünf Tage als
Grundlage ist gestrichen; die aFRR bindet die Leistung, der IDC zieht seinen
Wert aus wenigen spreadstarken Stunden; und der Schlusssatz lautet, dass der
Preis bis auf die FCR von allen Märkten bestimmt wird.

---

## 2 Dateiübersicht

Am 22.09.2026 aufgeräumt, weil das Wurzelverzeichnis unübersichtlich wurde.
**Im Wurzelverzeichnis liegen nur noch Dateien, die gelten.**

### Wurzelverzeichnis, sechs Dateien

| Datei | Rolle |
|---|---|
| `CLAUDE.md` | Auftrag, Stilregeln, Begriffe, Prüfungen. Claude ändert sie nicht, der Verfasser zieht selbst nach. |
| `HANDOFF.md` | diese Datei, Einstiegspunkt jeder Sitzung |
| `WORKFLOW.md` | Vorgehen: Absatzplan (3), Kommentardurchgang (7), Arbeitsweise am Absatz (10) |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen, nie ganz lesen |
| `README.md` | Beschreibung des Repositorys |
| `AUFTRAG_MAXIMASTUNDEN.md` | Auftrag an das Analyse-Repository vom 23.09.2026, Herkunft der Maxima in 4.3, dazu die Antwort auf Update 5. Nach Erledigung ins Archiv. |

### `archiv/`, sechzehn Dateien, nur zum Nachschlagen

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
| `AUFTRAG_FUELLGRAD_TAGESSTUNDEN.md` | Auftrag zum Füllgrad vom 23.09., vom Verfasser am selben Tag ins Archiv gelegt | Abschnitt 2 und Rückfrage 3.1 geliefert, Rückfrage 3.2 und die beiden Nebenpunkte laufen weiter, siehe Abschnitt 6 |

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
- **Eine Bildunterschrift hat zwei gesetzte Zeilen**, drei sind die oberste
  Grenze. Vorgabe des Verfassers vom 23.09.2026, an diesem Tag für alle 34
  Unterschriften der Arbeit umgesetzt. Gemessen wird am gebauten PDF über
  `pdftotext -layout`, denn `\cite`, `\ac` und `\si` setzen kürzer, als sie
  im Quelltext stehen. Was die Unterschrift nicht mehr trägt, gehört in den
  Fließtext. Bei neuen Abbildungen mitführen.
- **Kein Satz nach dem Muster „zeigt A und nicht B“**, Vorgabe des Verfassers
  vom 23.09.2026. Statt der Verneinung wird die Aussage positiv gewendet,
  etwa „Aus den fünf Tagen folgt die Reihenfolge der Verdrängung, aus dem
  Jahreslauf das Gewicht der einzelnen Märkte.“ In 4.4 bis 4.6 stehen acht
  Stellen dieses Musters noch offen, sie gehören in den Durchgang dort.
- **Das Wort Preisvektor kommt nicht vor**, Vorgabe des Verfassers vom
  23.09.2026. Kapitel 4 sagt stattdessen *die Preise der ersten* und *der
  zweiten Iteration*. In `chapters/chapter_5.tex` steht das Wort noch einmal,
  die Datei ist auskommentiert und beim Schreiben von Kapitel 5 nachzuziehen.
- **Die Einheit der Erlöse steht als Makro `\TsdEurMWa`**, seit dem
  23.09.2026 an allen Stellen des Kapitels. Ausgeschrieben steht sie allein
  bei ihrer Einführung in der Kapiteleinleitung.
- **Die kurative Reservierung wird je Stunde bestimmt**, nicht je
  Viertelstunde. Zeitscheibe und Bindungsdauer betragen im Basisfall eine
  Stunde, das Jahr 2025 trägt deshalb 8758 Preise je Richtung. Am 23.09.2026
  gegenüber der Vorgabe des Verfassers berichtigt, die 96 mal 365 nannte.
- **Kein Abschnitt beginnt mit einem Bild**, Vorgabe des Verfassers vom
  22.09.2026. In Kapitel 4 steht seither **jede Abbildung hinter dem Absatz,
  der sie einführt**. Das gilt auch für die beiden Abbildungen im Inneren von
  4.4 und 4.6.1, damit das Kapitel eine Reihenfolge trägt. Stilregel 16
  bleibt gewahrt, denn der einführende Absatz trägt den Verweis. Beim
  Einfügen neuer Abbildungen in 4.6.3, 4.6.4 und in Kapitel 5 ist die Regel
  mitzuführen.
- **Jeder Abschnitt endet mit drei bis fünf Sätzen Schlussfolgerungen**,
  Vorgabe des Verfassers vom 22.09.2026. Sie sind für die spätere Diskussion
  von Belang, nehmen sie aber nicht vorweg. Die Eröffnungsformel lautet
  **„Aus dieser Untersuchung lässt sich Folgendes mitnehmen."** und bleibt
  über alle Abschnitte gleich, damit die Stelle erkennbar ist. **Kein
  erstens, zweitens, drittens**, ausdrückliche Vorgabe. Kein Verweis auf
  Kapitel 5, weil Stilregel 15 strukturelle Vorverweise ausschließt. In 4.1,
  4.2 und 4.3 steht der Absatz, für 4.4 bis 4.6 fehlt er noch.
- **Der Fließtext wiederholt nicht den Anhang.** Der tagesbezogene Absatz in
  4.1 beschrieb anfangs denselben Schwellenlauf wie Anhang F. Er zeigt jetzt
  je Tag den Markt, für den der Tag ausgewählt ist, und höchstens eine
  auffällige Gegenüberstellung. Am Redispatchtag stehen die Handelsmärkte im
  Vordergrund, weil viel Preisspanne dort viel Handel bedeutet.
- **Leistungsangaben in 4.1 und Anhang F sind Tagesmittel über beide
  Richtungen**, deren Summe höchstens 200 MW beträgt. Der Satz steht einmal
  in 4.1 und einmal in Anhang F. Die Spaltenüberschrift der Quelle lautet
  *Mittlere belegte Leistung je Markt in MW*, es sind also Megawatt und nicht
  Megawattstunden.
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
- **Gleitumgebungen verschieben, nicht neu schreiben.** Beim Umstellen der
  Abbildungslage hat ein Skript die `figure`-Blöcke zeilenweise umgehängt und
  den Fließtext unangetastet gelassen; die Kommentarzeilen sind an der
  Überschrift geblieben, weil sie die Entscheidungen zur Überschrift
  dokumentieren. Gegenprobe war, dass der Absatz hinter der Umgebung deren
  Marke auch nennt.
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
- **Rückfrage an den Verfasser, ungeklärt.** Seine Vorgabe lautete
  *„afrr bindet den größten teil der leistung und afrr hat durch viel spread
  in wenigen stunden auch einen hohen wert"*. Das zweite *aFRR* ist als
  **IDC** umgesetzt, weil der Wert aus wenigen spreadstarken Stunden den
  kontinuierlichen Intraday-Handel beschreibt und nicht die
  Kapazitätsvorhaltung. Der Satz steht so in 4.1. **Vor dem nächsten Commit
  bestätigen lassen.**
- **Gehandelte Energie je Markt und Tag fehlt.** Der Verfasser hält sie für
  aussagekräftiger als die Leistungs-Tagesmittel in MW: *„die gehandelte
  energie wäre noch interessanter und aussagekräftiger"*. Diese Größe steht
  **nicht** in `ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md`. Erforderlich wäre ein
  Auftrag an das Analyse-Repository, die Energie je Markt, Tag und Preisstufe
  auszuweisen. **Update 5 vom 23.09.2026: kein neuer Lauf nötig**, die Größe
  steckt in den vorhandenen Zeitreihen. Das Analyse-Repository hat drei Wege
  zur Wahl gestellt, und **Weg 1 ist gewählt**, nämlich getrennte Blöcke für
  gehandelte Arbeit und vorgehaltene Leistung. Begründung in
  `AUFTRAG_MAXIMASTUNDEN.md` Abschnitt 4. Bis zur Lieferung stehen die
  MW-Werte im Text, mit dem erklärenden Satz zur Einheit.
- **Widerspruch im Analyse-Repository noch nicht gemeldet.**
  `ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` Abschnitt 2.3 nennt den 11.02.2025 als
  Tag, an dem der Day-Ahead zuerst weicht. Abschnitt 2.1 derselben Datei zeigt
  das Gegenteil, nämlich die Halbierung der aFRR bei 10 und die von Day-Ahead
  und IDC erst bei 15 Euro je Megawatt und Stunde. Die Schriftfassung folgt
  der Tabelle und nennt den 26.08.2025. ~~Gemeldet.~~ **Erledigt mit Update 5
  vom 23.09.2026**, der Fehler lag im Analyse-Repository und ist dort
  berichtigt. Der Day-Ahead weicht an genau einem der fünf Tage zuerst,
  nämlich am 26.08.2025, sodass die Stelle im Text richtig steht.
- ~~Einheit uneinheitlich.~~ **Erledigt am 23.09.2026**, das Makro steht an
  allen acht Stellen, ausgeschrieben allein in der Kapiteleinleitung.
- ~~Füllgrad über die Tagesstunden.~~ **Geliefert und eingebaut am 23.09.2026.**
  Abschnitt 4.2 trägt dafür einen dritten Absatz und Abbildung 4.2. Der
  Befund ist stärker als erwartet: die erste Iteration lässt gerade die
  **teuren** Stunden offen, der Füllgrad einer Tagesstunde fällt mit ihrem
  Preis ($r=-0{,}853$ entladend, $-0{,}608$ ladend). Die alten Füllgrade von
  84,5 und 89,0 sowie 99,04 und 99,78 Prozent sind **überholt**; gültig sind
  85,94 und 89,60 für die erste und zweimal 99,98 Prozent für die zweite
  Iteration.
- ~~Laufzahlen unter Vorbehalt.~~ **Erledigt mit Update 5 vom 23.09.2026.**
  Gemessen über eine Stichprobe von 16 Tagen, Läufe des Optimierungsmodells
  je Tag: erste Iteration 83 / 136 / 194, zweite Iteration 341 / 432 / 2284,
  zusammen 446 / 566 / 2479 als Minimum, Median und Maximum. Im Text steht
  auf Vorgabe des Verfassers allein das Verhältnis, nämlich **gut das
  Dreifache** aus 432 zu 136. Die zuvor vorgegebene Angabe *rund das
  Vierfache* ist damit überholt.
- **Abschnitt 3.2.4 bleibt richtig und unverändert.** Die dortigen 84 bis 167
  Läufe der ersten Iteration liegen innerhalb der gemessenen 83 bis 194, und
  *einige hundert* trifft die zweite Iteration im Median. Allein das Maximum
  von 2284 Läufen am 15.01.2025 liegt außerhalb dieser Wendung.
- **Woher die Maxima kommen, ist nicht geklärt.** Abschnitt 4.3 nennt 1008
  und 510\,€/(MW·h) als Einzelwerte, ohne sie zurückzuführen. Beauftragt am
  23.09.2026 in `AUFTRAG_MAXIMASTUNDEN.md`, nämlich welcher Markt in diesen
  Stunden zuletzt weicht und woran die Höhe liegt.
- **Die exakte Jahresverteilung der Läufe ist nicht bestellt.** Sie hätte
  eine Wiederholung des Jahreslaufs von rund zweieinhalb Stunden verlangt.
  Empfehlung an den Verfasser: dabei bleiben, denn der Rechenaufwand ist
  eine Angabe zum Verfahren und kein Ergebnis der Arbeit.
- **Markterlös der offenen Stunden nicht verfügbar.** Der Anteil der
  offenen Tagesstunden an den 88,6\,Tsd.\,€/(MW·a) lässt sich aus dem
  vorhandenen Lauf nicht ziehen, weil die Erlösdatei je Tag und nicht je
  Stunde geführt ist. Dafür müsste der Iterationsvergleich neu laufen.
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
- **Aus 4.2, Vorgabe des Verfassers vom 23.09.2026:** die erste Iteration ist
  ineffizient, weil sie allen Stunden eines Tages denselben Preis vorgibt. An
  dieser Stelle ist das Zeitscheibenproblem noch einmal aufzunehmen.
- **Aus 4.2, Vorgabe des Verfassers vom 23.09.2026:** die kurative
  Reservierung gibt dem Speicher eine Möglichkeit, seinen Erlös allein durch
  eine klügere Verteilung auf die Märkte zu steigern, sofern er die richtigen
  Preise setzt.
- **Aus 4.3, Vorgabe des Verfassers vom 23.09.2026:** die teuersten Stunden
  sind schwer zu prognostizieren, und ein Preis dieser Höhe wird selten
  erreicht. Die Wahrscheinlichkeit, dass solche Stunden eintreten, schlägt
  sich gleichwohl im Preis nieder. Das gehört in die Diskussion der
  Verteilung.
- **Aus 4.3, Vorgabe des Verfassers vom 23.09.2026:** der ermittelte Preis
  ist mit Unsicherheit behaftet, und der Betreiber würde auf ihn einen
  Aufschlag für den eigenen Aufwand des Anbietens nehmen. Das fügt sich an
  die Entscheidung, dass der Preis nur den opportunitätskostenbasierten Teil
  des Gebots bildet.
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
