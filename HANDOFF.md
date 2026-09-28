# Übergabe an die nächste Sitzung, Stand 27.09.2026

Diese Datei ersetzt die Fassung vom 26.09.2026 vollständig. Die alte Fassung
liegt unter `archiv/HANDOFF_2026-09-26.md`, ältere in der Git-Historie.

> **Das Arbeitsverzeichnis ist sauber, `origin/main` steht auf `57992d2`.**
> Gepusht wird nur auf ausdrückliche Anweisung, committet nur auf das Wort
> „commite".
>
> **Die Arbeit ist inhaltlich vollständig.** Kapitel 1 bis 6, Kurzfassung und
> Abstract, acht Anhänge, Literaturverzeichnis bereinigt. Was noch ansteht,
> steht in Abschnitt 5.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3, 7 und 10. `ENTSCHEIDUNGSPROTOKOLL.md` hat über
17 000 Zeilen und wird nie ganz gelesen, sondern nur angehängt und gezielt
durchsucht.

**Zwei Sitzungen arbeiten zeitweise parallel** an diesem Repository, eine an
den Betreuerkommentaren zu Kapitel 1 bis 3, eine an Kapitel 5 und 6. Vor
jeder Änderung `git status` lesen. Dateien mit fremden ungestageten
Änderungen werden nicht angefasst, auch das Protokoll nicht; der eigene
Eintrag wartet dann, bis die andere Sitzung committet hat (so geschehen am
27.09.2026 bei `c482ffb`).

**Die Warnung vom 26.09.2026 gilt weiter.** Der Verfasser zitiert beim
Kommentieren aus dem PDF. Ist das PDF älter als die Datei, zitiert er
zurückgenommene Sätze. Vor jedem Kommentardurchgang neu bauen, und jedes
Zitat gegen die Kapiteldatei prüfen, bevor es beantwortet wird.

---

## 1 Stand des Dokuments

**130 Seiten**, Build ohne Fehler und Warnung, Biber ohne Warnung,
`python tools/pruefen.py --alle` ohne Befund in 15 Dateien,
`tools/pruefe_stil.py` ohne Verstoß in Kapitel 4 bis 6, in Kapitel 1 bis 3
allein die Altbefunde zum Doppelpunkt.

| Teil | Seiten | Stand |
|---|---|---|
| Kurzfassung, Abstract | iii, iv | je genau eine Seite, 26.09.2026 |
| 1 Einleitung | 1 bis 6 | Betreuerkommentare eingearbeitet, 27.09.2026 (`c482ffb`) |
| 2 Grundlagen | 7 bis 30 | steht |
| 3 Marktmechanismus und Modellierung | 31 bis 49 | Betreuerkommentare eingearbeitet, 27.09.2026; *Lokationalität* heißt jetzt *Standortabhängigkeit* |
| 4 Ergebnisse | 50 bis 65 | am 26.09.2026 auf roten Faden geprüft |
| 5 Diskussion | 66 bis 77 | am 27.09.2026 vom Verfasser am Stück gelesen, alle Vorgaben gesetzt |
| 6 Zusammenfassung und Ausblick | 78 bis 81 | ein Kapitel ohne Unterabschnitte, Ausblick als ein Absatz mit Szenarien |
| Literaturverzeichnis | 82 bis 88 | am 27.09.2026 vereinheitlicht |
| Anhänge A bis H | 93 bis 121 | stehen |

**Der Hauptteil hat 81 Seiten, Ziel sind 80.** Vor `c482ffb` waren es 80;
die zwölf eingearbeiteten Betreuerkommentare haben eine Seite gekostet.
Kandidaten zum Kürzen: Kapitel 6 (K3 hat zwei Absätze) oder die längeren
Absätze in 5.2 (19 und 13 Sätze).

**Kapitel 5 nach dem Durchgang vom 27.09.2026.** Einleitung, 5.1 mit neun
Absätzen (A1 Reaktionszeit, A2 Vergütung mit Abrufvergütung und
Nachlaufpflicht, A3 Diskriminierungsfreiheit und Standortabhängigkeit, A4
Teilnahme, A5 Wirksamkeit am Engpass, A6 Zuschlag und Aufschläge, A7
Verträglichkeit, A8 Verbindlichkeit mit Pönale und Nachweis, A9
Zwischenfazit), 5.2 (Einleitung, Preissuche, vollständige Preiskenntnis,
Regelleistung mit FCR, aFRR-Leistung und aFRR-Arbeit in einem Absatz, IDC,
Perspektive), 5.3 (Vergleichspreis, Wettbewerbsfähigkeit, Wind und
Photovoltaik, Jahresverlauf, Zuschnitt und Aufwand), 5.4 (fünf Absätze), 5.5
(Rahmen, Markt, Übergangslösungen, Betrieb, Forschungsbedarf, Ausrollung als
Schluss). Die Protokolleinträge vom 27.09.2026 unter `## chapter_5.tex`
tragen jede Vorgabe und jeden zurückgenommenen Wortlaut.

