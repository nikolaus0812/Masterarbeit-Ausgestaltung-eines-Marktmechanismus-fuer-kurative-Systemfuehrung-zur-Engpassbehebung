# Durchsicht der Kapitel 1 bis 3, Stand 15.09.2026

Prüfung auf Anbindung der Sätze, Zusammenlegung von Absätzen, Dopplungen und
Platzierung der Gleitumgebungen. Befunde aus drei Subagenten je Kapitel und
der Sichtung des PDF. Nichts davon ist umgesetzt. Jede Option trägt eine
Nummer, eine Empfehlung (E = empfohlen, O = offen, N = nicht empfohlen) und
die erwartete Wirkung. Absatznummern beziehen sich auf die Zählung in den
gerenderten Textdateien der Sitzung, die ersten Wörter machen die Stelle
eindeutig.

---

## A Platzierung im PDF

| Nr. | Befund | Option | Wirkung | E |
|---|---|---|---|---|
| A1 | Seite 14 ist zu 40 % leer, weil Tabelle 2.1 mit der Option h nicht mehr auf die Seite passt und auf Seite 15 rutscht. | Tabelle 2.1 auf `[tbp]` setzen. Getestet: Seite 14 voll, Tabelle oben auf Seite 15, Kapitel 2 endet auf Seite 31 mit voller Seite. | Weißraum weg, keine Seite gespart | E |
| A2 | Seite 6 trägt nur acht Zeilen, Überlauf von Kapitel 1. | Kapitel 1 um etwa acht Zeilen kürzen, Kandidaten in K1. | Kapitel 1 auf 5 Seiten | E |
| A3 | Seite 31 trägt nur drei Zeilen, Überlauf von Kapitel 2. Nach A1 ist die Seite voll, der Befund entfällt. | Nach A1 prüfen. Sollte Kapitel 2 wieder mit wenigen Zeilen überlaufen, drei Zeilen aus K2 streichen. | eine Seite | O |
| A4 | Abbildung 3.3 (Ablauf der Preisbestimmung, DIN 66001) steht allein auf Seite 45 mit je einem Drittel Weißraum darüber und darunter. | Abbildung auf `height=0.6\textheight` skalieren, dann passt Text auf die Seite. Alternativ `[p]` belassen. | bis zu eine halbe Seite | E |
| A5 | Alle übrigen Abbildungen und Tabellen stehen oben auf der Seite, auf der oder nach der sie genannt werden. | keine | | |

---

## B Kapitel 1

### B1 Anbindung, mechanisch (ein Paket)

Bindewörter und Umstellungen ohne Inhaltsänderung, Liste im Protokoll nach
Umsetzung:

- 1.1 Absatz 6 (NEP 2045) bekommt einen Überleitungssatz vom heutigen Stand zur Planung.
- 1.1 Absatz 10 und 11: Satz 6 von Absatz 11 (zeitliche Lücke gilt auch kurativ) wandert ans Ende von Absatz 10, damit Absatz 11 an Absatz 9 Satz 6 (ungenutzte Reserve) anschließt.
- 1.2 Absatz 12: Satz 2 „Kurative Vorhaltung bezeichnet dabei“ ohne Bezug, Satz 5 „Abschnitt X nennt“ unverbunden.
- 1.2 Absatz 13: Satz 3 und Satz 5 bis 7 (2030) ohne Bindewörter, Absatz endet ohne Konsequenz.
- 1.2 Absatz 14: Satz 4 (Einsparung nicht Gegenstand) unterbricht Satz 3 und 5.

Empfehlung E. Wirkung: keine Zeile.

### B2 Zusammenlegung

| Nr. | Option | Wirkung | E |
|---|---|---|---|
| B2.1 | 1.1 Absatz 7 (ereignisabhängig, räumlich wandernd, Anforderung an das Instrument) auflösen: Satz 2 an Absatz 4, Satz 3 an Absatz 2, Satz 4 als Überleitung vor Absatz 9. Beseitigt zugleich die Dopplungen B3.2 und B3.3. | 1.1 von 8 auf 7 Absätze, etwa 3 Zeilen weniger | E |
| B2.2 | Alternativ Absatz 6 und 7 verbinden (8 Sätze). | 7 Absätze, keine Zeile | N |
| B2.3 | 1.2 Absatz 12 (9 Sätze, zwei Kernaussagen) teilen in Ziel und Begriffe (4) und Grund für einen Marktmechanismus (5). | 1.2 von 4 auf 5 Absätze | O |
| B2.4 | 1.2 Absatz 14 Satz 4 zu Absatz 13 hinter Satz 1 verschieben. | keine | E |

