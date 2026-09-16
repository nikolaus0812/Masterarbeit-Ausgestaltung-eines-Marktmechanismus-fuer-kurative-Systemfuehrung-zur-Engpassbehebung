# Änderungsliste Kapitel 1 und 2

Stand 14.09.2026. Arbeitsdokument für die Korrektur nach `WORKFLOW.md`.

Zwei Quellen sind hier zusammengeführt, nämlich die 106 Kommentare des
Betreuers zur PDF-Fassung, hier als **B01 bis B106** durchnummeriert, und die
Kürzungsliste vom 11.09.2026 in `KUERZUNGEN_KAP1_2.md` mit ihren Kennungen
**A, Q, E, G und P**. Die Kürzungsliste bleibt als Fundstellenverzeichnis
bestehen, ihre Zeilenangaben gelten weiter, denn die Kapiteldateien haben sich
seit der Fassung 74a9d8d nur in Kommentarzeilen geändert.

Der Betreuer hat den Vorspann, Kapitel 1 und Abschnitt 2.1 kommentiert. Für die
Abschnitte 2.2 bis 2.4 liegen nur die Kürzungen vor. Die abgeleiteten
Stilregeln gelten für alle Kapitel.

Zeilenangaben beziehen sich auf die Arbeitskopie vom 14.09.2026,
**E** auf [chapter_1.tex](chapters/chapter_1.tex) und **G** auf
[chapter_2.tex](chapters/chapter_2.tex). Kommentarzeilen sind mitgezählt.

Nichts davon ist umgesetzt. Jeder Absatz läuft über den Absatzplan nach
`WORKFLOW.md`, bevor ein Satz in eine Kapiteldatei geht.

---

## 0 Entscheidungen des Verfassers vor Beginn

Diese Punkte binden mehrere Absätze. Ohne sie lässt sich kein Abschnitt
abschließen.

| Nr | Frage | Vorschlag | Betrifft | Stand |
|---|---|---|---|---|
| V1 | **KI-Nutzung in der Eidesstattlichen Versicherung** (B02). Die RWTH und das IAEW haben dazu eigene Vorgaben. | Beim Betreuer erfragen, ob eine gesonderte Erklärung zur KI-Nutzung verlangt wird, und in welcher Form. Die Vorlage in `extras/declaration.tex` sieht keine vor. Nicht von Claude zu entscheiden. | Vorspann | entschieden 14.09.2026, keine Erklärung, Vorlage bleibt |
| V2 | **Begriff für das Produkt und für die Tätigkeit.** Kapitel 3 führt seit dem 11.09.2026 *kurative Reservierung* als Produktnamen, Kapitel 1 und 2 sprechen 14-mal von *kurativer Vorhaltung*, ohne sie zu definieren (B24, B40). | Beide Begriffe behalten und einmal trennen. *Kurative Vorhaltung* ist die Tätigkeit des Akteurs, nämlich das Bereithalten von Leistung und, bei Speichern, von Ladezustand für einen kurativen Abruf. *Kurative Reservierung* ist das Produkt, mit dem der ÜNB diese Vorhaltung beschafft. Definition beider Begriffe im ersten Absatz von 1.2. | 1.2, Kap. 2 durchgehend, Kap. 3 | entschieden 14.09.2026, wie vorgeschlagen |
| V3 | **Doppelpunkt im Fließtext.** Die bisherige Stilregel 7 verbot ihn, der Betreuer schlägt ihn für These und Erklärung vor (B06). | Zulassen, sparsam und nur für These mit folgender Erklärung. Sonst *denn*, *weil*, *sodass*. Die Prüfsuite meldet Doppelpunkte seit dem 14.09.2026 nicht mehr. | alle Kapitel | entschieden 14.09.2026, wie vorgeschlagen |
| V4 | **Wort für die Handlung des Akteurs.** Der Betreuer schreibt, die ÜNB sagten nicht *aktiviert*, und die Leistung werde innerhalb von fünf Minuten vollständig umgesetzt (B63). | Den vom Betreuer verwendeten Ausdruck erfragen, er hat das angeboten. Bis dahin *umsetzen* für die Leistungsänderung des Akteurs und *auslösen* für das Signal des ÜNB. *Aktivierung* bleibt nur in Zitaten aus SOGL und InnoSys. Zwölf Fundstellen in Kapitel 2, Zeilen 19, 20, 29, 33, 34, 38, 118, 136, 187, 297, 299, 420. | 2.1 | entschieden 14.09.2026, umsetzen für den Akteur, auslösen für das Signal |
| V5 | **Ersatz für *Reichweite*.** Der Betreuer fragt viermal, was gemeint ist (B50, B53, B54, B57). | Das Wort streichen und den Sachverhalt einmal benennen, nämlich als den Zeitpunkt der letzten Vorschaurechnung, bis zu dem der ÜNB einen Engpass vorab erkennen und präventiv beheben kann. Danach *Planungshorizont*. Vier Fundstellen G 67, 74, 80, 83. | 2.1.1 | entschieden 14.09.2026, wie vorgeschlagen |
| V6 | **Thermik in den Anhang, A2 oder A2b.** Grundsatzfrage, ob die Physik im Hauptteil bleibt. Drei Betreuerkommentare (B66, B67, B68) treffen genau diesen Block. | A2, also drei bis vier Sätze im Hauptteil und ein Anhang mit beiden Gleichungen, der Abbildung und dem Transformatorabsatz. Die drei Kommentare werden dann im Anhang umgesetzt. | 2.1.2 | entschieden 14.09.2026, A2 |
| V7 | **Weber-Ansatz in den Anhang, A1 oder A1b.** | A1, weil es der größte Hebel ist und die Basispreisfrage entschärft. | 2.3.2 | entschieden 14.09.2026, A1 |
| V8 | **Quelle für das Grenzwertkonzept der deutschen ÜNB.** Der Betreuer verweist zweimal darauf (B69, B94). In `literature.bib` gibt es dazu keinen Eintrag. | Beim Betreuer die Veröffentlichung erfragen, auf die er sich bezieht. Ohne Quelle bleiben beide Stellen als Vorbehalt ohne Beleg formuliert. | 2.1.2, 2.1.4 | entschieden 14.09.2026, Deutsches Grenzwertkonzept der ÜNB, November 2021, Schlüssel `uenb_grenzwertkonzept_2021` |
| V9 | **Belege für KuPilot.** Der Betreuer ergänzt, dass der Einsatz des PSKW im Pilotbetrieb auf eine Stunde begrenzt ist, weil das Becken auch die übrigen Turbinen bedient (B84). Die TenneT-Quelle ist ein Scan ohne Textebene und lässt sich nicht durchsuchen. | Der Verfasser liest die drei Seiten und prüft, ob die Stunde und die Formulierung *innerhalb von fünf Minuten* dort stehen. Steht die Stunde nicht dort, wird die Aussage ohne Zahl abgeschwächt. | 2.1.2, 2.1.3 | entschieden 14.09.2026, Stunde und fünf Minuten stehen in der TenneT-Mitteilung |
| V10 | **Tabelle 2.1** soll an die Verweisstelle (B85). | Float unmittelbar hinter den Verweissatz G 203 setzen, Platzierung `[htbp]` behalten, nach dem Build prüfen. | 2.1.3 | entschieden 14.09.2026, wie vorgeschlagen |
| V11 | **Definitionsort für Engpass, Ausfallvariante, Befund** (B43, B46). | In der Einleitung von 2.1 hinter der Definition des Engpassmanagements, drei bis vier Sätze. Kapitel 1 verwendet die Begriffe dann mit einem Halbsatz. | 2.1, 1.1 | entschieden 14.09.2026, wie vorgeschlagen |
| V12 | **Redispatch früher benennen** (B11) gegen Q5, die nur eine Definitionsstelle will. | Ein Halbsatz in 1.1 Absatz 2 bei der ersten Verwendung, die Definition bleibt in 2.1 Zeile 13, der Satz E 91 entfällt. | 1.1, 1.2, 2.1 | entschieden 14.09.2026, wie vorgeschlagen |
| V13 | **Klärung mit dem Betreuer zur Reaktion des ÜNB auf späte Fahrplanänderungen** (B21, B58). Der Text liest sich so, als sei das Netz ohne kurative Maßnahmen nicht N-1-sicher. | Mit dem Betreuer klären, mit welchen Mitteln der ÜNB heute Netzzustände beherrscht, die nach der letzten Vorschaurechnung entstehen. Erst danach lassen sich E 71 und G 83 richtig fassen. | 1.1, 2.1.1 | entschieden 14.09.2026, laufende Netzsicherheitsrechnung und kurzfristige Maßnahmen, das Netz bleibt sicher, teurer und mit kleinerem Anlagenkreis |

