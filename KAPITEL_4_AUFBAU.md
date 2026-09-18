# Aufbau von Kapitel 4, Aufnahme des Ist-Zustands und neue Sortierung

**Stand 17.09.2026.** Stichpunktphase nach `WORKFLOW.md` Abschnitt 3, also vor
dem ersten Absatzplan. Diese Datei enthält Vorschläge und keine Beschlüsse. Sie
verarbeitet `PLANUNG_KAPITEL_4.md` aus dem Modellrepository, den Wortlaut der
Kapitel 1 bis 3, die Entscheidungen 1 bis 14 aus `CLAUDE.md` Abschnitt 7 und die
offenen Punkte 9, 17 und 21 des Protokolls.

**Vorbehalt zu allen Zahlen.** Der Gesamtlauf vom 17.09.2026, 14:12 Uhr, läuft
noch. Die Zahlen dieser Datei stammen aus dem Lauf vom 15.09.2026
(`jahr_stunden_2025.parquet`, 15.09. 23:04) und aus `erloesaufteilung_afrr.csv`
vom 17.09. 09:57. Sie dienen der Sortierung und nicht dem Text. Vor dem ersten
Absatzplan sind sie neu zu lesen. Abschnitt 8 listet auf, was ich selbst
gerechnet habe.

---

## 1 Was Kapitel 4 tragen muss

### 1.1 Der Auftrag aus Kapitel 1

Abschnitt 1.2 stellt drei Teilfragen. Kapitel 4 trägt davon allein die zweite,
nämlich wie sich eine Reservierung auf Fahrplan und Erlöse einer Anlage
auswirkt, und liefert die Zahl zur Leitfrage, nämlich den kurativen
Reservierungspreis. Die dritte Teilfrage, die Einordnung in die bestehenden
Vergütungslogiken, gehört nach Kapitel 5. Die erste, der Anforderungskatalog,
ist in 3.1.1 abgearbeitet.

Abschnitt 1.2 legt außerdem die Messgröße fest, und Kapitel 4 darf sie nicht
verschieben: der kurative Reservierungspreis ist *der kleinste Preis, bei dem ein
Anlagenbetreiber die Leistung über die Bindungsdauer vollständig reserviert,
statt sie anderweitig zu vermarkten*. Er misst die Opportunitätskosten der
**zuletzt** reservierten Leistung und nicht die des ganzen Bandes.

### 1.2 Der Anschluss nach hinten, an 3.3.3

Kapitel 3 endet mit dem Fahrplan des 11.02.2025 bei einem vorgegebenen
Reservierungspreis von 5 Euro je Megawatt und Stunde und mit dem Satz, das
Verfahren sei für die Suche nach dem kleinsten vorgegebenen Reservierungspreis
bestätigt. Genau dort setzt Kapitel 4 an: Das Verfahren ist geprüft, und es läuft
nun über alle Tage des Jahres 2025.

Damit liegt die Überleitung fest. Sie lautet in der Sache, dass die Prüfung am
Einzeltag die Funktionsweise belegt, die Höhe des Preises aber erst der Jahreslauf
zeigt, weil ein einzelner Tag weder die Spannweite noch den Jahresgang trägt.

### 1.3 Der Anschluss nach vorn, an Kapitel 5

Kapitel 5 braucht aus Kapitel 4 genau fünf Befunde, und jeder von ihnen ist in
der neuen Sortierung an einen Abschnitt gebunden.

| Befund für Kapitel 5 | entsteht in |
|---|---|
| Höhe und Streuung des Preises, als Zahl mit Einheit | 4.1 |
| Lage der teuren Stunden im Tag und im Jahr | 4.2 |
| Verhältnis des Preises zum Engpassbedarf | 4.3 |
| Zahlung bei vollständiger Bindung gegen den Referenzerlös | 4.4 |
| Welcher Markt die Opportunität setzt | 4.5 |

### 1.4 Die Trennlinie zwischen Beschreiben und Bewerten

Der Dateikopf von `chapter_4.tex` verlangt, in diesem Kapitel nur zu beschreiben
und nicht zu interpretieren. Diese Vorgabe steht in Spannung zu den Stilregeln 1
und 4, nach denen ein Absatz mit seiner Konsequenz endet. Die Auflösung ist eine
Trennlinie nach dem Gegenstand der Konsequenz und nicht nach ihrem Vorhandensein.

- **In Kapitel 4 gehört** die Konsequenz für die Messgröße, für den Vergleich
  zwischen den Richtungen, für die Vergleichbarkeit der Läufe und für die Frage,
  welche Modellgröße den Befund erzeugt.
- **Nach Kapitel 5 gehört** die Konsequenz für das Produkt, für den Mechanismus,
  für den Netzbetrieb, für die Regulierung und für die Bewertung gegen den
  Anforderungskatalog.

Jeder Absatzplan trägt diese Unterscheidung in seiner Zeile *Nicht sagen*.

---

## 2 Ist-Zustand, aufgenommen aus `chapters/chapter_4.tex`

Die Datei hat 93 Zeilen, enthält keinen Fließtext und ist in `main.tex`
auskommentiert. Sie stammt aus dem Stand vom 18.08.2026 und ist seither nicht
angefasst, wie der Protokolleintrag zu Zeile 6217 vermerkt.

| Abschnitt | Marke | Ziel | Stichpunkte im Bestand |
|---|---|---|---|
| 4.1 Referenzfall ohne kurative Bindung | `sec:reference_case` | 3 S. | marktoptimaler Fahrplan am Beispieltag, Zyklenzahl und Erlöse je Markt, Plausibilisierung gegen die Preiszeitreihe |
| 4.2 Fahrplan- und Ladezustandsverläufe unter kurativer Bindung | `sec:bound_case` | 4 S. | Veränderung gegenüber dem Referenzfall, Verlauf des Ladezustands, Verlagerung der Lade- und Entladevorgänge |
| 4.3 Erlöswirkung und Opportunitätskosten | `sec:revenue_impact` | 4 S. | Erlösunterschied freier gegen gebundener Fahrplan, Aufteilung nach Märkten, Zerlegung in entgangene Arbitrage und Werteverbrauch |
| 4.4 Sensitivitätsanalyse | `sec:sensitivities` | 4 S. | Abrufhäufigkeit, Vergütungsniveau, Bindungsdauer und Band, Pönalehöhe, Anlagenauslegung |
| 4.5 Ableitung des kurativen Reservierungspreises | `sec:reservation_price` | 1 S. | keine, allein Kommentare zur Behauptungsstärke |