### B3 Dopplungen

| Nr. | Befund | Option | Wirkung | E |
|---|---|---|---|---|
| B3.1 | BESS als Akteur dreimal: Absatz 1 Satz 4, Absatz 11 Satz 8, Absatz 15 Satz 3. | Absatz 15 Satz 3 „Daraus folgt die Wahl der BESS“ streichen. | 1 Zeile | E |
| B3.2 | Absatz 7 Satz 2 wiederholt Absatz 4 Satz 3 bis 4 (Dezember 2024). | mit B2.1 erledigt | | E |
| B3.3 | Absatz 7 Satz 3 wiederholt Absatz 2 Satz 3 bis 4 (Engpassmuster wandert). | mit B2.1 erledigt | | E |
| B3.4 | 1.1 Absatz 3 Satz 1 und 3 bis 5 (Selbstdispatch, zonaler Preis) stehen wörtlich in 2.2.1 Absatz 36. | In Kapitel 1 auf zwei Sätze kürzen: Marktdesign nennt den zonalen Preis, Redispatch ist der vorgesehene Korrekturmechanismus. Definition bleibt in 2.2.1. | 2 bis 3 Zeilen | E |
| B3.5 | 1.1 Absatz 9 Satz 3 bis 5 (Marge, Betriebsmittel vertragen mehr) wörtlich wie 2.1.1 Absatz 5 und 8. | In Kapitel 1 belassen, es ist die Motivation. In 2.1.1 Absatz 8 Satz 2 den Wortlaut „das Freihalten dieser Marge ist der Eingriff“ variieren. | keine | O |
| B3.6 | 1.1 Absatz 10 Satz 2 bis 4 (Handelsfenster bis fünf Minuten) viermal: Kap. 1, 2.1.1 Absatz 8, 2.2.2 Absatz 39, 2.2.2 Absatz 40. | In 2.1.1 Absatz 8 Satz 6 bis 7 streichen und auf 2.2.2 verweisen, in Kap. 1 belassen. | 2 Zeilen in Kap. 2 | E |
| B3.7 | 1.1 Absatz 10 Satz 7 (teurer, kleinerer Kreis) dreimal in Kap. 2 (Absatz 8, 9, 26). | In 2.1.1 Absatz 8 Satz 8 bis 9 streichen, Absatz 9 trägt die Aussage mit Quelle. | 2 Zeilen in Kap. 2 | E |
| B3.8 | 1.1 Absatz 11 Satz 6 „ebenfalls vorab eingeplant“ steht in 2.1.1 Absatz 10 zweimal (Satz 3 und 6) und in Absatz 12. | In 2.1.1 Absatz 10 Satz 6 kürzen. | 1 Zeile | E |
| B3.9 | 1.2 Absatz 12 Satz 6 bis 8 nehmen das Zwischenfazit 2.4 Absatz 67 wörtlich vorweg (Verfügbarkeit nur über Preis, zwei Logiken). | In Kap. 1 belassen als Begründung des Vorgehens, in 2.4 Absatz 67 den Wortlaut ändern und auf die Herleitung in 2.3 stützen. | keine | O |
| B3.10 | 1.2 Absatz 13 Satz 5 (2030 als Rahmen) und 3.2.1 Absatz 20 Satz 5 sagen dasselbe. | In 3.2.1 auf einen Halbsatz mit Verweis kürzen. | 1 Zeile in Kap. 3 | E |
| B3.11 | 1.2 Absatz 14 Satz 7 begründet „opportunitätskostenbasierter Teil des Gebots“ mit Präqualifikation, Pönale und Anbieterzahl, 3.2.1 Absatz 19 Satz 8 mit der fehlenden Abrufwahrscheinlichkeit. Zwei Begründungen für denselben Satz. | In 1.2 die Abrufwahrscheinlichkeit ergänzen, oder in 3.2.1 die Pönale mitnennen. Vom Verfasser zu entscheiden. | keine | O |
| B3.12 | Reaktionszeit ist in 1.2 als „Zeit vom Abrufsignal bis zur vollständig umgesetzten Leistungsänderung“ definiert, in 2.1.2 Absatz 18 als „Zeit bis zur vollen Entlastungswirkung“. Bindungsdauer ist in 1.2 und in 3.1.2 Absatz 8 definiert. | Wortlaut in 2.1.2 an 1.2 angleichen. In 3.1.2 „Die Bindungsdauer ist der Zeitraum, über den die Zusage nach dem Zuschlag gilt“ auf „Die Bindungsdauer beträgt eine Zeitscheibe, also eine Stunde des Liefertages“ kürzen. | 1 Zeile | E |

