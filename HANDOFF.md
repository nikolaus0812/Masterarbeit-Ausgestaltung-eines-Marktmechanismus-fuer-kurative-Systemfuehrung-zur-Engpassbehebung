# Übergabe an die nächste Sitzung, Stand 23.09.2026

Diese Datei ersetzt die Fassung vom 22.09.2026 nachts vollständig, fortgeschrieben
am 23.09.2026 abends. Die alten Fassungen stehen in der Git-Historie.

> **Das Arbeitsverzeichnis ist sauber.** Der letzte Commit ist `b1b26e1`
> vom 23.09.2026 spät abends. `origin/main` steht auf `1c51db2` und ist
> damit **drei Commits zurück** — gepusht wird nur auf ausdrückliche
> Anweisung, committet nur auf das Wort „commite".
>
> **Kapitel 5 ist am 24.09.2026 begonnen.** Die Stichpunkte aller acht Abschnitte stehen in `chapters/chapter_5.tex`, das Kapitel ist in `main.tex` eingebunden, und der Verfasser geht die Stichpunkte durch. Danach folgt die Ausformulierung Absatz fuer Absatz. Der urspruengliche Auftrag steht in
> **`AUFTRAG_KAPITEL_5.md`** und ist die Lesekarte für die Diskussion.
> Kapitel 4 ist am 24.09.2026 vollstaendig kontrollgelesen, siehe die
> Tabelle in Abschnitt 1.3.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitte 3, 7 und 10. `ENTSCHEIDUNGSPROTOKOLL.md` hat über
16 000 Zeilen und wird nie ganz gelesen, sondern nur angehängt und gezielt
durchsucht.

---

## 1 Stand des Dokuments

### 1.0 Stand vom 25.09.2026, Kapitel 5 im Durchgang

**121 Seiten**, Build sauber, `python tools/pruefen.py --alle` ohne
Befund, `tools/pruefe_stil.py` ohne Verstoss in Kapitel 5. `main.tex`
bindet Kapitel 5 seit dem 24.09.2026 ein.

**Absatzlaenge ist bindend.** Der Verfasser hat am 25.09.2026 zweimal
verlangt, die Absaetze laenger zu fassen. Abschnitt 5.1 und 5.2 stehen
jetzt durchgaengig bei acht Saetzen, der Obergrenze nach Stilregel 1.
Mehr Laenge ist nur ueber mehr Absaetze zu gewinnen, nicht ueber
laengere. Die Abschnitte 5.3 bis 5.5 liegen noch bei fuenf bis sieben
Saetzen je Absatz und sind im jeweiligen Durchgang nachzuziehen.
`tools/pruefen.py` prueft die Absatzlaenge nicht; das Skript zum
Auszaehlen liegt im Scratchpad der Sitzung und ist bei Bedarf neu zu
schreiben.

**Stand der Abschnitte.**

| Abschnitt | Absaetze | Stand |
|---|---|---|
| 5.1 Anforderungen und ihre Umsetzung im Produkt | 11 zu je 8 Saetzen | durchgegangen, Absaetze zusammengezogen |
| 5.2 Modellierung und ihre Annahmen | 8 zu je 8 Saetzen | durchgegangen |
| 5.3 Wirtschaftlichkeit und Wirksamkeit | 4 zu 6 Saetzen | offen |
| 5.4 Die Rolle der BESS im Engpassmanagement und am Markt | 4 zu 6 bis 7 Saetzen | offen |
| 5.5 Umsetzung, systemweite Ausrollung und Forschungsbedarf | 4 zu 6 bis 7 Saetzen | offen |

**Offen, dem Verfasser vorgelegt.**

- Drei Saetze sind beim Zusammenziehen der Absaetze gefallen und
  stehen dem Verfasser zur Rueckholung offen, naemlich die Bedingung der
  Rueckbeschaffung, die Sicherheit des Reservierungserloeses und der
  Schlusssatz zur Verbindlichkeit.