---

## 1 Übergreifende Änderungen

Sie folgen aus B01 und aus den Kommentaren, die sich in Kapitel 1 und 2
wiederholen. Sie gelten für jeden Absatz und werden bei der Korrektur nicht
einzeln aufgeführt. Die Stilregeln dazu stehen in `CLAUDE.md` Abschnitt 4.

| Nr | Änderung | Auslöser | Suchmuster |
|---|---|---|---|
| U1 | Jeder Absatz beginnt mit seiner These und verbindet die Begründung mit *denn*, *weil*, *sodass* oder mit Doppelpunkt. Kein Behauptungssatz, dem unverbunden Erläuterungssätze folgen. | B01, B06, B13, B14 | Absatz für Absatz |
| U2 | Jeder Absatz endet mit der Konsequenz, also mit dem, was der Befund für Maßnahme, Mechanismus oder Netzbetrieb bedeutet. | B17, B106 | Absatz für Absatz |
| U3 | Pronomen und Demonstrativa werden aufgelöst, wenn der Bezug nicht im selben Satz steht. | B29, B35, B52, B72, B73, B90, B103 | `\b(sie|er|es|diese|dieser|dabei|damit|darin)\b` am Satzanfang |
| U4 | Unbestimmte Nominalphrasen bekommen ihr Attribut. | B16, B29, B71, B74, B77 | *die Arbeit*, *der Bedarf*, *das Netz*, *der Mechanismus*, *der Bestand* |
| U5 | Kapitel und Abschnitte handeln nicht. Verweise lauten *wie in Abschnitt X beschrieben* oder *in Abschnitt X wird X dargestellt*. | B39, B41, B81 | `Kapitel~\\ref\{[^}]+\} (untersucht|behandelt|prüft|begründet)`, `Abschnitt \\ref\{[^}]+\} (untersucht|darlegt|ausführen)` |
| U6 | Absätze werden kürzer. Ein Absatz trägt eine Kernaussage und vier bis acht Sätze. Der Betreuer hat in 2.1.4 selbst einen Umbruch eingefügt. | B98 | Absätze über zehn Sätzen in G 244 bis 255, G 260 bis 283, G 288 bis 300, G 629 |
| U7 | Relative Angaben bekommen Bezugsgröße oder Zahl. | B79, B86, B91 | *groß*, *klein*, *eng*, *spät*, *schnell*, *kurz*, *wenige* |
| U8 | Absolute Feststellungen bekommen einen Beleg oder werden abgeschwächt. | B60, B67, B80 | Absatz für Absatz, Belegzettel |
| U9 | Begriffe werden vor der ersten Verwendung definiert. Die Liste steht in `CLAUDE.md` Abschnitt 5. | B24, B37, B38, B40, B43, B46, B76 | erste Fundstelle je Begriff |
| U10 | Der Betrachtungsrahmen wird ausgesprochen, nämlich Deutschland gegen Europa, heutiger Stand gegen Planung, Zieljahr und Auswertungszeitraum. | B05, B30, B64, B65 | *europäisch*, *Zieljahr*, *Szenario* |

---

## 2 Kapitel 1, absatzweise

Für jeden Absatz stehen die Zeilen, die Kernaussage, die er tragen soll, die
Befunde und die Änderung. **Maßnahme** ist eine von *umbauen*, *kürzen*,
*streichen* oder *verschieben*.

### Vorspann, E 4 bis 6

- **Kernaussage.** Der Umbau der Erzeugung verändert die Transportaufgabe des Netzes, und die vorliegende Arbeit befasst sich mit einer Antwort darauf, nämlich der kurativen Systemführung mit BESS.
- **Befunde.** B03, der Absatz sei generisch und ohne Bezug zu BESS und kurativ. E1, die Sätze 5 und 6 tragen eine Aussage.
- **Maßnahme.** Umbauen. Der Klimaschutzsatz entfällt oder wird zum Halbsatz. Der Absatz nennt in drei Sätzen den Erneuerbarenanteil, die Folge für das Netz und die beiden Stichworte der Arbeit, nämlich kurative Systemführung und BESS als Akteur. Damit steht der Gegenstand vor der Motivation.

### 1.1 Absatz 1, E 11 bis 13, räumliche Ursache

- **Kernaussage.** Die Transportaufgabe folgt aus der räumlichen Trennung von Erzeugung und Last, und das Muster wird vielfältiger.
- **Befunde.** B04, die Achse verläuft von Nord-Ost nach Süd-West, Last im Süden und Westen. E2, Satz 12 hat kein eigenes Gewicht.
- **Änderung.** Satz 11 nennt Windkraft im Norden und Osten und Lastzentren im Süden und Westen. Beleg dafür prüfen, der NEP beschreibt die Transportaufgabe, die Richtungsangabe ist gegen `bundesnetzagentur_netzentwicklungsplan_2026` zu halten. Satz 12 in 13 aufnehmen nach E2.

### 1.1 Absatz 2, E 15 bis 21, institutionelle Ursache

- **Kernaussage.** Das Marktdesign erzeugt den Bedarf mit, denn Fahrpläne entstehen ohne Kenntnis der Netzbelastung, und der ÜNB korrigiert sie nachträglich durch Redispatch.
- **Befunde.** B05 europäisch gegen deutsch. B06 These mit Doppelpunkt. B07 Satz 17 an Satz 16 hängen. B08 *systematisch* unklar. B09 die Netzsituation ist selbst Folge des Marktergebnisses, Satz 21 stimmt so nicht. B10 den Zugriff des ÜNB besser umschreiben. B11 Redispatch hier einführen. E3, E4. Q4 gegen G 341 bis 343.
- **Änderung.** Umbauen auf vier Sätze. Erstens die These mit Doppelpunkt, dass das Marktdesign des europäischen Binnenmarkts, dem der deutsche Markt folgt, das Missverhältnis verstärkt. Zweitens der Selbstdispatch in einem Satz. Drittens, dass der zonale Preis die Netzbelastung nicht abbildet und marktoptimale Fahrpläne deshalb regelmäßig Flüsse erzeugen, die das Netz nicht aufnimmt, ohne das Wort *systematisch*. Viertens, dass der ÜNB die Fahrpläne nicht bestimmt und die Überlastung nachträglich durch Redispatch behebt, also durch die angeordnete Anpassung der Einspeisung einzelner Anlagen, mit dem Schluss, dass der Redispatchbedarf damit eine Folge des Marktdesigns ist. Satz 21 entfällt in seiner Gegenüberstellung von Netzsituation und Entkopplung, nach V12 steht die Kurzdefinition des Redispatch hier.

### 1.1 Absatz 3, E 23 bis 30, Mengen und Kosten

- **Kernaussage.** Volumen und Kosten sind hoch und die Kosten hängen an einzelnen Wetterereignissen.
- **Befunde.** B11 Umschreibung in Satz 24 durch *Redispatch* ersetzen. B12 welche Ereignisabhängigkeit. E5 Satz 23 streichen. E6 Sätze 29 und 30 verbinden. E7 gegen E 48 bis 50.
- **Änderung.** Kürzen und verbinden. Satz 24 sagt, dass die Abbildung das Redispatchvolumen zeigt. Satz 27 wird zur These mit Erklärung, nämlich dass die Jahressummen verdecken, wie stark einzelne Wetterereignisse die Kosten prägen, mit Doppelpunkt oder *denn* in die Monatszahlen. Dezember 2024 und Windfront in einem Satz. Damit ist die Ereignisabhängigkeit hier belegt und E 51 kann sich darauf beziehen.