---

## C Kapitel 2

### C1 Anbindung, mechanisch (ein Paket)

Bindewörter, Umstellungen innerhalb eines Absatzes und Überleitungssätze
ohne Inhaltsänderung. Die vollständige Liste hat 45 Stellen, die
wichtigsten:

- 2.1.1 Absatz 4 und 5: Überleitungen zum Vier-Zustands-Modell und zur Physik, Absatz 4 Satz 7 nutzt „Überlast“ vor der Einführung von PATL und TATL in Absatz 5.
- 2.1.1 Absatz 8 Satz 5 verweist auf Abbildung 2.3 in 2.2.2, 30 Absätze später.
- 2.1.1 Absatz 10 Satz 4: These nennt den Grenzwert, die Erklärung nach dem Doppelpunkt den Zeitpunkt.
- 2.1.1 Absatz 11 Satz 1 bis 3 sagen dreimal dasselbe (kein Fahrplaneingriff, präventiv greift immer ein, kurativ nur vorgehalten).
- 2.1.2 Absatz 13, 16, 17: Abschnittsbeginn ohne Anknüpfung, KuPilot-Einschub in Absatz 15 Satz 5.
- 2.1.4 Absatz 25: Absatz 24 kündigt die Vergütung an, es folgen die Herausforderungen. Überleitung an die Gliederung anpassen.
- 2.1.5 Absatz 32: der anknüpfende Satz steht an zweiter Stelle.
- 2.2.3 Absatz 41 Satz 7 (Betriebsführung) steht nach der Konsequenz, gehört davor.
- 2.3.1 Absatz 48: Satz 4 bis 8 (Übersicht der Positionen) logisch vor Satz 1 bis 3 (Einsatzpreis).
- 2.3.3 Absatz 59 (11 Sätze) trägt vier Gedanken, siehe C2.9.
- 2.3.4 Absatz 60 (mFRR) und 62 (Anreizkomponente) ohne Anknüpfung.
- 2.3.5 Absatz 63 Satz 7 „nicht unmittelbar anwendbar“ ohne Grund im Absatz, der Grund (kein Netzknotenbezug) steht erst in 2.4.
- 2.4 Absatz 69 ohne Übergang von Absatz 68.

Empfehlung E. Wirkung: keine Zeile.

### C2 Zusammenlegung und Teilung

