# Änderungsliste Kapitel 3

Stand 14.09.2026. Arbeitsdokument für die Korrektur nach `WORKFLOW.md`, als
Gegenstück zu `AENDERUNGEN_KAP1_2.md`.

Der Betreuer hat Kapitel 3 nicht kommentiert. Diese Liste entsteht aus der
Prüfung des Fließtexts gegen die Stilregeln in `CLAUDE.md` Abschnitt 4, gegen
die übergreifenden Änderungen U1 bis U10 und gegen die offenen Punkte in
`STRUKTUR.md` und im Protokoll. Befunde tragen die Kennung **K** und eine
laufende Nummer. Zeilenangaben beziehen sich auf
[chapter_3.tex](chapters/chapter_3.tex) in der Fassung 4b7e223, Kommentarzeilen
mitgezählt. Die Datei trägt 4120 Kommentarzeilen auf 467 Textzeilen, die
Zeilennummern springen deshalb.

Gemessen am Build vom 14.09.2026 läuft das Kapitel von Seite 35 bis 50, also 16
Seiten bei einem Ziel von 14. Abschnitt 5 nennt die Hebel.

Nichts davon ist umgesetzt.

---

## 0 Entscheidungen des Verfassers vor Beginn

| Nr | Frage | Vorschlag | Betrifft | Stand |
|---|---|---|---|---|
| W1 | **Mindestgröße im Standardlauf.** Zeile 3573 sagt, das Modell rechne im Standard mit stetiger Reservierung und schalte die Mindestgröße nur dort zu, wo ihre Wirkung geprüft wird. Der Basisfall vom 11.09.2026 nennt 25 MW Mindestgröße und damit ein gemischt-ganzzahliges Programm, und die Zeilen 2398 und 2399 beschreiben genau dieses. | Klären, wie der Code tatsächlich rechnet. Gilt die Mindestgröße im Basisfall, entfällt Satz 3573. Gilt sie nur in einer Sensitivität, ist der Basisfall in `CLAUDE.md` Abschnitt 7 und in `STRUKTUR.md` zu berichtigen und 2398 bis 2400 als Sensitivität zu fassen. | 3.2.1, 3.2.3, CLAUDE.md | offen |
| W2 | **Ablaufdiagramm und Schleifenabbildung.** `fig:reservierungspreis_ablauf` ist eine A4-Grafik und füllt eine Seite, `fig:schleifenebenen` eine halbe. Zusammen mit `fig:modellkette` und `fig:reservierungspreis_bisektion` tragen die Abbildungen von 3.2 rund drei Seiten. | Ablaufdiagramm und Schleifenabbildung nach Anhang B, im Text bleibt je ein Verweis. Modellkette und Bisektion bleiben. Ersparnis rund 1,5 Seiten, damit ist das Ziel von 14 Seiten erreichbar. | 3.2.4, Anhang B | offen |
| W3 | **Reaktionszeitklassen zwei, fünf und zehn Minuten** (Zeile 1428) gegen die drei InnoSys-Klassen unter zehn Sekunden, etwa zwei Minuten und bis 15 Minuten in Kapitel 2 Zeile 186. Die Begründung der Abweichung ist am 11.09.2026 gestrichen worden. | Ein Halbsatz, weshalb die Klassen enger geschnitten sind als bei InnoSys, sonst fragt der Leser. Wortlaut vom Verfasser, weil er die Klassen gesetzt hat. | 3.1.2 | offen |
| W4 | **Wort Grenzpreis für den höchsten Zuschlag der aFRR** (Zeilen 3434, 3435). Grenzpreis ist nach `CLAUDE.md` Abschnitt 5 für den Grenzpreis des Speichers im Weber-Ansatz belegt. | In der Leiter *höchster Zuschlag* schreiben, wie es Zeile 3427 und 3430 schon tun. | 3.2.3 | offen |
| W5 | **Ergebnis der Validierung.** 3.3.2 formuliert das Prüfkriterium und verweist auf die Abbildung, sagt aber nicht, ob das Kriterium erfüllt ist. Nach `STRUKTUR.md` darf 3.3 Zahlen tragen. | Ein Absatz mit dem Ergebnis, nämlich ob Jahresgang, Richtung in den Leistungsmärkten und Richtung in den Energiemärkten stimmen, mit den Zahlen aus der Abbildung. Ohne diesen Absatz hat der Abschnitt keine Konsequenz. | 3.3.2, Anhang C | offen |
| W6 | **Schlüsseltechnologie** (Zeile 85). Der Satz behauptet mehr als Abschnitt 2.1.3 trägt, Protokoll offener Punkt 16. | Zurücknehmen auf das, was 2.1.3 zeigt, nämlich dass BESS die geforderten Eigenschaften vereinen und an vielen Knoten in Betracht kommen. | Kapiteleinleitung | offen |
| W7 | **Bildunterschriften in 3.2** auf ein bis drei Zeilen, Vorgabe des Verfassers, fünf Vorschläge liegen nach `STRUKTUR.md` vor, die Freigabe steht aus. | Mit W2 zusammen entscheiden. | 3.2 | offen |