Dazu vier Kommentarblöcke, nämlich die drei Entscheidungen vom 18.08.2026, die
Streichung der Weber-Gegenüberstellung in 4.3, die Vorgabe, keine Obergrenze zu
nennen, und den Hinweis, das Ergebnis als konservative Obergrenze zu benennen.

---

## 3 Befunde am Ist-Zustand

Die Stichpunkte sind nicht falsch, sie sind älter als das Verfahren, das sie
beschreiben sollen. Zehn Befunde, jeder mit der Folge für die Sortierung.

**K1, die gesuchte Größe steht am Ende.** Der kurative Reservierungspreis ist
nach Entscheidung 6 nicht eine Sensitivität, sondern der Gegenstand der Arbeit.
Er steht im Bestand auf der letzten der 16 Seiten. Vier Fünftel des Kapitels
laufen auf ihn zu, statt von ihm auszugehen. *Folge:* Das Preisniveau kommt in
den ersten Abschnitt.

**K2, 4.1 und 4.2 sind nach Kapitel 3 gewandert.** Abschnitt 3.3.1 und 3.3.2
prüfen den Referenzerlös gegen den Revenue-Index, Abschnitt 3.3.3 zeigt Fahrplan
und Ladezustand des 11.02.2025 unter Bindung, und zwei Anhänge tragen
die Einzelmarktvalidierung und den Fahrplan ohne Mindestgröße. Ein Abschnitt 4.1
zum Referenzfall und ein Abschnitt 4.2 zum gebundenen Fahrplan wiederholten
damit sieben Seiten Kapitel 3. Das ist das Fehlerbild *Zwei Stellen sagen
dasselbe* aus `WORKFLOW.md` Abschnitt 9. *Folge:* Beide Abschnitte entfallen als
eigene Abschnitte. Was von ihnen bleibt, ist der Verweis auf Abbildung 3.6 in der
Kapiteleinleitung.

**K3, die Sensitivitätsliste ist überholt.** Abrufhäufigkeit, Vergütungsniveau
und Pönalehöhe sind durch die Entscheidungen 5, 6 und 13 gestrichen, wie der
offene Punkt 21 des Protokolls festhält. Die Anlagenauslegung ist nicht
gerechnet. Gerechnet sind die Modellierung der aFRR, die Abrufdauer, der Spread
am IDC, der Degradationssatz und die Mindestgröße. *Folge:* Die Liste wird durch
die drei Sensitivitäten aus `PLANUNG_KAPITEL_4.md` ersetzt, Degradationssatz und
Mindestgröße bleiben außen vor, Letztere weil Abschnitt 3.3.3 sie schon trägt.

**K4, die zwei Iterationen fehlen.** Der Bestand kennt das Suchverfahren aus
3.2.4 nicht, weil er älter ist. Abschnitt 3.2.4 nennt das Ergebnis der zweiten
Iteration ausdrücklich den Vollreservierungspreis und die erste Iteration einen
Startwert. Damit ist die in `PLANUNG_KAPITEL_4.md` als offen geführte
Entscheidung 6.1 durch den Wortlaut von Kapitel 3 bereits getroffen: Kapitel 4
weist die zweite Iteration aus, sonst widersprechen sich die Kapitel. *Folge:*
Heatmap und Jahreslauf sind auf `be_full_pos` und `be_full_neg` umzustellen. Die
erste Iteration erscheint in Kapitel 4 nur dort, wo der Unterschied zwischen den
Iterationen selbst die Aussage trägt, nämlich bei der Abrufdauer.

**K5, die Zählung der Misserfolgsausgänge ist offen und fällig.** Das Protokoll
gibt Kapitel 4 auf, aus dem Jahreslauf auszuzählen, wie oft die beiden
Misserfolgsausgänge des Verfahrens eintreten. Die Zahl liegt vor und ist
bemerkenswert klein. *Folge:* Sie gehört als eigener Stichpunkt in 4.1, weil sie
die Belastbarkeit aller folgenden Zahlen trägt.

**K6, der Begriff Bindungsdauer ist in der Planung falsch belegt.** Die
Sensitivität `sensi6_vorhaltedauer` variiert `kur_t_res`, und
`optimizer.py` Zeile 175 bezeichnet diese Größe als *Abrufdauer der
Energiebindung*. Sie setzt die Breite des reservierten Ladezustandsbandes, also
eine Megawattstunde je Megawatt bei einer Stunde. Die **Bindungsdauer** bleibt in
allen Varianten eine Stunde, denn die Reservierung ist nach Abschnitt 3.2.3 über
eine Zeitscheibe konstant. `PLANUNG_KAPITEL_4.md` und `MODELL.md` nennen die
Sensitivität Vorhaltedauer, und der alte Stichpunkt in 4.4 nennt sie
Bindungsdauer. Beides träfe im Text nicht zu. *Folge:* Die Sensitivität heißt in
Kapitel 4 **Abrufdauer**, und der Text sagt, dass sie das Ladezustandsband und
nicht die Bindungsdauer verändert. Das deckt sich mit Entscheidung 3, die die
Abrufdauer von einer Stunde als Basisfall setzt.

**K7, die Einheit ist nicht entschieden.** Offener Punkt 9 des Protokolls. Die
Daten führen Euro je Megawatt und Stunde, der Erlösvergleich Millionen Euro je
Jahr und der Revenue-Index Tausend Euro je Megawatt und Jahr. *Folge:* Kapitel 4
braucht die Entscheidung vor dem ersten Absatz und eine offengelegte Umrechnung.

**K8, es fehlt der Abschnitt, der den Preis erklärt.** Der Bestand zeigt
Fahrplan, Erlös und Sensitivitäten, sagt aber nie, **welcher Markt** die
Opportunität setzt. Genau das ist die Ursache des Preises und die Brücke zu den
Sensitivitäten. Die Erlösaufteilung liefert die Zahlen dafür. *Folge:* Die
Sensitivitäten werden nicht als Liste geführt, sondern als drei Antworten auf
diese eine Frage, siehe Abschnitt 4.5 der neuen Sortierung.

