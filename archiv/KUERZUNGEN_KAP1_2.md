# Kürzungsliste Kapitel 1 und 2

Stand 11.09.2026, Arbeitsdokument zum gemeinsamen Durchgehen. Nichts davon ist
umgesetzt. Zeilenangaben beziehen sich auf die Fassung 74a9d8d, und zwar
**E** auf [chapter_1.tex](chapters/chapter_1.tex), **G** auf
[chapter_2.tex](chapters/chapter_2.tex) und **Anh.** auf
[attachment.tex](extras/attachment.tex). Kommentarzeilen sind nicht gezählt.

Formulierungen in dieser Liste sind Skizzen der Richtung und keine Fassungen.
Jeder Satz, der danach in eine Kapiteldatei geht, läuft wie gewohnt über A, B
und C.

---

## Ausgangslage

| | Seiten laut Build | Ziel |
|---|---|---|
| Kapitel 1 | 1 bis 5, also 5 | 5 |
| Kapitel 2 | 6 bis 34, also 29 | 25 |
| Kapitel 3 | 35 bis etwa 51, also rund 17 | 14 |

Damit die Ergebnisse vor Seite 50 beginnen, fehlen rund sieben Seiten, davon
mindestens vier in Kapitel 2. Als Faustwert trägt eine Seite im Satzspiegel rund
16 Sätze. Eine Tabelle mit fünf Zeilen kostet etwa eine Drittelseite, eine
Abbildung in Textbreite eine halbe bis zwei Drittel.

## Übersicht, sortiert nach Ersparnis

| ID | Maßnahme | Ersparnis in Seiten | Eingriff |
|---|---|---|---|
| A1 | Weber-Ansatz in 2.3.2 auf den Kern kürzen, Rest in Anhang A | 2,5 bis 3 | groß |
| A2 | Thermische Herleitung der Überlastdauer in 2.1.2 in einen Anhang B | 1,5 bis 1,8 | groß |
| Q | Mehrfach gesagte Aussagen je einmal stehen lassen, 20 Stellen | 1 bis 1,5 | klein je Stelle |
| G | Satzweise Straffung Kapitel 2 außerhalb der A-Blöcke | 1,5 bis 2 | klein je Stelle |
| E | Satzweise Straffung Kapitel 1 | 1 bis 1,2 | klein je Stelle |
| A3 | Regelleistung an einer Stelle und mit einer Tabelle | 0,6 bis 0,8 | mittel |
| A5 | Rechtsrahmen 2.1.5 straffen | 0,5 bis 0,7 | mittel |
| A4 | Fließtext in 2.3.1 wiederholt die Tabelle | 0,5 | klein |
| A6 | Herausforderungen 2.1.4 straffen | 0,3 bis 0,4 | klein |
| A7 | Abbildung 1.2 zum Netzentwicklungsplan weglassen | 0,4 | klein, optional |

Q, G und E überschneiden sich teilweise, weil eine Doppelung zugleich ein
satzweiser Befund ist. Realistisch sind ohne A2 rund sechs Seiten, mit A2 rund
acht.

---

## Teil A, Abschnitte und Anhang

### A1 Abschnitt 2.3.2, Bemessung entgangener Erlösmöglichkeiten (S. 25 bis 29)

Der Abschnitt umfasst rund vier Seiten mit zwei Tabellen, einer Abbildung, drei
Gleichungen und einem vollständig durchgerechneten Beispiel. Anhang A rechnet
dasselbe Beispiel mit denselben Zahlen noch einmal und ausführlicher.

**Was im Hauptteil bleiben muss**, weil 2.3.3, das Zwischenfazit und 3.2.6
darauf aufbauen:

- der Optionsgedanke, G 493 bis 495
- Call und Put, entweder als Tabelle `tab:optionsarten` oder in einem Satz aus
  G 514, 515 und 518
- zwei Seiten beim Speicher mit je einem Grenzpreis als Basispreis, die aus der
  geordneten Reihe der IDA-1 und den Volllaststunden folgen, ein Satz statt G 520
  und 526 bis 529