---

## 1 Übergreifende Änderungen in Kapitel 3

Die Regeln U1 bis U10 aus `AENDERUNGEN_KAP1_2.md` gelten. Die Suche über den
Fließtext hat folgende Fundstellen ergeben.

| Regel | Fundstellen |
|---|---|
| U3, Pronomen am Satzanfang ohne Bezug im selben Satz | 84 *Sie*, 590 *Sie*, 1564 *Er*, 1656 *Diese drei Eigenschaften*, 1776 *Dabei vergleichen sie*, 2112 *Er*, 3078 *Sie*, 4444 *Er*, 4445 *Seine*, 4504 *Sein* |
| U5, Kapitel, Abschnitt oder Arbeit als handelndes Subjekt | 97 *Dieses Kapitel leitet ab*, 333 *Dieser Abschnitt stellt zusammen*, 2111 *Diese Arbeit bestimmt*, 2405 *nach Abschnitt*, 4258 *Der Ansatz nach Abschnitt* |
| U6, Absätze über acht Sätzen | 740 bis 877 Katalog mit 24 Sätzen, 1515 bis 1583 mit 15, 2392 bis 2400 mit 9, 2402 bis 2413 mit 12, 2874 bis 2936 mit 16, 3305 bis 3320 mit 9, 3426 bis 3435 mit 11, 3876 bis 3885 mit 10, 4258 bis 4267 mit 10 |
| U6, Absätze mit ein bis zwei Sätzen, die keinen Absatz tragen | 333, 578 und 590, 1288 und 1305, 1434 |
| U8, Feststellung ohne Beleg | 2874 *Größenordnung bestehender Anschlüsse im Hoch- und Höchstspannungsnetz*, 3429 eigene Rechnung ohne Vermerk, 3885 eigene Rechnung, 4125 Laufzeit |
| Stilregel 13, Jargon ohne Erklärung | 783 *Lokationalität*, 1412 *Opportunitätskosten*, 1664 und 1776 *Sensitivität des Netzknotens*, 4259 *einperiodig*, 3878 *Füllgrad* |
| Stilregel 14, Begriffskonstanz | 86, 87, 590, 804 *kurative Vorhaltung* gegen *kurative Reservierung* nach V2 prüfen, 843 *kurative Bindung*, 1560 und 1583 *kurative Zusage*, 3434 *Grenzpreis* (W4), 97 *Erlösvergleich* gegen 4440 *Erlösindex* |
| V4, aktivieren | 3485 *aktivierte Volumen* bleibt, weil es die Regelarbeit auf PICASSO meint und dort der Fachausdruck ist |

Verstärkende Adjektive, das Wort Reichweite und strukturelle Vorverweise auf
Kapitel 4 bis 6 kommen im Fließtext nicht vor.

---

## 2 Kapiteleinleitung und 3.1