### 1.1 Absatz 4, E 41 bis 48, Restbedarf nach NEP

- **Kernaussage.** Der Bedarf bleibt auch nach dem Ausbau, weil der NEP ihn als Teil des Optimums ausweist.
- **Befunde.** B13 Satz 41 und 42 verbinden. B14 Satz 45 und 46 verbinden. B15 *um mehr senkt, als er selbst verursacht* liest sich schlecht. B16 welcher Bedarf in Satz 48. E8 doppelte 13 TWh, Satz 43 streichen, 45 und 46 verbinden. A7 Abbildung 1.2 optional streichen.
- **Änderung.** Umbauen auf fünf Sätze. These in 41 mit *denn* in den NEP-Wert. Zahlenverlauf in einem Satz ohne die zweite Nennung der 13 TWh. Dann die Erklärung, dass der Restbedarf aus dem Verfahren folgt, denn der NEP baut nur so weit aus, wie die eingesparten Engpassmanagementkosten die Ausbaukosten übersteigen. Schluss, dass der verbleibende Engpassmanagementbedarf zum Zielzustand gehört und Instrumenten jenseits des Ausbaus zufällt. Ob Abbildung 1.2 bleibt, entscheidet der Verfasser nach dem Seitenstand.

### 1.1 Absatz 5, E 50 bis 52, zwei Eigenschaften

- **Kernaussage.** Der Bedarf ist ereignisabhängig und räumlich wandernd, und beides stellt Anforderungen an das Instrument.
- **Befunde.** B16 *des Bedarfs* benennen. B17 was bedeutet das für die Maßnahmen. E7 Rückschau auf 27 bis 30 tilgen.
- **Änderung.** Kürzen und zu Ende führen. Satz 50 nennt den Engpassmanagementbedarf. Die beiden Eigenschaften in je einem Halbsatz, ohne die Zahlen zu wiederholen. Neuer Schlusssatz mit der Konsequenz, nämlich dass ein Instrument für diesen Bedarf nur im Ereignisfall wirken und an wechselnden Orten verfügbar sein muss. **Eigenständiges Argument, vom Verfasser zu prüfen.** Es bereitet die Wahl von Vorhaltung und BESS vor, ohne sie zu nennen.

### 1.1 Absätze 6 und 7, E 63 bis 82, Zeitstruktur und kurative Systemführung

Beide Absätze sind zusammen zu behandeln, denn der Betreuer bemängelt, dass
Absatz 6 präventive Begriffe verwendet, die erst Absatz 7 erklärt.

- **Kernaussage 6.** Die präventive Systemführung braucht Kenntnis der Netzbelastung im Voraus, und die kurzfristigen Märkte verkürzen den Zeitraum, in dem sie diese Kenntnis hat.
- **Kernaussage 7.** Die kurative Systemführung nutzt die kurzfristige Überlastbarkeit der Betriebsmittel, greift erst nach dem Fehler ein und braucht dafür einen Akteur, der schnell und verlässlich reagiert.
- **Befunde.** B18 Übergang *Neben dem Volumen* unklar. B19 Zusammenhang der präventiven Betriebsplanung. B20 warum die Voraussetzung schwerer einzuhalten ist, Prozesse und Zeiten. B21 was der Netzbetreiber dann tut, das Netz ist N-1-sicher. B22 Absatz 7 ist für Fachfremde unverständlich. B23 Satz 80 liest sich, als sei nur kurativ N-1-Sicherheit erreichbar. E9 Satz 66 doppelt 19. E10. Q1, Q2, Q19 gegen Kapitel 2. V13.
- **Änderung.** Umbauen in drei kürzere Absätze in neuer Reihenfolge.
  1. *Präventive Systemführung in vier Sätzen.* Betriebsmittel haben eine dauerhaft zulässige Belastung. Der ÜNB plant den Betrieb so, dass auch nach dem Ausfall eines Betriebsmittels kein anderes darüber belastet wird. Dafür muss die Belastung im Normalbetrieb unter der Dauergrenze bleiben, und diese Marge erzwingt den Redispatch. Betriebsmittel vertragen kurzzeitig mehr, sodass eine Reserve ungenutzt bleibt. Das ist der Inhalt von E 73 bis 75 in einfacher Sprache.
  2. *Zeitliche Grenze in vier bis fünf Sätzen.* Überleitung, dass zum Volumen und zum Ort eine dritte Eigenschaft tritt, nämlich der Zeitpunkt, an dem der Engpass erkennbar wird. Der ÜNB rechnet am Vortag und untertägig, und zwischen der letzten Rechnung und dem Lieferbeginn bleibt ein Handelsfenster, im regelzoneninternen Handel bis fünf Minuten vor Lieferung. Fahrpläne, die sich dort noch ändern, gehen in keine Rechnung mehr ein. Dann die Antwort auf B21, also was der ÜNB heute tut, nach V13. Satz 66 und 70 entfallen nach E9 und E10.
  3. *Kurative Systemführung in fünf Sätzen.* Sie nutzt die kurzzeitige Überlastbarkeit, greift erst nach dem Fehler ein und braucht deshalb weniger Volumen. Sie ist von der zeitlichen Lücke weniger betroffen, weil sie nach dem Fehler wirkt, ohne zu behaupten, sie sei die einzige Antwort (B23). Voraussetzung ist ein Akteur, der innerhalb von Minuten und verlässlich reagiert und dessen Stellpotenzial nicht durch die eigene Vermarktung aufgebraucht ist. Schluss auf BESS wie E 82.

### 1.2 Absatz 1, E 88 bis 97, Ziel und Anreizfrage

- **Kernaussage.** Die Arbeit entwirft ein Produkt für die kurative Vorhaltung und bestimmt seinen Preis, denn im Selbstdispatch entsteht Verfügbarkeit nur über einen Anreiz, und keine der beiden bestehenden Vergütungslogiken ist dafür gemacht.
- **Befunde.** B24 kurative Vorhaltung wovon. B25 Zusammenhang zu InnoSys unklar. B26 die Höherauslastung reduziert den präventiven Redispatch, *ersetzt sie nicht* greift zu kurz. B27 zu viele Aspekte ohne roten Faden. E11 auf drei bis vier Sätze. Q5 bis Q8. V2, V12.
- **Änderung.** Umbauen auf vier bis fünf Sätze. Erstens das Ziel mit der Definition beider Begriffe nach V2, nämlich der kurativen Vorhaltung als Bereithalten von Leistung und Ladezustand für einen Abruf nach dem Fehler und der kurativen Reservierung als dem Produkt dafür. Zweitens die Abgrenzung zum Redispatch nach B26, nämlich dass die kurative Systemführung den präventiven Redispatch verringert, ihn aber nicht ersetzt, weil nach einem Abruf ein Redispatch den sicheren Zustand wiederherstellt. Drittens, dass der Betreiber im Selbstdispatch selbst entscheidet und Verfügbarkeit deshalb eine Vergütung braucht. Viertens die beiden Logiken in einem Satz, Regelleistung vergütet die Bereitstellung, Engpassmanagement den Eingriff. Fünftens die offene Frage. InnoSys, die Einordnung als Systemdienstleistung und die Vorrangigkeit der marktlichen Beschaffung entfallen hier und bleiben in Kapitel 2.

### 1.2 Absatz 2, E 99 bis 107, Betrachtungsrahmen und Gegenstand