- erwartetes Preisniveau und Volatilitätsmaß, ein bis zwei Sätze aus G 525 und
  530
- innerer Wert und Zeitwert sowie das nicht auf die Restzeit skalierte
  Volatilitätsmaß, G 534, 535 und 579
- die Zuordnung der Optionsart nach dem Day-Ahead-Preis in einem Satz, dazu
  G 577 und 578, weil die Marktstruktur dahinter entfallen ist
- die Unabhängigkeit der Intervalle, G 516
- warum überhaupt ein Optionsansatz, G 585 und 586, auch ohne Abbildung sagbar
- die Aggregation über die gesperrte Leistung gegen den Werteverbrauch, G 607 als
  ein Satz

**Was in den Anhang gehen kann**

| Stelle | Inhalt | Wohin | Bemerkung |
|---|---|---|---|
| G 595 bis 605 und 608 | Berechnungsbeispiel, zwölf Sätze | entfällt, steht in Anh. A.1 und A.3 | reine Doppelung, ein Verweissatz bleibt |
| G 526 bis 529 | iterative Grenzpreisbestimmung, vier Sätze | Anh. A.1 | dort vollständig |
| `tab:weber_symbole` und Gl. `eq:weber_d` bis `eq:weber_put` | Formelzeichen und Bewertungsformeln | Anh. A.3 | Marke `tab:weber_symbole` bleibt, CLAUDE.md Abschnitt 10 verweist darauf. Anh. Z. 95 sagt „abweichend von den Gleichungen des Grundlagenkapitels“ und wäre anzupassen |
| `fig:weber_optionswert` | Optionswert über dem erwarteten Preis | Anh. A.3 | zeigt genau die Viertelstunde des Beispiels |
| G 521 bis 523 | Normalverteilung, BDEW-Leitfaden, SDAC als Index | Einleitung Anh. A | Herkunft des Wortes modifiziert |
| G 531 bis 533 | Abweichungen zwischen Weber und Festlegung beim Volatilitätsmaß | Anh. A.3 | |
| G 574 bis 576 | SDAC-Erklärung, Seitenzuordnung, Vereinfachung | Anh. A.3 | ein Satz bleibt im Hauptteil |
| G 580 bis 582 | Schätzung des erwarteten Preises vor 15.15 Uhr | entfällt, steht ausführlich in Anh. A.5 | |

**Ersparnis** rund 2,5 bis 3 Seiten. **Nebeneffekt** Die offene Frage Basispreis
oder Strikepreis nach CLAUDE.md Abschnitt 5 wird kleiner, weil die meisten
Fundstellen von Basispreis in den Anhang wandern, der durchgehend Strikepreis
führt. **Risiko** Wer den Anhang nicht liest, muss 2.3.3 und 3.2.6 trotzdem
verstehen, deshalb bleibt der Kern oben vollständig. **Variante A1b** Die
Abbildung bleibt im Hauptteil, weil sie anschaulich ist, alles andere wandert.
Ersparnis dann rund 2 Seiten.

### A2 Abschnitt 2.1.2, Thermik der zulässigen Überlastdauer (G 133 bis 172)

Bestand sind Wärmebilanz mit Variablenliste, zwei Sätze zu Vereinfachungen,
Kühlung und Freileitungsmonitoring, Joule-Gleichung mit Skineffekt, das
Zehn-Prozent-Beispiel, vier Sätze zum Temperaturverlauf, die Abbildung
`fig:tatl_berechnung` und sechs Sätze zu Transformatoren, zusammen rund
zweieinhalb Seiten.

**Was die Arbeit davon braucht.** Die Dauer der TATL ist keine Konstante des
Betriebsmittels, sondern folgt aus der Wärmebilanz und hängt von Vorbelastung und
Wetter ab. Daraus folgt G 174 bis 178, dass der Akteur seine Reaktionszeit nicht
wählt, und daraus A1 im Katalog. Das Modell verwendet keine der Gleichungen.