**K9, der Erlösvergleich ist im Bestand nicht vorgesehen.** Die Abbildung
`erloesvergleich_vollverdraengung_2025.pdf` liegt in `figures/chapter_4/` und
trägt die Kostenaussage des Kapitels. Der alte Abschnitt 4.3 wollte stattdessen
die Zerlegung in entgangene Arbitrage und zusätzlichen Werteverbrauch, die aus
der Vergütungsstruktur der Festlegung stammt und nach Kapitel 5 gehört. *Folge:*
Der Erlösvergleich erhält einen eigenen Abschnitt, die Zerlegung nach der
Festlegung entfällt hier.

**K10, der Kapiteltitel trifft nicht mehr.** *Exemplarische Anwendung und
Ergebnisse* passt zu einem Beispieltag. Gerechnet ist das ganze Jahr 2025, und
das Exemplarische steckt jetzt in Kapitel 3. *Folge:* Titelvorschlag *Der
kurative Reservierungspreis*, parallel zu Kapitel 3 *Marktmechanismus und
Modellierung des Speicherbetriebs*. Entscheidung des Verfassers.

---

## 4 Neue Sortierung im Überblick

Der rote Faden in einem Satz: **Der kurative Reservierungspreis ist zuerst als
Zahl zu zeigen, dann als Muster über Tag und Jahr, dann gegen den Bedarf zu
halten, dann in seiner Gesamtwirkung auf den Erlös zu beziffern, und zuletzt ist
zu prüfen, an welchem Markt er hängt.**

| Abschnitt | Kernaussage in einem Satz | Abbildung | S. |
|---|---|---|---|
| Einleitung | Das in Kapitel 3 geprüfte Verfahren läuft über alle Tage des Jahres 2025, und die Ergebnisse beantworten, was die kurative Vorhaltung kostet. | – | 0,5 |
| 4.1 Preisniveau und Streuung | Der kurative Reservierungspreis liegt im Median im niedrigen zweistelligen Bereich und ist stark rechtsschief, und die volle Reservierung ist in fast jeder Stunde des Jahres erreichbar. | Tab. 4.1 | 2,5 |
| 4.2 Zeitliches Muster | Die teuren Stunden folgen der Einspeisung und nicht dem Kalender, denn die Entladerichtung ist abends und die Laderichtung mittags teuer. | Abb. 4.1 Heatmap | 2,5 |
| 4.3 Preis und Engpassbedarf | Der Preis folgt dem Redispatchbedarf nicht, denn er ist im Dezember am niedrigsten und im September am höchsten. | Abb. 4.2 Jahreslauf | 2 |
| 4.4 Zahlung bei vollständiger Bindung | Eine durchgehende Reservierung des ganzen Jahres kostet mehr als den Referenzerlös, weil jede Stunde ihren eigenen Grenzpreis für die volle Leistung erhält. | Abb. 4.3 Erlösvergleich | 2,5 |
| 4.5 Sensitivitäten | Die Opportunität setzt die aFRR und nicht der Energiemarkt, und deshalb bewegen weder die Abrufdauer noch ein überschätzter Spread am IDC den Preis wesentlich. | Abb. 4.4 bis 4.6 | 5 |
| 4.6 Zusammenfassung | Die Ergebnisse tragen zusammen die Aussage, dass der kurative Reservierungspreis ein Preis gegen die Regelleistung ist. | – | 1 |

Die Reihenfolge der Abbildungen aus `PLANUNG_KAPITEL_4.md` bleibt unverändert,
nämlich Heatmap, Jahreslauf, Erlösvergleich, dann die drei Sensitivitäten. Neu
ist allein, dass die Höhe des Preises vorher in einer Tabelle steht, denn die
Farbskala einer Heatmap ist der schlechteste Ort, um das Niveau der zentralen
Größe zu erfahren.

### 4.1 Die drei Sensitivitäten als Argument statt als Liste

Der Übergang von 4.4 nach 4.5 ist die schwierigste Stelle des Kapitels, weil
dort aus einem Ergebnis eine Prüfung wird. Er trägt, wenn die drei
Sensitivitäten als drei Antworten auf eine Frage auftreten und nicht als
Aufzählung von Varianten.

Der Preis ist ein Opportunitätskostenpreis. Wovon er abhängt, ist damit die
Frage, welche Vermarktung die Reservierung verdrängt, und dafür kommen drei
Größen in Betracht.

1. **Die Modellierung der aFRR**, weil die aFRR die teuerste verdrängte
   Vermarktung ist und ihre Abbildung im Modell mehrere zulässige Formen hat.
2. **Die Abrufdauer**, weil sie als einzige der drei Größen ein Parameter des
   Produkts ist und der ÜNB sie festlegt.
3. **Der Spread am IDC**, weil er die Größe ist, die ein Betreiber zu hoch
   ansetzen kann, um einen höheren Preis zu fordern.

Die Reihenfolge ist damit begründet und nicht gesetzt: zuerst die Größe mit der
stärksten gemessenen Wirkung, dann die Größe, über die der ÜNB entscheidet,
zuletzt die Größe, über die der Betreiber entscheidet. Der Bogen schließt sich,
weil die dritte Sensitivität auf die erste zurückführt, denn die
Regelleistungsmärkte deckeln den Hebel am IDC.

---

## 5 Die Abschnitte im Einzelnen

Ein Stichpunkt entspricht etwa einem Satz. Die Zeile *Anschluss* ist der Kern
des Auftrags, die Zeile *Nicht sagen* ist nach `WORKFLOW.md` Abschnitt 7
Pflicht.

### Kapiteleinleitung, etwa 5 Stichpunkte

- Anschluss an 3.3.3: Die Prüfung am 11.02.2025 belegt die Funktionsweise des
  Verfahrens, und offen ist die Höhe des kurativen Reservierungspreises.
- Der Jahreslauf rechnet jeden Tag des Jahres 2025 für sich, mit identischem
  Anfangs- und Endladezustand, sodass die Tage vergleichbar bleiben.
- Ausgewiesen wird der Vollreservierungspreis aus der zweiten Iteration, weil
  allein er alle Stunden des Tages zugleich voll reserviert.
- Aufbau des Kapitels in einem Satz, mit handelnden Subjekten nach Stilregel 10.
- **Nicht sagen:** kein Wort zur Eignung des Mechanismus, keine Bewertung gegen
  den Anforderungskatalog, keine Aussage über den Preis, den ein Akteur bieten
  würde.

### 4.1 Preisniveau und Streuung, etwa 14 Stichpunkte, Tabelle 4.1

