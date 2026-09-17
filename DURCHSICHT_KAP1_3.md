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

## F Dopplungen in Kapitel 3, Wortlaut zur Entscheidung

Stand 16.09.2026 nach der Umsetzung von A, D1 und D2. Nichts davon ist
gestrichen. Je Nummer der Wortlaut beider Stellen und der Vorschlag. Antwort
je Nummer: ja (Vorschlag umsetzen), nein (beide bleiben) oder eine andere
Anweisung.

| Nr. | Stelle 1 | Stelle 2 | Vorschlag |
|---|---|---|---|
| F1 | 3.1 Einleitung: „Aus den Befunden des Kapitels 2 folgen Anforderungen, aus denen die kurative Reservierung als Produkt entwickelt wird.“ | 3.1.1 Satz 1: „Der Katalog überführt die Befunde des vorangehenden Kapitels in Bedingungen, die sich an einem Mechanismus prüfen lassen.“ Dazu Kapiteleinleitung: „In diesem Kapitel werden die Anforderungen abgeleitet …“ | Einleitungssatz von 3.1 streichen, 3.1.1 folgt unmittelbar auf die Überschrift. |
| F2 | 3.1.2 Absatz 5 Satz 1: „Eine kurative Reservierung verbindet den Akteur mit dem ÜNB: Der Akteur sagt eine Leistungsänderung zu, der ÜNB nimmt sie in seine Einsatzplanung auf und ruft sie im Fehlerfall ab.“ | Satz 3 desselben Absatzes: „Der Akteur sagt zu, seine Leistung im Fehlerfall um die angebotene Leistungsänderung zu verschieben, und reserviert dafür ein Leistungsband.“ | Beide behalten, Satz 1 ist die Definition, Satz 3 der Inhalt der Zusage. Nur Satz 2 „Der folgende Entwurf bestimmt die Merkmale …“ streichen, weil er ein struktureller Vorverweis ist. |
| F3 | 3.1.2 Absatz 5 Satz 8: „Den Energieanteil eines Abrufs bildet das Modell in Abschnitt 3.2 nicht ab.“ | 3.2.4 letzter Absatz: „Den Energieanteil eines Abrufs, den der Preis der kurativen Reservierung mit abdeckt, bildet das Modell nicht ab.“ Dazu 3.2.1: „das Modell bewertet die Reservierung also ohne Abruf“ | Satz in 3.1.2 streichen, der Produktentwurf spricht nicht über das Modell. In 3.2.4 belassen. |
| F4 | 3.1.2 Absatz 8 Satz 8: „Höhe und Form der Sanktion bestimmt die Untersuchung nicht, weil das Modell die daraus folgende Risikoprämie nicht trägt.“ | 3.2.4 letzter Absatz: „Die Höhe der Pönale bestimmt die Untersuchung nicht, weil das Modell die daraus folgende Risikoprämie nicht trägt.“ | In 3.1.2 kürzen auf „Höhe und Form der Sanktion bleiben offen.“, die Begründung mit dem Modell steht in 3.2.4. |
| F5 | 3.2.1 Absatz 16: „Erst die Mindestgröße von 25 MW macht die Reservierung halbstetig … Für die Mindestgröße ist je Stunde und Richtung eine Binärvariable nötig … Die Mindestgröße wird als Sensitivität geführt, wie in Abschnitt 3.2.3 beschrieben.“ | 3.2.3 Kurative Reservierung, nach der Gleichung: „Die Mindestgröße von 25 MW ist ein Parameter des Produkts, sodass eine Stunde entweder ungebunden bleibt oder mit mindestens diesem Wert reserviert wird. Im Basisfall rechnet das Modell mit stetiger Reservierung, weil jeder Tag viele Läufe verlangt. Die Mindestgröße wird als Sensitivität zugeschaltet, um ihre Wirkung zu prüfen.“ | Die drei Sätze in 3.2.3 streichen und den Verweis in 3.2.1 entfernen, weil dort alles steht. Alternativ die drei Sätze in 3.2.3 behalten und in 3.2.1 nur den Satz zur Binärvariable lassen. |
| F6 | 3.2.1 Absatz 17 Satz 8: „Die beiden letzten Vereinfachungen wirken in eine benennbare Richtung auf den Preis: Ohne Abruf ist der Preis der opportunitätskostenbasierte Teil des Gebots, und die sicheren Zuschläge heben die entgangenen Erlöse an.“ | 3.2.4 letzter Satz: „Der ermittelte kurative Reservierungspreis ist damit der opportunitätskostenbasierte Teil des Gebots und nicht das Gebot.“ | Beide behalten, in 3.2.1 ist es die Wirkung der Vereinfachung, in 3.2.4 das Fazit der Abgrenzung. Kein Eingriff. |
| F7 | 3.2.1 Absatz 15 Satz 5: „… eine prognosegestützte Strategie erreicht im kontinuierlichen Intraday-Handel rund neunzig Prozent des unter vollständiger Preiskenntnis erzielbaren Erlöses [Hornek].“ | 3.3.2 Satz 4: „Das Modell kennt dagegen alle Preise des Liefertages, und dieser Unterschied allein macht rund zehn Prozent des Erlöses im kontinuierlichen Intraday-Handel aus [Hornek].“ | In 3.3.2 auf „…, und dieser Unterschied allein macht rund zehn Prozent des Erlöses im kontinuierlichen Intraday-Handel aus, wie in Abschnitt 3.2.1 dargestellt.“ ohne zweites Zitat. Zahl bleibt, weil das Prüfkriterium sie braucht. |
| F8 | 3.2.1 Absatz 16 Satz 1: „Gelöst wird je Liefertag ein eigenes Problem, sodass kein Ladezustand in den Folgetag übergeht und die Tage untereinander vergleichbar bleiben.“ | 3.2.2 Bilanzabsatz: „Anfang und Ende eines Tages tragen denselben Ladezustand, damit kein Tag mit eingelagerter Energie endet und die Tage untereinander vergleichbar bleiben.“ | In 3.2.1 kürzen auf „Gelöst wird je Liefertag ein eigenes Problem.“, die Begründung steht bei der Bilanz. |
| F9 | Anforderung A8 Satz 2: „Gegenstand der Beschaffung ist nicht das einzelne Gebot, sondern ein Verbund von Geboten, der den Engpass entlastet und bilanziell ausgeglichen ist.“ | 3.1.2 Zuschlag: „Bezuschlagt wird kein einzelnes Gebot, sondern ein Verbund aus Geboten beider Richtungen, denn die Maßnahme muss sich bilanziell ausgleichen.“ | In A8 streichen, der Verbund gehört sachlich nicht zur Umsetzbarkeit. Alternativ zu A3 verschieben. |
| F10 | 3.1.2 Präqualifikation: „Die Sensitivität des Standorts, also die Wirkung einer Leistungsänderung an diesem Knoten auf das Betriebsmittel, …“ | 3.1.2 Zuschlag: „Für den Zuschlag vergleichen die ÜNB jedes Gebot nach seiner Wirkung, also nach der Sensitivität des Netzknotens, …“ | Im Zuschlagsabsatz „also nach der Sensitivität des Netzknotens“ streichen. |
| F11 | 3.2.2 Bilanzabsatz: „Auf jeder Seite teilen sich der Handel, die aFRR, die kurative Reservierung und die auf beiden Seiten stehende FCR die Anschlussleistung. Eine kurativ reservierte Leistung steht deshalb keinem anderen Markt zur Verfügung.“ | 3.2.3 Kurative Reservierung: „Die Reservierung tritt in dieselbe Leistungsschranke wie die FCR und die aFRR und bindet darüber hinaus ein Ladezustandsband, das den Abruf über die Bindungsdauer deckt.“ | In 3.2.3 kürzen auf „Die Reservierung bindet ein Ladezustandsband, das den Abruf über die Bindungsdauer deckt.“ |
| F12 | 3.2.4 erste Iteration: „… genügen 84 bis 167 Läufe je Tag, im Mittel rund 130.“ | 3.2.4 Schleifen: „Beide Iterationen zusammen verlangen je Tag einige hundert Läufe.“ Dazu 3.2.2: „weil die Preissuche das Tagesmodell einige hundert Mal je Tag löst“ | Den Satz bei den Schleifen streichen. Der Satz in 3.2.2 bleibt, weil er die Degradationsvereinfachung begründet. |
| F13 | 3.2.4 Satz 3: „Ein Lauf löst dabei stets den ganzen Tag mit allen 24 Stunden und beiden Richtungen zugleich, weil die Stunden über den Ladezustand zusammenhängen.“ | 3.2.4 zweite Iteration: „Eine Suche je Stunde führt hier nicht zum Ziel, weil die Stunden über den Ladezustand zusammenhängen.“ | In der zweiten Iteration kürzen auf „Eine Suche je Stunde führt hier nicht zum Ziel.“ |
| F14 | 3.2.3 Kurative Reservierung Satz 1: „Die Zielfunktion trägt für die kurative Reservierung den Erlös aus vorgegebenem Preis mal reservierter Leistung.“ | Satz 3: „Anders als die übrigen Märkte trägt die kurative Reservierung keinen beobachteten Preis, sondern einen vorgegebenen, und sie ist eine Variable je Viertelstunde und Richtung.“ | Satz 3 kürzen auf „Die reservierte Leistung ist eine Variable je Viertelstunde und Richtung.“ |
| F15 | 3.2 Einleitung Satz 2: „Ob sich eine systemweite Integration der kurativen Systemführung lohnt, hängt für den ÜNB davon ab, ob der Nutzen der höheren Vorauslastung die Kosten der Reservierung und ihrer Umsetzung übersteigt.“ | Satz 7: „Der Preis liefert die Kostenseite der Abwägung, der der ÜNB den Nutzen der höheren Vorauslastung gegenüberstellen kann.“ Dazu 1.2 Absatz 14 Satz 4 (Einsparung nicht Gegenstand). | Satz 1, 2 und 7 der Einleitung streichen, sie behandeln die ÜNB-Sicht, die nicht Gegenstand ist. Die Einleitung beginnt dann mit „Welchen Preis ein Akteur fordert, …“. |
| F16 | 3.2.1 Absatz 14 Satz 3: „Der ungebundene Fahrplan zeigt, wie die Anlage ohne kurative Reservierung vermarktet würde.“ | Satz 4: „Am ungebundenen Fahrplan lässt sich ablesen, was die Reservierung verdrängt.“ | Zu einem Satz: „Der ungebundene Fahrplan zeigt, wie die Anlage ohne kurative Reservierung vermarktet würde, und damit, was die Reservierung verdrängt.“ |
| F17 | 3.2.1 Absatz 15 Satz 3: „Alle Märkte entscheidet das Modell gemeinsam und mit vollständiger Preiskenntnis, …“ | 3.2.3 Absatz 24 Satz 6: „Das Modell setzt alle Märkte eines Liefertages gleichzeitig, und jeder trägt dabei seinen eigenen Produktzuschnitt, seinen Energievorhalt und seinen Preis.“ | In 3.2.3 kürzen auf „Jeder Markt trägt seinen eigenen Produktzuschnitt, seinen Energievorhalt und seinen Preis.“ |
| F18 | 3.2.3 IDC Satz 5: „Das Modell lässt nur Arbitrage zwischen Viertelstunden zu, während ein Betreiber dieselbe Viertelstunde mehrfach handeln und eine frühere Position … wieder glattstellen kann.“ | Satz 8: „Weil ein Betreiber dieselbe Viertelstunde mehrfach handeln kann, verbessert jede zusätzliche Handelsmöglichkeit den erzielbaren Preis, …“ | Satz 8 kürzen auf „Jede zusätzliche Handelsmöglichkeit verbessert den erzielbaren Preis, sodass der IDC insgesamt mehr trägt als ein einzelnes Geschäft zum Index.“ |
| F19 | 1.2 Absatz 14: „Der kurative Reservierungspreis misst damit die Opportunitätskosten der Bindung, also die Erlöse, die der Betreiber an den übrigen Märkten aufgibt.“ | 3.1.2 Absatz 6 Satz 1 bis 2: „Der Akteur nimmt die kurativ gebundene Leistung aus seiner übrigen Vermarktung heraus. Daraus entstehen die Opportunitätskosten, die der Akteur über den Preis ersetzt verlangt.“ | In 3.1.2 zu einem Satz: „Weil der Akteur die kurativ gebundene Leistung aus seiner übrigen Vermarktung herausnimmt, verlangt er die Opportunitätskosten über den Preis ersetzt.“ |
| F20 | 1.2 Absatz 14: „… über die Bindungsdauer …, also über den Zeitraum, für den die Zusage gilt“ | 3.1.2 Absatz 6 letzter Satz: „Die Bindungsdauer ist der Zeitraum, über den die Zusage nach dem Zuschlag gilt, und beträgt eine Zeitscheibe, also eine Stunde des Liefertages.“ | In 3.1.2 kürzen auf „Die Bindungsdauer beträgt eine Zeitscheibe, also eine Stunde des Liefertages.“ |
| F21 | Kapiteleinleitung 3: „Für BESS ist die Bemessung der Vergütung im Engpassmanagement jedoch nicht abschließend geklärt.“ | 3.2 Einleitung Satz 4: „Für die kurative Reservierung besteht kein Vergütungsrahmen, an dem sich ein Akteur ausrichten könnte.“ Dazu 2.3.3 Absatz 59. | Beide behalten, die Kapiteleinleitung nennt den Befund, 3.2 zieht die Folge. Kein Eingriff. |
| F22 | 2.3.4 Absatz 60: „… denn die mFRR bietet bei gleichem Produktschnitt den geringeren Leistungspreis.“ | 3.2.3 Absatz 24: „Die mFRR führt das Modell nicht, weil sie der aFRR im Produktschnitt gleicht und im Jahr 2025 den geringeren Leistungspreis erzielte, wie in Abschnitt 2.3.4 dargestellt.“ | In 3.2.3 kürzen auf „Die mFRR führt das Modell nicht, wie in Abschnitt 2.3.4 begründet.“ |
| F23 | 1.2 Absatz 13: „Das Jahr 2030 dient nicht als Eingangsgröße, sondern als Rahmen …“ | 3.2.1 Absatz 18: „Der Szenariorahmen 2030 ordnet die Untersuchung qualitativ ein und geht nicht als Eingangsgröße in das Modell [NEP].“ | In 3.2.1 belassen, weil dort die Quelle steht, in 1.2 belassen, weil dort die Begründung steht. Kein Eingriff. |
| F24 | 3.3.1 Absatz 44 Satz 3: „… des ungebundenen Fahrplans, also einer Zwischengröße des Modells.“ | Satz 5: „Der ungebundene Erlös ist eine Zwischengröße und kein Ergebnis der Arbeit.“ | Satz 5 und 6 zu einem Satz: „Weil der ungebundene Erlös kein Ergebnis der Arbeit ist, nennt die Validierung ihre Zahlen schon hier.“ |
| F25 | 3.2.4 Absatz 42 Satz 6: „Die Kopplung über den Ladezustand wiegt bei einem Energieinhalt je Leistung von 2,5 Stunden schwer, denn …“ | 3.2.4 Absatz 43: „Anders als Anlage 5 der Festlegung … bleibt die Anlage unter der kurativen Reservierung handlungsfähig, …“ | Keine Dopplung, nur Hinweis: Absatz 42 und 43 sind jetzt verbunden und tragen 12 Sätze. Mit F3, F4 und F6 sinkt die Zahl auf 10. |