- **Kernaussage.** Beantwortet wird die Frage mit einem Optimierungsmodell des Speicherbetriebs, das den kurativen Reservierungspreis aus historischen Preisen des Jahres 2025 bestimmt.
- **Befunde.** B28 Übergang zur Simulation fehlt. B29, B35 welche Arbeit. B30 welches Zieljahr. B31 Überprüfbarkeit als Argument ausführen oder fallen lassen. B32 welche erste Unsicherheit. B33 *Bindung* und *indifferent* erklären. B34 *Eigenschaft der Anlage* klingt technisch. B36 Satz 104 ergibt so keinen Sinn. B37 Bindungsdauer wovon. B38 Reaktionszeit definieren. E12 Methodenbegründung nach 3.2.1. E13. P6 ganzes Jahr 2025 statt 2030-Szenario mit 2025. P8 *entgangene Erlösmöglichkeiten* ist der Begriff aus § 13a.
- **Änderung.** Umbauen auf sechs bis sieben Sätze.
  1. Überleitungssatz, dass die Fragen mit einem Optimierungsmodell des Speicherbetriebs beantwortet werden.
  2. Rahmen in einem Satz, das Jahr 2030 als qualitativer Rahmen mit hohem Erneuerbarenanteil und gewachsenem Speicherbestand, gerechnet wird mit den beobachteten Preisen des Jahres 2025.
  3. Ein Satz zur Begründung, nämlich dass beobachtete Preise die Volatilität tragen, auf die es ankommt, und eine Prognose dem Ergebnis eine weitere Annahme hinzufügte, deren Fehler sich vom Effekt der Reservierung nicht trennen ließe. Das Wort *zweite* entfällt (B32), die längere Begründung geht nach 3.2.1 (E12).
  4. Definition des Preises in einfacher Sprache, nämlich der Betrag, den ein Betreiber mindestens verlangen muss, damit er mit der kurativen Reservierung genauso viel verdient wie ohne sie. *Bindung* wird eingeführt als die Verpflichtung, Leistung und Ladezustand über die Bindungsdauer vorzuhalten, *indifferent* entfällt oder wird erklärt (B33).
  5. Satz 103 neu, der Preis misst die Opportunitätskosten der Bindung und hängt von Leistung, Energieinhalt und den Preisen der übrigen Märkte ab (B34, P8).
  6. Satz 104 neu, wie viel Engpassmanagement die kurative Systemführung einspart, ist nicht Gegenstand, Gegenstand ist allein der Preis der Vorhaltung (B36).
  7. Satz 105 mit den Definitionen von Bindungsdauer als Zeitraum der Vorhaltepflicht und Reaktionszeit als Zeit vom Abrufsignal bis zur vollständig umgesetzten Leistungsänderung (B37, B38, V4). Satz 106 zu den Einflüssen auf den Marktpreis nach E13 auf einen Halbsatz oder nach 3.2.
  8. Die drei Teilfragen bleiben.

### 1.2 Absatz 3, E 109 bis 134, Kapitelüberblick

- **Befunde.** B39 Kapitel untersuchen nichts, Subjekte prüfen. E14 ein bis zwei Sätze je Kapitel. P1 der Überblick zu Kapitel 3 ist veraltet, 3.3 beansprucht keine Verifikation, die Marktdesignansätze sind gestrichen.
- **Änderung.** Kürzen auf zehn Sätze mit der Form *In Kapitel X wird ... dargestellt* oder mit handelndem Subjekt. Kapitel 3 nach `STRUKTUR.md`, nämlich Anforderungen und Produkt, Optimierung des Speicherbetriebs, Validierung des unrestringierten Fahrplans gegen den Erlösindex. Erst nach der Korrektur von Kapitel 3 endgültig fassen.

---

## 3 Abschnitt 2.1, absatzweise

### Kapiteleinleitung, G 4 bis 7

- **Befunde.** B40 kurative Vorhaltung definieren. B41 *untersucht es* Subjekt. G1 Satz 4 streichen.
- **Änderung.** Satz 4 entfällt, die Definition steht nach V2 in 1.2. Sätze 5 bis 7 in der Form *Zunächst werden ... dargelegt*. Drei Sätze.

### Einleitung 2.1, G 12 bis 22

- **Kernaussage.** Engpassmanagement und Redispatch, das N-1-Kriterium und die beiden Systemführungskonzepte werden benannt.
- **Befunde.** B46 Engpass definieren im Zusammenhang mit N-1 und Befunden. B43 Ausfallvariantenliste erklären. G2, G3, G4, G5, G6 zu den Sätzen 14, 15, 16, 18, 20, 21, 22. V4 zu *aktivierbare* und *Aktivierungszeiten* in 19 und 20. V11.
- **Änderung.** Umbauen in zwei Absätze. Der erste trägt Engpassmanagement, Redispatch und die neuen Definitionen, nämlich Ausfallvariante als angenommener Ausfall eines einzelnen Betriebsmittels, Ausfallvariantenliste als die Menge der Ausfälle, die der ÜNB durchrechnet, Befund als eine in dieser Rechnung ermittelte Grenzwertverletzung und Engpass als der Zustand, in dem im Grundfall oder in einer Ausfallvariante ein Grenzwert überschritten würde. Der zweite trägt das N-1-Kriterium mit dem Zitat und die beiden Konzepte in je einem Satz, InnoSys und die Anschlussarbeiten in einem Satz (G5), Satz 22 entfällt (G6).

### 2.1.1 Absatz 1, G 27 bis 46, Vier-Zustands-Modell und Grenzwerte

- **Kernaussage.** Beide Konzepte halten das Netz im Normalzustand, unterscheiden sich aber im Zeitpunkt des Eingriffs, und die Zeit dafür gibt die Überlastbarkeit vor.
- **Befunde.** B42 welche Ansätze. B43 Ausfallvariantenliste. B44 Satz 34 ist gut, bleibt. G7 Not- und Blackoutzustand entfallen. G8 Sätze 32 und 33 verbinden. G9 Satz 42 als Fußnote oder streichen. Q13 gegen 2.1.5. V4 in 29, 33, 34, 38.
- **Änderung.** Umbauen in zwei Absätze. Der erste von 27 bis 37 mit der Nennung *präventive und kurative Systemführung* in Satz 27, ohne 30 und 31, mit 32 und 33 verbunden, Satz 34 unverändert. Der zweite von 38 bis 46 zur Überlastbarkeit, Satz 42 als Fußnote, Satz 43 schließt mit der Konsequenz, wie viel Zeit für die Gegenmaßnahme bleibt. Die Abbildung folgt dem Absatz.

### 2.1.1 Absatz 2, G 57 bis 62, präventives Vorgehen

- **Befunde.** B45 die Anpassungen sind meist präventiver Redispatch, hier sagen. Q1 Satz 57 doppelt 45. Q14 gegen G 374 bis 378. G11 Sätze 61 und 62 verbinden.
- **Änderung.** Kürzen auf vier Sätze. Satz 57 nennt den präventiven Redispatch als Regelfall der Anpassung und lässt die Wiederholung der Marge weg. Sätze 58 bis 60 auf zwei, denn die Stufung steht in 2.2.2 ausführlich (Q14). Sätze 61 und 62 als ein Satz.

### 2.1.1 Absatz 3, G 64 bis 72, drei Merkmale

- **Kernaussage.** Der präventive Ansatz kostet, weil die Marge Eingriffe erzwingt, weil sein Planungshorizont vor dem Lieferbeginn endet und weil die Kosten an der Anlagenart hängen.
- **Befunde.** B47 Satz 65 passt grammatisch nicht. B48 *Breite* durch *Höhe* ersetzen. B49 die Marge ist keine Wahl, sondern durch das Netz vorgegeben. B50 Reichweite. B51 Prozess mit Zeiten. B52 *dabei* in Satz 71. Q1 Satz 65 kürzen. Q3 gegen E 51. Beleg `sous_comparison_2025` für Satz 66 prüfen, die Quelle definiert die Marge, ob sie den Zusammenhang mit Volumen und Kosten trägt, ist offen.
- **Änderung.** Umbauen auf sieben Sätze. Erstens neu, dass die Marge nicht gewählt wird, sondern aus der ungünstigsten Ausfallvariante folgt, und dass ihr Freihalten der Eingriff ist. Zweitens mit *Höhe* und geprüftem Beleg. Zweites Merkmal nach V5 als Planungshorizont, mit den Zeiten aus 2.2.2, nämlich Vortagesrechnung, untertägige Rechnung und Handelsschluss fünf Minuten vor Lieferung, und einem Sachverweis auf Abbildung `fig:markt_zeitschiene`. Drittes Merkmal wie bisher, Satz 71 mit *zugleich* statt *dabei*. Satz 72 bleibt als Konsequenz, E 51 verweist dann hierher oder entfällt (Q3).