**Kernaussage.** Der kurative Reservierungspreis ist im Median klein, in den
oberen Prozenten der Stunden aber um zwei Größenordnungen größer, und die volle
Reservierung ist in fast jeder Stunde des Jahres physisch erreichbar.

- Median, Quartile und 95-Prozent-Quantil je Richtung, in der zu entscheidenden
  Einheit, als Tabelle 4.1.
- Vorliegende Werte aus dem Lauf vom 15.09.2026, Entladerichtung: Median 13,5,
  Quartile 5,0 und 29,7, 95-Prozent-Quantil 78,5 Euro je Megawatt und Stunde.
- Laderichtung: Median 9,2, Quartile 2,0 und 30,0, 95-Prozent-Quantil 88,6 Euro
  je Megawatt und Stunde.
- Die Verteilung ist rechtsschief, denn das arithmetische Mittel liegt mit 24,9
  und 23,6 Euro je Megawatt und Stunde nahe dem dritten Quartil.
- Das Jahresmaximum liegt in der Entladerichtung bei rund 1.000 und in der
  Laderichtung bei rund 505 Euro je Megawatt und Stunde.
- Anteil der Stunden unter einer Schwelle, damit die Schiefe nicht allein aus
  Quantilen gelesen werden muss: in der Entladerichtung 41 Prozent unter 10 und
  97 Prozent unter 101 Euro je Megawatt und Stunde.
- Die beiden Richtungen werden nie gemittelt oder summiert, weil sie zwei
  Produkte mit eigener Opportunität und eigenem Ladezustandsband sind.
- In der Laderichtung ist der Median kleiner als in der Entladerichtung, und der
  obere Rand ist es nicht, weshalb die billige Reservierung häufiger, die teure
  aber seltener in der Laderichtung liegt.
- Auszählung des ersten Misserfolgsausgangs nach K5: Von 8.758 Paaren aus Stunde
  und Richtung bleibt die volle Reservierung genau einmal in jeder Richtung
  unerreicht, nämlich am 22.02.2025 in der Stunde 21 in der Entlade- und in der
  Stunde 6 in der Laderichtung, und dort ist der ausgewiesene Preis eine untere
  Schranke.
- Folge daraus für die Belastbarkeit der Statistik, nämlich dass Median und
  Quantile keine Schranken mit echten Werten mischen.
- Auszählung des zweiten Misserfolgsausgangs, nämlich des übersprungenen
  Abstiegs: Er tritt an drei der 365 Tage ein, und zwei dieser drei Tage sind die
  beiden Zeitumstellungstage, sodass allein der 22.02.2025 ein inhaltlicher Fall
  ist.
- Folge daraus, nämlich dass der Preisvektor an diesen drei Tagen der Wert des
  Aufstiegs ist und damit über dem koordinatenweisen Minimum liegt.
- Das Minimalitätszertifikat scheitert dagegen an jedem Tag des Jahres an
  mindestens 18 und im Median an 32 der 48 Paare aus Stunde und Richtung, weshalb
  der Abstieg kein Formalismus, sondern die tragende Hälfte des Verfahrens ist.
- Der Preis ist ein Wert je Leistung und Zeit und keine Arbeitsvergütung, weshalb
  er sich nicht mit einem Preis je Megawattstunde vergleichen lässt.
- Umrechnung auf einen Betrag je Megawatt und Jahr einmal offengelegt, damit der
  Vergleich mit dem Revenue-Index aus 3.3.1 möglich bleibt.
- **Nicht sagen:** nicht, der Preis sei niedrig oder hoch, ohne den
  Vergleichsmaßstab zu nennen, und keine Obergrenze des Preises, auch nicht
  verneinend, nach Entscheidung 9.

*Abbildung.* Keine. Die Verteilung trägt eine Tabelle besser als ein Bild, weil
sechs Kennzahlen je Richtung abzulesen sind. Falls der Verfasser ein Bild
wünscht, wäre die Summenhäufigkeit beider Richtungen in einem Feld die
naheliegende Form, und sie wäre die siebte Abbildung.

### 4.2 Zeitliches Muster, etwa 12 Stichpunkte, Abbildung 4.1

**Kernaussage.** Die teuren Stunden folgen der Einspeisung und nicht dem
Kalender, denn die Entladereservierung ist abends und die Ladereservierung
mittags teuer.

- Anschluss: Die Kennzahlen aus 4.1 geben die Höhe, nicht die Lage der teuren
  Stunden, und die Lage entscheidet darüber, wann Vorhaltung günstig zu
  beschaffen ist.
- Aufbau der Abbildung in einem Satz, nämlich Stunde über Kalendertag, oben die
  Entlade- und unten die Ladereservierung.
- Tagesgang der Entladerichtung: Median 47 Euro je Megawatt und Stunde um
  19 Uhr gegen 2,8 Euro je Megawatt und Stunde um 4 Uhr.
- Tagesgang der Laderichtung: Median 57 Euro je Megawatt und Stunde um 13 Uhr
  gegen 1,0 Euro je Megawatt und Stunde um 20 Uhr.
- Die beiden Tagesgänge sind gegenläufig, und die Ursache ist die
  Photovoltaikeinspeisung, die mittags den Ladewert und abends den Entladewert
  setzt.
- Folge für die Beschaffung: Eine Stunde ist selten in beiden Richtungen teuer,
  sodass ein Verbund aus beiden Richtungen nach Abschnitt 3.1.2 nicht
  gleichzeitig zwei Maxima zahlt.
- Jahresgang: Der Median ist im September mit 24,0 und im Oktober mit 23,5 Euro
  je Megawatt und Stunde am größten und im Dezember mit 7,2 Euro je Megawatt und
  Stunde am kleinsten.
- Der Jahresgang folgt damit nicht der Photovoltaik allein, sondern den
  Leistungspreisen der Regelleistung, was 4.5 belegt.
- Die gesperrten Stunden der beiden Zeitumstellungstage erscheinen als Lücke, und
  die Behandlung steht in Abschnitt 3.2.3.
- Die Streuung innerhalb einer Stunde über das Jahr ist größer als der
  Unterschied zwischen den Stunden, weshalb das Muster eine Tendenz und keine
  Regel ist.
- Folge für die Auswertung: Ein Mittelwert über alle Stunden verdeckt das Muster,
  weshalb die folgenden Abschnitte nach Richtung und Tageszeit getrennt
  auswerten.