Umgesetzt ohne Rückfrage, weil zwei Sätze desselben Absatzes dasselbe
sagten: Präqualifikation in 3.1.2 (zwei Sätze zu einem), A8 Satz 1 und 2
(These und Erläuterung zu einem Satz), A7 Satz 1 und 2 (These und Begründung
zu einem Satz).

---

## E Reihenfolge der Umsetzung, Vorschlag

1. A1 und A4 (Platzierung), dann Build und Seitenzahlen messen.
2. Sachfehler C3.15 und D3.17.
3. Kapitel 3: D2 und D3 in einem Skript je Unterabschnitt, danach D1.
4. Kapitel 2: C3 und C2, danach C1.
5. Kapitel 1: B2.1, B3.1, B3.4, B3.12, dann B1, Ziel 5 Seiten (A2).
6. Kapitelübergreifende Abgleiche B3.6 bis B3.11, C4.
7. Fremdleser-Prüfung je geändertem Abschnitt, Protokoll, Commit je Kapitel.

---

## G Offene Punkte aus den Kommentaren von chapter_3.tex

Aufgenommen am 17.09.2026, als die Kapiteldatei von Kommentaren befreit wurde.
Die Spalte Quelle nennt die Zeile im Stand vom 17.09.2026, der vollstaendig in
`archiv/KOMMENTARBESTAND_KAP3.md` steht. Nichts davon ist umgesetzt.