**Kapitel 6.** Einleitung, fünf Erkenntnisse mit wechselnden Einstiegen
(zuerst, zweitens, drittens, viertens, schließlich), die dritte in zwei
Absätzen, dann der Ausblick als ein Absatz mit 22 Sätzen: Netzausbau bleibt
zurück, Netzausbau holt auf, Nachfrage steigt, Markt bildet Kapazität ab,
Sättigung der Regelleistung, Anschlussregeln, dann die drei
szenariounabhängigen Voraussetzungen. Der Grenzen-Absatz ist gestrichen, ein
Satz daraus hängt an der dritten Erkenntnis.

---

## 2 Entscheidungen vom 27.09.2026, die weiter binden

- **Die Grenze von acht Sätzen je Absatz ist aufgehoben.** Die Absatzlänge
  folgt der Kernaussage, `tools/absatzlaengen.py` gibt nur noch Auskunft, und
  beim Zusammenlegen wird kein Inhalt halbiert. `CLAUDE.md` Stilregel 1
  nennt noch vier bis acht Sätze; der Verfasser zieht selbst nach.
- **Kapitel 5 trägt zwei Zitate**: Consentec in 5.4 und Burger (Fraunhofer
  ISE) in 5.3; Weber und Mahgoub in 5.2 sind gestrichen.
- **Präventiver Vergleichspreis** ist der Name des mittleren Arbeitspreises
  des präventiven Redispatch, eingeführt am Ende des ersten Absatzes von 5.3.
  Kapitel 4 nennt weiter den *Arbeitspreis des präventiven Redispatch von
  101 Euro je bewegter Megawattstunde*, der Einführungssatz verbindet beides.
- **Standortabhängigkeit** statt Lokationalität, Betreuerkommentar 5,
  umgesetzt in Kapitel 3, 5 und 6 (`c482ffb`).
- **Windstromerzeugung im Winter** steht in 1.1 mit Zahlen (November bis
  Februar 52,9 TWh, Mai bis August 34,8 TWh, Burger 2026, Folie 54) und in
  5.3 als Verhältnis. Eine eigene Auswertung der Energy-Charts-API hatte
  dieselben Werte geliefert und ist auf Vorgabe wieder entfernt.
- **Nachlaufpflicht** ist in 5.1 A2 erklärt und nicht im Betriebsabsatz von
  5.5: sie hält ein BESS nach dem Abruf von der verschärfenden Richtung ab und
  lässt sich in der Reservierung am Vortag berücksichtigen.
- **Der Redispatch lässt sich um eine Komponente für die vorgehaltene
  Leistung erweitern**, die harte Fassung (*ausgeschlossen, in das
  Duldungsregime einzufügen*) ist zurückgenommen. Der Schlusssatz von 5.5 A1
  sagt weiter *neben dem Ausgleich nach § 13a*.
- **Die betrieblichen Voraussetzungen sind komplex, werden in InnoSys 2030
  und KuPilot aber erarbeitet**; mein Vorschlag, sie wögen schwerer als der
  Rahmen, ist zurückgenommen.
- **Die zusätzlich anschließbare Speicherleistung ist keine offene Frage**
  der kurativen Systemführung, gestrichen aus Forschungsbedarf und
  Übergangsabsatz; der positive Satz zum Nutzen bleibt.
- **Forschungsbedarf** in 5.5 nach Markt, Preis, Betrieb, System geordnet;
  die systemweite Aussage verlangt eine **Modellkette** aus Marktsimulation
  mit Reservierung, Lastflussrechnung und Redispatchplanung an einem
  Datensatz der Netzentwicklungsplanung, keine Netzsicherheitsrechnung.
- **Literaturverzeichnis.** Jede URL trägt ein Abrufdatum, lange Dateilinks
  sind durch die Seiten der Herausgeber ersetzt, Zotero-Dateipfade sind
  entfernt, und die dehnbaren URL-Abstände von biblatex stehen in
  `extras/header.tex` auf null. Neue Einträge nach diesem Muster anlegen.