- **Nicht sagen:** nicht, dass der Engpass zu diesen Stunden auftritt, denn das
  Modell kennt kein Netz, und nicht, die kurative Reservierung sei mittags oder
  abends zu beschaffen.

*Abbildung 4.1.* Heatmap beider Richtungen, umzustellen auf `be_full_*` nach K4,
in Textbreite zu setzen und mit Achsen nach `PLANUNG_KAPITEL_4.md` Abschnitt 2.

### 4.3 Preis und Engpassbedarf, etwa 10 Stichpunkte, Abbildung 4.2

**Kernaussage.** Der kurative Reservierungspreis folgt dem Redispatchbedarf
nicht, denn im Dezember trifft der niedrigste Preis auf den zweithöchsten
Bedarf.

- Anschluss: Das Muster aus 4.2 sagt, wann Vorhaltung teuer ist, und offen ist,
  ob diese Stunden mit dem Bedarf zusammenfallen.
- Aufbau der Abbildung, nämlich der Tagespreis als Band mit Median auf der linken
  und das Redispatchvolumen des Tages auf der rechten Achse.
- Der Redispatchbedarf ist im Januar mit rund 2.680 Megawatt im Mittel am größten
  und im August mit rund 510 Megawatt am kleinsten.
- Der Preis ist im September und Oktober am größten, der Bedarf im Januar,
  Februar, November und Dezember, sodass die Maxima auseinanderfallen.
- Der Rangkorrelationskoeffizient zwischen dem Tagesmedian des Preises und dem
  Redispatchvolumen des Tages liegt zwischen 0,05 und 0,25, je nach Richtung und
  Redispatchrichtung, und zeigt damit keinen Zusammenhang.
- Zuordnung der Richtungen, nämlich die Entladereservierung zum Redispatch nach
  oben und die Ladereservierung zum Redispatch nach unten, mit der Begründung aus
  der ersetzten Maßnahme.
- Der spezifische Preis des heutigen präventiven Redispatch liegt bei 101 Euro je
  Megawattstunde, aus 3,08 Milliarden Euro Kosten und 30,44 Terawattstunden
  bewegter Menge im Jahr 2025.
- Dieser Vergleichswert ist ein Arbeitspreis je bewegter Megawattstunde und der
  kurative Reservierungspreis ein Leistungspreis je vorgehaltener Megawattstunde,
  weshalb die Abbildung beide nebeneinanderstellt und nicht gegeneinander
  aufrechnet.
- Folge für die Auswertung: Der Preis ist eine Eigenschaft der Vermarktung und
  nicht des Netzzustands, was die Unabhängigkeit von Modell und Bedarf bestätigt.
- **Nicht sagen:** nicht, die kurative Vorhaltung sei deshalb günstig oder
  lohnend, denn dieser Schluss verlangt den Nutzen und gehört nach Kapitel 5, und
  nicht, der fehlende Zusammenhang sei ein Ergebnis über Netzknoten, denn
  ausgewertet ist der deutschlandweite Redispatch.

*Abbildung 4.2.* Jahreslauf mit Redispatch, umzustellen auf `be_full_*` nach K4,
Achsenbeschriftung von *Breakeven* auf *Reservierungspreis* zu ändern.

### 4.4 Zahlung bei vollständiger Bindung, etwa 12 Stichpunkte, Abbildung 4.3

**Kernaussage.** Eine durchgehende Reservierung des ganzen Jahres kostet mehr
als der Referenzerlös, weil jede Stunde ihren eigenen Grenzpreis für die volle
Leistung erhält, während die Anlage ihren Erlös an Stundenpaaren verdient.

- Anschluss: Die Abschnitte 4.1 bis 4.3 zeigen den Preis je Stunde, und offen
  ist, was die Summe dieser Preise gegenüber der Vermarktung bedeutet.
- Aufbau der Abbildung, nämlich drei Balken, und Definition der drei Größen.
- Der Referenzerlös des Jahres 2025 beträgt 34,67 Millionen Euro für die
  betrachtete Anlage mit 100 Megawatt.
- Unter dem Preisvektor der zweiten Iteration zahlt der ÜNB 42,02 Millionen Euro
  für die Vorhaltung, und die Anlage verdient daneben noch 0,25 Millionen Euro
  am Markt.
- Die Zahlung liegt damit um 21,9 Prozent über dem Referenzerlös.
- Je Tag liegt die Überschätzung im Median bei 19,6 Prozent und im
  90-Prozent-Quantil bei 48,8 Prozent, weshalb die Jahreszahl kein
  Durchschnittstag ist.
- Die Ursache ist das Stundenprodukt: Jede Stunde erhält ihren Grenzpreis für die
  vollen 100 Megawatt, während sich der verdrängte Erlös aus Arbitrage auf ein
  Paar aus Lade- und Entladestunde verteilt und beide Stunden dieselbe Spanne
  spiegeln.
- Der Preisvektor der ersten Iteration verdrängt die Vermarktung nicht
  vollständig, denn die Anlage verdient daneben 9,31 Millionen Euro, und die
  Summe aus Zahlung und Markterlös liegt mit 50,28 Millionen Euro um 45,1 Prozent
  über dem Referenzerlös.
- Folge daraus für die Wahl der Messgröße, nämlich dass die zweite Iteration die
  vollständigere Verdrängung bei geringerer Zahlung liefert und deshalb
  ausgewiesen wird.
- Der ausgewiesene Preisvektor ist ein koordinatenweises und kein globales
  Minimum, und die umgekehrte Reihenfolge des Abstiegs liegt an den beiden
  vermessenen Tagen um 5,5 und 17,7 Prozent darunter.
- Folge daraus für die Lesart der Zahl, nämlich dass sie die vorsichtigere Seite
  einer gemessenen Spanne ist.
- **Nicht sagen:** nicht, die kurative Reservierung sei damit zu teuer oder
  unwirtschaftlich, denn dafür fehlt der Nutzen, und nicht, ein Tagesprodukt wäre
  besser, denn dieser Schluss ist eine Empfehlung und gehört nach Kapitel 5.

*Abbildung 4.3.* Erlösvergleich, Achse nach `PLANUNG_KAPITEL_4.md` Abschnitt 2
zu berichtigen, Zahl der Tage in der Bildunterschrift gegen den neuen Gesamtlauf
zu prüfen.

### 4.5 Sensitivitäten, etwa 30 Stichpunkte, Abbildungen 4.4 bis 4.6