| Nr. | Befund | Quelle | Stand |
|---|---|---|---|
| G1 | Der Unterabschnitt Abgleich bestehender Marktdesignansätze ist am 08.09.2026 geparkt, sein Ort ist nicht entschieden. In Betracht kommen 3.1.2, 3.3.1 und Kapitel 5. Der vom Verfasser bestätigte Gedanke, der kapazitätsbasierte Redispatch beschaffe im Kern dieselbe Größe wie eine kurative Vorhaltung und unterscheide sich nur in Auslöser und Reaktionszeit, steht bis heute in keinem Absatz. | Z367 bis Z551 | offen, Ort zu entscheiden |
| G2 | Die Belege ehrhart_analysis_2025, horsch_role_2017 und einsiedler_analysis_2025 sind ungeprüft, die Volltexte ließen sich nicht öffnen. Die Aussage, der Mechanismus bemesse die bereitgehaltene Kapazität statt des Eingriffs, stammt aus einem eigenen Kommentar und nicht aus der Quelle. | Z529 | vor Abgabe bestätigen oder zurücknehmen |
| G3 | Vormerkung des Verfassers vom 09.09.2026: Der Bestand an BESS wächst, während sich der Bedarf an Regelleistung aus der Dimensionierung des Systems ergibt und nicht mitwächst, sodass die Ausschließlichkeit der kurativen Zusage die Regelleistung weniger verdrängt. Das Argument ist nicht geschrieben. | Z1477 | offen, Ort zu entscheiden |
| G4 | Vormerkung vom 11.09.2026: der Unterschied zur Anlage 5 der Festlegung, die von gesperrter Leistung ausgeht, während das Produkt allein die zugesagte Leistung sperrt. Nach Entscheidung 1 gehört der Vergleich nach Kapitel 5. | Z5264 | offen für Kapitel 5 |
| G5 | Die Degradationskosten von 8 Euro je Megawattstunde Durchsatz stammen aus main.py Zeile 401 und tragen dort keine Quelle. Der Code nennt die Spanne 3 bis 20 Euro je Megawattstunde, die Sensitivität sensi2_deg fährt 0 bis 18. Ob juelch_comparison_2016, garttan_battery_2025 oder rystad_energy_renewables__power_analytics_energy_2026 die 8 Euro trägt, ist ungeprüft. | Z3247, Z3347 | offen |
| G6 | Der Aufschlag am IDC von drei Prozent im Verkauf und im Kauf stammt nach MODELL.md aus dem Battery-Revenue-Index von energy-charts, ein Eintrag dafür fehlt. Der Verfasser hat am 12.09.2026 entschieden, dass ein Beleg nicht nötig ist. | Z3873 | entschieden, Eintrag fehlt nur für den Fall eines Zitats |
| G7 | Der Code setzt die ausgeschriebene aFRR-Menge auf 2000 MW, woraus der Anteil von rund vier Prozent folgt. Die Zahl ist als Eingangsgröße zu nennen und zu belegen. | Z4121 | offen |
| G8 | Der Code verlangt das Ladezustandsband der Regelleistung nur am Beginn jeder Vier-Stunden-Zeitscheibe, das kurative Band in jeder Viertelstunde. Entweder nennt der Text diese Vereinfachung, oder der Code zieht nach. | Z3970 | offen |
| G9 | Die Monotonie des Füllgrads über dem Preis ist nur für den Preis einer Stunde bei festen übrigen Preisen gesichert. Die erste Iteration hebt den einheitlichen Preis aller Stunden zugleich, sodass eine Stunde Leistung an eine Nachbarstunde verlieren kann. Der Text sagt deshalb setzt voraus und nicht gilt. Die Einschränkung gehört mit der Reihenfolge des Abstiegs und dem koordinatenweisen Minimum nach Kapitel 5. | Z4504 | offen für Kapitel 5 |
| G10 | Die Laufzahlen 84 bis 167 stammen nach MODELL.md aus den Schwellen der 20 Sensitivitätstage und nicht aus dem Jahr 2025. Die Rechenzeit von früher 17 bis 44 Sekunden je Tag ist nach dem Umbau der zweiten Iteration nicht nachgemessen, deshalb steht im Text nur die Laufzahl. | Z4509, Z5155 | offen, Nachmessung möglich |
| G11 | Die Überschrift von 3.2 lautet nach CLAUDE.md Modellierungsansatz und Systemgrenzen und überschneidet sich mit dem ersten Unterabschnitt. Alternative ist Modellierung des Speicherbetriebs. | Z2290 | offen |
| G12 | Die Methodikveröffentlichung der ISEA Battery Charts fehlt als Eintrag. Ohne sie stützt sich die Beschreibung des Rolling-Intrinsic-Verfahrens allein auf semmelmann_algorithm_2024 und den Quelltext. Offen ist außerdem, ob ergänzend Grenzfallprüfungen am eigenen Modell aufgenommen werden, nämlich Wirkungsgrad eins, Vorhalteleistung null und konstanter Preis. | Z5529 | offen |
| G13 | Vor Abgabe ist zu prüfen, ob eine Mitteilung der Beschlusskammer zu Batteriespeichern ergangen ist, denn dieser Punkt trägt die Forschungslücke. Recherchestand August 2026 ist, dass keine vorliegt. | Z6072 | offen, vor Abgabe |
| G14 | Der Verweis auf sec:model_critique am Satz zum Optionswert ist nach Stilregel 15 ein Grenzfall, Befund S7. Zu prüfen, ob sich die Folge ohne Abschnittsnummer sagen lässt. | Z5423 | offen |