### 2.1.1 Absatz 4, G 74 bis 78, Verlagerung in die kurzfristigen Märkte

- **Befunde.** B53 Reichweite. G12 fünf Sätze auf drei, Satz 75 doppelt E 66. Q2.
- **Änderung.** Kürzen auf drei Sätze mit *Planungshorizont*. Der Beleg `mahgoub_wie_2025` steht in Kapitel 1, hier genügt der Sachverhalt mit dem Beleg zur Produktumstellung.

### 2.1.1 Absatz 5, G 80 bis 91, zwei Ausprägungen

- **Kernaussage.** Die kurative Systemführung tritt als Höherauslastung und als kurativer Redispatch auf, beide wirken erst nach dem Fehler und verändern die Art der Kosten.
- **Befunde.** B54, B57 Reichweite. B55 der kurative Redispatch wird ebenfalls vorgeplant, nur mit anderen Grenzwerten. B56 er behebt die Verletzung, nachdem sie eingetreten ist. B58 Satz 83 behauptet zu viel, der präventive Ansatz deckt diese Zustände heute ebenfalls ab. B59, B61 die Ausprägungen beim Namen nennen. B60 Beleg für Satz 87. G13 Satz 89 Vorverweis streichen. G14 Satz 91 halbieren. V13.
- **Änderung.** Umbauen in zwei Absätze.
  1. *Die beiden Ausprägungen, fünf Sätze.* Satz 80 nennt sie beim Namen. Höherauslastung wie 81. Kurativer Redispatch neu, nämlich dass auch er vorgeplant und scharfgeschaltet wird, der Unterschied zur präventiven Planung im angesetzten Grenzwert liegt, die Maßnahme aber erst ausgeführt wird, nachdem der Fehler eingetreten ist. Satz 83 entfällt, an seine Stelle tritt nach V13 die zurückhaltende Aussage, dass die kurative Maßnahme für spät entstehende Netzzustände weniger Vorlauf braucht.
  2. *Gemeinsame Wirkung, fünf Sätze.* Sätze 84 bis 86 wie bisher mit Namen statt *beide Ausprägungen*. Sätze 87 und 88 zu einem Satz mit Beleg. Satz 89 entfällt, Satz 90 bleibt, Satz 91 ohne den zweiten Halbsatz.

### 2.1.1 Absatz 6, G 93 bis 96

- **Befunde.** B62 *spät* worauf bezogen. G15 Verweis auf `sec:sensitivities` streichen.
- **Änderung.** Satz 93 mit *Netzzustände, die erst nach der letzten Vorschaurechnung entstehen*. Satz 96 ohne den Verweis. Der Absatz ist der Übergang zur Vorhaltung als Gegenstand und bleibt sonst.

### 2.1.2 Absatz 1 und 2, G 101 bis 122, vier Phasen

- **Befunde.** B63 *aktiviert* in Satz 118, Wortlaut der Quelle prüfen, V4 und V9. G16, G17 je zwei Sätze verbinden.
- **Änderung.** Kürzen auf zusammen acht Sätze. Satz 118 nach V9 mit dem geprüften Wortlaut, sonst *innerhalb von fünf Minuten vollständig umgesetzt*. Sätze 113 und 114, 117 und 118 je verbunden.

### 2.1.2 Absatz 3, G 124 bis 135, Erkennung und Maßnahmenraum

- **Kernaussage.** Der ÜNB erkennt gefährdete Zustände in der laufenden Rechnung, und nur die Maßnahmen, die ein Dritter erbringt, brauchen eine Zusage.
- **Befunde.** B64 HGÜ als kurative Maßnahme und Netzbooster sind noch nicht im Betrieb. B65 Stand der Technik und Planung trennen. G18 Sätze 120 und 121 auf einen, Q15. P7 *Paar von Zusagen* gegen *Verbund von Geboten* in 3.1. B81 in 2.1.3 verlangt, dass der bilanzielle Ausgleich hier als Regelfall und nicht als Gesetz beschrieben wird.
- **Änderung.** Umbauen auf acht Sätze. Satz 124 bleibt, 125 entfällt oder wird Halbsatz. Satz 128 neu in zwei Sätzen, heute verfügbar sind Schaltmaßnahmen und Phasenschieber, in Umsetzung sind die HGÜ-Korridore und die Netzbooster, mit Beleg `consentec_systembooster_2026` für die Netzbooster. Satz 134 neu mit Definition, nämlich dass eine marktbezogene kurative Maßnahme in der Regel bilanziell ausgeglichen wird, wobei die Anlage, die ihre Einspeisung erhöht, als Quelle und die, die sie senkt, als Senke wirkt. Satz 135 mit *Verbund von Geboten* nach P7 oder ohne diesen Schluss.

### 2.1.2 Absätze 4 bis 6, G 136 bis 178, Thermik

- **Befunde.** B66 *engsten* unklar. B67 Beleg für die Heißpunkttemperatur oder abschwächen. B68 die Unterscheidung zwischen Grenztemperatur und Alterung überzeugt nicht, auch am Leiterseil zählt die Wirkung der Temperatur. A2 oder A2b. Q10, Q11 gegen 2.1.4.
- **Änderung nach V6.** Bei A2 bleiben im Hauptteil vier Sätze, nämlich dass die zulässige Dauer aus der Wärmebilanz folgt, dass sie von Vorbelastung und Witterung abhängt und in windschwachen Stunden am kürzesten ist (B66), dass sie bei Transformatoren länger ist, dort aber wegen der Alterung der Isolation auch die Häufigkeit begrenzt, und dass für eine Strecke das Minimum über alle Betriebsmittel zählt. Dazu der Verweis auf den neuen Anhang. Im Anhang wird B67 mit `iec_60076_7_2018` belegt und B68 so gefasst, dass die Temperatur bei beiden Betriebsmitteln für eine Wirkung steht, nämlich Durchhang und Festigkeit am Leiterseil und Isolationsalterung am Transformator, und dass sich beim Transformator die Wirkung über die Einsätze summiert.

### 2.1.2 Absatz 7 und 8, G 180 bis 188, Reaktionszeit und Klassen

- **Befunde.** B69 die Höherauslastung hängt an weiteren Bedingungen des Grenzwertkonzepts, V8. G20, Q12 Sätze 182 und 184 verbinden. V4 zu *Aktivierungsgeschwindigkeit* in 187.
- **Änderung.** Kürzen auf sieben Sätze. Satz 183 neu nach dem Deutschen Grenzwertkonzept `uenb_grenzwertkonzept_2021`, nämlich dass die Höherauslastung nur zulässig ist, soweit der ÜNB den Stromkreis dafür freigegeben hat, die zulässige Überlastdauer die Reaktionszeit des Akteurs deckt und die weiteren Grenzwerte des Konzepts, nämlich Schutz, Spannung, Stabilität und Genehmigungen, eingehalten sind. Sätze 182 und 184 als ein Satz. Satz 187 mit *Wirksamkeit* statt *Aktivierungsgeschwindigkeit*, InnoSys selbst spricht von Wirksamkeit.
- **Grundlage aus dem Grenzwertkonzept, für den Absatzplan.** Die TATL ist dort das Minimum aus vier Faktoren, nämlich externen Limitierungen wie Genehmigungen und Immissionsschutz, systemischen Limitierungen wie Netz- und Kraftwerksstabilität und Spannungshaltung, dem Schutzengpassstrom und dem thermischen Engpassstrom der gesamten Betriebsmittelkette. Betriebliche Voraussetzungen sind die Freigabe des Stromkreises durch den ÜNB, sonst gilt TATL gleich PATL, die Abhängigkeit von der Vorbelastung und damit vom Freileitungsmonitoring, die Anwendungsdauer mindestens gleich der Umsetzungszeit der Maßnahme, die Koordination mit den beeinflussten ÜNB vor dem Ausfall, kein anderer Stromkreis über seinem dauerhaften Engpassstrom und ein Zielzustand unter der PATL. Fundstellen sind vor dem Schreiben mit `tools/quellencheck.py --key uenb_grenzwertkonzept_2021` zu belegen.