**Einleitung des Abschnitts, etwa 5 Stichpunkte.** Sie trägt den Übergang aus
Abschnitt 4.1 dieser Datei, nämlich die Frage, welche Vermarktung die
Reservierung verdrängt, und die Ankündigung der drei Größen mit ihrer
Begründung. Dazu ein Satz zur Grundgesamtheit, weil die drei Sensitivitäten
nicht über denselben Zeitraum rechnen, siehe Entscheidung 6.3 in
`PLANUNG_KAPITEL_4.md`.

#### 4.5.1 Modellierung der aFRR, Abbildung 4.4

**Kernaussage.** Die Abbildung der aFRR im Modell bewegt den kurativen
Reservierungspreis um mehr als das Dreifache, weil die aFRR und nicht der
Energiemarkt die verdrängte Vermarktung ist.

- Anschluss: Die aFRR ist unter den geführten Märkten derjenige mit dem größten
  Erlösbeitrag, und ihre Abbildung im Modell hat nach Abschnitt 3.2.3 mehrere
  zulässige Formen.
- Welche Größen variiert werden, nämlich die Preisquelle und der Liefermodus der
  Energie.
- Ergebnis am 15.05.2025 in der Laderichtung: 37,9 Euro je Megawatt und Stunde
  ohne aFRR, 111,7 mit dem mengengewichteten Mittelpreis und 265,1 mit dem
  höchsten Zuschlag.
- Ergebnis am 26.08.2025 in derselben Richtung: 19,5 ohne, 59,9 mit dem
  Mittelpreis und 77,8 Euro je Megawatt und Stunde mit dem höchsten Zuschlag.
- Die Wirkung des Liefermodus der Energie ist kleiner als die der Preisquelle der
  Leistung, weshalb der Leistungspreis und nicht die gelieferte Arbeit die
  Opportunität setzt.
- Folge für die Lesart aller übrigen Ergebnisse, nämlich dass der Basisfall mit
  dem mengengewichteten Mittelpreis rechnet und der höchste Zuschlag nach
  Abschnitt 3.2.3 allein eine Sensitivität ist.
- Folge für die Vergleichbarkeit: Die Spanne der Modellierung ist größer als die
  Spanne, die die beiden folgenden Sensitivitäten erzeugen.
- **Nicht sagen:** nicht, das Modell überschätze oder unterschätze den Preis,
  denn die Richtung der Verzerrung ist eine Frage der Modellannahmen und gehört
  nach Abschnitt 5.4.

#### 4.5.2 Abrufdauer und Breite des Ladezustandsbandes, Abbildung 4.5

**Kernaussage.** Eine kürzere Abrufdauer senkt den kurativen
Reservierungspreis kaum, denn der Effekt, den die erste Iteration zeigt, ist
weitgehend eine Eigenschaft der stundenweisen Betrachtung.

- Anschluss: Die Abrufdauer ist die einzige der drei Größen, über die der ÜNB
  entscheidet, denn sie folgt aus der Zeit, die er die Maßnahme braucht.
- Was sie im Modell verändert, nämlich die Breite des reservierten
  Ladezustandsbandes von einer Megawattstunde je Megawatt bei einer Stunde, nach
  Abschnitt 3.2.3, und nicht die Bindungsdauer.
- Gerechnet sind eine Stunde als Basisfall sowie eine halbe und eine
  Viertelstunde, jeweils über das ganze Jahr.
- In der ersten Iteration senkt die Viertelstunde den Median deutlich, nämlich um
  15 Prozent in der Entlade- und um 32 Prozent in der Laderichtung.
- Nach der zweiten Iteration verschwindet der Effekt nahezu, denn die
  Vollverdrängung ändert sich nicht und die Halbverdrängung um 9 Prozent.
- Die Erklärung: Ist der Tag vollständig gebunden, steht ohnehin keine Leistung
  für andere Märkte frei, sodass die Breite des Bandes keine weitere Vermarktung
  mehr verdrängt.
- Folge für die Produktgestaltung im beschreibenden Sinn, nämlich dass die
  Abrufdauer den Preis der vollständigen Bindung nicht bestimmt.
- Folge für das Verfahren, nämlich dass ein Befund aus der ersten Iteration nicht
  auf die zweite übertragbar ist, was die Wahl der Messgröße in 4.4 stützt.
- **Nicht sagen:** nicht, der ÜNB solle die Abrufdauer so oder so wählen, denn
  die Empfehlung gehört nach Abschnitt 5.5, und nicht, das Ladezustandsband sei
  unerheblich, denn bei Teilreservierung wirkt es.

#### 4.5.3 Spread am kontinuierlichen Intraday-Handel, Abbildung 4.6

**Kernaussage.** Ein um den Faktor zwei gestreckter Spread am IDC hebt den
kurativen Reservierungspreis nur wenig, weil die Regelleistungsmärkte die
Opportunität setzen, sobald sie teurer sind.

- Anschluss: Der Spread am IDC ist die Größe, die ein Betreiber zu hoch ansetzen
  kann, denn nach Abschnitt 3.2.3 bewertet ein Aufschlag den mehrfachen Handel
  und seine Höhe ist nicht beobachtbar.
- Was variiert wird, nämlich die Streckung des Spreads um das Tagesmittel, sodass
  das Preisniveau bleibt und allein die Handelsspanne wächst.
- Ergebnis ohne Systemdienstleistungen am 11.02.2025: Der Preis steigt in der
  Entladerichtung von 9,1 auf 21,4 Euro je Megawatt und Stunde, also um das
  2,3-Fache.
- Ergebnis mit vollem Marktsatz am selben Tag: Der Preis steigt von 11,6 auf 21,4
  Euro je Megawatt und Stunde, und der Abstand zwischen beiden Kurven schließt
  sich mit steigender Streckung.
- Der Abstand beider Kurven ist der Befund, nämlich dass die aFRR die
  Opportunität setzt, solange sie über dem gestreckten Spread liegt.
- Damit führt die dritte Sensitivität auf die erste zurück, und die drei
  Sensitivitäten tragen zusammen eine Aussage.
- Vorbehalt zur Grundgesamtheit, nämlich fünf Beispieltage für die Mechanik und
  ein Jahreslauf für die Tragweite, sofern der Jahreslauf vorliegt.
- Vorbehalt zur Aussage, nämlich dass ein steigender Preis ohne zusätzlich
  belegte Stunden allein Buchhaltung wäre.