| Nr. | Option | Absätze vorher, nachher | Wirkung | E |
|---|---|---|---|---|
| C2.1 | 2.1.1 Absatz 5 Satz 8 bis 9 (Abbildungsvergleich) zu Absatz 7 ziehen. | 8, 8 | keine | E |
| C2.2 | 2.1.1 Absatz 8 (11 Sätze) teilen: Satz 1 bis 7 Marge und Planungshorizont, Satz 8 bis 11 mit Absatz 9 (Kosten hängen von der Anlagenart ab) verbinden, dabei Absatz 9 Satz 5 als Dopplung streichen. | 8, 8 | 1 Zeile | E |
| C2.3 | 2.1.1 Absatz 11 (9 Sätze, drei Kernaussagen) teilen in Satz 1 bis 4 und Satz 5 bis 9, dabei Satz 1 bis 3 auf einen Satz kürzen. | 8, 9 | 2 Zeilen | E |
| C2.4 | 2.1.1 Absatz 10 mit Absatz 12 Satz 1 bis 2 verbinden (dieselbe thermische Reserve), Absatz 12 Satz 3 bis 5 an Absatz 11 Satz 1 bis 4 hängen. | 8, 7 nach C2.3 | keine | O |
| C2.5 | 2.1.2 Absatz 16 (11 Sätze) teilen in Maßnahmenraum (5) und Meldung, Ladezustand, Verbund (6). | 5, 6 | keine | E |
| C2.6 | 2.1.3 Absatz 19 (12 Sätze) teilen in Zusage eines Dritten (4) und vier Merkmale mit Tabelle (8). | 5, 6 | keine | E |
| C2.7 | 2.1.3 Absatz 22 (3 Sätze) mit Absatz 23 Satz 1 bis 5 verbinden (Speicher in beide Richtungen, 8), Absatz 23 Satz 6 bis 9 als Standort und Bestand (4). | 5, 5 | keine | E |
| C2.8 | 2.2.2 Absatz 37 (1 Satz) mit Absatz 39 Satz 1 bis 3 verbinden, Absatz 39 Satz 4 bis 8 als eigenen Absatz. | 3, 3 | keine | E |
| C2.9 | 2.3.3 Absatz 59 (11 Sätze) teilen in Bemessung bei BESS offen (6) und Hirth-Einwand nicht übertragbar (5). | 5, 6 | keine | E |
| C2.10 | 2.3.3 Absatz 57 (8 Sätze, zwei Kernaussagen) Satz 5 bis 8 mit Absatz 58 Satz 1 bis 2 verbinden. | 5, 5 | keine | O |
| C2.11 | 2.3.4 Absatz 60 (mFRR, 3 Sätze) mit Absatz 61 verbinden, dabei Absatz 61 Satz 2 bis 3 (Arbeitspreis, PICASSO, beides schon in 2.2.3) streichen. | 4, 3 | 2 Zeilen | E |
| C2.12 | 2.3.5 Absatz 64 mit 65 verbinden (dieselbe Leistung und derselbe Energieinhalt), Absatz 64 Satz 4 (Wettbewerb unter Anbietern) streichen. | 3, 2 | 1 Zeile | E |
| C2.13 | 2.4 Absatz 67 mit 68 und Absatz 69 mit 70 verbinden. | 4, 2 | keine | E |
| C2.14 | Kapiteleinleitung (3 Sätze), 2.2 Einleitung (1 Satz), 2.3 Einleitung (1 Satz) bleiben unter vier Sätzen. | | | N, Einleitungen dürfen kurz sein |

### C3 Dopplungen innerhalb von Kapitel 2

