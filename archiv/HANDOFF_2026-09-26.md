# Übergabe an die nächste Sitzung, Stand 26.09.2026

Diese Datei ersetzt die Fassung vom 25.09.2026 vollständig. Die alte Fassung
liegt unter `archiv/HANDOFF_2026-09-25.md`, ältere in der Git-Historie.

> **Das Arbeitsverzeichnis ist sauber.** `origin/main` stand zuletzt auf `d4ea26f`
> vom 26.09.2026, die spaeteren Commits desselben Tages stehen zum Push aus. Gepusht wird
> nur auf ausdrückliche Anweisung, committet nur auf das Wort „commite".
>
> **Kapitel 5 ist am 26.09.2026 abgeschlossen** und vollständig geprüft. Der
> Verfasser liest es als Nächstes am Stück, mit dem PDF vom Stand `d4ea26f`.
> Kapitel 6 ist in `main.tex` noch auskommentiert.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3, 7 und 10. `ENTSCHEIDUNGSPROTOKOLL.md` hat über
16 000 Zeilen und wird nie ganz gelesen, sondern nur angehängt und gezielt
durchsucht; die Einträge zu Kapitel 5 stehen am Ende des Abschnitts
`## chapter_5.tex`.

**Eine Warnung, die den 26.09.2026 dreimal aufgehalten hat.** Der Verfasser
zitiert beim Kommentieren aus dem PDF. Ist das PDF älter als der Stand der
Datei, zitiert er zurückgenommene Sätze, und die Sitzung diskutiert Text, den
es nicht mehr gibt. **Vor jedem Kommentardurchgang neu bauen**, und Claude
prüft jedes Zitat gegen `chapters/chapter_5.tex`, bevor sie es beantwortet.

---

## 1 Stand des Dokuments

### 1.0 Stand vom 26.09.2026, Kapitel 5 abgeschlossen

**124 Seiten**, Build sauber, Biber ohne Warnung, `python tools/pruefen.py
--alle` ohne Befund in 15 Dateien, `tools/pruefe_stil.py` ohne Verstoß in
Kapitel 4 und 5, Kapitel 1 bis 3 allein mit den Altbefunden zum Doppelpunkt.
`python tools/absatzlaengen.py chapters/chapter_5.tex` meldet keinen Absatz
außerhalb von acht Sätzen, die Kapiteleinleitung eingeschlossen.

| Abschnitt | Absätze | Stand |
|---|---|---|
| Einleitung | 1 zu 8 Sätzen | abgeschlossen |
| 5.1 Anforderungen und ihre Umsetzung im Produkt | 12 | abgeschlossen, A11 neu: Nachweis der Verfügbarkeit |
| 5.2 Modellierung und ihre Annahmen | 7 | abgeschlossen |
| 5.3 Wirtschaftlichkeit und Wirksamkeit | 6 | abgeschlossen |
| 5.4 Die Rolle der BESS im Engpassmanagement und am Markt | 5 | am 26.09.2026 neu: Kurzfristigkeit, Netzanschluss, Einbindung, Mehrfachnutzung, Märkte |
| 5.5 Umsetzung, systemweite Ausrollung und Forschungsbedarf | 6 | am 26.09.2026 von zehn auf sechs: Rechtsrahmen, Marktrahmen, Betrieb, Ausrollung, Übergangslösungen, Forschungsbedarf |

**Wo alles steht.** Fünf Protokolleinträge vom 26.09.2026 am Ende von
`## chapter_5.tex` tragen jede Entscheidung, jeden zurückgenommenen Wortlaut
und jede eigenständige Ableitung. `BEFUNDE_KAP5.md` ist das geschlossene
Register der Kontrollprüfung, B1 bis B35, nichts offen. Der ersetzte
Fließtext steht je Stelle als Kommentar mit Datum und Befund in
`chapters/chapter_5.tex`.

**Was am 26.09.2026 entschieden wurde und weiter bindet.**

- **Kapitel 5 trägt keine Zitate**, bis auf zwei: Weber und Mahgoub in 5.2,
  weil der Satz berichtet, was ein namentlich genannter Autor sagt, und
  Consentec in 5.4, weil die Quelle sonst aus dem Verzeichnis fiele. Alles
  andere ist in den Kapiteln 1 bis 4 belegt, je Schlüssel geprüft.