### Kapiteleinleitung, Zeilen 83 bis 97

- **Kernaussage.** Die kurative Systemführung braucht ein eigenes Produkt, und dieses Kapitel entwirft es und bestimmt seinen Preis.
- **Befunde.** K01 Zeile 84 *Sie* auflösen. K02 Zeile 85 *Schlüsseltechnologie* und *damit* ohne tragende Begründung, W6. K03 Zeile 86 *ihrer Vergütung* ohne klaren Bezug, gemeint ist die Vergütung der BESS. K04 Zeilen 86 und 87 *kurative Vorhaltung* nach V2, hier ist das Produkt gemeint, also *kurative Reservierung*. K05 Zeile 97 *Dieses Kapitel leitet ab* nach U5, und *Erlösvergleich* durch *Erlösindex* ersetzen. K06 Zeile 97 sagt *prüft*, während 3.3 ausdrücklich nur die Plausibilität des Erlösniveaus prüft, die Behauptung angleichen.
- **Änderung.** Umbauen auf sechs Sätze. Die ersten beiden bleiben mit aufgelöstem Bezug. Dritter Satz nach W6. Vierter und fünfter mit *kurative Reservierung*. Überblickssatz in der Form *In diesem Kapitel werden ... abgeleitet* mit der Validierung als Plausibilitätsprüfung des ungebundenen Erlöses.

### Einleitung 3.1, Zeile 333

- **Befunde.** K07 Ein Satz allein, U6. K08 *Dieser Abschnitt stellt zusammen*, U5. K09 Die Aussage, das Produkt konkurriere nicht mit dem präventiven Redispatch um dieselbe Leistung, nimmt A7 vorweg und ist an dieser Stelle unbegründet.
- **Änderung.** Kürzen auf einen Überleitungssatz ohne die Konkurrenzaussage und mit dem ersten Absatz von 3.1.1 verbinden, oder streichen, weil die Kapiteleinleitung den Aufbau schon nennt.

### 3.1.1 Einleitung, Zeilen 578 und 590

- **Befunde.** K10 Zwei Sätze mit Lücke dazwischen, *Sie gelten* ohne Bezug im Satz, U3 und U6.
- **Änderung.** Beide Sätze als Einleitung des Katalogs zusammenziehen, mit *Die Anforderungen gelten*.

### 3.1.1 Katalog, Zeilen 740 bis 877

- **Kernaussage.** Acht Anforderungen, jede mit These und Begründung.
- **Befunde.** K11 24 Sätze in einer Umgebung, was für einen Katalog zulässig ist, aber jede Anforderung sollte auf These plus höchstens zwei Begründungssätze begrenzt sein. A1 hat drei, A2 drei, A4 vier, A5 drei, A7 drei. K12 Zeile 783 *Lokationalität* erklären oder durch *Knotenschärfe* ersetzen, Stilregel 13. K13 Zeile 804 *kurative Vorhaltung* nach V2 richtig, weil hier die Tätigkeit gemeint ist, prüfen. K14 Zeile 843 *kurative Bindung* gegen *Bindung* nach der Definition in 1.2. K15 Zeile 877 *Verbund von Geboten* ist der Begriff, den P7 für Kapitel 2 verlangt, hier ist er richtig eingeführt.
- **Änderung.** Kürzen auf höchstens drei Sätze je Anforderung, Ersparnis rund acht Sätze. Reihenfolge und Nummern bleiben, weil Kapitel 5 darauf verweist.

### 3.1.2 Einleitung und Zusage, Zeilen 1288 bis 1414