| Nr. | Befund | Option | Wirkung | E |
|---|---|---|---|---|
| C3.1 | Präventiv gegen kurativ fünfmal erklärt: 2.1 Einleitung Absatz 3 Satz 3, 2.1.1 Absatz 4 Satz 8, Absatz 5 Satz 9, Absatz 10 Satz 4 bis 5, 2.1.4 Absatz 26 Satz 2 bis 3. | Absatz 4 Satz 8 und Absatz 26 Satz 2 bis 3 streichen, Absatz 3 und Absatz 5 (mit Abbildung) tragen die Erklärung. | 3 bis 4 Zeilen | E |
| C3.2 | § 13a knüpft an den Eingriff an, fünfmal: Absatz 11 Satz 9, 31 Satz 2, 44 Satz 4, 46 Satz 3 und 5, 68 Satz 1. | Absatz 11 Satz 9 und 44 Satz 4 bis 6 kürzen, die Aussage bleibt in 2.1.5, 2.3.1 und 2.4. | 3 Zeilen | E |
| C3.3 | Regelleistung vergütet die Vorhaltung, fünfmal: Absatz 41 Satz 5 bis 6, 42 Satz 3 bis 4, 61 Satz 1, 63 Satz 2, 67 Satz 2. | Absatz 42 Satz 3 bis 4 kürzen, Absatz 63 Satz 2 kürzen. | 2 Zeilen | E |
| C3.4 | Leistung und Arbeit getrennt, viermal: 42 Satz 6, 43 Satz 6, 61 Satz 2, 63 Satz 3. PICASSO zweimal eingeführt (43 Satz 7, 61 Satz 3). | mit C2.11 erledigt | | E |
| C3.5 | Ladezustand über die Bindungsdauer freihalten, sechsmal: 11 Satz 4, 16 Satz 7 bis 8, 24 Satz 4, 62 Satz 5 bis 6, 69 Satz 1, 70 Satz 2. | Absatz 24 Satz 4 und 69 Satz 1 kürzen, 62 betrifft die Regelleistung und bleibt. | 2 Zeilen | E |
| C3.6 | Netzbooster wörtlich zweimal (16 Satz 3, 28 Satz 3), KuPilot als Echtbetrieb zweimal (15 Satz 5, 28 Satz 2), netzseitige Maßnahmen dreimal (4 Satz 6, 16 Satz 3, 29 Satz 4). | Absatz 16 Satz 3 auf die Aufzählung ohne Erklärung kürzen, Absatz 15 Satz 5 den KuPilot-Einschub streichen (steht in 2.1.4). | 2 Zeilen | E |
| C3.7 | Vorbelastung und Witterung dreimal (17 Satz 6, 18 Satz 1, 25 Satz 4), Freigabe je Stromkreis zweimal (18 Satz 3, 25 Satz 3 und 5). | Absatz 25 Satz 3 bis 5 auf einen Satz mit Verweis kürzen, dann Absatz 25 mit 26 verbinden. | 2 Zeilen, 2.1.4 von 4 auf 3 Absätze | E |
| C3.8 | Intervalle unabhängig, viermal in 2.3.2 und 2.3.3 (49 Satz 8, 51 Satz 1, 55 Satz 2, 59 Satz 4). | Absatz 49 Satz 8 streichen, 55 Satz 2 kürzen. | 1 Zeile | E |
| C3.9 | Zeitwert unabhängig vom Anweisungszeitpunkt zweimal (57 Satz 7 bis 8, 68 Satz 3 bis 4). | In 2.4 Absatz 68 auf einen Halbsatz kürzen. | 1 Zeile | E |
| C3.10 | Beschränkung auf den marktlichen Akteur dreimal (13 Satz 2, 16 Satz 5, 29 Satz 7). | Absatz 16 Satz 5 streichen. | 1 Zeile | E |
| C3.11 | Handelsfenster nach der letzten Vorschaurechnung dreimal (8 Satz 6 bis 7, 39 Satz 7, 40 Satz 5). | siehe B3.6 | | E |
| C3.12 | Abschnitt 2.1.2 Absatz 16 Satz 4 und 2.1.3 Absatz 19 Satz 1 (Zusage eines Dritten). | Absatz 19 Satz 1 kürzen zu einem Anschlusssatz. | 1 Zeile | E |
| C3.13 | 2.3.5 Absatz 66 Satz 5 und Satz 8 (Alternative wechselt mit den Preisen). | Satz 8 streichen. | 1 Zeile | E |
| C3.14 | 2.3.2 Absatz 55 Satz 5 und Satz 7 (BESS ein bis zwei Stunden). | Satz 7 streichen. | 1 Zeile | E |
| C3.15 | Widerspruch: 3.2.2 sagt, 2,5 Stunden lägen „am oberen Rand des Bereichs der Großspeicher am Netz, wie in Abschnitt 2.1.3 dargestellt“, dort stehen aber 1 bis 2 Stunden. Nach der Registerauswertung liegen die geplanten Anlagen im Median bei 2 und leistungsgewichtet bei 3 Stunden. | Satz in 3.2.2 ändern: „Die Auslegung liegt über dem Bereich von ein bis zwei Stunden, den die Großspeicher in Betrieb erreichen, und im Bereich der geplanten Anlagen, wie in Abschnitt 2.1.3 dargestellt.“ Dazu die Fußnote von Tabelle 2.1 um „in Planung leistungsgewichtet 3 Stunden“ ergänzen. | keine | E |

### C4 Dopplungen zwischen Kapitel 2 und 3

| Nr. | Befund | Option | E |
|---|---|---|---|
| C4.1 | Vergütungsstruktur der Festlegung mit Quelle in 2.3.2 Absatz 49 Satz 7 und 3.2.4 Absatz 43 Satz 1. | In 3.2.4 auf einen Verweis ohne Wiederholung des Aufbaus kürzen. | E |
| C4.2 | mFRR-Begründung in 2.3.4 Absatz 60 und 3.2.1 Absatz 20 Satz 4 trotz Verweis wiederholt. | In 3.2.1 auf „Die mFRR führt das Modell nicht, wie in Abschnitt 2.3.4 begründet.“ kürzen. | E |
| C4.3 | Anforderung A5 und 2.1.3 Absatz 19 Satz 4 wortgleich (Eigenschaften statt Technologie), A1 und 2.1.2 Absatz 18 Satz 2 (Reaktionszeit nicht wählbar), A7 und 2.3.5 Absatz 65 (dieselbe Ressource), A4 Satz 4 und 2.3.3 Absatz 59 Satz 9 (Redispatch löst Arbeit aus). | Im Katalog zulässig, weil er die Befunde bündelt. Wortlaut in A1, A5, A7 leicht variieren. | O |
| C4.4 | Zusage besteht durchgehend, Abruf nur im Fehlerfall: 2.3.5 Absatz 63 Satz 4 und 3.1.2 Absatz 6 Satz 3 wortgleich. | In 2.3.5 belassen, in 3.1.2 steht die Definition. Keine Änderung. | N |