### 2.1.3 Absatz 1, G 195 bis 204, Merkmale des Vergleichs

- **Befunde.** B70 Satz 195 schwer lesbar. B71 welcher Mechanismus. B72, B73 *er* zweimal. B74 Bestand wovon. B75 warum vier, wenn oben zwei. B76 Bemessungsgrundlage erklären. B77 *Netz* in der Typologie. G22 vier Sätze auf zwei. Q16 gegen 3.1.
- **Änderung.** Umbauen auf sechs Sätze. Satz 195 in zwei kurzen Sätzen. Satz 197 nennt *der zu entwerfende Marktmechanismus*, 198 wiederholt das Subjekt. Sätze 199 bis 202 zählen die vier Merkmale einmal auf, nämlich Reaktionszeit, Energiebindung, Anlagenbestand mit seiner Entwicklung und Vergütungspfad, mit dem Zusatz, dass eine Bemessungsgrundlage die Regel ist, nach der der Ausgleich eines Eingriffs berechnet wird. Satz 204 mit *netzseitige Betriebsmittel*.

### 2.1.3 Absatz 2, G 206 bis 218, konventionelle Kraftwerke, Wind und PV, PSKW

- **Befunde.** B78 Vorlaufzeit als Ausschluss deutlich machen. B79 wie schnell sind Gasturbinen, welcher Bestand. B80 Dargebot pauschal falsch, Wind im Norden verschärft, PV im Süden wirkt entgegen. B81 *nach Abschnitt* durch *wie in Abschnitt beschrieben*, und nicht jede kurative Maßnahme wird bilanziert. B82 Quelle und Senke vertauscht. B83 *trägt*. B84 KuPilot auf eine Stunde begrenzt. B86 *großer Energieinhalt* relativ. G23 sechs Sätze auf drei.
- **Änderung.** Umbauen in zwei Absätze, konventionelle Kraftwerke und Wind mit PV im ersten, PSKW im zweiten.
  1. Konventionell in drei Sätzen, nämlich beide Richtungen ohne Energiebindung, aber gebundener Betriebspunkt, und die Anfahrzeit als Ausschluss, wenn die Anlage steht. Die Gasturbinen entfallen, es sei denn, eine Zahl mit Beleg liegt vor (B79). Wind und PV in drei Sätzen, nur abregelnd, verfügbar nur dort, wo ihre eigene Einspeisung den Engpass verschärft, was für Wind im Norden bei Nord-Süd-Engpässen zutrifft und für Photovoltaik im Süden nicht (B80, eigenes Argument des Betreuers, Beleg suchen oder als Beispiel ohne Beleg). Satz 215 neu, soweit die Maßnahme bilanziell ausgeglichen wird, wie in Abschnitt 2.1.2 beschrieben, braucht die Rücknahme eine Erhöhung an anderer Stelle (B81, B82).
  2. PSKW in drei Sätzen, beide Richtungen, schnell, Energieinhalt in Stunden Entladedauer bei Nennleistung beziffert, KuPilot mit dem Vorbehalt nach V9, Standorte begrenzt.

### Tabelle 2.1, G 220 bis 242

- **Befunde.** B85 an die Verweisstelle. B86 *großer* und *geringer Energieinhalt* mit Bezugsgröße.
- **Änderung.** Nach V10 verschieben. Spalte Energiebindung mit Entladedauer bei Nennleistung in Stunden für PSKW und BESS, Zahlen mit Beleg nachtragen, in Betracht kommen der NEP für PSKW und die ISEA Battery Charts für Großspeicher. Ohne Beleg bleibt die Spalte qualitativ und die Fußnote nennt die Größenordnung.

### 2.1.3 Absatz 3, G 244 bis 255, BESS

- **Kernaussage.** BESS vereinen die Merkmale, ihre Grenze liegt im Energieinhalt, und diese Grenze trifft die kurative Vorhaltung anders als den Redispatch.
- **Befunde.** B87 die Verfügbarkeit am Knoten ist nicht durch Wachstum gesichert. B88 Übergang zu *Technisch*. B89 *diese* ohne Bezug. B90 *Ihre*. B91 *relativ klein bleiben kann*. B92 Verlagerung auf die Vorhaltung wird als mehr Energie gelesen. B93 dem Abschluss mehr Raum. G24 zwölf Sätze auf acht.
- **Änderung.** Umbauen in zwei Absätze.
  1. *Eigenschaften, fünf Sätze.* 244 bis 248 gekürzt, ohne 250. Satz 249 neu, für eine knotenscharfe Beschaffung zählt, ob am betroffenen Knoten ein Anbieter steht, und Standortfreiheit und wachsender Bestand machen das wahrscheinlicher, ohne es zu sichern.
  2. *Grenze und Schluss, sechs Sätze.* Satz 251 mit *die Grenze eines BESS*. 252 wie bisher. 253 mit *vergleichsweise klein bleiben kann*. 254 neu, die abgerufene Energie ist klein, aber der dafür nötige Ladezustandsbereich muss über die gesamte Bindungsdauer frei bleiben, die Grenze liegt also nicht in der Energiemenge, sondern in der Dauer der Reservierung. Abschluss in zwei bis drei Sätzen, nämlich die vier Merkmale für BESS in einem Satz, die Feststellung, dass die technischen Voraussetzungen vorliegen, und die offene Frage der Vergütung als Überleitung.

### 2.1.4, G 260 bis 283, Herausforderungen

- **Befunde.** B94 Grenzwertkonzept, V8. B95 standort- und situationsabhängig, Vorbelastung und Witterung. B96 *sichere Seite* durch PATL als Rückfallgrenze ersetzen. B97 Ausfall der Kette, thermische Trägheit lässt Zeit, konventioneller Redispatch bleibt möglich. B98 Absatzumbruch vor *Auf der Planungsseite*, allgemein häufiger. B99 die Einplanung wird mit der Zahl kurativer Maßnahmen schwieriger, in KuPilot ist sie binär mit fester Menge. A6, Q10, Q11, G 268 Vorverweis.
- **Änderung.** Umbauen in vier Absätze.
  1. *Potenzial, vier Sätze.* 260 bis 262 mit Beleg `uenb_grenzwertkonzept_2021` für Spannungsgrenzwerte, systemische Grenzen und die Betriebsmittelkette. Die Kurzschlussfestigkeit in 262 trägt das Konzept nicht, dafür bleibt allein die SOGL, oder das Wort entfällt. 264 bis 266 entfallen (Q10, Q11), 267 mit *standort- und situationsabhängig, denn neben der Strecke bestimmen Vorbelastung und Witterung die zulässige Dauer*, 268 neu nach dem Konzept, solange der ÜNB den Stromkreis nicht für die Höherauslastung freigegeben hat, gilt die PATL.
  2. *Sicherheit, fünf Sätze.* 269 bis 273 und ein neuer Satz nach B97, nämlich dass der Ausfall der Kette nicht sofort schadet, weil die thermische Trägheit Zeit lässt, in der der ÜNB auf präventive Mittel zurückgreifen kann, nur später und teurer. Satz 274 entfällt (Vorverweis).
  3. *Planung, vier Sätze.* 275 bis 277 und ein neuer Satz nach B99, nämlich dass die Auswahl mit der Zahl kurativer Maßnahmen im Netz zur kombinatorischen Aufgabe wird, während KuPilot je Maßnahme nur entscheidet, ob sie eingeplant wird, und die Menge fest ist. **Hinweis des Betreuers, Beleg fehlt**, als Vorbehalt formulieren.
  4. *Umsetzung und Beschaffung, fünf Sätze.* 278 bis 283 unverändert.