- **Kernaussage.** Die Reservierung bindet Leistung und Ladezustand, vergütet wird die Vorhaltung, und die Anlage darf weiterhandeln.
- **Befunde.** K16 Zeilen 1288 und 1305 zwei Sätze allein, U6, mit dem Zusageabsatz verbinden. K17 Zeile 1411 sagt, der Preis decke auch die Energie eines Abrufs, Zeile 4265 sagt, das Modell bilde diesen Anteil nicht ab. Beides stimmt, aber der Leser muss den Zusammenhang hier erfahren, ein Halbsatz genügt. K18 Zeile 1412 *Opportunitätskosten* ist nach der Änderungsliste in 1.2 Absatz 2 erklärt, die Erklärung dort ist Voraussetzung. K19 Zeile 1413 *doch* als Konjunktion ist umgangssprachlich, *aber*.
- **Änderung.** Umbauen auf einen Absatz mit acht Sätzen, Anschluss nach K17.

### 3.1.2 Reaktionszeit und Bindungsdauer, Zeilen 1424 bis 1434

- **Befunde.** K20 W3 zu den Klassen. K21 Zeile 1434 ist ein Satz allein, die Bindungsdauer bekommt keinen Absatz, und die Definition steht nach der Änderungsliste bereits in 1.2. Hier bleibt allein die Setzung, nämlich eine Stunde je Zeitscheibe.
- **Änderung.** Zeile 1434 mit dem Klassenabsatz verbinden und um die Setzung ergänzen, die derzeit erst in Zeile 1765 steht.

### 3.1.2 Abruf und Erfüllung, Zeilen 1515 bis 1583

- **Kernaussage.** Der ÜNB löst den Abruf aus, die Anlage hält höchstens eine Stunde, danach gilt eine Nachlaufpflicht, und die Erfüllung ist binär und mit Pönale bewehrt.
- **Befunde.** K22 15 Sätze, U6, zwei Themen, nämlich Abruf und Nachweis. K23 Zeile 1564 *Er weist* nach U3. K24 Zeile 1583 nennt drei Sanktionsformen ohne Wahl, die Arbeit entscheidet die Pönale nicht, Entscheidung 5, der Satz sollte das sagen. K25 Zeile 1549 sagt *nicht Gegenstand dieser Arbeit*, das ist ein zulässiger Vorbehalt, aber *dieser Arbeit* nach U4 als *der vorliegenden Arbeit*.
- **Änderung.** Teilen in *Abruf und Freistellung* mit 1515 bis 1557 und *Nachweis und Pönale* mit 1560 bis 1583. Der zweite Absatz endet mit der Konsequenz aus K24.

### 3.1.2 Präqualifikation, Zeilen 1655 bis 1677

- **Befunde.** K26 Zeile 1656 *Diese drei Eigenschaften* mit Bezug im Vorsatz, nach U3 ausschreiben. K27 Zeile 1664 *Sensitivität des Standorts* ist im Kapitel nicht erklärt, seit die PTDF-Sätze am 14.09.2026 aus A3 entfallen sind, ein Halbsatz nach dem Muster *also wie stark eine Leistungsänderung an diesem Knoten das Betriebsmittel entlastet*. K28 `STRUKTUR.md` Punkt 5, der Entzug der Präqualifikation ist in den Bedingungen nicht geregelt, der Rahmenvertrag liegt nicht vor, deshalb in Zeile 1583 nicht als geregelte Sanktion darstellen.
- **Änderung.** Umbauen mit K26 und K27, sonst behalten.

### 3.1.2 Ausschreibung, Gebot und Zuschlag, Zeilen 1760 bis 1779

- **Befunde.** K29 Zeile 1776 *Dabei vergleichen sie* nach U3. K30 Zeile 1772 *etwa* ist zweideutig, *zum Beispiel*. K31 Zeile 1779 hängt an der Frist von 30 Minuten vor Lieferung aus Kapitel 2 Zeile 385, mit Kapitel 2 stimmig, prüfen nach der Korrektur von 2.2.2.
- **Änderung.** Zwei Absätze behalten, K29 und K30 einarbeiten.

---

## 3 Abschnitt 3.2

### Einleitung 3.2, Zeilen 2107 bis 2144