---

## D Kapitel 3

Der Verfasser findet, dass Kapitel 3 je Unterabschnitt zu viele Absätze
hat. Stand: 45 Textabsätze. Mit den empfohlenen Optionen etwa 35.

### D1 Anbindung, mechanisch (ein Paket)

- Kapiteleinleitung Satz 3 und 4 ohne Bindewörter.
- Anforderungskatalog: A2, A3, A4, A7 hängen die Begründung ohne denn oder weil an, A8 Satz 2 wiederholt die These, A8 Satz 3 (Verbund) gehört zu A3.
- 3.1.2 Absatz 9: Satz 8 bis 9 (ungünstigster Fall, Ladezustandsband) nach Satz 3, Satz 10 (Bilanzverantwortung) unverbunden.
- 3.1.2 Absatz 11: Satz 8 bis 9 vor Satz 5 bis 7, damit Präqualifikation und Standort nicht verschränkt sind.
- 3.1.2 Absatz 12: Satz 10 bis 11 (Höchstleistung, Teilzuschlag) zu Absatz 13.
- 3.1.2 Absatz 13 Satz 4 „damit“ ohne Grund, der bilanzielle Ausgleich ist im Absatz nicht genannt.
- 3.2 Einleitung Absatz 14: Satz 8 „dafür“ und „das Modell“ ohne Einführung.
- 3.2.1 Absatz 18 Satz 2 „damit“ folgt nicht aus der Tageszerlegung, Absatz 19 als Liste ohne Bindewörter, Absatz 20 Satz 6 gehört zu Satz 1 bis 2.
- 3.2.3 Absatz DA: drei Sätze in Folge mit „damit“. Absatz 29 Satz 4 bis 5 gehören zur Preisbasis.
- 3.2.4 Absatz 36 Satz 8 (Monotonie) unterbricht den Ablauf, Absatz 39 Satz 4 gehört vor Satz 3.
- 3.3.2 Absatz 46 Satz 8 „deshalb“ und „denn“ doppelt.

Empfehlung E. Wirkung: keine Zeile.

### D2 Zusammenlegung