- **Kapitel 5 nennt fast keine Zahlen.** Verblieben sind die drei
  Reaktionszeitklassen mit ihren Werten in 5.1 A1, *fünf Minuten vor
  Lieferbeginn* in 5.4 A1, § 17 Abs. 2b in 5.1 A6, die halbe gegen die
  viertel Megawattstunde je Megawatt in 5.3 A5, *um ein Sechstel* in 5.4 A5
  und § 13a in 5.5 A1. Der Kopfkommentar der Kapiteldatei führt die Liste.
- **Begriffe.** *Vergütung der vorgehaltenen Leistung* gegen *Vergütung der
  bewegten Arbeit* ist das geführte Paar; *kapazitätsbasiert* und
  *arbeitsbasiert* kommen in der Arbeit nicht vor. *Verfügbarkeit* für den
  Nachweis zum Zeitpunkt der Einplanung, *Lieferfähigkeit* für den
  Fehlerfall. *Abrufdauer* bleibt in Kapitel 4 als Name der Zeitdauer
  zulässig, *vorgehaltene Energie je Abruf* ist die Größe. *Gebot* bleibt dem
  Marktgebot vorbehalten. *FCA* kommt nicht vor, der Begriff ist die
  *flexible Netzanschlussvereinbarung*. *Rahmenvorgabe* ist nicht definiert
  und steht als *Vorgabe für den Betrieb*.
- **Die Marken *bestätigt am 26.09.2026* im Quelltext heißen: der
  Verfasser hat die Aussage diktiert.** Gerechnet ist keine davon. Die drei
  Aussagen zum Anschlussverfahren in 5.4 A2 stehen abgeschwächt, weil die
  BNetzA-FAQ zum Netzanschluss von Stromspeichern sich nicht in Text wandeln
  lässt.
- **Nicht gesetzt**, weil unbelegt oder mit Kapitel 1 im Widerspruch: dass
  das N-1-Kriterium selbst die Signalwege erfasse, und dass der Netzausbau
  die Begrenzung perspektivisch aufhebe. Der Text sagt *Sicherheitsbetrachtung*
  und *der Ausbau verändert den Charakter der Begrenzung*.

**Kapitel 4 ist am 26.09.2026 auf roten Faden und grobe Schnitzer geprüft**,
siehe die beiden Einträge unter `## chapter_4.tex` im Protokoll. Vier Befunde
mit Gewicht und neun Kleinigkeiten sind behoben, nichts ist offen; die
Absätze von Kapitel 4 liegen alle innerhalb von vier bis acht Sätzen.

**Zwei Zeilen außerhalb von Kapitel 5**, beide am 26.09.2026:
`chapters/chapter_4.tex` Zeile 863 sagt jetzt *fast das ganze Jahr über*, weil
Zeile 844 362 von 365 Tagen ausweist; `chapters/chapter_2.tex` Zeile 1295
trägt den Beleg für § 13c EnWG.

**Was als Nächstes ansteht.**

1. Der Verfasser liest Kapitel 5 am Stück und kommentiert. Claude prüft jedes
   Zitat gegen die Datei, legt Befund, Wortlaut und Empfehlung vor und setzt
   erst auf sein Wort.
2. Kapitel 6 ist zu schreiben. `AUSBLICK.md` sammelt, was der Verfasser für
   6.2 bestimmt hat; Abschnitt 7 unten nennt die Reste aus den Vormerkungen
   für Kapitel 5, die nicht verwendet wurden.
3. Ein Strukturdurchgang durch die Kapitel 1 bis 4 ist angeboten und nicht
   beauftragt: Ankündigung gegen Absatzfolge, Absatzeröffnungen gegen
   Stilregel 3. Für Kapitel 5 hat er zwei Befunde ergeben, B32 und B33.

**Die Abschnitte 1.1 bis 1.5 der Fassung vom 25.09.2026** zum Stand von
Kapitel 4 sind in `archiv/HANDOFF_2026-09-25.md` nachzulesen. Kapitel 4 ist
seit dem 24.09.2026 vollständig kontrollgelesen.

---

## 2 Dateiübersicht

Am 22.09.2026 aufgeräumt, weil das Wurzelverzeichnis unübersichtlich wurde.
**Im Wurzelverzeichnis liegen nur noch Dateien, die gelten.**