- **Nicht sagen:** nicht, der Mechanismus sei gegen strategisches Bieten
  geschützt, denn das Modell bildet nach Abschnitt 3.2.2 keinen Bietwettbewerb
  ab, und dieser Schluss gehört nach Abschnitt 5.2.

### 4.6 Zusammenfassung, etwa 7 Stichpunkte

- Anschluss: Die drei Sensitivitäten weisen auf denselben Markt, und daraus folgt
  die Einordnung des Ergebnisses.
- Der kurative Reservierungspreis liegt im Median im niedrigen zweistelligen
  Bereich je Megawatt und Stunde, mit einem oberen Rand zwei Größenordnungen
  darüber.
- Die volle Reservierung ist in nahezu jeder Stunde des Jahres erreichbar.
- Der Preis folgt dem Tagesgang der Einspeisung und nicht dem Redispatchbedarf.
- Die Zahlung bei durchgehender Bindung übersteigt den Referenzerlös um
  21,9 Prozent, und die Ursache liegt im Stundenprodukt.
- Der Preis hängt an der aFRR, weshalb er ein Preis gegen die Regelleistung und
  nicht gegen die Arbitrage ist.
- Der ermittelte Wert ist der opportunitätskostenbasierte Teil eines Gebots und
  nicht das Gebot, nach Entscheidung 5.
- **Nicht sagen:** keine Einordnung in die Vergütungslogiken, keine Bewertung
  gegen den Anforderungskatalog, keine Empfehlung.

---

## 6 Was daraus in Kapitel 5 gehört

Sieben Anschlüsse, die das Ergebniskapitel für die Diskussion öffnet. Vier
davon sind neu und in der Sammlung von Kapitel 5 noch nicht angelegt.

**D1, der Preis ist ein Preis gegen die Regelleistung.** Anschluss an C1 und an
Anforderung A7 der Verträglichkeit. Die kurative Reservierung konkurriert nicht
mit der Arbitrage, sondern mit der aFRR-Leistung, und sie greift auf dasselbe
Ladezustandsband zu, das die Präqualifikationsbedingungen für die Regelleistung
schon beanspruchen. Damit wird A7 quantitativ prüfbar, statt qualitativ zu
bleiben. **Neu.**

**D2, die Granularität des Produkts bestimmt die Zahlung.** Anschluss an eine
neue Handlungsempfehlung neben G1 bis G4. Weil jede Stunde ihren eigenen
Grenzpreis für die volle Leistung erhält, übersteigt die Summe der Stundenpreise
die Opportunität des ganzen Tages strukturell. Ein Produkt mit größerer
Zeitscheibe oder ein Paketpreis je Tag ist deshalb für denselben Umfang billiger.
Das ist eine Aussage über den Produktschnitt aus Abschnitt 3.1.2 und keine über
die Anlage. **Neu.**

**D3, günstig genau dann, wenn viel gebraucht wird.** Anschluss an E2 und an die
Übertragbarkeit in Abschnitt 5.3. Der fehlende Zusammenhang zwischen Preis und
Redispatchbedarf ist für den Mechanismus günstig, denn die teuren Monate des
Redispatch sind die billigen Monate der Vorhaltung. Die Aussage trägt allerdings
nur deutschlandweit, denn ohne Netzmodell ist nicht gesagt, dass sie an einem
einzelnen Netzknoten gilt. **Neu, mit Vorbehalt.**

**D4, die teuren Stunden liegen im Abendmaximum.** Anschluss an E2. Fällt der
kurative Bedarf in die Abendstunden, zahlt der ÜNB in der Entladerichtung das
Maximum des Tagesgangs. Ob das der Fall ist, entscheidet das Netz und nicht das
Modell. **Neu.**

**F11, Abhängigkeit vom Suchverfahren.** Steht in Kapitel 5 bereits als
Stichpunkt. Kapitel 4 liefert die Zahlen dazu, nämlich 5,5 und 17,7 Prozent
Spanne zwischen den Abstiegsreihenfolgen an den beiden vermessenen Tagen, das an
jedem Tag des Jahres scheiternde Minimalitätszertifikat mit im Median 32 von 48
Paaren und die drei Tage, an denen der Abstieg übersprungen ist und der
ausgewiesene Preis deshalb über dem koordinatenweisen Minimum liegt.

**F1 und F2, die konservative Obergrenze.** Steht in Kapitel 5 bereits. Kapitel 4
liefert mit der Zahl aus 4.4 den Bezug, gegen den die Verzerrung eingeordnet
wird. Die Wortkollision beim Begriff Obergrenze ist nach Befund I7 des Protokolls
in 4.6 und 5.4 aufzulösen, und der Vorschlag lautet, in Kapitel 4 von der
vorsichtigeren Seite einer gemessenen Spanne zu sprechen und den Ausdruck
Obergrenze allein für den Marktpreis zu sperren.

**F6, kein Optionswert enthalten.** Steht in Kapitel 5 bereits. Kapitel 4 sagt
dazu nichts, weil Entscheidung 1 die Abgrenzung aus 3.2.4 gestrichen hat.

---

## 7 Offene Entscheidungen

Zuerst die fünf Punkte aus `PLANUNG_KAPITEL_4.md` Abschnitt 6, soweit die
Durchsicht sie beantwortet oder verschoben hat.

**6.1 Welche Iteration.** Nicht mehr offen. Abschnitt 3.2.4 nennt das Ergebnis
der zweiten Iteration den Vollreservierungspreis, und Kapitel 4 muss ihm folgen,
siehe K4. Zu tun bleibt die Umstellung der beiden Abbildungen.

**6.2 Soll die Preissenkung gebaut werden.** Empfehlung, den Umfang zu
verkleinern. Weil die aFRR die Opportunität setzt, siehe 4.5.1, trägt der Hebel
auf die aFRR-Kapazitätspreise die Aussage der Sättigung fast allein, und dieser
Hebel ist mit `SZENARIO_AKTIV = "afrr_runter"` bereits vorhanden. Die fünf
Stellschrauben aus Abschnitt 5 der Planung wären dann nicht zu bauen. Vorschlag
für die Reihenfolge: erst nach der Abgabe der Kapitel 4 und 5 entscheiden, und
nur, wenn die Zeit aus `WORKFLOW.md` Abschnitt 8 es trägt.