| Nr. | Option | Absätze vorher, nachher | Sätze danach | E |
|---|---|---|---|---|
| D2.1 | 3.1 Einleitung (1 Satz) in den ersten Absatz von 3.1.1 aufnehmen, der dasselbe sagt. | 3.1: 3, 2 | 3 | E |
| D2.2 | 3.1.2 Absatz 5 (Einleitung, 2 Sätze) und Absatz 6 (Zusage) verbinden, Absatz 6 Satz 6 (Modell bildet Energieanteil nicht ab) streichen, weil er in 3.2.4 steht. | 3.1.2: 9, 8 | 7 | E |
| D2.3 | 3.1.2 Absatz 7 (Opportunitätskosten, Richtungen) und Absatz 8 (Klasse, Bindungsdauer) verbinden, dabei Absatz 7 Satz 1 bis 2 streichen, weil 1.2 die Opportunitätskosten definiert. | 9, 7 | 8 | E |
| D2.4 | 3.1.2 Absatz 12 (Ausschreibung, 11 Sätze) und 13 (Zuschlag) nicht verbinden, nur Satz 10 bis 11 verschieben. | 7, 7 | 9 und 9 | E |
| D2.5 | 3.2 Einleitung Absatz 14: Satz 1 bis 2 und Satz 7 (ÜNB-Abwägung, steht in 1.2) streichen. | 1, 1 | 7 | E |
| D2.6 | 3.2.1 Absatz 16 und 17 verbinden (ungebundener Fahrplan, Kopplung, Preiskenntnis, obere Schranke), dabei Absatz 16 Satz 4 als Dopplung von Satz 3 streichen. | 3.2.1: 5, 4 | 10 | O, über der Satzgrenze |
| D2.7 | Alternativ zu D2.6 die Absätze 16 bis 18 neu schneiden: Bezug und Opportunitätskosten (6), Kopplung und obere Schranke (7), lineares Programm und Lösung (7). | 5, 5 | | O |
| D2.8 | 3.2.1 Absatz 20 auf die Rückwirkung der Preise kürzen (Satz 3 bis 5 sind Dopplungen, siehe D3), Satz 3 bis 4 (nicht geführte Märkte) zu 3.2.3 Absatz 26. | 5, 5 | 4 | E |
| D2.9 | 3.2.2 Absatz 23 Satz 1 bis 3 (Zeitstruktur, Variablen) mit Absatz 24 und 25 (Zielfunktion, Gleichung) verbinden, Absatz 23 Satz 4 bis 8 (Ladezustandsbilanz, Leistungsschranke) als eigenen Absatz. | 3.2.2: 5, 4 | 6 und 5 | E |
| D2.10 | 3.2.2 Absatz 21 (Anlage) und 22 (Degradation) verbinden, Absatz 22 Satz 3 bis 4 (Verschleiß real) zu den Systemgrenzen in 3.2.1 Absatz 19. | 4, 3 | 9 | O |
| D2.11 | 3.2.3 Absatz 26 und 27 verbinden (sechs Märkte, Jahr 2025, Tabelle). | 3.2.3: 11, 10 | 8 | E |
| D2.12 | 3.2.3 IDC und Absatz 29 verbinden, Dopplung „dieselbe Viertelstunde mehrfach handeln“ streichen, Satz 29.4 (DA neben IDC) zu Absatz 26. | 10, 9 | 9 | E |
| D2.13 | 3.2.3 aFRR-Leistung und Absatz 31 Satz 1 bis 3 verbinden, die Leiter (Satz 4 bis 7) als eigenen Absatz belassen oder zu den Studien in 3.2.4 Absatz 40. | 9, 8 | 10 | O |
| D2.14 | 3.2.3 Kurative Reservierung und Absatz 34 verbinden, Absatz 34 Satz 1 bis 3 (Mindestgröße, steht in 3.2.1) streichen. | 8, 7 | 6 | E |
| D2.15 | 3.2.4 Absatz 42 (Weber) und 43 (Festlegung) verbinden, Satz 43.3 bis 43.5 als Dopplungen streichen. | 3.2.4: 6, 5 | 9 | E |
| D2.16 | 3.2.4 Absatz 36 Satz 11 bis 12 (Rechenaufwand) zu Absatz 40 Satz 1, Absatz 39 Satz 4 und 10 als Dopplungen streichen. | 5, 5 | 10 und 8 | E |
| D2.17 | 3.3.1 Absatz 44 und 45 verbinden, Absatz 44 Satz 5 streichen, Absatz 45 Satz 3 bis 4 (Unterschiede) nach 3.3.2. | 3.3.1: 2, 1 | 8 | O |
| D2.18 | 3.3.2 Absatz 46 (12 Sätze) und 48 (11 Sätze) in vier Absätze schneiden: Unterschiede (7), Prüfkriterium (5), marktübergreifend (4), je Markt (7). | 3.3.2: 2, 4 | | O, gegen die Absatzzahl |

### D3 Dopplungen in Kapitel 3