**Vorschlag.** Drei bis vier Sätze im Hauptteil. Die Dauer folgt aus der
Wärmebilanz, sie hängt von Vorbelastung und Wetter ab, bei Transformatoren ist
sie länger, begrenzt aber über die Alterung auch die Häufigkeit, und maßgeblich
ist das Minimum über die Strecke. Dazu ein Verweis auf einen neuen Anhang B,
etwa „Zulässige Überlastdauer von Freileitung und Transformator“, mit beiden
Gleichungen, der Abbildung und dem Transformatorabsatz.

**Ersparnis** 1,5 bis 1,8 Seiten. **Risiko** Am IAEW gehört die Physik zu den
erwarteten Grundlagen, und die Abbildung ist eigene Arbeit. **Variante A2b**
Abbildung und Wärmebilanz bleiben, es entfallen die Joule-Gleichung, die
Vereinfachungssätze G 141, 142 und 152 und der Transformatorabsatz bis auf einen
Satz. Ersparnis dann rund 0,8 Seiten.

### A3 Regelleistung an zwei Stellen, 2.2.3 und 2.3.4

| Aussage | 2.2.3 | 2.3.4 |
|---|---|---|
| Zuschlag verpflichtet zur Bereithaltung über die Erbringungsperiode | G 391 | G 636, fast wörtlich |
| Leistung und Arbeit getrennt, FCR nur Leistung | G 393 | G 637 |
| Präqualifikation legt den Arbeitsbereich fest | G 392 | G 646 |
| Handelsschluss 8 und 9 Uhr | `tab:regelleistung` | `tab:balancing_remuneration` |
| FCR-Bedarf 564 MW | G 395 | G 681 in 2.3.5 |

**Vorschlag.** Beide Tabellen zu einer zusammenführen, mit den Spalten Produkt,
Richtung, Produktschnitt, Beschaffung, Bemessung und Aktivierung. 2.2.3 trägt dann
nur die Einordnung und den Bedarf, 2.3.4 nur Vergütung, Anreizkomponente, die
Folge für den Ladezustand und die drei Befunde. Alternativ geht 2.3.4 ganz in
2.2.3 auf. **Ersparnis** 0,6 bis 0,8 Seiten.

### A4 Abschnitt 2.3.1, der Text wiederholt die Tabelle

- G 465 bis 471 beschreiben die fünf Tabellenzeilen noch einmal in sieben
  Sätzen. Es bleibt allein G 467 zum Einsatzpreis des Speichers, weil er über
  die Tabelle hinausgeht.
- G 436 zur Überführung des Einspeisemanagements 2021 trägt für die Arbeit
  nichts.
- G 473 bis 478 in sechs Sätzen lassen sich auf zwei bringen. Konventionelle
  Kraftwerke fallen unter die Nummern 1 bis 4, Wind und Photovoltaik unter
  Nummer 5, PSKW und BESS unter 1 bis 3, und damit führt das Regime zwei
  Bemessungslogiken. G 474 wiederholt die Liste aus `tab:akteursvergleich`.

**Ersparnis** rund eine halbe Seite.

### A5 Abschnitt 2.1.5, Rechtlicher Rahmen

- G 288 bis 292 zur SOGL und zum Normalzustand doppeln das Vier-Zustands-Modell
  in 2.1.1 (Q13). Die Aussage sollte an einer Stelle stehen.
- § 13c in G 301 bis 305 braucht zwei statt fünf Sätze.
- § 17 Abs. 2b in G 308 bis 314 braucht drei bis vier statt sieben Sätze. G 313
  und G 314 tragen die beiden Argumente und bleiben.
- § 13k in G 315 bis 318 braucht zwei bis drei statt vier Sätze. Der Kern bleibt,
  weil CLAUDE.md Abschnitt 8 § 13k als Vorlage nennt.
- Im Schluss G 319 bis 321 sagen G 320 und G 321 fast dasselbe.

**Ersparnis** 0,5 bis 0,7 Seiten.

### A6 Abschnitt 2.1.4, Herausforderungen der Umsetzung

- G 255 bis 262 umfassen acht Sätze. G 258 zum Freileitungsmonitoring doppelt
  G 145 (Q10), G 259 und 260 doppeln G 172 (Q11). Übrig bleiben vier Sätze.