### 2.1.5 Absatz 1, G 288 bis 300, Rechtsrahmen

- **Befunde.** B100 *beiden Kategorien* erklären. B101 *diesen Fall* benennen. B102 wozu der Normalzustand. B103 *sie* auflösen. B104 welches Zeitfenster. B105 der Schluss auf die Zulässigkeit ist nicht nachvollziehbar. B106 Konsequenz der echtzeitnahen Aktivierung. A5, Q13.
- **Änderung.** Umbauen in zwei Absätze.
  1. *EnWG, fünf Sätze.* 288 und 289 wie bisher. 290 neu, kurative Maßnahmen können netzbezogen oder marktbezogen sein, mit Doppelpunkt in die beiden Beispiele aus 291 und 292. 293 neu, die vorliegende Arbeit betrachtet allein den Fall, dass ein Akteur am Markt die Maßnahme erbringt.
  2. *SOGL und Binnenmarkt, fünf Sätze.* Die Schlusskette nach B105 in der Reihenfolge, erstens verlangt die SOGL, die Flüsse nach einem Ausfall innerhalb der vorübergehend zulässigen Überlast zu halten, zweitens rechnet sie die Wirkung vorbereiteter Entlastungsmaßnahmen dem Netzzustand zu, drittens knüpft sie an den Zeitpunkt ihres Einsatzes keine Bedingung, viertens bleibt das Netz deshalb auch dann im Normalzustand, wenn die Maßnahme erst nach dem Fehler und innerhalb der zulässigen Überlastdauer wirkt. Die Fundstelle Art. 32 Abs. 2 SOGL nach dem Protokolleintrag vom 01.09.2026. Satz 296 entfällt (B102, Q13), *sie* wird zu *die Leitlinie* (B103), *Zeitfenster* zu *zulässige Überlastdauer* (B104). Satz 299 schließt mit der Konsequenz, dass die Leitlinie einen Eingriff nach dem Fehler nicht nur zulässt, sondern für schlecht vorhersehbare Netzzustände vorzieht (B106). Satz 300 bleibt.

### 2.1.5 Absätze 2 und 3, G 302 bis 327

- **Befunde.** A5, nämlich § 13c auf zwei Sätze, § 17 Abs. 2b auf vier, § 13k auf drei, Schluss 320 und 321 zusammenziehen.
- **Änderung.** Kürzen nach A5, sonst unverändert. Die übergreifenden Regeln U3 und U5 anwenden.

---

## 4 Abschnitte 2.2 bis 2.4

Ohne Betreuerkommentare. Es gelten die Kürzungen aus `KUERZUNGEN_KAP1_2.md`
und die übergreifenden Regeln.

| Abschnitt | Kürzungen | Übergreifend |
|---|---|---|
| 2.2 Einleitung und 2.2.1 | G25, G26, G27, G28, Q4 | U1, U5 |
| 2.2.2 | G29, G30, G31, Q2, Q14 | U6 in G 376 bis 393 |
| 2.2.3 | G32, G33, Q8, Q18, A3 | U2 |
| 2.3 Einleitung und 2.3.1 | G34, G35, A4, P9 | U3 |
| 2.3.2 | A1, P5, Rundung nach Protokoll 08.09.2026 | U6 |
| 2.3.3 | G36, G37, P4 | U6 in G 629, 631 und 633 bis 638, der Absatz 629 trägt 13 Sätze |
| 2.3.4 | G38, G39, A3, Q17 | U2 |
| 2.3.5 | G39, Q18, Q20 | U6 |
| 2.4 | G40, Q9 | U1 |

---

## 5 Reihenfolge

1. Die Entscheidungen V1 bis V13, soweit sie nicht den Betreuer brauchen. V4, V8, V9 und V13 laufen parallel als Rückfragen.
2. Kapitel 1, denn es ist kurz und der Betreuer hat es vollständig kommentiert. Nach `WORKFLOW.md` ein Abschnitt je Zyklus, also Vorspann mit 1.1, dann 1.2.
3. Abschnitt 2.1 in der Reihenfolge der Unterabschnitte.
4. Die Abschnitte 2.2 bis 2.4 nach der Kürzungsliste, mit A1 zuerst.
5. Kapitel 3 nach `STRUKTUR.md`, mit den übergreifenden Regeln, aber ohne Betreuerkommentare.

Nach jedem Abschnitt läuft die Prüfsuite und die Fremdleser-Prüfung aus
`WORKFLOW.md`. Der Betreuer hat empfohlen, einen Absatz jemandem ohne Kenntnis
der kurativen Systemführung zu geben. Die Fremdleser-Prüfung ist der Ersatz
dafür, bis ein Mensch liest.

---

## Anhang, Kommentarliste B01 bis B106

Reihenfolge wie in der Kommentarübersicht des Betreuers. Die Spalte Absatz
verweist auf die Absätze in den Abschnitten 2 und 3 dieser Datei.