- **Kernaussage.** Der Preis ist aus dem Betrieb des Speichers zu bestimmen, und das Modell tut das, indem es dem Betreiber einen Preis vorgibt.
- **Befunde.** K32 Zeile 2111 *Diese Arbeit bestimmt* nach U5, etwa *Bestimmt wird deshalb* oder *Das Modell bestimmt*. K33 Zeile 2112 *Er liefert* nach U3. K34 Zeile 2143 *Dazu* knüpft an einen Absatz an, der durch die Abbildung getrennt ist, den Bezug nennen.
- **Änderung.** Umbauen, Sätze und Reihenfolge bleiben.

### 3.2.1 Modellansatz, Zeilen 2245 bis 2400

- **Kernaussage.** Das Modell führt den ungebundenen Fahrplan mit, koppelt den Ladezustand und entscheidet alle Märkte unter vollständiger Preiskenntnis, weshalb der Preis eine obere Schranke ist.
- **Befunde.** K35 Zeilen 2392 bis 2400 tragen neun Sätze und zwei Themen, nämlich die vollständige Preiskenntnis mit ihrer Folge und die Struktur des Programms. K36 Zeilen 2397 bis 2400 beantworten die alten offenen Punkte zu linearem oder gemischt-ganzzahligem Programm und zur Nennung von Gurobi, mit W1 abzugleichen. K37 Zeile 2394 trägt die Konsequenz, der Preis falle eher zu hoch aus, das ist gut und soll den ersten Absatz schließen.
- **Änderung.** Teilen in *Preiskenntnis und Schranke* mit 2245 bis 2394 und *Programm und Lösung* mit 2395 bis 2400.

### 3.2.1 Systemgrenzen, Zeilen 2402 bis 2413

- **Kernaussage.** Das Modell betrachtet eine Anlage ohne Netz, ohne Abruf und ohne Intraday-Auktionen und mFRR, und jede Auslassung wirkt in eine benennbare Richtung auf den Preis.
- **Befunde.** K38 Zwölf Sätze als Aufzählung ohne These und ohne Konsequenz, U1, U2, U6. K39 Zeile 2405 *nach Abschnitt* nach U5. K40 Zeile 2407 *Der Zuschlag gilt als sicher* steht allein, die Folge steht erst in 3.3.2 Zeile 4506, hier den Halbsatz ergänzen, dass das die Erlöse der Leistungsmärkte überschätzt. K41 Die Abrufwahrscheinlichkeit und die Pönale in Zeile 2406 und in 3.2.4 Zeile 4266 doppelt, eine Stelle genügt, naheliegend 3.2.4, weil dort die Gebotsbestandteile stehen.
- **Änderung.** Teilen in *Was das Modell nicht abbildet* mit 2402 bis 2407 und *Welche Märkte es nicht führt* mit 2409 bis 2413, jeder Absatz mit einem Leitsatz und einem Schlusssatz zur Richtung der Wirkung auf den Preis.

### 3.2.2 Anlage, Speicher und Zielfunktion, Zeilen 2874 bis 2936

- **Befunde.** K42 16 Sätze in einem Absatz, U6. K43 Zeile 2874 *Größenordnung bestehender Anschlüsse* ohne Beleg, U8, in Betracht kommt die ISEA-Datenbasis oder der Monitoringbericht, sonst abschwächen. K44 Zeile 2902 *8 Euro je Megawattstunde* wird erst in Zeile 2923 belegt, beide Sätze zusammenrücken. K45 Zeile 2926 zählt neun Variablengruppen in einem Satz, zulässig, aber Tabelle B.1 im Anhang trägt dasselbe, ein Verweis genügt.
- **Änderung.** Teilen in *Anlage* mit 2874 bis 2877, *Degradation* mit 2902 bis 2924, *Zeit, Variablen und Bilanz* mit 2925 bis 2930 und *Zielfunktion* mit 2931 bis 2936. Ersparnis rund drei Sätze durch K45.

### 3.2.3 Einleitung und Tabelle, Zeilen 3077 bis 3209