- G 268 ist ein struktureller Vorverweis auf den Ausblick nach Stilregel 9.
- G 269 bis 277 bleiben, weil die Bemessung gegen ein Spektrum von Netzzuständen
  und die Frage nach dem Preis später gebraucht werden.
- Alternativ geht 2.1.4 in 2.1.1 auf. Chapter 6 Zeile 87 verweist auf
  `sec:challenges`, die Marke wäre mitzuziehen.

**Ersparnis** 0,3 bis 0,4 Seiten.

### A7 Abbildung 1.2, Engpassmanagement nach Netzentwicklungsplan

Die Zahlen stehen vollständig in E 40 und 42. Ohne Abbildung spart das rund 0,4
Seiten, die Motivation wird allerdings weniger anschaulich. Optional.

---

## Teil Q, Doppelungen, je einmal stehen lassen

| ID | Aussage | Stellen | Vorschlag |
|---|---|---|---|
| Q1 | Präventiv wird die Vorauslastung so begrenzt, dass die Belastung nach einem Ausfall unter der PATL bleibt | E 69 bis 70, G 45, G 55, G 63 | G 55 streichen, denn es ist G 45. G 63 auf „diese Marge verursacht den Eingriff“ kürzen |
| Q2 | Nach der letzten Netzsicherheitsrechnung bleibt ein Handelsfenster, das keine Rechnung mehr erfasst | E 64 bis 67, G 65 bis 66, G 72 bis 76, G 80 bis 81, G 379 | G 379 streichen, G 73 kürzen, denn mahgoub steht schon in E 62 |
| Q3 | Volumen und Kosten entwickeln sich nicht proportional | E 49, G 70 | eine Stelle |
| Q4 | Selbstdispatch, zonaler Preis, nachgelagerte Korrektur, Volumen als Folge des Marktdesigns | E 16 bis 21, G 338, G 341 bis 343 | G 343 und E 21 fast wörtlich gleich. G 341 bis 343 auf einen Satz mit Beleg |
| Q5 | Definition des Redispatch | E 87, G 13 | eine Stelle |
| Q6 | InnoSys 2030 hat den Maßnahmenraum systematisiert | E 85, G 20 | eine Stelle, naheliegend G 20 |
| Q7 | Die kurative Vorhaltung gehört zur Betriebsführung | E 86, G 387, Einleitung Kap. 3 | E 86 streichen |
| Q8 | Regelleistung vergütet die Bereitstellung, das Engpassmanagement den Eingriff | E 91 bis 92, G 386, G 420 bis 424, G 651, G 690 | G 424 streichen, denn es ist G 690 |
| Q9 | Der Zeitwert ist vom Anweisungszeitpunkt unabhängig und trifft den Speicher stärker | G 615, G 617, G 692 mit fünf Sätzen, Anh. A.5 | G 692 im Zwischenfazit auf einen Satz |
| Q10 | Das Freileitungsmonitoring passt den Dauergrenzwert an die Witterung an | G 145, G 258 | eine Stelle |
| Q11 | Maßgeblich ist das Minimum über alle Betriebsmittel der Strecke, der nutzbare Grenzwert liegt unter dem thermischen | G 172, G 259 bis 260 | eine Stelle |
| Q12 | Der Akteur muss auf eine feste Reaktionszeit festgelegt sein, weil sie in die Einsatzplanung eingeht | G 178, G 182, Kap. 3 A1 | G 178 und G 182 zu einem Satz |
| Q13 | Kurative Maßnahmen sind Entlastungsmaßnahmen, das Netz bleibt im Normalzustand | G 32 bis 35, G 290 bis 292 | eine Stelle |
| Q14 | Gestufte Betriebsplanung und Rechenläufe am Vortag und untertägig | E 64, G 56 bis 58, G 374 bis 378 | G 374 bis 378 als Hauptstelle, G 56 bis 58 auf einen Satz |
| Q15 | PTDF- und LODF-Sensitivitäten | G 121, Kap. 3 A3 | eine Stelle, Kapitel 3 liegt bei der anderen Sitzung |
| Q16 | Der Mechanismus setzt an Eigenschaften an und nicht an der Technologie | G 191 bis 192, Kap. 3 A5 | wie Q15 |
| Q17 | Die Vorhaltung reserviert Leistung, der Redispatch löst Energie aus | G 630, Kap. 3 A4 | wie Q15 |
| Q18 | FCR-Bedarf 564 MW | G 395, G 681 | in G 681 allein die 810 MW |
| Q19 | Die Maßnahme wirkt nur im Fehlerfall, deshalb fällt weniger Volumen an | E 75, G 82 bis 83 | eine Stelle |
| Q20 | Die Leistungsscheibe am Regelleistungsmarkt steht nicht für Redispatch zur Verfügung | G 683, Anh. Z. 205 | darf bleiben, der Anhang braucht sie für die Rechnung |