> **Aus der Kontrolllesung vom 24.09.2026, fuer jede weitere Sitzung.**
> Die eingebundene Abbildung `sensi_zukunft_erloes_2025.pdf` war dreizehn
> Minuten aelter als die des Lieferordners und trug eine ueberholte
> Variante, und der Text trug deren Zahlen. **Vor jeder Durchsicht sind
> die Abbildungen gegen `analysen/12_schrift/kapitel_4/` des
> Analyse-Repositorys zu pruefen**, naemlich mit `md5sum`, und bei
> Abweichung ist zuerst zu klaeren, welche Fassung die neuere ist. Eine
> Ausnahme ist `erloesvergleich_vollverdraengung_2025.pdf`: dort ist die
> Fassung der Schriftfassung die richtige, weil sie den gesperrten
> Begriff *Schwellenpreise* durch *Preisvektor der 1. Iteration* ersetzt.

### Wurzelverzeichnis, acht Dateien

| Datei | Rolle |
|---|---|
| `CLAUDE.md` | Auftrag, Stilregeln, Begriffe, Prüfungen. Claude ändert sie nicht, der Verfasser zieht selbst nach. |
| `HANDOFF.md` | diese Datei, Einstiegspunkt jeder Sitzung |
| `WORKFLOW.md` | Vorgehen: Absatzplan (3), Kommentardurchgang (7), Arbeitsweise am Absatz (10) |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen, nie ganz lesen |
| `BEFUNDE_KAP5.md` | **Geschlossenes Register der Kontrollprüfung von Kapitel 5**, B1 bis B35, angelegt und geschlossen am 26.09.2026. Nachweis, keine Arbeitsliste. |
| `README.md` | Beschreibung des Repositorys |
| `AUSBLICK.md` | **Sammeldatei für den Ausblick, angelegt am 25.09.2026.** Alles, was der Verfasser für Abschnitt 6.2 bestimmt, wird hier unmittelbar eingetragen, mit Herkunft, zurückgenommenem Wortlaut und Begründung. |
| `AUFTRAG_KAPITEL_5.md` | Lesekarte für Kapitel 5. **Am 26.09.2026 erledigt**, Kapitel 5 ist geschrieben; kann nach `archiv/`. Die Fundstellen bleiben für Kapitel 6 brauchbar. |
| ~~`AUFTRAG_REFERENZAUFTEILUNG.md`~~ | **Am 24.09.2026 erledigt und nach `archiv/` verschoben.** Die Lieferung beantwortet ihn in ERGEBNISSE Abschnitt 7.14, und Abschnitt 4.6.4 steht jetzt auf dieser Aufteilung. |

### `archiv/`, dreiundzwanzig Dateien, nur zum Nachschlagen

| Datei | war | abgelöst durch |
|---|---|---|
| `ANFRAGE_AFRR_HERBST_2025.md` | Anfrage vom 23.09.2026 zum aFRR-Leistungspreis | am 24.09.2026 selbst beantwortet |
| `ANTWORT_AFRR_HERBST_2025.md` | die Antwort vom 24.09.2026, Auswertung in `analysen/afrr_herbst_2025/` | **trägt die beiden fertigen Bibliographieeinträge**, siehe Abschnitt 6 |
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
| `AUFTRAG_FUELLGRAD_TAGESSTUNDEN.md` | Auftrag zum Füllgrad vom 23.09. | vollständig erledigt, alle Rückfragen beantwortet |
| `AUFTRAG_REDISPATCH_ZEITMUSTER.md` | Auftrag zum Zeitmuster des Redispatch vom 23.09. | geliefert, **Anhang H** trägt die Abbildung |
| `AUFTRAG_MAXIMASTUNDEN.md` | Auftrag zur Herkunft der Maxima vom 23.09. | erledigt, Befund in 4.3 eingearbeitet, gehandelte Energie geliefert |
| `UEBERGABE_KAP5_PRUEFUNG.md` | Prompt der Kontrollprüfung von Kapitel 5 vom 26.09. | vollständig abgearbeitet, Register in `BEFUNDE_KAP5.md` |
| `HANDOFF_2026-09-25.md` | diese Datei in der Fassung vom 25.09. | mit Abschnitten 1.1 bis 1.5 zu Kapitel 4 und 7, 7a zu Kapitel 5 |

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