**6.3 Grundgesamtheit der Sensitivitäten.** Empfehlung, die Bildunterschriften
sprechen zu lassen und keine weiteren Jahresläufe zu rechnen, denn die
Aussagerichtung der drei Sensitivitäten unterscheidet sich ohnehin. Die
Einleitung von 4.5 nennt den Unterschied ausdrücklich, damit die drei
Abbildungen nicht als gleichartig gelesen werden.

**6.4 Format von `idc_hebel`.** Empfehlung, die Kurven über der Streckung zu
behalten, weil der Abstand der beiden Kurven der Befund ist und ein Band je
Variante ihn nicht zeigt. Das gemeinsame Format bleibt für 4.5.1 und 4.5.2.

**6.5 Sechs oder sieben Abbildungen.** Bei der hier vorgeschlagenen Sortierung
sind es sechs. Die siebte wäre, falls der Verfasser sie will, die
Summenhäufigkeit in 4.1 und nicht die Preissenkung.

Dazu fünf Entscheidungen, die diese Durchsicht neu aufwirft.

**N1, Einheit des kurativen Reservierungspreises.** Offener Punkt 9 des
Protokolls, bindet Kapitel 3 und 4 gemeinsam. Vorschlag: Euro je Megawatt und
Stunde im Text und in allen Achsen, Millionen Euro je Jahr allein im
Erlösvergleich, und die Umrechnung einmal in 4.1 offengelegt.

**N2, Kapiteltitel.** Vorschlag *Der kurative Reservierungspreis*, siehe K10.

**N3, Name der Sensitivität aus K6.** Vorschlag *Abrufdauer*, mit einem Satz,
der sie von der Bindungsdauer trennt. Ohne diese Entscheidung ist der Absatz
nicht zu schreiben, weil beide Begriffe nach `CLAUDE.md` Abschnitt 5 belegt sind.

**N4, Behandlung der ersten Iteration.** Vorschlag, sie in Kapitel 4 allein in
4.4 und 4.5.2 zu zeigen, und zwar jeweils dort, wo der Unterschied zwischen den
Iterationen die Aussage trägt.

**N5, Zahl der Tage.** Die Läufe rechnen verschieden viele Tage.
`jahr_stunden_2025.parquet` und die Heatmap führen 365 Tage mit gesperrter
Stunde 2 an den beiden Zeitumstellungstagen, der Iterationsvergleich und damit
der Erlösvergleich überspringen diese Tage und führen 363. Abschnitt 3.2.3
beschreibt die Sperrung, nicht das Überspringen. Vorschlag: In Kapitel 4 je
Abbildung die Zahl nennen, in 4.1 den Unterschied einmal begründen und prüfen,
ob Abschnitt 3.2.3 um einen Satz zum Überspringen zu ergänzen ist.

---

## 8 Belegzettel und Argumentzettel zu dieser Vorlage

**Aus dem Repository übernommen.** Erlössummen und Iterationsvergleich aus
`analysen/10_reservierungspreis/iterationsvergleich_erloessummen_2025.csv`,
Füllgrade und Maximalpreise aus `MODELL.md` Abschnitt 15, Zensierung und
Reihenfolgeabhängigkeit aus `MODELL.md` Abschnitt 11.3, Wirkung der Abrufdauer
aus `MODELL.md` Abschnitt 13.2, Werte des IDC-Hebels aus
`analysen/05_sensitivitaet/idc_hebel.csv`, Werte der aFRR-Leiter aus
`analysen/04_erloesaufteilung/erloesaufteilung_afrr.csv`, spezifischer Preis des
präventiven Redispatch aus dem Docstring von
`analysen/code/jahreslauf/jahreslauf_redispatch.py`.

**Eigene Rechnung vom 17.09.2026, eigenständige Ableitung.** Alle Kennzahlen der
Verteilung in 4.1, die Monats- und Stundenmediane in 4.2 und 4.3 sowie die
Rangkorrelation zwischen Preis und Redispatchvolumen habe ich selbst aus
`jahr_stunden_2025.parquet` und aus `redispatch.load_redispatch(2025)` gerechnet.
Das Skript liegt im Arbeitsverzeichnis der Sitzung und ist nicht Teil des
Repositorys. Die Rangkorrelation ist gegen die Aggregation im Jahreslauf-Skript
zu prüfen, bevor eine Zahl in den Text geht, denn ich habe die mittlere Leistung
je Maßnahme auf die Stunden zwischen Beginn und Ende verteilt und damit
möglicherweise anders aggregiert als das Skript.

**Eigenständiges Argument, nicht vom Verfasser.** Die Begründung der
Sensitivitätsreihenfolge in Abschnitt 4.1 dieser Datei, die Ableitung D2 zur
Granularität des Produkts, die Ableitung D3 zum Verhältnis von Preis und Bedarf
und der Befund K6 zur Verwechslung von Abrufdauer und Bindungsdauer stammen aus
dieser Durchsicht und nicht aus einer Vorgabe. Jedes dieser vier Stücke ist vom
Verfasser zu prüfen, bevor es in einen Absatzplan eingeht.

**Auszählung der Misserfolgsausgänge, eigene Rechnung vom 17.09.2026.** Das
Protokoll gibt diese Zählung Kapitel 4 auf, und sie liegt hiermit vor. Aus
`jahr_stunden_2025.parquet` gezählt, Lauf vom 15.09.2026: Der erste Ausgang,
also die Stunde ohne Preis am höchsten Deckel, tritt je Richtung genau einmal
ein, beide Fälle am 22.02.2025. Der zweite Ausgang, also der übersprungene
Abstieg, tritt an drei Tagen ein, nämlich am 22.02., am 30.03. und am
26.10.2025, wobei die beiden letzten die Zeitumstellungstage sind. Die Spalte
`vv_nicht_minimal` trägt in diesen Fällen den Wert minus eins und
`vv_ueberschuss_pct` den Wert null, was den übersprungenen Abstieg von einem Tag
ohne Senkung unterscheidet. Die zwei Stunden mit gesetzter Marke `be_full_*_offen`
an den Zeitumstellungstagen sind die gesperrte Stunde 2 und kein inhaltlicher
Fall. `MODELL.md` Abschnitt 15 nennt für den ersten Ausgang dieselben zwei Fälle,
bezieht sie aber auf 8.712 statt auf 8.758 Paare, weil der dortige Stand 363 Tage
zählt. Vor der Verwendung im Text ist die Zählung auf dem neuen Gesamtlauf zu
wiederholen.