---

## Teil E, Kapitel 1 satzweise

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| E1 | 5, 6 | Zwei Sätze für eine Aussage | „Mit einem Anteil von 58,8 % … verändert sich nicht allein …“ | −1 |
| E2 | 12 | Aussage ohne eigenes Gewicht | in 13 aufnehmen, „Während der Netzausbau an dieser Achse ansetzt, wird …“ | −1 |
| E3 | 16 bis 18 | 17 ist ein Halbsatz, 18 folgt aus 16 | „Im Selbstdispatch-Modell, dem der deutsche Strommarkt folgt, …“, 18 streichen | −2 |
| E4 | 20, 21 | Folge und Schluss trennbar nur künstlich | zu einem Satz | −1 |
| E5 | 23 | Überleitung, die 24 selbst leistet | streichen | −1 |
| E6 | 29, 30 | Monat und Ursache getrennt | „Auf diesen Monat, geprägt von einer Windfront, entfielen …“ | −1 |
| E7 | 27, 48 bis 50 | 48 bis 50 wiederholen 27 bis 30 und 13 als Rückschau | entweder 48 bis 50 streichen und die Relevanz an 27 hängen, oder 27 streichen | −2 |
| E8 | 40, 42, 43, 45, 46 | 13 TWh stehen zweimal, 43 kündigt 44 nur an, 45 und 46 bilden einen Gedanken | Doppelzahl tilgen, 43 streichen, 45 und 46 verbinden | −2 |
| E9 | 66 | wiederholt 19, dass der zonale Preis die Netzbelastung nicht zeigt | streichen | −1 |
| E10 | 69 bis 71, 74 bis 75 | 70 hat kein eigenes Gewicht, 74 und 75 sind ein Gedanke | 70 in 69, 74 und 75 verbinden | −2 |
| E11 | 85 bis 93 | Neun Sätze nehmen den Befund von Kapitel 2 vorweg, Q5 bis Q8 | auf drei bis vier Sätze, nämlich Anreiz aus Vergütung, zwei Logiken, offene Frage | −5 |
| E12 | 95 bis 97 | 97 ist Methodenbegründung und gehört nach 3.2.1, siehe P6 | 97 verlagern | −1 |
| E13 | 101, 102 | 102 zählt nicht modellierte Einflüsse auf, die 3.2.6 trägt | auf einen Satz oder nach 3.2.6 | −1 |
| E14 | 105 bis 126 | Kapitelüberblick mit bis zu drei Sätzen je Kapitel, der zu Kapitel 3 veraltet, siehe P1 | je Kapitel ein bis zwei Sätze | −2 |

Zusammen rund 23 Sätze, also rund 1,2 Seiten, mit A7 rund 1,6.

---

## Teil G, Kapitel 2 satzweise, ohne die Blöcke aus Teil A

**Kapiteleinleitung und 2.1**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G1 | 4 | Rahmensatz ohne Aussage | streichen | −1 |
| G2 | 14 | struktureller Vorverweis nach Stilregel 9 | streichen | −1 |
| G3 | 15, 16 | 16 ist ein Nachtrag zu 15 | verbinden | −1 |
| G4 | 18 | Brückensatz | streichen | −1 |
| G5 | 20, 21 | InnoSys und Anschlussarbeiten, Q6 | ein Satz | −1 |
| G6 | 22 | Abschnittsankündigung nach Stilregel 9 | streichen | −1 |