`tools/absatzlaengen.py` zählt seit dem 26.09.2026 die Sätze je Absatz
und ist Teil der Prüfungen, `--nur-kurze` zeigt allein die Absätze außerhalb
von acht Sätzen. `tools/pruefen.py` prüft die Absatzlänge nicht.

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
- **Auffällige Perioden werden begründet, nicht nur beschrieben**, Vorgabe
  des Verfassers vom 23.09.2026. Die Ursache ist aus den Daten zu belegen,
  damit Kapitel 5 sie deuten kann. Was die Daten nicht hergeben, wird als
  offen benannt und nicht vermutet.
- **Eine Bildunterschrift hat zwei gesetzte Zeilen**, drei sind die oberste
  Grenze. Vorgabe des Verfassers vom 23.09.2026, an diesem Tag für alle 34
  Unterschriften der Arbeit umgesetzt. Gemessen wird am gebauten PDF über
  `pdftotext -layout`, denn `\cite`, `\ac` und `\si` setzen kürzer, als sie
  im Quelltext stehen. Was die Unterschrift nicht mehr trägt, gehört in den
  Fließtext. Bei neuen Abbildungen mitführen.
- **Kein Satz nach dem Muster „zeigt A und nicht B“**, Vorgabe des Verfassers
  vom 23.09.2026. Statt der Verneinung wird die Aussage positiv gewendet,
  etwa „Aus den fünf Tagen folgt die Reihenfolge der Verdrängung, aus dem
  Jahreslauf das Gewicht der einzelnen Märkte.“ **Erledigt am 24.09.2026.**
  Im Durchgang durch 4.6 sind die letzten drei Stellen positiv gewendet,
  in 4.4 und 4.5 stand keine mehr.
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

**Zwei Mängel an gelieferten Abbildungen**, vom Verfasser am 23.09.2026
unmittelbar im Analyse-Repository gemeldet. **Keinen eigenen Auftrag dazu
schreiben**, sonst entsteht doppelte Arbeit.

- **Der Erlösvergleich trägt das gestrichene Wort.**
  `erloesvergleich_vollverdraengung_2025.pdf` beschriftet die Balken mit
  *Preisvektor der 1.* und *der 2. Iteration*. Die Abbildung liegt mit
  dieser Beschriftung im Repository und **ist vor der Abgabe zu ersetzen**.
  Ihre Aufteilung nach Märkten ist dagegen ein Gewinn und soll bleiben.
- **Die Referenzaufteilung der Zukunftsvariante fehlt als Zahl.** Die
  Abbildung `sensi_zukunft_erloes_2025.pdf` zeigt sie in beiden
  Referenzbalken, `ERGEBNISSE…md` Abschnitt 7.13 führt sie nicht. Bis dahin
  steht sie nicht in 4.6.4, denn keine Zahl wird aus einer Abbildung
  abgelesen.

**Eine Entscheidung, die der Verfasser treffen muss**

- **Heißt die Größe in 4.6.2 *Abrufdauer* oder *Vorhaltdauer*?** Der
  Verfasser hat am 23.09.2026 die Vorhaltdauer in der Aufzählung des
  Abschnitts 4.6 vermisst. **Eine eigene Vorhaltdauer-Sensitivität gibt es
  nicht**: die Konfiguration `sensi6_vorhaltedauer` mit `kur_t_res` in
  {0,25; 0,5; 1,0} **ist** der Abschnitt 4.6.2. Das Analyse-Repository hat
  den Namen selbst festgelegt, in `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md`
  Zeile 419: „Die Größe heißt in der Schriftfassung **Abrufdauer** — nicht
  Vorhaltedauer, nicht Bindungsdauer." Der Code nennt sie Vorhaltedauer, die
  Arbeit nennt sie Abrufdauer. In der Einleitung steht deshalb seit dem
  23.09. die Abgrenzung, dass die **Bindungsdauer** in allen Varianten eine
  Stunde bleibt. **Soll die Größe doch Vorhaltdauer heißen, ist das eine
  Umbenennung in 4.6.2, in der Bildunterschrift und in der Abbildung
  selbst** — und ein Auftrag an das Analyse-Repository, denn die
  Achsenbeschriftung steckt im PDF.
  **Entschieden am 26.09.2026, Befund B28:** die Größe heißt weiter
  *Abrufdauer*, denn *vorgehaltene Energie je Abruf* ist die Größe und die
  Abrufdauer ihre Ursache; Kapitel 4 trennt beides. Keine Umbenennung.

**Eine Vorkehrung, die mitzuführen ist**