- Die Entscheidungen vom 26.09.2026 gelten unverändert: das Begriffspaar
  *Vergütung der vorgehaltenen Leistung* gegen *Vergütung der bewegten
  Arbeit*; *Verfügbarkeit* für den Nachweis bei der Einplanung,
  *Lieferfähigkeit* für den Fehlerfall; *Gebot* nur für das Marktgebot;
  *flexible Netzanschlussvereinbarung* statt FCA; *Vorgabe für den Betrieb*
  statt Rahmenvorgabe; *Bemessungsgegenstand* nicht im Fließtext von
  Kapitel 5; die Marken *bestätigt am 26.09.2026* heißen, dass der Verfasser
  die Aussage diktiert hat.
- Die älteren Entscheidungen stehen in `archiv/HANDOFF_2026-09-26.md`
  Abschnitt 3 und gelten weiter (Betreiber gegen EIV, Dispatch-Modelle,
  Indifferenzprinzip, Abrufdauer, Bezugslinie 101 Euro, Bildunterschriften
  mit zwei Zeilen, keine Abschnitte mit Bild am Anfang, Schlussfolgerungen
  je Abschnitt in Kapitel 4, `\TsdEurMWa`).

---

## 3 Dateiübersicht

**Im Wurzelverzeichnis liegen nur Dateien, die gelten.** Am 27.09.2026 sind
`AUFTRAG_KAPITEL_5.md`, `AUSBLICK.md` und `BEFUNDE_KAP5.md` nach `archiv/`
verschoben, alle drei erledigt.

| Datei | Rolle |
|---|---|
| `CLAUDE.md` | Auftrag, Stilregeln, Begriffe, Prüfungen. Claude ändert sie nicht, der Verfasser zieht selbst nach. |
| `HANDOFF.md` | diese Datei, Einstiegspunkt jeder Sitzung |
| `WORKFLOW.md` | Vorgehen: Absatzplan (3), Kommentardurchgang (7), Arbeitsweise am Absatz (10) |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen, nie ganz lesen; CRLF |
| `README.md` | Beschreibung der LaTeX-Vorlage |

`archiv/` trägt die erledigten Arbeitsdokumente, darunter seit dem
27.09.2026 `BEFUNDE_KAP5.md` (geschlossenes Register B1 bis B35),
`AUSBLICK.md` (Sammeldatei für den Ausblick, mit Abschlussvermerk),
`AUFTRAG_KAPITEL_5.md` (Lesekarte für Kapitel 5) und
`HANDOFF_2026-09-26.md`. Die Zuordnung der älteren Dateien steht in
`archiv/HANDOFF_2026-09-26.md` Abschnitt 2.

Eigene Auswertungen liegen in `analysen/` (mastr_speicher,
redispatch_tagesmuster, zeitmuster_ursachen, afrr_herbst_2025,
mfrr_leistungspreise, vollreservierung_pruefung, redispatch_einheiten,
afrr_abruf). Das Modellrepository `C:/GIT-HUB/bess_dispatch_optimization`
ist für die Schriftfassung lesend; fertige Abbildungen liegen dort unter
`analysen/12_schrift/kapitel_N/`, vor dem Holen die Zeitstempel vergleichen.

---

## 4 Arbeitstechnik

- Änderungen an Kapiteldateien **über ein Python-Skript**, angelegt mit dem
  Write-Werkzeug (Bash-Heredocs verstümmeln Backslashes), gelesen und
  geschrieben mit `encoding="utf-8", newline=""`, Zeilenenden unverändert
  (Kapiteldateien und Protokoll CRLF, übrige Markdown-Dateien LF). Anker
  greifen genau einmal, nur auf Fließtextzeilen, ersetzter Text bleibt als
  Kommentar mit Datum und Grund über der neuen Fassung, Kommentare zwischen
  den Sätzen bleiben stehen. Beim Zusammenlegen von Absätzen genau eine
  Leerzeile entfernen.
- Nach jeder Änderung: `python tools/pruefen.py <datei>`,
  `python tools/pruefe_stil.py`, Build (`pdflatex; biber; pdflatex;
  pdflatex`), `main.log` auf `LaTeX Warning` und `^!`, `main.blg` auf
  `WARN`, Seitenzahl und Beginn des Literaturverzeichnisses aus `main.toc`,
  dann den ganzen geänderten Absatz im Chat zeigen.