**2.1.1 Präventive und kurative Systemführung**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G7 | 30, 31 | Not- und Blackoutzustand werden für das Argument nicht gebraucht, 27 nennt sie bereits | streichen | −2 |
| G8 | 32, 33 | Regel und Anwendung, ein Gedanke | verbinden | −1 |
| G9 | 42 | Hinweis, dass die Verordnung PATL und TATL nicht so nennt | Fußnote oder streichen. Vermutlich aus der Quellenprüfung, vorher im Protokoll prüfen | −1 |
| G10 | 45, 46, 55 | Q1 | 55 streichen | −1 |
| G11 | 59, 60 | Vorteil und Optimalfall, ein Gedanke | verbinden | −1 |
| G12 | 72 bis 76 | fünf Sätze, 73 doppelt E 62 | auf drei | −2 |
| G13 | 87 | struktureller Vorverweis auf 2.1.2 und 2.1.4 | streichen | −1 |
| G14 | 89 | zweite Hälfte ist ein Vorverweis auf 2.3.1 und 2.4 | Hälfte streichen | 0 |
| G15 | 94 | Verweis auf `sec:sensitivities` in Kapitel 4, Vorverweis und im Build „??“ | Verweis streichen | 0 |

**2.1.2 Prozessablauf und Zeitanforderungen, ohne A2**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G16 | 100, 101 | 101 ist ein Nachtrag | verbinden | −1 |
| G17 | 113, 114 und 117, 118 | jeweils ein Schritt in zwei Sätzen | je verbinden | −2 |
| G18 | 120, 121 | Grundlagen der Netzsicherheitsrechnung, später nicht gebraucht, 121 ist Q15 | auf einen Satz | −1 |
| G19 | 128, 129 | ein Gedanke | verbinden | −1 |
| G20 | 178, 182 | Q12 | verbinden | −1 |

**2.1.3 Technologien kurativer Akteure**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G21 | 189, 190 | Frage in zwei Sätzen | verbinden | −1 |
| G22 | 193 bis 196 | vier Sätze kündigen die Tabellenspalten an | auf zwei | −2 |
| G23 | 201 bis 206 | sechs Sätze zu konventionellen Kraftwerken, 203 wiederholt die Tabelle | auf drei | −3 |
| G24 | 238 bis 249 | zwölf Sätze zum BESS. 240 wiederholt 202 und 207, 244 zur Leistungselektronik ist entbehrlich, 245 bis 248 lassen sich auf drei bringen | auf acht | −4 |

**2.2 Marktrahmen und Systemdienstleistungen**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G25 | 326 | Abschnittsankündigung | streichen | −1 |
| G26 | 331, 332 | Terminologie Self-Dispatch und Scheduling Agents | Fußnote oder Halbsatz | −1 |
| G27 | 341 bis 343 | Q4 | auf einen Satz | −2 |
| G28 | 345 | zweite Hälfte verweist auf einen Abgleich, den es nicht mehr gibt, siehe P2 | Hälfte streichen | 0 |
| G29 | 359, 360 | Terminmarkt und OTC in zwei Sätzen | ein Satz | −1 |
| G30 | 364, 368 | Erklärung von pay-as-cleared ausführlich, 368 für die Arbeit ohne Folge | 364 kürzen, 368 streichen | −1 |
| G31 | 374 bis 379 | Q2 und Q14 | auf drei Sätze | −2 |
| G32 | 383 bis 385 | Spannungshaltung und Versorgungswiederaufbau in drei Sätzen | ein Satz | −2 |
| G33 | 420 bis 424 | fünf Sätze, 424 ist Q8 | auf zwei | −3 |