- **Die Dateiliste in `tools/pruefen.py` ist fest verdrahtet.** Ein neuer
  Anhang wird sonst nicht geprüft, und Marken darin gelten als nicht
  auflösbar. Am 23.09.2026 um `attachment_redispatch.tex` ergänzt, die Suite
  prüft jetzt 15 Dateien. Bei jedem weiteren Anhang nachziehen.

**Für den Durchgang durch 4.5 vorgemerkt**, Stand 23.09.2026

- **Die Aussage zur Tageszeit gegen die Jahreszeit** ist aus den
  Schlussfolgerungen von 4.4 herausgenommen und gehört nach 4.5. Der Median
  der Summe schwankt über den Tag um den Faktor 8,3 und über die Monate nur
  um 4,2. Beide Zahlen stehen in 4.4, die Wertung nicht.
- **Das Tagesmuster des Redispatch ist gerechnet**, aus den 19\,369
  Einzelmaßnahmen des Jahres 2025 in
  `data/processed/Redispatch_netztransparnez.net`. Auswertung in
  `analysen/redispatch_tagesmuster`. Die Zahlen für 4.5:

  | Größe | Wert |
  |---|---|
  | Redispatch reduzieren | 1701 MW um 12 Uhr gegen 793 MW um 0 Uhr, Faktor 2,14 |
  | Redispatch erhöhen | 1788 MW um 10 Uhr gegen 1236 MW um 0 Uhr, Faktor 1,45 |
  | Redispatch gesamt | 3440 MW um 11 Uhr gegen 2029 MW um 0 Uhr, Faktor 1,70 |
  | Reservierungspreis über den Tag | Faktor 8,28 |
  | Winter Nov bis Feb | 4016 MW bei 21,2\,€/(MW·h) |
  | Sommer Mai bis Aug | 1783 MW bei 39,8\,€/(MW·h) |
  | Rangkorrelation über die Monate | $-0{,}48$ |
  | Rangkorrelation reduzieren gegen Ladereservierung, über den Tag | $+0{,}59$ |
  | Anteil des Reduzierungsbedarfs in den sechs teuersten Ladestunden | 33 gegen 25 Prozent |
  | Anteil des Erhöhungsbedarfs in den sechs teuersten Entladestunden | 26 gegen 25 Prozent |

  **Der tragende Befund:** über den Tag schwankt der Bedarf um 1,70 und der
  Preis um 8,28, die Tageszeit ist für den Bedarf also zweitrangig. Die
  Mittagsspitze fällt jedoch zusammen, denn der Reduzierungsbedarf hat sein
  Maximum um 12 Uhr und die Ladereservierung ist von 10 bis 15 Uhr am
  teuersten. In der Entladerichtung trifft der teure Abend dagegen keinen
  erhöhten Bedarf. Über das Jahr laufen beide gegenläufig.
- ~~Abzugrenzen ist, warum 4.5 kein Tagesmuster des Redispatch zeigt.~~
  **Mit den obigen Zahlen begründbar.** Frueherer Vermerk:
  Vorgabe des Verfassers vom 23.09.2026: das Tagesmuster soll dort nicht
  betrachtet werden, die Saisonalität schon. **Nicht zu behaupten ist, der
  Redispatch sei von der Tageszeit unabhängig** — dafür gibt es keinen
  Beleg, und die Windeinspeisung in der Nacht spricht eher dagegen.
  Tragfähig ist die Datenlage: die Redispatchleistung liegt in der
  zitierten Mitteilung der Bundesnetzagentur als Tageswert vor, sodass der
  Vergleich auf der Jahreszeit stattfindet. Ob SMARD den Redispatch
  stundenscharf veröffentlicht, ist als dritte Frage in
  `archiv/ANFRAGE_AFRR_HERBST_2025.md` gestellt.

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
  auszuweisen. ~~Angefordert.~~ **Geliefert am 23.09.2026** nach Weg 1, also
  in getrennten Blöcken für gehandelte Arbeit und vorgehaltene Leistung, für
  alle fünf Tage und zehn Preisstufen, in `ERGEBNISSE…md` Abschnitt 2.4.
  **Noch nicht in den Text übernommen.** Die Energie zeigt zweierlei, das die
  Leistungsmittel verdecken: die kurative Vorhaltung bindet das Band überall
  nahezu vollständig, auch am 15.05., wo die Leistung nur 89 Prozent
  ausweist; und die gehandelte Arbeit fällt sehr ungleich, an drei Tagen auf
  null bis 2 Prozent, am 26.08. nur auf 46 Prozent. **Zu entscheiden:** ob
  4.1 und Anhang F auf Energie umgestellt werden oder ob die Energie neben
  den MW-Werten tritt. Beide Stellen sind bereits durchgegangen, eine
  Umstellung rührt sie erneut an.
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
- ~~Woher die Maxima kommen.~~ **Geliefert und eingearbeitet am 23.09.2026**,
  ohne neuen Lauf, aus `jahr_slots_2025.parquet`. Zahlen in `ERGEBNISSE…md`
  Abschnitt 7.11, Text als eigener Absatz in 4.3. Der Befund ist stärker als
  erwartet: **in der Spitze der Verteilung setzt nicht die \ac{aFRR} den
  Preis.** Entladend hält der \ac{IDC} 70,2\,MW gegen 4,9 im Jahresmittel,
  ladend tragen ein hoher \ac{aFRR}-Leistungspreis und negative Preise am
  \ac{IDC}.