| Nr. | Befund | Option | Wirkung | E |
|---|---|---|---|---|
| D3.1 | Ankündigung des Katalogs dreimal (Kapiteleinleitung Satz 7, 3.1 Satz 1, 3.1.1 Satz 1). | mit D2.1 erledigt | 1 Zeile | E |
| D3.2 | 3.1.2 Absatz 5 Satz 1 und Absatz 6 Satz 1 (Akteur sagt Leistungsänderung zu). | mit D2.2 erledigt | 1 Zeile | E |
| D3.3 | Energieanteil eines Abrufs nicht modelliert: 3.1.2 Absatz 6 Satz 6, 3.2.4 Absatz 43 Satz 3, dazu 3.2.1 Absatz 19 Satz 6. | mit D2.2 und D2.15 erledigt, bleibt in 3.2.1. | 2 Zeilen | E |
| D3.4 | Pönale nicht bestimmt, wortgleich: 3.1.2 Absatz 10 Satz 8 und 3.2.4 Absatz 43 Satz 4. | mit D2.15 erledigt | 1 Zeile | E |
| D3.5 | Mindestgröße dreimal: 3.1.2 Absatz 12 Satz 6, 3.2.1 Absatz 18 Satz 5 bis 7, 3.2.3 Absatz 34 Satz 1 bis 3. | mit D2.14 erledigt | 2 Zeilen | E |
| D3.6 | Opportunitätskostenbasierter Teil des Gebots: 3.2.1 Absatz 19 Satz 8 und 3.2.4 Absatz 43 Satz 5. | 3.2.4 Satz 43.5 bleibt als Schlusssatz, 19.8 kürzen. | 1 Zeile | E |
| D3.7 | Zahl aus Hornek (rund zehn Prozent) mit Quelle zweimal: 3.2.1 Absatz 17 Satz 2 und 3.3.2 Absatz 46 Satz 4. | In 3.3.2 auf „wie in Abschnitt 3.2.1 dargestellt“ kürzen. | 1 Zeile | E |
| D3.8 | Tage untereinander vergleichbar, zweimal: 3.2.1 Absatz 18 Satz 1 und 3.2.2 Absatz 23 Satz 5. | 18.1 kürzen auf „Jeder Liefertag bildet ein eigenes Problem.“ | 1 Zeile | E |
| D3.9 | Verbund aus Geboten beider Richtungen: A8 Satz 3 und 3.1.2 Absatz 13 Satz 4. | A8 Satz 3 streichen, Verbund steht in A3 und 3.1.2. | 1 Zeile | E |
| D3.10 | Sensitivität zweimal mit „also“ erklärt: 3.1.2 Absatz 11 Satz 5 und Absatz 13 Satz 3. | In Absatz 13 die Erklärung streichen. | 1 Zeile | E |
| D3.11 | Präqualifikation doppelt: 3.1.2 Absatz 11 Satz 1 und 2. | Satz 1 streichen, Satz 2 als Überleitung umbauen. | 1 Zeile | E |
| D3.12 | Leistungsschranke: 3.2.2 Absatz 23 Satz 7 bis 8 und 3.2.3 Kur Satz 5. | Kur Satz 5 kürzen. | 1 Zeile | E |
| D3.13 | Läufe je Tag: 3.2.2 Absatz 22 Satz 4, 3.2.3 Absatz 34 Satz 2, 3.2.4 Absatz 36 Satz 12, Absatz 40 Satz 1. | 40.1 streichen, 34.2 mit D2.14 weg. | 1 Zeile | E |
| D3.14 | Kopplung über den Ladezustand als Begründung wortgleich in 3.2.4 Absatz 35 Satz 3 und 39 Satz 4. | mit D2.16 erledigt | | E |
| D3.15 | Vorgegebener Preis zweimal in 3.2.3 Kur Satz 1 und 3. | Satz 3 auf die Variable je Viertelstunde kürzen. | 1 Zeile | E |
| D3.16 | 2030 als Rahmen: siehe B3.10. | | | E |
| D3.17 | Widerspruch in der aFRR-Leiter: 3.2.3 Absatz 31 Satz 6 nennt die sechste Stufe „bis zu zehn Prozent des deutschen Abrufs“, aFRR-Arbeit Satz 5 „bis zum vollen Abruf“. | Im Code (erloesaufteilung.py, SATZ_AFRR) ist Stufe 6 „frei bis 10 % des DE-Abrufs“. Der Satz bei der aFRR-Arbeit ist falsch und wird auf „bis zu zehn Prozent des deutschen Abrufs“ berichtigt. | keine | E, Sachfehler |
| D3.18 | 3.3.1 Absatz 45 Satz 3 bis 4 nimmt die Unterschiede aus 3.3.2 vorweg. | mit D2.17 oder allein verschieben. | | O |

---

## E Reihenfolge der Umsetzung, Vorschlag

1. A1 und A4 (Platzierung), dann Build und Seitenzahlen messen.
2. Sachfehler C3.15 und D3.17.
3. Kapitel 3: D2 und D3 in einem Skript je Unterabschnitt, danach D1.
4. Kapitel 2: C3 und C2, danach C1.
5. Kapitel 1: B2.1, B3.1, B3.4, B3.12, dann B1, Ziel 5 Seiten (A2).
6. Kapitelübergreifende Abgleiche B3.6 bis B3.11, C4.
7. Fremdleser-Prüfung je geändertem Abschnitt, Protokoll, Commit je Kapitel.