- Die Aussage, die kurative Vorhaltung sei von jeglichen Eingriffen
  ausgeschlossen, ist **nicht gesetzt**, weil sie in keinem Kapitel
  steht. Abschnitt 3.1.2 sagt allein, dass Fahrplanaenderungen die
  Vorhaltung nicht mehr aufheben. Soll die staerkere Aussage stehen,
  waere sie in Kapitel 3 festzulegen.
- Der Push des Commits `2fc1be7` vom 24.09.2026 steht beim Verfasser
  noch aus, GitHub hat mit einem Internal Server Error geantwortet.

**Begriff.** *FCA* kommt in der Arbeit nicht vor. Der gefuehrte Begriff
ist die *flexible Netzanschlussvereinbarung* nach Paragraf 17 Absatz 2b
EnWG aus Abschnitt 2.1, Beleg `bundesnetzagentur_faq_2025`.


Build sauber, Biber ohne Warnung, **111 Seiten**, Stand 23.09.2026 abends. `python tools/pruefen.py
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
| 4.4 Zeitliches Muster | Heatmap, Zeitmuster | geschrieben und durchgegangen |
| 4.5 Kurativer Reservierungspreis und Engpassbedarf | Jahreslauf Median und Mittel | geschrieben |
| 4.6 Sensitivitäten | | |
| 4.6.1 Modellierung der aFRR | aFRR Leistung, aFRR Energie | geschrieben |
| 4.6.2 Abrufdauer | Abrufdauer, 2. Iteration | geschrieben |
| 4.6.3 Handelsspanne am IDC | Faktor auf die Handelsspanne | geschrieben |
| 4.6.4 Zukünftig niedrigere Preise | Erlösvergleich beider Welten | geschrieben |

Seit dem 23.09.2026 steht kein Abschnitt mehr leer, und die Diskussion der
Ergebnisse ist als Abschnitt gestrichen, weil sie Kapitel 5 ist. Der frühere
Abschnitt *Zahlung bei vollständiger Bindung* ist gestrichen, sein Inhalt
steckt in 4.2. **Tabelle 4.1 ist ersatzlos entfallen**, die Verteilung trägt
jetzt der Boxplot. Kapitel 4 hat keine Tabelle mehr.

**Die Anweisung nannte die Sensitivitäten 4.7 und die Diskussion 4.8, strich
aber zugleich 4.6.** Beides zugleich ginge nur mit einer Lücke in der
Nummerierung, deshalb zählt LaTeX hier fortlaufend. Die Marken tragen die
Sache und nicht die Nummer.

### 1.2 Alle Zahlen stammen aus dem Analyse-Repository

Keine Zahl des Kapitels ist aus einer Abbildung abgelesen oder in der
Schriftfassung nachgerechnet. Quelle ist
`analysen/code/schrift/ERGEBNISSE_VERDRAENGUNG_UND_AFRR.md` Abschnitt 7 und
Abschnitt 4 der Anweisung. **Rückfragen dorthin, nicht nachrechnen.**

Zwölf Abbildungen liegen in `figures/chapter_4/`, die beiden letzten seit
der Lieferung `sensi8` vom 23.09.2026. Die drei Sensitivitätsabbildungen sind am 23.09.2026 neu
geholt worden; sie tragen dieselben Zahlen und allein eine klarere
Beschriftung mit den Maxima als Zahl am Whisker. Stand am 22.09.2026 abends
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
| 4.4 Zeitliches Muster | **durch** am 23.09., acht Absätze, dazu die Beschreibung der Heatmap zwischen den beiden Abbildungen |
| 4.5 Preis und Engpassbedarf | **durch** am 23.09. abends, drei Absätze, Anhang H angelegt |
| 4.6 Einleitung | **durch** am 23.09. abends, sieben Sätze, zählt jetzt vier Abschnitte |
| 4.6.1 Modellierung der aFRR | **durch** am 23.09. abends, sieben Absätze, vollständig neu sortiert |
| 4.6.1 Modellierung der aFRR | **zweimal durch** am 23.09. abends, sechs Absätze, je einer pro Abbildung |
| 4.6.2 Abrufdauer | **durch** am 23.09. spät abends, der Befund zur halben Stunde ist ergänzt |
| 4.6.3 Handelsspanne | **durch** am 24.09. in der Kontrolllesung, Faktor 1,5 benannt, Schlusssatz angefügt |
| 4.6.4 Zukunftsvariante | **neu gefasst** am 24.09., vier Absätze, Abbildung und Zahlen auf die Variante ohne FCR-Senkung gezogen, Erlösaufteilung über den Bruttoerlös |
| ganzes Kapitel | **Kontrolllesung am 24.09.**, zwölf Befunde A1 bis A6 und B1 bis B6, elf umgesetzt, B5 bewusst belassen |
| ~~4.7 Diskussion~~ | **gestrichen**, die Diskussion ist Kapitel 5 |

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

### 1.4 Was am 23.09.2026 abends dazugekommen ist

**Anhang H, Zeitmuster des Redispatch.** `extras/attachment_redispatch.tex`,
eingebunden in `main.tex` nach dem Jahreslauf. Der Anhang trägt die
Zuordnung der Richtungen und den Befund; **was die Abbildung zeigt und wie
der Redispatch aggregiert ist, steht in Abschnitt 4.5**, wo der Leser es
zuerst braucht. So steht nichts doppelt. Zitiert wird
`netztransparenz_regelenergie_2026`.

**Abschnitt 4.5 steht in drei Absätzen.** Der erste erklärt Anhang H vor dem
Verweis und hält den Tagesgang von Bedarf und Preis gegeneinander (Faktor
1,7 gegen 8,3). Der zweite beschreibt Abbildung 4.6. Der dritte trägt die
Schlussfolgerungen. Vier Vorgaben des Verfassers sind darin umgesetzt:

- Die Begründung des arithmetischen Mittels ist **gestrichen**.
- Die Bezugslinie von 101 Euro je bewegter Megawattstunde steht jetzt unter
  ihrer Annahme, nämlich dass die Kosten linear mit dem Maßnahmenvolumen
  steigen.
- Der Satz zu den 952 Millionen Euro Reservekraftwerkskosten ist
  **gestrichen**.
- Der Jahresgang hängt jetzt am günstigsten **Monat** und nennt **beide**
  Richtungen, und der Redispatch wird über die bedarfsreichsten Tage
  beschrieben statt über Mittelwerte je Jahreszeit.

**Abschnitt 4.6.1 ist vollständig neu sortiert**, sieben Absätze in der vom
Verfasser vorgegebenen Reihenfolge: Basisfall und Prüfumfang, Verteidigung
der Annahmen gegen das Rosinenpicken, Leistungsdiagramm, Arbeitsdiagramm,
Schieflage und ihre Verlagerung, Ungewissheit des Abrufs, Abgrenzung der
Jahresrechnung. Die Stufen heißen jetzt wie im Bild; die Stufe *ohne
Lieferung* kam im Text bisher gar nicht vor und trägt jetzt den Befund, dass
die aFRR-Arbeit in der Laderichtung einen größeren Teil des Preises trägt
als in der Entladerichtung.

**Ein falscher Satz ist zurückgenommen.** „Zwei Annahmen, die sich im Median
ähnlich auswirken…" — der Grenzpreis hebt den Median um 16 Prozent, die
freie Lieferung um 69. **Nicht wieder aufnehmen.**

**Zwei neue eigene Auswertungen im Schriftrepository.**

| Verzeichnis | was es trägt |
|---|---|
| `analysen/afrr_abruf/` | `abruf.py` und `BEFUND.md`. In Deutschland wurden 2025 im Mittel **51 MW positive und 53 MW negative aFRR-Arbeit** abgerufen, gegen bezuschlagte 2010 und 1820 MW also **2,5 und 2,9 Prozent**; in 92 Prozent der Viertelstunden bleibt der Abruf unter einem Zehntel der Vorhaltung. Die Bezugsanlage hat **100 MW**, sodass die Sensitivitätsstufe *bis zum Abruf* ihr den gesamten deutschen Abruf allein zuschreibt. |
| `analysen/zeitmuster_ursachen/monate_tagesebene.py` | `BEFUND_MONATE_TAG.md`, je Monat der Median der Tagesmittel und die mittlere Redispatchleistung, dazu wie viele der bedarfsreichsten Tage in welche Jahreszeit fallen. Dieselbe Kenngröße wie `BEFUND_JAHRESZEITEN_TAG.md`, damit beide Befunde zusammenpassen. |

**Der Code des Modellrepositorys stützt die Verteidigung in 4.6.1.**
`optimizer.py` Zeile 292 führt `prorata` als „pro-rata-Abruf, kein
Rosinenpicken (konservativ/realistisch)", und Zeile 312 sagt zu
`afrr_ene_qde_anteil` = 1,0: „der volle Abruf unterstellt, dass sie ihn
allein bedient". Das ist genau das Argument des Verfassers, unabhängig
aufgeschrieben.

### 1.5 Was am 23.09.2026 spät abends dazugekommen ist

**Abschnitt 4.6.1 ist zweimal umgebaut worden** und trägt jetzt sechs
Absätze: den verschmolzenen Einleitungsabsatz, je einen Absatz zu Abbildung
4.7 und 4.8 mit Niveau, Quantilen und Schieflage, die Ungewissheit des
Abrufs, die Abgrenzung der Jahresrechnung und einen Schlussfolgerungsabsatz.
Beide Abbildungen sind einen Absatz nach hinten gerückt, zwischen ihnen
steht genau ein Absatz.

**Zwei Befunde des Verfassers aus den Abbildungen, nachgerechnet.** Der
Grenzpreis hebt das obere Ende der mittleren 50 Prozent nur um 4,6 und
4,9 €/(MW·h), das Maximum dagegen auf das 4,6- und das 3,8-Fache; die
Schieflage steigt vom 1,9- auf das 2,3-Fache. Die freie Lieferung wirkt
umgekehrt und **senkt** die Schieflage auf das 1,6-Fache. Die Stufe *ohne
Lieferung* zeigt, dass die aFRR-Arbeit in der Laderichtung schwerer wiegt,
denn sie senkt den Median der Ladereservierung um 44 Prozent und lässt den
der Entladereservierung nahezu unverändert.

**Abschnitt 4.6.2 trägt einen neuen Befund zum Produktzuschnitt.** Die halbe
Stunde Abrufdauer liegt fast auf dem Preis der Viertelstunde (11,91 gegen
11,72 €/(MW·h) entladend, 8,56 gegen 8,59 ladend) und verschafft dem ÜNB die
doppelte Zeit für eine Ablösung der Maßnahme. Der Schritt auf die volle
Stunde kostet 0,30 €/(MW·h) entladend und 1,28 €/(MW·h) ladend. **Die
Schätzung des Verfassers, die volle Stunde sei „ein paar Euro je MWh"
teurer, ist damit berichtigt.**

**Die sechs gleichlautenden Schlusssätze sind variiert.** „Aus dieser
Untersuchung lässt sich Folgendes mitnehmen." stand sechsmal im Kapitel und
ist **nicht wieder aufzunehmen**. Jeder Abschnitt hat jetzt seinen eigenen
Satz, drei davon mit der Zahl der folgenden Sätze. **Diese drei Zahlen sind
beim Umbau eines Schlussblocks mitzuführen.**

**Weitere Vorgaben umgesetzt.** Die FCR ist aus der Sättigungsaussage
genommen, weil dieser Markt bereits als gesättigt gilt; der Abschlag von
zehn Prozent auf die FCR-Preise bleibt in der Rechnung. Der Satz zur eigenen
Referenzrechnung mit der Abweichung von 0,01 €/(MW·h) und der
Bindungsdauersatz in der Einleitung 4.6 sind gestrichen.

**Dreizehn Stellen im Kapitel tragen jetzt ihre Einheit.** Vorgabe des
Verfassers: *jede Zahl hat eine Einheit*. Betroffen waren 4.2, 4.3, 4.6.1,
4.6.2, 4.6.3 und 4.6.4, jeweils die **erste** Zahl eines Paares.

**Zwei eigene Fehler, aus denen Regeln geworden sind.** Beide stehen in
`AUFTRAG_KAPITEL_5.md` Abschnitt 9, damit der nächste Chat sie nicht
wiederholt.

1. Ein `git checkout chapters/chapter_4.tex` hat die ungesicherten
   Änderungen der Kapiteldatei verworfen. Sie sind aus den Skripten im
   Scratchpad vollständig wiederhergestellt und gegen das PDF geprüft.
   **Kein `git checkout` auf eine Datei mit ungesicherten Änderungen.**
2. Ein Anker mit `str.index` hat die **auskommentierte** Fassung getroffen
   und dabei einen lebenden Absatz mit in den Kommentarblock gezogen.
   **Anker an den Zeilenanfang binden oder Kommentarzeilen überspringen.**

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

### Wurzelverzeichnis, sechs Dateien

| Datei | Rolle |
|---|---|
| `CLAUDE.md` | Auftrag, Stilregeln, Begriffe, Prüfungen. Claude ändert sie nicht, der Verfasser zieht selbst nach. |
| `HANDOFF.md` | diese Datei, Einstiegspunkt jeder Sitzung |
| `WORKFLOW.md` | Vorgehen: Absatzplan (3), Kommentardurchgang (7), Arbeitsweise am Absatz (10) |
| `ENTSCHEIDUNGSPROTOKOLL.md` | Nachweis aller Entscheidungen, nur anhängen, nie ganz lesen |
| `README.md` | Beschreibung des Repositorys |
| `AUSBLICK.md` | **Sammeldatei für den Ausblick, angelegt am 25.09.2026.** Alles, was der Verfasser für Abschnitt 6.2 bestimmt, wird hier unmittelbar eingetragen, mit Herkunft, zurückgenommenem Wortlaut und Begründung. |
| `AUFTRAG_KAPITEL_5.md` | Lesekarte für Kapitel 5 mit jeder Fundstelle und dem Material für die Diskussion. **Abschnitt 8 ist am 24.09.2026 erledigt**, die Gliederung steht, der dortige Strukturvorschlag ist überholt. Die Abschnitte 1 bis 7 und 9 gelten weiter. |
| ~~`AUFTRAG_REFERENZAUFTEILUNG.md`~~ | **Am 24.09.2026 erledigt und nach `archiv/` verschoben.** Die Lieferung beantwortet ihn in ERGEBNISSE Abschnitt 7.14, und Abschnitt 4.6.4 steht jetzt auf dieser Aufteilung. |

### `archiv/`, einundzwanzig Dateien, nur zum Nachschlagen

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
- **Aus 4.4, Vorgabe des Verfassers vom 23.09.2026:** ein \ac{BESS} wird eher
  zum Entladen als bilanzieller Ausgleich für erneuerbare Erzeugung
  eingeplant. Im Tagesmuster lohnen deshalb die Mittagsstunden am meisten,
  wenn er mit regelbarer Photovoltaik gekoppelt wird; saisonal eher der
  Winter, in dem die Winderzeugung dominiert. Die Abendstunden sind dagegen
  oft teuer.
- **Aus 4.4, Befund vom 23.09.2026:** die beiden Tage mit der steilsten
  Staffel der Arbitragespannen, nämlich der 26.08.2025 mit 10 und der
  15.05.2025 mit 11 Prozent, sind genau die beiden Tage, an denen die
  Verdrängung nach Abschnitt 4.1 auch bei 200\,€/(MW·h) unvollständig
  bleibt. Der Zusammenhang erklärt einen Befund des Abschnitts 4.1 und stand
  bis zum 23.09.2026 in 4.4; er gehört in die Diskussion.
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

- **Aus 4.6.2, Vorgabe des Verfassers vom 24.09.2026:** die Sensitivität
  zur Handelsspanne misst nicht, was sie messen soll. Der Faktor streckt
  um das Tagesmittel und hebt damit die Stunden, die ohnehin weit davon
  liegen. Der Vorteil des mehrfachen Handels derselben Viertelstunde
  entsteht dagegen in Viertelstunden mit großer Preisbewegung innerhalb
  desselben Lieferzeitpunkts. Beide fallen nicht zusammen. Steht als
  Absatz 6 in den Stichpunkten zu 5.5.

---

## 7a Stand von Kapitel 5, 24.09.2026

Kapitel 5 heisst seit dem 24.09.2026 nur noch **Diskussion**. Die Gliederung
mit acht Abschnitten vom selben Tag ist verworfen; es gilt die Gliederung
nach der Logik des Gesamtkonzepts. Einzelheiten im Protokoll.

| Abschnitt | Absaetze | Stand |
|---|---|---|
| Einleitung | 1 | **ausformuliert**, acht Saetze, beschreibt den Aufbau genau einmal |
| 5.1 Anforderungen und ihre Umsetzung im Produkt | 4 | **ausformuliert** |
| 5.2 Modellierung und ihre Annahmen | 5 | **ausformuliert** |
| 5.3 Wirtschaftlichkeit und Wirksamkeit | 4 | **ausformuliert** |
| 5.4 Die Rolle der BESS im Engpassmanagement und am Markt | 4 | **ausformuliert** |
| 5.5 Umsetzung, systemweite Ausrollung und Forschungsbedarf | 4 | **ausformuliert** |

**Der Umfang liegt bei rund sechs Seiten gegen einen Zielumfang von 14.**
Ursache ist, dass die Stichpunkte einen Satz je Punkt vorgaben. Zum Fuellen
kaemen in Betracht, die Argumente in 5.1 und 5.5 zu entfalten, die in
Kapitel 3 benannten Annahmen einzeln abzuhandeln statt gebuendelt, und die
Folgerungen fuer den UENB und den Betreiber je Abschnitt auszufuehren.

**Was beim Ausformulieren bindet.**

- **Die Diskussion nennt fast keine Zahlen.** Vorgabe des Verfassers vom
  24.09.2026: statt der Zahlen stehen die Erkenntnisse und Schluesse. Jede
  Zahl, die doch noetig wird, ist einzeln zu begruenden.
- **Die Einleitung beschreibt den Aufbau genau einmal.** Kein weiterer
  Abschnitt wiederholt ihn.
- Die fett gesetzten Absatzkoepfe und die `itemize`-Umgebungen sind Geruest
  und fallen mit dem Fliesstext weg.
- **Der Begriff *kapazitaetsbasierter Redispatch* in 5.5 ist in den Kapiteln
  1 bis 4 nicht eingefuehrt** und braucht dort einen Definitionssatz und
  einen Beleg. In Betracht kommt `consentec_ausarbeitung_2024`.
- **Die Erklaerung in 5.1 Absatz 2 ist vom Verfasser zu bestaetigen**,
  naemlich dass die Summe der stuendlichen Indifferenzpreise die entgangene
  Vermarktung uebersteigt.
- **Ein `cs` am Anfang einer Ueberschrift zerlegt den Eintrag im
  Inhaltsverzeichnis.** Der Titel von 5.4 beginnt deshalb mit einem Wort.
- **Pruefung 1 findet keine Steuerzeichen.** Am 24.09.2026 sind drei
  zerstoerte `c`-Befehle nur am Inhaltsverzeichnis aufgefallen, nicht an
  der Pruefsuite. Vorschlag: Pruefung 1 erweitern.

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