**2.3 Vergütungslogiken, ohne A1, A3 und A4**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G34 | 430 | Abschnittsankündigung | streichen | −1 |
| G35 | 486, 487 | Rechenregel in zwei Sätzen, siehe P9 | ein Satz | −1 |
| G36 | 613 | ein Absatz mit elf Sätzen. Der Wortwechsel im Konsultationsverfahren braucht zwei statt drei Sätze. Ob der Satz zur verschobenen statt entfallenen Einspeisung gebraucht wird, ist zu prüfen | auf acht bis neun | −2 |
| G37 | 617 bis 622 | Anreizwirkung in sechs Sätzen, 618 wiederholt den Selbstdispatch | auf vier | −2 |
| G38 | 629 bis 631 | 630 ist Q17, 631 ist ein Brückensatz | 631 streichen | −1 |
| G39 | 681, 683 | 564 MW ist Q18, der Präqualifikationssatz in 683 doppelt G 392 und G 646 | kürzen | −1 |

**2.4 Zwischenfazit**

| ID | Stelle | Befund | Vorschlag | Sätze |
|---|---|---|---|---|
| G40 | 692 | Q9, fünf Sätze wiederholen 2.3.3 | auf einen bis zwei | −3 |

Zusammen rund 50 Sätze, also rund drei Seiten. Ein Teil davon ist in Teil Q
bereits mitgezählt.

---

## Teil P, präziser formulieren und Befunde

| ID | Stelle | Befund |
|---|---|---|
| P1 | E 120 bis 122 | Der Überblick zu Kapitel 3 ist veraltet. Er nennt eine Einordnung bestehender Marktdesignansätze, die entfallen ist, und eine Verifikation gegen den Erlösindex, obwohl 3.3 ausdrücklich keine Verifikation beansprucht. Die Suche nach dem Reservierungspreis aus 3.2.5 fehlt |
| P2 | G 345 | Der Verweis auf `sec:market_design_comparison` kündigt einen Abgleich an, den Kapitel 3 seit dem 08.09.2026 nicht mehr führt |
| P3 | G 94 | Verweis auf Kapitel 4, das in `main.tex` auskommentiert ist, im PDF steht „??“ |
| P4 | G 613 | Der Umschlagpunkt zwischen vier und sechs Volllaststunden ist nach der Prüfung vom 07.09.2026 eine eigene Deutung, der Text schreibt ihn dem Berechnungsbeispiel zu |
| P5 | G 507, 509, 515, 520, 525, 526 und `tab:weber_symbole` | Basispreis und Strikepreis, offen nach CLAUDE.md Abschnitt 5. Mit A1 wandern die meisten Fundstellen in den Anhang |
| P6 | E 95 bis 96 | „2030-Szenario“ und „Preiszeitreihen des Jahres 2025“. Nach Entscheidung 10 ist 2030 ein qualitativer Rahmen und ausgewertet wird das vierte Quartal 2025 |
| P7 | G 130 bis 131 | „ein aufeinander abgestimmtes Paar von Zusagen“, während der Verfasser in 3.1.1 A8 bewusst „Verbund von Geboten“ gewählt hat |
| P8 | E 99 | „Er bemisst die entgangenen Erlösmöglichkeiten“ benutzt den Begriff aus § 13a Nr. 3 und legt nahe, der Preis folge der Bemessung aus 2.3.2. Präziser wäre Opportunitätskosten der Bindung |
| P9 | G 486 bis 487 | Die Rechenregel sollte in derselben Form stehen wie Entscheidung 11, also Erzeugungsauslagen zuzüglich des Maximums aus Werteverbrauch und Opportunität, sonst liest sie sich gegen Anh. Z. 185 |
| P10 | G 14, 22, 87, 89, 94, 268, 326, 345, 430 | strukturelle Vor- und Rückverweise nach Stilregel 9, unabhängig von der Seitenfrage zu beheben |

---

## Vorschlag für die Reihenfolge

1. **A1**, weil es der größte Hebel ist und den Anhang mitbetrifft.
2. **A2**, eine Grundsatzfrage, ob die Physik im Hauptteil bleiben soll.
3. **A3** und die **Q-Liste**, weil sie die Stellen festlegen, an denen eine
   Aussage bleibt.
4. **E** und **G** satzweise.
5. **P**, teils unabhängig von der Seitenfrage.