| Nr | Stelle | Kommentar des Betreuers, verkürzt | Absatz |
|---|---|---|---|
| B01 | Titel | These und Begründung strukturell verbinden, Text schwer lesbar, stringenter argumentieren | U1, U2 |
| B02 | Eidesstattliche Versicherung | KI-Nutzung angeben? | V1 |
| B03 | E 4 | Generisch, Bezug zu BESS und kurativ | Vorspann |
| B04 | E 11 | Achse Nord-Ost nach Süd-West | 1.1 Abs. 1 |
| B05 | E 15 | Deutschland gegen EU | 1.1 Abs. 2 |
| B06 | E 15 | These, dann Doppelpunkt | 1.1 Abs. 2, V3 |
| B07 | E 17 | An den ersten Satz hängen | 1.1 Abs. 2 |
| B08 | E 19 | Was heißt systematisch | 1.1 Abs. 2 |
| B09 | E 21 | Netzsituation ist Ergebnis des Marktes | 1.1 Abs. 2 |
| B10 | E 20 | Zugriff des ÜNB besser umschreiben | 1.1 Abs. 2 |
| B11 | E 24 | Redispatch vorher erwähnen | 1.1 Abs. 2 und 3, V12 |
| B12 | E 27 | Welche Ereignisabhängigkeit | 1.1 Abs. 3 |
| B13 | E 41 | These und Begründung verbinden | 1.1 Abs. 4 |
| B14 | E 45 | These und Erklärung verknüpfen | 1.1 Abs. 4 |
| B15 | E 46 | Liest sich komisch | 1.1 Abs. 4 |
| B16 | E 48, 50 | Welcher Bedarf | 1.1 Abs. 4 und 5 |
| B17 | E 52 | Was bedeutet das für die Maßnahmen | 1.1 Abs. 5 |
| B18 | E 63 | Zum einen, zum anderen, Zusammenhang | 1.1 Abs. 6 |
| B19 | E 64 | Wie passt die präventive Betriebsplanung dazu | 1.1 Abs. 6 |
| B20 | E 65 | Warum schwerer, Prozesse unbekannt | 1.1 Abs. 6 |
| B21 | E 71 | Was macht der Netzbetreiber, das Netz ist N-1-sicher | 1.1 Abs. 6, V13 |
| B22 | E 73 | Unklar, fachfremder Leser | 1.1 Abs. 7 |
| B23 | E 80 | Liest sich, als sei nur kurativ N-1-sicher | 1.1 Abs. 7 |
| B24 | E 88 | Vorhaltung von was | 1.2 Abs. 1, V2 |
| B25 | E 89, 90 | Zusammenhang zu InnoSys unklar | 1.2 Abs. 1 |
| B26 | E 91 | Höherauslastung reduziert den präventiven Redispatch | 1.2 Abs. 1 |
| B27 | E 88 bis 97 | Zu viele Aspekte, roter Faden | 1.2 Abs. 1 |
| B28 | E 99 | Übergang zu Simulationen | 1.2 Abs. 2 |
| B29 | E 100 | Welche Arbeit | 1.2 Abs. 2 |
| B30 | E 101 | Welches Zieljahr | 1.2 Abs. 2 |
| B31 | E 101 | Überprüfbarkeit als Argument ausführen | 1.2 Abs. 2 |
| B32 | E 101 | Welche erste Unsicherheit | 1.2 Abs. 2 |
| B33 | E 102 | Bindung und indifferent erklären | 1.2 Abs. 2 |
| B34 | E 103 | Eigenschaft der Anlage klingt technisch | 1.2 Abs. 2 |
| B35 | E 103 | Welche Arbeit | 1.2 Abs. 2 |
| B36 | E 104 | Ergibt der Satz Sinn | 1.2 Abs. 2 |
| B37 | E 105 | Bindungsdauer von was | 1.2 Abs. 2 |
| B38 | E 105 | Reaktionszeit definiert? | 1.2 Abs. 2 |
| B39 | E 109 | Kapitel untersucht etwas? | 1.2 Abs. 3, U5 |
| B40 | G 4 | Kurative Vorhaltung sauber definieren | Kap. 2 Einleitung, V2 |
| B41 | G 7 | Siehe oben, Subjekt | Kap. 2 Einleitung, U5 |
| B42 | G 27 | Welche Ansätze | 2.1.1 Abs. 1 |
| B43 | G 29 | Ausfallvariantenliste erklären, Exkurs | 2.1 Einleitung, V11 |
| B44 | G 34 | Schön | bleibt |
| B45 | G 57 | Anpassungen sind meist präventiver Redispatch | 2.1.1 Abs. 2 |
| B46 | G 61 | Engpässe definieren, N-1 und Befunde | 2.1 Einleitung, V11 |
| B47 | G 65 | Da passt etwas nicht | 2.1.1 Abs. 3 |
| B48 | G 66 | Der Betrag statt die Breite | 2.1.1 Abs. 3 |
| B49 | G 66 | Marge ist keine Wahl | 2.1.1 Abs. 3 |
| B50 | G 67 | Was heißt Reichweite | 2.1.1 Abs. 3, V5 |
| B51 | G 68 | Prozess mit Zeiten darstellen | 2.1.1 Abs. 3 |
| B52 | G 71 | Wobei | 2.1.1 Abs. 3 |
| B53 | G 74 | Reichweite | 2.1.1 Abs. 4, V5 |
| B54 | G 80 | Reichweite | 2.1.1 Abs. 5, V5 |
| B55 | G 82 | Kurativ wird auch vorgeplant, andere Grenzwerte | 2.1.1 Abs. 5 |
| B56 | G 82 | Behebt die Verletzung nach ihrem Eintritt | 2.1.1 Abs. 5 |
| B57 | G 83 | Reichweite | 2.1.1 Abs. 5, V5 |
| B58 | G 83 | Präventiver Redispatch deckt das auch ab | 2.1.1 Abs. 5, V13 |
| B59 | G 80 | Welche zwei Ausprägungen | 2.1.1 Abs. 5 |
| B60 | G 87 | Referenz | 2.1.1 Abs. 5 |
| B61 | G 84 | Welche Ausprägungen | 2.1.1 Abs. 5 |
| B62 | G 93 | Spät worauf bezogen | 2.1.1 Abs. 6 |
| B63 | G 118 | Steht *aktiviert* so in der Referenz, Wortwahl | 2.1.2 Abs. 1, V4, V9 |
| B64 | G 128 | HGÜ und Netzbooster gibt es noch nicht | 2.1.2 Abs. 3 |
| B65 | G 124 bis 130 | Stand der Technik und Planung trennen | 2.1.2 Abs. 3 |
| B66 | G 148 | Eng im Sinne von was | 2.1.2 Thermik, V6 |
| B67 | G 174 | Referenz oder weniger absolut | 2.1.2 Thermik, V6 |
| B68 | G 177 | Unterscheidung Grenztemperatur und Alterung | 2.1.2 Thermik, V6 |
| B69 | G 183 | Weitere Bedingungen, Grenzwertkonzept | 2.1.2 Abs. 7, V8 |
| B70 | G 195 | Mehrmals lesen müssen | 2.1.3 Abs. 1 |
| B71 | G 197 | Welcher Mechanismus | 2.1.3 Abs. 1 |
| B72 | G 198 | Wer, der Mechanismus? | 2.1.3 Abs. 1 |
| B73 | G 198 | Wer | 2.1.3 Abs. 1 |
| B74 | G 200 | Bestand von was | 2.1.3 Abs. 1 |
| B75 | G 201 | Oben zwei, jetzt vier | 2.1.3 Abs. 1 |
| B76 | G 202 | Bemessungsgrundlage erklären | 2.1.3 Abs. 1 |
| B77 | G 204 | Was für ein Netz | 2.1.3 Abs. 1 |
| B78 | G 210 | Vorlaufzeit eines stehenden Kraftwerks als Ausschluss? | 2.1.3 Abs. 2 |
| B79 | G 211 | Wie schnell, welcher Bestand | 2.1.3 Abs. 2 |
| B80 | G 214 | Dargebot nicht pauschal, Wind gegen PV | 2.1.3 Abs. 2 |
| B81 | G 215 | Wie in Abschnitt beschrieben, nicht jede Maßnahme bilanziert | 2.1.3 Abs. 2 |
| B82 | G 215 | Quelle und Senke vertauscht | 2.1.3 Abs. 2 |
| B83 | G 216 | Trägt | 2.1.3 Abs. 2 |
| B84 | G 217 | KuPilot auf eine Stunde begrenzt | 2.1.3 Abs. 2, V9 |
| B85 | Tab. 2.1 | Näher an den Text | V10 |
| B86 | G 216, 236 | Was ist groß, relativ | 2.1.3 Abs. 2, Tabelle |
| B87 | G 249 | Wachstum sichert den Knoten nicht | 2.1.3 Abs. 3 |
| B88 | G 250 | Übergang schaffen | 2.1.3 Abs. 3 |
| B89 | G 250 | *Diese* passt logisch nicht | 2.1.3 Abs. 3 |
| B90 | G 251 | Ihre, welche | 2.1.3 Abs. 3 |
| B91 | G 253 | Relativ klein bleiben kann | 2.1.3 Abs. 3 |
| B92 | G 254 | Verlagerung auf die Vorhaltung unklar | 2.1.3 Abs. 3 |
| B93 | G 255 | Abschluss mehr Raum | 2.1.3 Abs. 3 |
| B94 | G 262 | Referenz Grenzwertkonzept | 2.1.4, V8 |
| B95 | G 267 | Auch Vorbelastung und Witterung | 2.1.4 |
| B96 | G 268 | Was heißt sichere Seite, PATL | 2.1.4 |
| B97 | G 272 | Thermische Trägheit, Zeit, konventioneller Redispatch möglich | 2.1.4 |
| B98 | G 275 | Absatz eingefügt, öfter machen | 2.1.4, U6 |
| B99 | G 277 | Effekt dominanter bei mehr Maßnahmen, KuPilot binär | 2.1.4 |
| B100 | G 290 | Was heißt beide Kategorien | 2.1.5 Abs. 1 |
| B101 | G 293 | Welchen Fall | 2.1.5 Abs. 1 |
| B102 | G 296 | Normalzustand, um was zu machen | 2.1.5 Abs. 1 |
| B103 | G 295 | *Sie* konkret angeben | 2.1.5 Abs. 1 |
| B104 | G 298 | Welches Zeitfenster | 2.1.5 Abs. 1 |
| B105 | G 298 | Schluss nicht nachvollziehbar | 2.1.5 Abs. 1 |
| B106 | G 299 | Konsequenz | 2.1.5 Abs. 1 |