- **Befunde.** K46 Zeile 3078 *Sie wirken* nach U3. K47 Tabelle 3.1 steht nach dem Verweis in 3118, Stilregel 16 erfüllt.
- **Änderung.** K46, sonst behalten.

### 3.2.3 Day-Ahead, Zeilen 3241 bis 3259

- **Befunde.** Keine. Fünf Sätze, Beleg, Gleichung.

### 3.2.3 Kontinuierlicher Intraday-Handel, Zeilen 3305 bis 3320

- **Befunde.** K48 Neun Sätze, zwei Themen, nämlich Bewertung mit dem ID1 und der Aufschlag. K49 Zeile 3318 *dessen Höhe als Sensitivität variiert wird* im Passiv, Stilregel 12, und der Sachverweis auf die Sensitivität in Kapitel 4 ist zulässig, aber das Kapitel sollte genannt werden.
- **Änderung.** Teilen bei Zeile 3317.

### 3.2.3 FCR, Zeilen 3340 bis 3377

- **Befunde.** Keine.

### 3.2.3 aFRR-Leistung, Zeilen 3426 bis 3440

- **Befunde.** K50 Elf Sätze, zwei Themen, nämlich der Preisansatz und die Bindung mit der Leiter. K51 Zeile 3429 ist eine eigene Rechnung aus den Ausschreibungsdaten, im Belegzettel als solche führen und im Text *nach eigener Auswertung der Ausschreibungsdaten* ergänzen. K52 Zeile 3434 *Grenzpreis*, W4. K53 Zeile 3434 zählt sechs Stufen in einem Satz, schwer lesbar, entweder als Aufzählung mit *nämlich* in zwei Sätzen oder als Verweis auf die Tabelle der Sensitivitäten in Kapitel 4.
- **Änderung.** Teilen bei Zeile 3431, K51 bis K53 einarbeiten.

### 3.2.3 aFRR-Arbeit, Zeilen 3484 bis 3494

- **Befunde.** K54 Zeile 3485 *aktivierte* bleibt, Regelarbeit. Sonst keine.

### 3.2.3 Kurative Reservierung, Zeilen 3563 bis 3573

- **Befunde.** K55 Zeile 3573 gegen den Basisfall, W1. K56 Zeile 3567 trägt die Kernaussage des ganzen Modells, nämlich dass die Anlage nur reserviert, wenn der Preis die entgangenen Erlöse übersteigt, sie sollte den Absatz eröffnen oder schließen und nicht in der Mitte stehen.
- **Änderung.** Umbauen nach W1 und K56.

### 3.2.4 Suche, Zeilen 3876 bis 3885 und 4029 bis 4033

- **Kernaussage.** Eine Bisektion außerhalb der Optimierung findet je Stunde den Preis der vollen Reservierung, und eine zweite Iteration löst die Kopplung der Stunden auf.
- **Befunde.** K57 Zehn Sätze, zwei Themen, nämlich das Prinzip mit dem Füllgrad und die erste Iteration. K58 Zeile 3878 *Füllgrad* wird im selben Satz definiert, gut, aber die Toleranz *0,01 MW von 100 MW* ist eine Anlagenzahl im Verfahrensabsatz, als Anteil schreiben. K59 Zeile 3885 eigene Rechnung, Belegzettel. K60 W2 zu den Abbildungen.
- **Änderung.** Teilen in *Prinzip* mit 3876 bis 3878 und *Erste Iteration* mit 3879 bis 3885. Der Absatz zur zweiten Iteration bleibt.

### 3.2.4 Schleifen, Zeilen 4125 bis 4128

- **Befunde.** K61 Zeile 4125 Laufzeit ohne Rechnerangabe, entweder mit Rechner oder streichen. K62 W2 zur Schleifenabbildung.
- **Änderung.** Nach W2, sonst behalten.

### 3.2.4 Abgrenzung und Gebotsbestandteile, Zeilen 4258 bis 4267