- **Welcher Markt in den Maximastunden zuletzt weicht, bleibt offen.**
  Geliefert ist, welcher Markt die Leistung im Referenzfall **hält**. Die
  Frage nach dem Weichen verlangt ein Preisgitter je Stunde für die
  betroffenen Tage. Der Text sagt deshalb *hält* und nicht *weicht*.
- **Kopplung über das Ladezustandsband in der Laderichtung ist offen.**
  7 der 20 teuersten Ladestunden liegen um mehr als die Hälfte über der
  Opportunität der eigenen Stunde, bis zum Faktor 10,6. Der Text nennt das
  als *mit einer Kopplung vereinbar*, nicht als belegt. Entscheiden ließe es
  sich mit einem Preisgitter je Stunde.
- **Die exakte Jahresverteilung der Läufe ist nicht bestellt.** Sie hätte
  eine Wiederholung des Jahreslaufs von rund zweieinhalb Stunden verlangt.
  Empfehlung an den Verfasser: dabei bleiben, denn der Rechenaufwand ist
  eine Angabe zum Verfahren und kein Ergebnis der Arbeit.
- **Markterlös der offenen Stunden nicht verfügbar.** Der Anteil der
  offenen Tagesstunden an den 88,6\,Tsd.\,€/(MW·a) lässt sich aus dem
  vorhandenen Lauf nicht ziehen, weil die Erlösdatei je Tag und nicht je
  Stunde geführt ist. Dafür müsste der Iterationsvergleich neu laufen.
- ~~4.6.3 und 4.6.4 sind leer.~~ **Am 23.09.2026 geschrieben**, `sensi8` ist
  geliefert. Frueher stand hier, sie warteten auf `sensi8_spanne_und_niveau` aus
  dem Analyse-Repository. Nicht mit den Einzeltagsfassungen füllen.
- **Für 4.6.4 vorgemerkt (G3), Entscheidung des Verfassers vom 22.09.2026:**
  Die niedrigeren \ac{aFRR}-Preise der Zukunftsvariante lassen sich damit
  begründen, dass der Bestand an \ac{BESS} wächst, während der Bedarf an
  Regelleistung aus der Dimensionierung des Systems folgt und nicht mitwächst.
  Hilfsweise gehört das Argument in die Diskussion.
- ~~**4.7 Diskussion ist leer** und folgt nach den beiden Sensitivitäten.~~
  Überholt: die Diskussion ist Kapitel 5, abgeschlossen am 26.09.2026.
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