- Protokolleinträge nur mit ASCII (Umlaute als ae, oe, ue), sonst schlägt
  die Konsole fehl; ein versehentliches kyrillisches е hat am 27.09.2026
  einen Lauf gekostet.
- Der Verfasser diktiert Vorgaben satzweise aus dem PDF; jede wird sofort
  gesetzt, geprüft, gebaut und gestaged, committet auf „commite". Eigener
  Vorschlag statt Rückfrage, im Protokoll als eigenständig gekennzeichnet,
  und beim ersten Widerspruch zurückgenommen.
- Subagenten nur nach Rückfrage. `pdftotext` liefert bei manchen PDFs nur
  Zeichensalat (Schriften ohne Unicode-Zuordnung), dann `pdftoppm -png` und
  das Read-Werkzeug; das Read-Werkzeug selbst lehnt einige PDFs als
  passwortgeschützt ab.

---

## 5 Offene Punkte

**Aus dem 27.09.2026**

1. **Kapitel 6 an Kapitel 5 angleichen.** Vier Stellen in den Erkenntnissen
   stehen noch gegen die Entscheidungen des Tages: K2 trägt den Satz zum
   einheitlichen Tagespreis, der in 5.3 als trivial gestrichen ist; K3
   (zweiter Absatz) sagt *Arbeitspreis* statt *präventiver Vergleichspreis*;
   K4 begründet die Nichteinbindung mit Werteverbrauch und Opportunität statt
   mit dem modifizierten Weber-Ansatz; K5 sagt, die Vergütung lasse sich
   *nicht in das Duldungsregime einfügen*. Der Verfasser hat die Liste, die
   Angleichung wartet auf sein Wort.
2. **Hauptteil auf 80 Seiten**, siehe Abschnitt 1.
3. **Titel von 5.5** lautet *Umsetzung, systemweite Ausrollung und
   Forschungsbedarf*, die Reihenfolge im Text ist Umsetzung, Forschungsbedarf,
   Ausrollung. Angleichung dem Verfasser gemeldet, nicht entschieden.
4. **`CLAUDE.md` zieht der Verfasser nach**: Stilregel 1 ohne die acht
   Sätze; Dateiliste (die drei verschobenen Dateien, `DURCHSICHT_KAP1_3.md`
   und `KOMMENTARE_KAP3.md` liegen in `archiv/`, Anhänge D bis H fehlen);
   Begriffe Standortabhängigkeit, präventiver Vergleichspreis, EIV,
   Dispatch-Modelle, Indifferenzprinzip, Abrufdauer; Entscheidung 3 zur
   Mindestgröße.
5. **Der Betreuerdurchgang zu Kapitel 1 bis 3 läuft in der anderen Sitzung**
   (`c482ffb`, zwölf Kommentare). Ob weitere Kommentare zu Kapitel 4 bis 6
   folgen, ist offen.

**Älter, weiter offen** (Einzelheiten in `archiv/HANDOFF_2026-09-26.md`
Abschnitt 6)

- 4.5: die Richtungsmengen 12,15 gegen 18,30 TWh stammen aus energy-charts
  ohne Eintrag; entweder Eintrag anlegen oder auf die Zahlen der
  Bundesnetzagentur umstellen.
- 4.4: der Mittagsgipfel des aFRR-Leistungspreises in der Laderichtung
  bleibt ohne Ursache; Ganz und Kern 2025 (Eintrag in
  `archiv/ANTWORT_AFRR_HERBST_2025.md` Abschnitt 6) tragen die Begründung
  über die PV-Einspeisung, Satz und Eintrag fehlen.
- Die Abbildung `erloesvergleich_vollverdraengung_2025.pdf` trägt das
  gestrichene Wort *Preisvektor* und ist vor der Abgabe zu ersetzen.
- G13: vor Abgabe prüfen, ob eine Mitteilung der Beschlusskammer zu
  Batteriespeichern ergangen ist.
- `chapters/chapter_3.tex`: zwei verwaiste Marken `sec:market_design_comparison`
  und `sec:product_design`.
- Zahlenprüfung für 3.3.2 gegen den aktuellen Lauf steht aus.
- Die Dateiliste in `tools/pruefen.py` ist fest verdrahtet; bei jedem
  weiteren Anhang nachziehen.
- Erledigt am 27.09.2026 und deshalb hier gestrichen: Sous 2022 ohne Tagung,
  FAQ Stromspeicher ohne URL, Preisreihen in Kapitel 3 zitieren energy-charts.