- **Kernaussage.** Der Weber-Ansatz lässt sich aus drei methodischen Gründen nicht in das Modell einbetten, und der ermittelte Preis ist der opportunitätskostenbasierte Teil des Gebots.
- **Befunde.** K63 Zehn Sätze, zwei Themen. K64 Zeile 4258 *Der Ansatz nach Abschnitt* nach U5. K65 Zeile 4259 *einperiodig* trifft nicht, das Modell führt 96 Perioden, gemeint ist *deterministisch mit vollständiger Preiskenntnis*, das Wort streichen. K66 Zeile 4266 doppelt mit 2406, K41. K67 Zeile 4267 ist die Konsequenz und steht richtig am Ende.
- **Änderung.** Teilen in *Drei methodische Gründe* mit 4258 bis 4262 und *Bestandteile des Gebots* mit 4263 bis 4267.

---

## 4 Abschnitt 3.3

### 3.3.1 Vergleichsmaßstab, Zeilen 4440 bis 4447

- **Befunde.** K68 Zeilen 4441 und 4442 tragen zwei Verneinungen hintereinander, erst sagen, was geprüft wird, dann, was nicht. K69 Zeilen 4443 bis 4445 *er*, *Er*, *Seine* nach U3. K70 Die Begründung, weshalb 3.3 Zahlen trägt, obwohl es vor den Ergebnissen steht, soll der Abschnitt nach `STRUKTUR.md` selbst sagen, sie fehlt.
- **Änderung.** Umbauen auf acht Sätze mit K68 bis K70.

### 3.3.2 Unterschiede und Ergebnis, Zeilen 4503 bis 4517

- **Befunde.** K71 Zeile 4504 *Sein Intraday-Handel* nach U3. K72 W5, das Ergebnis fehlt. K73 Bildunterschrift 4515 führt *Tausend Euro je Megawatt und Jahr*, das ist die Einheit des Index, Protokoll offener Punkt 18, mit dem Preis in Euro je Megawatt und Stunde nicht zu verwechseln, ein Halbsatz im Text.
- **Änderung.** Absatz 4503 bis 4510 behalten mit K71. Neuer Absatz nach der Abbildung mit dem Ergebnis nach W5, vier bis sechs Sätze, dazu der Verweis auf Anhang C für den Vergleich je Markt.

---

## 5 Seitenziel

Das Kapitel muss zwei Seiten verlieren. Die Hebel in der Reihenfolge ihrer
Ersparnis.

| Hebel | Ersparnis in Seiten | Entscheidung |
|---|---|---|
| Ablaufdiagramm und Schleifenabbildung nach Anhang B | 1,5 | W2 |
| Katalog auf drei Sätze je Anforderung | 0,4 | K11 |
| Variablenliste 2926 als Verweis auf Anhang B | 0,1 | K45 |
| Abruf und Erfüllung von 15 auf 11 Sätze | 0,2 | K22 |
| Systemgrenzen ohne die Doppelung zur Abrufwahrscheinlichkeit | 0,1 | K41 |
| Bildunterschriften kürzen | 0,2 | W7 |

Zusammen rund 2,5 Seiten, davon 1,5 allein aus W2. Ohne W2 ist das Ziel nicht
zu erreichen, es sei denn, 3.1.2 wird um eine Seite gekürzt, was die
Produktbeschreibung ausdünnt, auf der Kapitel 5 aufsetzt.

---

## 6 Reihenfolge

1. W1 bis W7 entscheiden, W1 vorab, weil er den Basisfall berührt.
2. Kapiteleinleitung und 3.1 in einem Zyklus je Unterabschnitt.
3. 3.2.1 und 3.2.2, dann 3.2.3 je Markt, dann 3.2.4.
4. 3.3 zuletzt, weil W5 die Zahlen aus dem Rechenlauf 2025 braucht.
5. Nach dem Kapitel bauen und den Seitenstand messen.

Der Kapitelüberblick in `chapter_1.tex` Zeilen 128 bis 130 wird nach diesem
Kapitel nachgezogen, siehe P1 in `KUERZUNGEN_KAP1_2.md`.