- ~~Die Antwort des SMARD-Chats steht aus.~~ **Erledigt am 24.09.2026**, die
  Schriftfassung hat die Anfrage selbst beantwortet, siehe
  `archiv/ANTWORT_AFRR_HERBST_2025.md`. Vier Ergebnisse binden den Text:
    - **Der Abgleich der Eingangsdaten ist bestanden.** Die Monatswerte der
      Spalte `GERMANY_AVERAGE_CAPACITY_PRICE` sind aus der Quelldatei
      reproduziert, die einzige Abweichung ist der März mit 12,1 statt 12,2
      und folgt aus der Mittelung über Zeitscheiben statt Viertelstunden.
    - **Die Verdopplung im September und Oktober ist ein Angebotsereignis.**
      Das Angebot fällt auf sein Jahresminimum von 3849 gegen 4337 Megawatt,
      die beschaffte Menge bleibt bei rund 2000 Megawatt, und der Preis folgt
      2025 der Angebotsmenge mit −0,61 statt dem Energiepreis mit +0,18.
      Revisionen und Schwachwind sind verworfen. **Offen bleibt die Hälfte
      der Verdopplung**, nämlich das höhere Gebotsniveau bei gleicher Menge;
      das ist im Text als offen zu kennzeichnen.
    - **Die Nebenfrage ist belegt.** Ganz und Kern 2025 von der FfE tragen den
      Zusammenhang zwischen PV-Einspeisung, verringerter Verfügbarkeit
      thermischer Kraftwerke und dem Preis negativer Sekundärreserve in den
      Mittagsstunden. Die eigenen Daten stützen ihn, denn der Anstieg liegt
      vollständig in den Scheiben 08 bis 12 und 12 bis 16 Uhr. Der
      Bibliographieeintrag steht in `archiv/ANTWORT_AFRR_HERBST_2025.md` Abschnitt 6
      und ist erst mit dem zugehörigen Satz einzutragen.
    - Der Julieinbruch bleibt ohne Beleg und damit unerwähnt.
    - **Offen und noch einzubauen:** Abschnitt 4.4 beschreibt den Mittagsgipfel des \ac{aFRR}-Leistungspreises in der Laderichtung mit 82,2 Euro je Megawatt und Stunde im Mai, nennt aber keine Ursache. Die stehende Vorgabe des Verfassers vom 23.09.2026 lautet, auffällige Perioden zu begründen. Ganz und Kern 2025 tragen die Begründung über die PV-Einspeisung, der Eintrag `ffe_regelreserve_2025` steht fertig in `archiv/ANTWORT_AFRR_HERBST_2025.md` Abschnitt 6. **Ein Satz in 4.4 und ein Eintrag in `literature.bib` fehlen noch.**

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
## 7 Reste aus den Vormerkungen für Kapitel 5

Die Vormerkungen vom 22. bis 24.09.2026 sind beim Schreiben von Kapitel 5
überwiegend verbraucht; die vollständige Liste steht in
`archiv/HANDOFF_2026-09-25.md` Abschnitt 7. Nicht verwendet und für Kapitel 6
oder `AUSBLICK.md` zu prüfen:

- Anlage 1 der Festlegung, Seite 13: die PSKW-Vorgaben sind auf
  Batteriespeicher „auch ohne weitere Anpassungen" anwendbar.
- Der Auftraggeber des Weber-Gutachtens ist in den Quellen widersprüchlich,
  EnBW gegen BDEW; die Literaturdatei folgt dem Deckblatt.
- Der Consentec-Befund zu KuPilot.
- **Aus 4.4:** die beiden Tage mit der steilsten Staffel der
  Arbitragespannen, der 26.08.2025 mit 10 und der 15.05.2025 mit 11 Prozent,
  sind die beiden Tage, an denen die Verdrängung nach Abschnitt 4.1 auch bei
  200 Euro je Megawatt und Stunde unvollständig bleibt. Der Zusammenhang
  erklärt einen Befund aus 4.1 und steht in keinem Kapitel.
- **Aus 4.3:** die teuersten Stunden sind schwer zu prognostizieren, und die
  Wahrscheinlichkeit, dass sie eintreten, schlägt sich im Preis nieder.
  Teilweise verbraucht: der Forschungsbedarf nennt das Gebot unter
  Unsicherheit über die Handelsspannen.

**Verworfen und nicht wieder aufzunehmen:** der *kapazitätsbasierte
Redispatch* als Anschlusspunkt, Entscheidung des Verfassers vom 25.09.2026,
weil der Begriff in keinem Kapitel definiert ist und im Kern die kurative
Systemführung selbst wäre.

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

Eigene Auswertungen der Schriftfassung: `analysen/redispatch_tagesmuster`
mit dem Tagesmuster des Redispatch aus den Einzelmaßnahmen,
`analysen/zeitmuster_ursachen` mit
sieben Skripten und einer eigenen `README.md`, die sagt, welches Skript
welche Frage beantwortet und welcher Befund überholt ist,
`analysen/mastr_speicher`,
`analysen/mfrr_leistungspreise`, `analysen/vollreservierung_pruefung`,
`analysen/redispatch_einheiten`. Der Quelltext des Erlösindex der ISEA Battery
Charts liegt lokal unter `C:/GIT-HUB/battery_revenue_index-main`.
