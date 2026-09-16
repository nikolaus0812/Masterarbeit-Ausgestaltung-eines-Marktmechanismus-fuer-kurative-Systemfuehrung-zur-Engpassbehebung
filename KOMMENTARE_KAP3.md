# Kommentare des Verfassers zu Kapitel 3

Stand des Textes: 16.09.2026, Commit 532fb67. Jeder Absatz trägt eine Kennung
aus Unterabschnitt und laufender Nummer, jeder Satz eine Nummer in Klammern.
Unter jedem Absatz steht ein Feld *Kommentar*. Dort trägst du ein, was zu
ändern ist, in freier Form. Beispiele:

- `(3) streichen`
- `(2) neu: Der Akteur sagt zu, ...` (vollständiger neuer Satz)
- `(4) und (5) verbinden`
- `Inhalt: Der Abruf endet nicht, wenn ...` (inhaltlicher Hinweis, ich formuliere)
- `F3 ja` oder `F3 nein` (Entscheidung zu einem Vorschlag aus DURCHSICHT_KAP1_3.md)
- `ok` oder leer lassen, wenn nichts zu ändern ist

Zitate und Verweise sind hier ausgeblendet, sie bleiben im Text erhalten.
Deine Kommentare haben Vorrang vor den Vorschlägen aus der Durchsicht.

## 3.0 Kapiteleinleitung

### 3.0 Absatz 1

(1) Die kurative Systemführung hält für den Fehlerfall eine nachgelagerte Handlungsmöglichkeit bereit und erlaubt es dem ÜNB, das Netz im Normalbetrieb höher auszulasten.
(2) Die kurative Systemführung kommt damit als zusätzliche Systemdienstleistung für das Engpassmanagement in Betracht, deren Gegenstand nicht ein Eingriff, sondern die Bereitschaft zu einem Eingriff ist.
(3) Als kurativer Akteur kommen BESS in Betracht, denn sie vereinen die Eigenschaften, die ein kurativer Akteur braucht, und stehen an vielen Netzknoten, wie in Abschnitt X dargestellt.
(4) Für BESS ist die Bemessung der Vergütung im Engpassmanagement jedoch nicht abschließend geklärt.
(5) Eine kurative Reservierung fügt sich deshalb nicht in den bestehenden Rahmen ein, sondern ist eigens auszugestalten.
(6) Dazu ist die kurative Reservierung zuerst als Produkt zu entwerfen und dieses Produkt anschließend aus der Sicht des Anlagenbetreibers zu bewerten.
(7) In diesem Kapitel werden die Anforderungen abgeleitet, der Produktrahmen entworfen und der kurative Reservierungspreis mit einem Optimierungsmodell bestimmt, das den fehlenden Vergütungsrahmen ausfüllt.
(8) Zum Abschluss wird der ungebundene Erlös des Modells gegen einen veröffentlichten Erlösindex für BESS auf Plausibilität geprüft.

Kommentar:

## 3.1 Anforderungen und Produkt

Offene Vorschläge aus der Durchsicht: F1.

### 3.1 Absatz 1

(1) Aus den Befunden des Kapitels X folgen Anforderungen, aus denen die kurative Reservierung als Produkt entwickelt wird.

Kommentar:

## 3.1.1 Anforderungskatalog

Offene Vorschläge aus der Durchsicht: F9.

### 3.1.1 Absatz 1

(1) Der Katalog überführt die Befunde des vorangehenden Kapitels in Bedingungen, die sich an einem Mechanismus prüfen lassen.
(2) Die Anforderungen gelten für die Umsetzung einer kurativen Systemführung, deren Vorhaltung marktlich beschafft wird.

Kommentar:

### 3.1.1 Absatz 2

(1) **A1 -- Reaktionszeit.** Die kurative Reservierung muss nach der Reaktionszeit differenziert sein, weil das betroffene Betriebsmittel die Reaktionszeit vorgibt und der Akteur sie nicht wählen kann.
(2) Der ÜNB legt die zulässige Vorauslastung vor dem Fehlerfall fest und muss die Reaktionszeit der zugesagten Maßnahme dafür bereits kennen.
(3) Hält eine Anlage die zugesagte Zeit nicht ein, entwertet das nicht allein ihr Gebot, sondern auch die Vorauslastung, die der ÜNB im Vertrauen darauf gefahren hat.

Kommentar:

### 3.1.1 Absatz 3

(1) **A2 -- Verbindlichkeit.** Die Zusage muss binden und damit bei Nichterfüllung wirksame Sanktionen enthalten.
(2) Die Sanktion ist nötig, denn durch Nichterfüllung entsteht dem ÜNB ein Schaden, der die Vergütung der Vorhaltung um ein Vielfaches übersteigen kann.
(3) Die Sanktion darf deshalb nicht auf die entgangene Vergütung beschränkt bleiben.
(4) Eine Bemessung nach dem Grad der Abweichung scheidet aus, denn eine Leistungsänderung nach dem Ende des Überlastintervalls hat nicht einen verminderten, sondern gar keinen Wert.

Kommentar:

### 3.1.1 Absatz 4

(1) **A3 -- Lokationalität.** Die Beschaffung muss netzknotenscharf erfolgen, denn dieselbe Leistungsänderung entlastet ein Betriebsmittel je nach Netzknoten unterschiedlich stark.
(2) Die Wirkung je Knoten muss der ÜNB in seinen Vorschau- und Netzsicherheitsrechnungen mitprüfen.

Kommentar:

### 3.1.1 Absatz 5

(1) **A4 -- Bemessungsgegenstand.** Die Vergütung muss an der vorgehaltenen Leistung und an der Bindungsdauer ansetzen, denn die Bindung schränkt den Betrieb über ihre gesamte Dauer ein und nicht allein im Fehlerfall.
(2) Die Kosten fallen deshalb auch ohne Abruf an.
(3) Gegenstand der Vergütung ist damit die reservierte Leistung und keine Energielieferung.
(4) Die kurative Vorhaltung unterscheidet sich damit vom Redispatch, der stets zugleich Arbeit auslöst.

Kommentar:

### 3.1.1 Absatz 6

(1) **A5 -- Diskriminierungsfreiheit.** Der kurative Marktmechanismus muss an den geforderten Eigenschaften ansetzen und nicht an der Technologie, damit der Zugang diskriminierungsfrei bleibt.
(2) In der Präqualifikation heißt das, technische und physikalische Eigenschaften zu prüfen und nicht die Art der Anlage.
(3) Der offene Zugang dient zugleich der Verfügbarkeit, denn je mehr Technologien die geforderten Eigenschaften erfüllen, desto eher steht an einem betroffenen Knoten ein Anbieter zur Verfügung.

Kommentar:

### 3.1.1 Absatz 7

(1) **A6 -- Teilnahme.** Der kurative Marktmechanismus muss die Teilnahme für den Betreiber lohnend ausgestalten, weil der Betreiber über sein Gebot allein entscheidet und die Maßnahme ohne Gebot nicht verfügbar ist.
(2) Die marktliche Beschaffung ist damit nicht allein eine Frage der Zugangsform, sondern die Bedingung dafür, dass sich eine kurative Systemführung umsetzen lässt.

Kommentar:

### 3.1.1 Absatz 8

(1) **A7 -- Verträglichkeit.** Der kurative Marktmechanismus muss neben den bestehenden Verpflichtungen bestehen können, denn die Bindung durch die Reservierung greift auf denselben Betriebszustand zu, den die Anlage für die Regelleistung und für die Vermarktung an den Spotmärkten bereithält.
(2) Die kurative Zusage und die Vermarktung an den übrigen Märkten dürfen sich nicht gegenseitig ausschließen, und die Verfügbarkeit der Anlage für den Redispatch muss erhalten bleiben.

Kommentar:

### 3.1.1 Absatz 9

(1) **A8 -- Umsetzbarkeit.** Der kurative Marktmechanismus muss in bestehende Betriebsprozesse integrierbar sein, nämlich in die Beschaffung, den Abruf und den Nachweis, die der ÜNB für das Engpassmanagement bereits führt.
(2) Gegenstand der Beschaffung ist nicht das einzelne Gebot, sondern ein Verbund von Geboten, der den Engpass entlastet und bilanziell ausgeglichen ist.

Kommentar:

## 3.1.2 Die kurative Reservierung

Offene Vorschläge aus der Durchsicht: F2, F3, F4, F10, F19, F20.

### 3.1.2 Absatz 1

(1) Eine kurative Reservierung verbindet den Akteur mit dem ÜNB: Der Akteur sagt eine Leistungsänderung zu, der ÜNB nimmt sie in seine Einsatzplanung auf und ruft sie im Fehlerfall ab.
(2) Der folgende Entwurf bestimmt die Merkmale der kurativen Reservierung und lässt die Anforderungen dabei einfließen.
(3) Der Akteur sagt zu, seine Leistung im Fehlerfall um die angebotene Leistungsänderung zu verschieben, und reserviert dafür ein Leistungsband.
(4) Neben dem Leistungsband reserviert die Zusage ein Ladezustandsband, innerhalb dessen die Anlage zu bleiben hat.
(5) Vorhaltung und Abruf sind zu unterscheiden: Die Zusage besteht durchgehend, ein Abruf erfolgt nur im Fehlerfall.
(6) Vergütet wird allein die Vorhaltung.
(7) Der Preis deckt damit sowohl die Bindung als auch die Energie, die ein Abruf kostet.
(8) Den Energieanteil eines Abrufs bildet das Modell in Abschnitt X nicht ab.

Kommentar:

### 3.1.2 Absatz 2

(1) Der Akteur nimmt die kurativ gebundene Leistung aus seiner übrigen Vermarktung heraus.
(2) Daraus entstehen die Opportunitätskosten, die der Akteur über den Preis ersetzt verlangt.
(3) Eine Anlage kann beide Richtungen anbieten, aber jede Richtung bindet einen anderen Teil des Ladezustandsbandes und ist deshalb ein eigenes Gebot.
(4) Gesperrt ist damit allein die zugesagte Leistung, während für das gebundene Zeitfenster kein allgemeines Handelsverbot gilt.
(5) Neben Richtung und Leistung nennt ein Gebot die Reaktionszeitklasse, für die der Akteur einsteht.
(6) Weil zu jeder Höhe der Überlast eine zulässige Dauer gehört, schaltet jede Reaktionszeit ein anderes Maß an Höherauslastung frei.
(7) Die kurative Reservierung übernimmt deshalb die drei Klassen aus InnoSys 2030, nämlich unter zehn Sekunden, etwa zwei Minuten und bis 15 Minuten, wie in Abschnitt X beschrieben.
(8) Wer die kürzeste Klasse erfüllt, erfüllt damit auch die längeren, sodass ein schneller Akteur in jeder Klasse anbieten kann.
(9) Die Klassen ersparen dem ÜNB die Rechnung mit der Reaktionszeit jeder einzelnen Anlage, und drei Stufen halten den Zugang zugleich für viele Technologien offen.
(10) Die Bindungsdauer ist der Zeitraum, über den die Zusage nach dem Zuschlag gilt, und beträgt eine Zeitscheibe, also eine Stunde des Liefertages.

Kommentar:

### 3.1.2 Absatz 3

(1) Den Abruf löst der ÜNB aus, sobald nach einem Ausfall die Überlastung tatsächlich eintritt.
(2) Der Akteur erhält zum Abruf ein Signal, auf das seine Anlage innerhalb der zugesagten Klasse reagiert.
(3) Die Anlage hält die Leistungsänderung höchstens eine Stunde, und diese Stunde kann über zwei Zeitscheiben reichen.
(4) Angenommen ist der ungünstigste Fall eines einstündigen Abrufs.
(5) Das Ladezustandsband hält deshalb je zugesagtem Megawatt eine Megawattstunde vor, in positiver Richtung als gespeicherte Energie und in negativer Richtung als freien Speicherraum.
(6) Der Abruf endet früher, sobald der ÜNB den Engpass mit anderen Mitteln behoben hat.
(7) Nach einem Abruf ist der Akteur für den restlichen Liefertag von der Vorhaltung freigestellt.
(8) An die Stelle der Lieferpflicht tritt jedoch eine Nachlaufpflicht, nach der der Akteur seine Leistung nicht wieder in die den Engpass verschärfende Richtung verschieben darf.
(9) Wie lange die Nachlaufpflicht gilt, folgt aus dem Betrieb und bleibt hier offen.
(10) Die bilanzielle Verantwortung für die Abweichung vom Fahrplan im Abruf liegt nicht beim Akteur, sondern beim ÜNB, der den Abruf ausgelöst hat.

Kommentar:

### 3.1.2 Absatz 4

(1) Die kurative Zusage führt der Akteur in den Planungsdaten mit, die er dem ÜNB übermittelt.
(2) Der Akteur weist zweierlei nach, nämlich dass seine Anlage die beiden Bänder über die Bindung eingehalten und im Abruf die Leistungsänderung innerhalb der Klasse erbracht hat.
(3) Eine verspätete oder zu geringe Leistungsänderung bringt das Betriebsmittel nicht mehr in einen dauerbelastbaren Zustand, weshalb die Erfüllung binär ist.
(4) Die Pönale knüpft deshalb nicht erst an einen gescheiterten Abruf, sondern schon an die fehlende Handlungsfähigkeit, weil die Vorauslastung auf der Zusage beruht.
(5) Von der Pönale befreit den Akteur allein der Nachweis, dass seine Handlungsfähigkeit an einem unvorhersehbaren Ereignis außerhalb seines Betriebs scheiterte.
(6) Ein solches Ereignis hat der Akteur dem ÜNB unverzüglich zu melden, damit der ÜNB Gegenmaßnahmen einleiten kann.
(7) Die Sanktion kann von einer Strafzahlung über den Entzug der Präqualifikation bis zur Übernahme der entstandenen Schäden reichen.
(8) Höhe und Form der Sanktion bestimmt die Untersuchung nicht, weil das Modell die daraus folgende Risikoprämie nicht trägt.

Kommentar:

### 3.1.2 Absatz 5

(1) Ob ein Akteur die zugesagte Klasse erfüllen kann, prüft der ÜNB vor dem ersten Gebot in der Präqualifikation, in der der Akteur die geforderte Reaktionszeit, die vorhaltbare Leistung und die Einhaltung des Ladezustandsbandes nachweist.
(2) Die Reaktionszeit, die Leistung und das Ladezustandsband prüft die Präqualifikation der Regelleistung bereits, nämlich als Folgen eines Sollwerts des ÜNB, als Leistung und als Arbeitsvermögen.
(3) Eine für die Regelleistung präqualifizierte Anlage weist die dort geprüften Eigenschaften nicht erneut nach, sodass sich ihr Aufwand auf die zusätzlichen Anforderungen der kurativen Zusage beschränkt.
(4) Die Klasse bis 15 Minuten deckt die Präqualifikation der aFRR und der mFRR ab, während eine Anlage für die Klassen von etwa zwei Minuten und unter zehn Sekunden die schnellere Reaktion eigens nachweist.
(5) Anlagen, die nicht an der Regelleistung teilnehmen, weisen alle drei Eigenschaften selbst nach.
(6) Die Sensitivität des Standorts, also die Wirkung einer Leistungsänderung an diesem Knoten auf das Betriebsmittel, weist der Akteur nicht selbst nach, denn sie folgt aus dem Netzmodell des ÜNB.
(7) Der Akteur gibt deshalb allein den Netzknoten an, dem seine Anlage zugeordnet ist.
(8) Wie in der Regelleistung bestätigt der Netzbetreiber, an dessen Netz die Anlage angeschlossen ist, dass Vorhaltung und Abruf an diesem Anschluss möglich sind.

Kommentar:

### 3.1.2 Absatz 6

(1) Präqualifizierte Akteure bieten in einer gemeinsamen Ausschreibung der deutschen ÜNB, wie sie bei der aFRR bereits besteht, und durchlaufen damit nur ein Verfahren.
(2) Den Bedarf ermitteln die ÜNB in den Rechenläufen ihrer Redispatchplanung am Vortag, sodass er vor dem Zuschlag feststeht.
(3) Ausgeschrieben wird je Zeitscheibe von einer Stunde, was der Dauer des ungünstigsten Abrufs entspricht.
(4) Die Ausschreibung findet täglich statt, und zwar gleichzeitig für alle 24 Zeitscheiben des Folgetages, für die ein Akteur jeweils ein eigenes Gebot abgeben kann.
(5) Das Gebot nennt für jede Zeitscheibe einen Preis in Euro je Megawatt und Stunde, getrennt für die positive und die negative Richtung.
(6) Die Mindestgröße eines Gebots beträgt 25 MW, die eine Anlage allein oder mehrere Anlagen am selben Netzknoten zusammen erreichen.
(7) Anders als die Regelleistung, die Anlagen innerhalb einer Regelzone zusammenfasst, erlaubt die kurative Reservierung die Zusammenfassung nur je Netzknoten.
(8) Maßgeblich für die Zusammenfassung ist allein die Wirkung am angegebenen Knoten.
(9) Bei Anlagen, die an vielen Knoten der Mittelspannung angeschlossen sind, zählt zum Beispiel nur die Wirkung am übergeordneten Knoten im 110-kV-Netz.

Kommentar:

### 3.1.2 Absatz 7

(1) Einen Anspruch auf Zuschlag hat der Akteur nicht.
(2) Die ÜNB nehmen Gebote nach pay-as-bid, also zum jeweils gebotenen Preis, nur für die Zeitscheiben an, die sie benötigen.
(3) Neben dem Preis nennt das Gebot eine Höchstleistung, von der die ÜNB auch einen Teil bezuschlagen können.
(4) Der bezuschlagte Teil darf die Mindestgröße nicht unterschreiten.
(5) Für den Zuschlag vergleichen die ÜNB jedes Gebot nach seiner Wirkung, also nach der Sensitivität des Netzknotens, mit dem präventiven Redispatch und den Maßnahmen in ihrem eigenen Verfügungsbereich.
(6) Bezuschlagt wird kein einzelnes Gebot, sondern ein Verbund aus Geboten beider Richtungen, denn die Maßnahme muss sich bilanziell ausgleichen.
(7) Im Verbund lassen sich die Sensitivitäten aufeinander abstimmen, indem die eine Richtung an einem wirksamen Knoten den Engpass entlastet.
(8) Die Gegenrichtung steht dann an einem Knoten, der auf das Betriebsmittel kaum wirkt.
(9) Die ÜNB geben die Zuschläge vor 23.30 Uhr des Vortages bekannt, damit der Akteur für die erste Stunde des Liefertages noch vor dem Handelsschluss zwischen den Regelzonen umplanen kann.

Kommentar:

## 3.2 Optimierung des Speicherbetriebs

Offene Vorschläge aus der Durchsicht: F15, F21.

### 3.2 Absatz 1

(1) Für den ÜNB bedeutet die kurative Reservierung vor allem neue Abläufe in der Systemführung, von der Ermittlung des Bedarfs über den Verbund der Gebote bis zum Nachweis der Erfüllung.
(2) Ob sich eine systemweite Integration der kurativen Systemführung lohnt, hängt für den ÜNB davon ab, ob der Nutzen der höheren Vorauslastung die Kosten der Reservierung und ihrer Umsetzung übersteigt.
(3) Welchen Preis ein Akteur fordert, hängt davon ab, was ihm die Reservierung unter den bestehenden Nebenbedingungen an anderer Vermarktung nimmt.
(4) Für die kurative Reservierung besteht kein Vergütungsrahmen, an dem sich ein Akteur ausrichten könnte.
(5) Der Preis ist deshalb aus dem Betrieb des Speichers selbst zu bestimmen.
(6) Der kurative Reservierungspreis wird dafür als der kleinste Preis bestimmt, bei dem ein BESS eine Zeitscheibe voll reserviert, statt die Leistung anderweitig zu vermarkten.
(7) Der Preis liefert die Kostenseite der Abwägung, der der ÜNB den Nutzen der höheren Vorauslastung gegenüberstellen kann.
(8) Für die Bestimmung wird ein Optimierungsmodell aufgebaut, das abbildet, wie ein BESS über einen Liefertag an mehreren Märkten zugleich vermarktet wird.
(9) Für die kurative Reservierung gibt das Modell einen Preis vor, auf den der Betreiber seine Vermarktung einstellt.
(10) Abbildung N zeigt den Weg eines Liefertages von den Marktdaten über die Dispatch-Optimierung bis zu den Ergebnissen.

Kommentar:

## 3.2.1 Ansatz und Lösungsverfahren

Offene Vorschläge aus der Durchsicht: F5, F6, F8, F16, F23.

### 3.2.1 Absatz 1

(1) Die Bestimmung des kurativen Reservierungspreises verlangt ein Modell, das den ungebundenen Fahrplan als Bezug mitführt, den Ladezustand über den Tag koppelt und alle Märkte gemeinsam entscheidet.
(2) Der ungebundene Fahrplan entsteht in einem Lauf mit Preis null.
(3) Der ungebundene Fahrplan zeigt, wie die Anlage ohne kurative Reservierung vermarktet würde.
(4) Am ungebundenen Fahrplan lässt sich ablesen, was die Reservierung verdrängt.
(5) Die Opportunitätskosten der kurativen Reservierung entstehen damit im Modell selbst, weil die Reservierung der Anlage Leistung und Ladezustandsband für den Markt entzieht.
(6) Ein gesonderter Kostenansatz für die Vorhaltung ist deshalb nicht nötig.

Kommentar:

### 3.2.1 Absatz 2

(1) Neben dem Bezug koppelt das Modell den Ladezustand über den ganzen Liefertag.
(2) Das Ladezustandsband einer Reservierung legt fest, wie viel Energie oder Speicherraum die Anlage schon vor der Zeitscheibe bereithalten muss, und bindet so auch die Stunden davor.
(3) Alle Märkte entscheidet das Modell gemeinsam und mit vollständiger Preiskenntnis, sodass die Anlage ihre Leistung und ihren Ladezustand in einer Entscheidung optimal über alle Märkte und Stunden verteilt.
(4) Der Akteur trifft seine Entscheidungen in Wirklichkeit dagegen nacheinander, von der FCR am Vortag bis zur aFRR-Arbeit in der Lieferviertelstunde.
(5) Ein BESS kommt dem so berechneten Betrieb mit heutigen Handelsstrategien allerdings nahe, denn eine prognosegestützte Strategie erreicht im kontinuierlichen Intraday-Handel rund neunzig Prozent des unter vollständiger Preiskenntnis erzielbaren Erlöses.
(6) Der Erlös des Modells bleibt gleichwohl eine obere Schranke der übrigen Vermarktung.
(7) Der kurative Reservierungspreis fällt deshalb eher zu hoch als zu niedrig aus.

Kommentar:

### 3.2.1 Absatz 3

(1) Gelöst wird je Liefertag ein eigenes Problem, sodass kein Ladezustand in den Folgetag übergeht und die Tage untereinander vergleichbar bleiben.
(2) Zielfunktion und Nebenbedingungen sind durchweg linear, sodass das Problem im Basisfall ein lineares Programm ist und die kurative Reservierung jeden Wert zwischen null und der Anschlussleistung annehmen darf.
(3) Erst die Mindestgröße von 25 MW macht die Reservierung halbstetig, denn die reservierte Leistung beträgt dann entweder null oder mindestens 25 MW.
(4) Für die Mindestgröße ist je Stunde und Richtung eine Binärvariable nötig, und das Problem wird zu einem gemischt-ganzzahligen linearen Programm.
(5) Die Mindestgröße wird als Sensitivität geführt, wie in Abschnitt X beschrieben.
(6) Die numerische Lösung erfolgt in beiden Fällen mit Gurobi 13.0.2.
(7) Als Abbruchkriterium des gemischt-ganzzahligen Programms dient eine relative Optimalitätslücke von 0,01 Prozent zwischen der besten gefundenen zulässigen Lösung und der besten relaxierten Schranke, dazu ein Zeitlimit von 60 Sekunden je Lauf.

Kommentar:

### 3.2.1 Absatz 4

(1) Das Modell betrachtet eine einzelne Anlage und nicht das System, denn gesucht ist der Preis aus der Sicht eines Betreibers.
(2) Der Akteur ist als einzelne Anlage Preisnehmer und bewegt keinen Marktpreis.
(3) Netzrestriktionen und die Zusammenfassung mehrerer Anlagen zu einem Pool bildet das Modell ebenfalls nicht ab.
(4) Ohne Netzmodell ist der kurative Bedarf nicht räumlich aufgelöst, sodass jede Zeitscheibe gleich behandelt wird.
(5) Auch die Gegenseite der Maßnahme fehlt, obwohl der bilanzielle Ausgleich einen Verbund von Zusagen verlangt, wie in Abschnitt X beschrieben.
(6) Die Abrufwahrscheinlichkeit bleibt ebenso außer Betracht, das Modell bewertet die Reservierung also ohne Abruf.
(7) Der Zuschlag in den Regelleistungsmärkten gilt zudem als sicher, was die Erlöse der Leistungsmärkte überschätzt.
(8) Die beiden letzten Vereinfachungen wirken in eine benennbare Richtung auf den Preis: Ohne Abruf ist der Preis der opportunitätskostenbasierte Teil des Gebots, und die sicheren Zuschläge heben die entgangenen Erlöse an.

Kommentar:

### 3.2.1 Absatz 5

(1) Die Regelleistungsmärkte sind mengenmäßig begrenzt, weil ihr Bedarf der Systemgröße folgt und nicht mit der Speicherflotte wächst.
(2) Ein Zubau im Gigawattmaßstab drängt die zusätzliche Leistung deshalb überwiegend in die Arbitrage.
(3) Speicher heben Niedrigpreisphasen an, senken Hochpreisphasen ab und verzehren damit die Spreads der Arbitrage.
(4) Der Szenariorahmen 2030 ordnet die Untersuchung qualitativ ein und geht nicht als Eingangsgröße in das Modell.
(5) Die Rückwirkung der Speicher auf die Preise bildet das Modell ebenfalls nicht ab, sodass die Preise des Jahres 2025 als gegeben gelten.

Kommentar:

## 3.2.2 Anlage, Speicher und Zielfunktion

Offene Vorschläge aus der Durchsicht: F8, F11.

### 3.2.2 Absatz 1

(1) Innerhalb dieser Grenzen wird eine einzelne Anlage abgebildet.
(2) Die Anlage ist ein BESS mit 100 MW je Richtung und 250 MWh Speicherkapazität, also einem Energieinhalt je Leistung von 2,5 Stunden.
(3) Die Auslegung liegt über dem Bereich von ein bis zwei Stunden, den die Großspeicher in Betrieb erreichen, und im Bereich der geplanten Anlagen, wie in Abschnitt X dargestellt.
(4) Eine kurative Reservierung über die volle Anschlussleistung erschöpft den Speicher damit erst nach 2,5 Stunden.
(5) Laden und Entladen laufen mit einem Wirkungsgrad von 0,95 je Richtung, woraus ein Umlaufwirkungsgrad von 0,9025 folgt.
(6) Der nutzbare Ladezustand liegt zwischen 5 und 95 Prozent, sodass die Anlage 225 MWh bewegen kann.
(7) Jede Reservierung nimmt ihr Ladezustandsband aus dem nutzbaren Ladezustand.

Kommentar:

### 3.2.2 Absatz 2

(1) Die Degradation belastet mit 8 Euro je Megawattstunde Durchsatz den Handel und die gelieferte Arbeit, nicht aber die Vorhaltungen.
(2) Der Satz entspricht der Größenordnung, die sich aus den Investitionskosten eines schlüsselfertigen Speichersystems und seinem Lebensdauerdurchsatz ergibt.
(3) Der Verschleiß hängt tatsächlich von Temperatur, Ladezustand und Strom ab und ließe sich erst mit zusätzlichen Binärvariablen abbilden.
(4) Das Modell nimmt die Vereinfachung in Kauf, weil die Preissuche das Tagesmodell einige hundert Mal je Tag löst.

Kommentar:

### 3.2.2 Absatz 3

(1) Der Liefertag zerfällt in 96 Viertelstunden, und die Blockprodukte binden Zeitscheiben von einer und von vier Stunden.
(2) Entscheidungsvariablen sind die Leistungen an den Energiemärkten, die vorgehaltenen Leistungen der Regelleistung, die kurativ reservierte Leistung je Richtung, die gelieferte aFRR-Arbeit mit ihrem Ausgleich am IDC und der Ladezustand, alle stetig und nichtnegativ.
(3) Anhang X führt die Variablen vollständig auf.
(4) Die Zielfunktion maximiert den Nettoerlös eines Liefertages über alle geführten Märkte abzüglich der Degradationskosten.
(5) [Gleichung]
(6) Die vollständige Formulierung mit allen Nebenbedingungen steht in Anhang X.

Kommentar:

### 3.2.2 Absatz 4

(1) Die Ladezustandsbilanz führt den Speicherinhalt über den Tag fort, wobei allein der Handel und die gelieferte aFRR-Arbeit ihn bewegen und die Wirkungsgrade beider Richtungen eingehen.
(2) Anfang und Ende eines Tages tragen denselben Ladezustand, damit kein Tag mit eingelagerter Energie endet und die Tage untereinander vergleichbar bleiben.
(3) Die zeitgekoppelte Formulierung folgt der Darstellung von Flexibilitätsgeboten.
(4) Auf jeder Seite teilen sich der Handel, die aFRR, die kurative Reservierung und die auf beiden Seiten stehende FCR die Anschlussleistung.
(5) Eine kurativ reservierte Leistung steht deshalb keinem anderen Markt zur Verfügung.

Kommentar:

## 3.2.3 Abbildung der Märkte

Offene Vorschläge aus der Durchsicht: F5, F11, F14, F17, F18, F22.

### 3.2.3 Absatz 1

(1) Das Modell führt neben der kurativen Reservierung die Märkte, an denen ein BESS heute seine Erlöse erzielt, nämlich den DA, den IDC, die FCR und die aFRR mit Leistung und Arbeit.
(2) Der DA und der IDC zusammen bilden ab, was eine Anlage am Spotmarkt erreichen kann, weil sich Arbitrage zu unterschiedlichen Zeitpunkten ergibt.
(3) Die Intraday-Auktionen führt das Modell nicht, weil auch der Vergleichsmaßstab der Validierung sie nicht enthält.
(4) Die mFRR führt das Modell nicht, weil sie der aFRR im Produktschnitt gleicht und im Jahr 2025 den geringeren Leistungspreis erzielte, wie in Abschnitt X dargestellt.
(5) Die Märkte wirken auf zwei Arten auf den Speicher: DA, IDC und aFRR-Arbeit bewegen den Ladezustand, während FCR, aFRR-Leistung und die kurative Reservierung Leistung und ein Ladezustandsband binden, ohne Energie umzuschlagen.
(6) Das Modell setzt alle Märkte eines Liefertages gleichzeitig, und jeder trägt dabei seinen eigenen Produktzuschnitt, seinen Energievorhalt und seinen Preis.

Kommentar:

### 3.2.3 Absatz 2

(1) Auswertungszeitraum ist das Jahr 2025.
(2) Weil der DA erst seit dem 01.10.2025 in Viertelstunden gehandelt wird, gilt davor sein Stundenpreis für alle vier Viertelstunden.
(3) Die beiden Tage der Zeitumstellung führt das Modell mit 96 Viertelstunden, indem es die fehlende Stunde im Frühjahr durch Platzhalter ersetzt, im Herbst die zweite Ausführung der doppelten Stunde verwirft und die betroffene Stunde in beiden Fällen sperrt.
(4) Tabelle N fasst die Produktmerkmale der sechs geführten Märkte zusammen.

Kommentar:

**Day-Ahead**

### 3.2.3 Absatz 3

(1) Die Preisreihe des DA ist der Auktionspreis der Gebotszone Deutschland und Luxemburg.
(2) Die Käufe und Verkäufe am DA gleichen sich über den Tag energetisch aus und müssen ihre eigenen Degradationskosten decken.
(3) So bildet das Modell nach, dass der Betreiber am DA bietet, bevor der Zuschlag der kurativen Reservierung feststeht, und die Reservierung den Handel dort nicht mitfinanziert.
(4) Ein Geschäftspaar am DA kommt deshalb nur zustande, wenn die Preisspanne der Arbitrage die Degradationskosten übersteigt.
(5) Der Erlös am DA ist die über den Tag summierte Differenz aus Verkauf und Kauf, jeweils zum Auktionspreis der Viertelstunde.

Kommentar:

### 3.2.3 Absatz 4

(1) [Gleichung]

Kommentar:

**Kontinuierlicher Intraday-Handel**

### 3.2.3 Absatz 5

(1) Auch am IDC handelt die Anlage Energie, bewertet wird dieser Handel aber je Viertelstunde mit dem ID1, dem Preisindex der letzten Stunde vor Lieferbeginn.
(2) Im kontinuierlichen Handel kommt jedes Geschäft zu seinem eigenen Preis zustande, sodass es für eine Viertelstunde keinen einheitlichen Preis gibt.
(3) Eine viertelstundenübergreifende Arbitrage greift deshalb auf volumengewichtete Durchschnittspreise zurück.
(4) Der Höchst- und der Niedrigstpreis einer Viertelstunde bleiben außer Betracht, weil sie keine Menge führen und damit offen bliebe, wie viel Leistung zu ihnen handelbar gewesen wäre.
(5) Das Modell lässt nur Arbitrage zwischen Viertelstunden zu, während ein Betreiber dieselbe Viertelstunde mehrfach handeln und eine frühere Position innerhalb desselben Lieferzeitpunktes wieder glattstellen kann.
(6) Was der Betreiber damit zusätzlich verdient, ließe sich nur aus den Orderbüchern ablesen.
(7) Ohne Orderbücher bleibt ein rollierender Handel mit laufender Neubewertung eine Schätzung.
(8) Weil ein Betreiber dieselbe Viertelstunde mehrfach handeln kann, verbessert jede zusätzliche Handelsmöglichkeit den erzielbaren Preis, sodass der IDC insgesamt mehr trägt als ein einzelnes Geschäft zum Index.
(9) Das Modell bildet den Vorteil des mehrfachen Handels über einen Aufschlag ab, der Verkäufe über und Käufe unter dem Index bewertet und den Spread damit weitet.
(10) Die Höhe des Aufschlags wird als Sensitivität variiert.

Kommentar:

**\acs{FCR**

### 3.2.3 Absatz 6

(1) Die FCR wird zu einem Einheitspreis bezuschlagt, und das Modell übernimmt diesen Preis je Vier-Stunden-Zeitscheibe in Euro je Megawatt und Stunde.
(2) Weil die FCR allein die Bereitschaft vergütet und keinen Arbeitspreis kennt, ist ihr Erlös der Leistungspreis mal der vorgehaltenen Leistung.
(3) Je vorgehaltenem Megawatt bindet die FCR ein Ladezustandsband von einer Viertelstunde, das für den Handel nicht mehr zur Verfügung steht.
(4) Die FCR ist symmetrisch und bleibt über ihre Zeitscheibe von vier Stunden konstant.
(5) In Gleichung N bezeichnet $s(t)$ die Vier-Stunden-Zeitscheibe, in der die Viertelstunde $t$ liegt.

Kommentar:

### 3.2.3 Absatz 7

(1) [Gleichung]

Kommentar:

**\acs{aFRR**

### 3.2.3 Absatz 8

(1) Anders als die FCR wird die aFRR-Leistung nach pay-as-bid vergütet, weshalb das Modell den mengengewichteten Durchschnitt der Zuschläge einer Vier-Stunden-Zeitscheibe ansetzt.
(2) Den höchsten Zuschlag setzt das Modell nicht an, weil ein Anbieter ihn nicht sicher erreicht.
(3) Die Merit-Order der Ausschreibung, also die nach ihrem Preis geordneten Gebote, zeigt, welches Volumen zu welchem Preis bezuschlagt wird.
(4) Der mengengewichtete Durchschnitt der Merit-Order trifft den Wert, den ein Anbieter im Mittel erzielt.
(5) Im Jahr 2025 lag der höchste Zuschlag nach eigener Auswertung der Ausschreibungsdaten im Median 16 Prozent über dem Durchschnitt in der positiven und 22 Prozent in der negativen Richtung.
(6) Ein höherer Zuschlag beruht nicht auf einem technischen Vorteil, denn alle bezuschlagten Gebote erbringen dieselbe Leistung, sondern auf dem Bietverhalten.
(7) Der höchste Zuschlag wird deshalb allein als Sensitivität geführt.

Kommentar:

### 3.2.3 Absatz 9

(1) Der Erlös der aFRR-Leistung ist ihr Leistungspreis mal der vorgehaltenen Leistung.
(2) Je vorgehaltenem Megawatt bindet sie ein Ladezustandsband von einer Stunde.
(3) Vorgehalten wird je Richtung, und die Vorhaltung bleibt über die Vier-Stunden-Zeitscheibe konstant.
(4) Die Modellierung der aFRR ist eine Stufe einer Leiter aus sechs Stufen.
(5) Die ersten drei Stufen lauten ohne aFRR, nur Leistung zum Mittelpreis und nur Leistung zum höchsten Zuschlag.
(6) Die drei weiteren Stufen fügen die Arbeit hinzu, nämlich anteilig am Abruf, bis zur vorgehaltenen Leistung oder bis zu zehn Prozent des deutschen Abrufs.
(7) Der Basisfall nutzt die vierte Stufe, also die Leistung zum Mittelpreis und die Arbeit anteilig am Abruf.

Kommentar:

### 3.2.3 Absatz 10

(1) [Gleichung]

Kommentar:

**\acs{aFRR**

### 3.2.3 Absatz 11

(1) Die aFRR-Arbeit bewertet das Modell je Viertelstunde und Richtung mit dem volumengewichteten Mittel der Grenzpreise der Plattform PICASSO, gebildet über die 225 Vier-Sekunden-Zyklen einer Viertelstunde.
(2) Als Gewicht dient in der Mittelung der Sollwert, weil das je Zyklus aktivierte Volumen nicht veröffentlicht wird.
(3) Viertelstunden ohne Abruf einer Richtung bleiben für diese Richtung gesperrt.
(4) Die Anlage liefert aFRR-Arbeit anteilig am deutschen Abruf, im Verhältnis ihrer vorgehaltenen Leistung zur ausgeschriebenen Menge, und wählt keine einzelnen Viertelstunden aus.
(5) Wie viel Arbeit die Anlage liefern darf, prüft eine Sensitivität, die den anteiligen Abruf gegen eine freie Lieferung bis zur eigenen Reservierung und bis zu zehn Prozent des deutschen Abrufs stellt.
(6) Die gelieferte Arbeit stammt aus dem Speicher und wird am IDC in einer späteren Viertelstunde ausgeglichen, wobei der Ausgleich nie vor der Lieferung liegt und sich über den Tag schließt.
(7) Der Erlös der aFRR-Arbeit ist ihr Arbeitspreis mal der gelieferten Energie, vermindert um den Wert des Ausgleichs am IDC.

Kommentar:

### 3.2.3 Absatz 12

(1) [Gleichung]

Kommentar:

**Kurative Reservierung**

### 3.2.3 Absatz 13

(1) Die Zielfunktion trägt für die kurative Reservierung den Erlös aus vorgegebenem Preis mal reservierter Leistung.
(2) Die Anlage reserviert deshalb nur dann, wenn der vorgegebene Preis die entgangenen Erlöse der übrigen Märkte übersteigt.
(3) Anders als die übrigen Märkte trägt die kurative Reservierung keinen beobachteten Preis, sondern einen vorgegebenen, und sie ist eine Variable je Viertelstunde und Richtung.
(4) Die Variable bleibt über ihre Zeitscheibe konstant, die von einer vollen Stunde zur nächsten läuft, sodass jeweils vier aufeinanderfolgende Viertelstunden dieselbe reservierte Leistung tragen.
(5) Die Reservierung tritt in dieselbe Leistungsschranke wie die FCR und die aFRR und bindet darüber hinaus ein Ladezustandsband, das den Abruf über die Bindungsdauer deckt.
(6) Die positive und die negative Reservierung betrachtet das Modell getrennt, jede mit eigener Leistung und eigenem Ladezustandsband.
(7) [Gleichung]
(8) Die Mindestgröße von 25 MW ist ein Parameter des Produkts, sodass eine Stunde entweder ungebunden bleibt oder mit mindestens diesem Wert reserviert wird.
(9) Im Basisfall rechnet das Modell mit stetiger Reservierung, weil jeder Tag viele Läufe verlangt.
(10) Die Mindestgröße wird als Sensitivität zugeschaltet, um ihre Wirkung zu prüfen.

Kommentar:

## 3.2.4 Bestimmung des kurativen Reservierungspreises

Offene Vorschläge aus der Durchsicht: F3, F4, F6, F12, F13, F25.

### 3.2.4 Absatz 1

(1) Den kurativen Reservierungspreis bestimmt eine Suche außerhalb der Optimierung.
(2) Die Suche ruft das Tagesmodell wiederholt mit einem vorgegebenen Preis auf und liest aus jedem Lauf ab, wie viel Leistung die Anlage kurativ reserviert.
(3) Ein Lauf löst dabei stets den ganzen Tag mit allen 24 Stunden und beiden Richtungen zugleich, weil die Stunden über den Ladezustand zusammenhängen.
(4) Die Schleifen über die Stunden liegen deshalb allein in der Suche.
(5) Der Füllgrad einer Stunde und Richtung ist der Anteil der reservierten an der höchstmöglichen Leistung.
(6) Als voll reserviert gilt eine Stunde, wenn höchstens ein Hundertstel Prozent der Anschlussleistung fehlt.
(7) Die Bisektion setzt voraus, dass der Füllgrad mit dem Preis monoton steigt und jede Stunde damit genau eine Schwelle hat, wie Abbildung N für eine Beispielstunde zeigt.

Kommentar:

### 3.2.4 Absatz 2

(1) Die erste Iteration sucht je Stunde und Richtung den kleinsten für den ganzen Tag einheitlichen Preis, bei dem die Stunde voll reserviert ist, nach dem oberen Teil von Abbildung N.
(2) Ein Lauf mit einem Startdeckel von 800 Euro je Megawatt und Stunde prüft zunächst, ob jede Stunde voll ist.
(3) Der Deckel verdoppelt sich, bis alle Stunden voll sind, höchstens bis 51.200 Euro je Megawatt und Stunde.
(4) Zu Beginn teilen sich alle 48 Paare aus Stunde und Richtung dasselbe Suchintervall, und je offenem Intervall läuft eine Optimierung mit seiner Mitte als Preis.
(5) Jede Stunde des Intervalls liest ihren Füllgrad aus demselben Lauf ab.
(6) Ist die Stunde voll, setzt sie die obere Grenze ihres Intervalls auf diesen Preis, sonst die untere.
(7) Das Intervall zerfällt damit in zwei Gruppen.
(8) Die Suche bricht ab, sobald kein Intervall breiter als 0,05 Euro je Megawatt und Stunde ist.
(9) Die obere Grenze ist dann der einheitliche Reservierungspreis der ersten Iteration, mit dem die zweite beginnt.
(10) Je Paar aus Stunde und Richtung sind 14 Halbierungen nötig, also 672 Läufe je Tag, wenn jedes Paar allein liefe.
(11) Weil sich die Paare eines Intervalls einen Lauf teilen, genügen 84 bis 167 Läufe je Tag, im Mittel rund 130.

Kommentar:

### 3.2.4 Absatz 3

(1) Werden die Preise der ersten Iteration als Vektor gleichzeitig vorgegeben, sind nicht alle Stunden voll reserviert.
(2) Jede Stunde hat ihre Schwelle unter einem einheitlichen Preis gefunden, also gegen eine andere Konkurrenz um Leistung und Ladezustand.
(3) Eine Suche je Stunde führt hier nicht zum Ziel, weil die Stunden über den Ladezustand zusammenhängen.
(4) Die zweite Iteration gibt den Preisvektor der ersten Iteration vor und hebt alle noch offenen Stunden zugleich um ein Viertel an, bis der Speicher alle Stunden zusammen voll reserviert, nach dem unteren Teil von Abbildung N.
(5) Eine gerade gefüllte Stunde fällt wieder heraus, sobald die nächste Stunde steigt.
(6) Weil ein grober Aufstieg über das Ziel hinausschießt, senkt ein Abstieg danach jede Stunde einzeln um die Toleranz und prüft dabei die volle Reservierung aller Stunden.
(7) Der Abstieg endet erst, wenn ein ganzer Durchgang ohne Senkung bleibt.
(8) Ergebnis der zweiten Iteration ist je Stunde und Richtung der Vollreservierungspreis.
(9) Beim Vollreservierungspreis lässt sich keine einzelne Stunde mehr um die Toleranz senken, ohne dass eine Stunde aus der vollen Reservierung fällt.
(10) Die positive und die negative Richtung bleiben dabei als zwei Produkte getrennt.

Kommentar:

### 3.2.4 Absatz 4

(1) Beide Iterationen zusammen verlangen je Tag einige hundert Läufe.
(2) Die Suche ist die innerste von mehreren Schleifen, nämlich über Tage, Konfigurationen und Studien, wie Abbildung N zeigt.
(3) Innerhalb eines Tages steht die Suche neben einem Preis-Sweep über zehn vorgegebene Preise.
(4) Eine der Studien ist der $\lambda$-Hebel, der die Preise des IDC mit einem Faktor $\lambda$ zwischen 1,0 und 2,0 um ihr Tagesmittel streckt und damit den Spread erhöht.
(5) Eine andere Studie ist die Leiter der aFRR-Modellierung.
(6) Die Studie Einzelmarkt optimiert jeden Markt für sich und trägt den Vergleich je Markt in der Validierung.

Kommentar:

### 3.2.4 Absatz 5

(1) Der so bestimmte Preis ist gegen die Bewertung abzugrenzen, die der geltende Rahmen für entgangene Erlöse vorsieht.
(2) Der in Abschnitt X beschriebene Weber-Ansatz ist Stand der Technik und prägt die Bemessung entgangener Erlösmöglichkeiten im geltenden Rahmen.
(3) Eine deterministische Optimierung mit vollständiger Preiskenntnis kennt jedoch kein Volatilitätsmaß und macht den Zeitwert der Option damit konstruktionsbedingt zu null.
(4) Hinzu kommt, dass Fahrplanbildung und erwarteter Preis aus derselben Preiszeitreihe stammen und eine Bewertung des entgangenen Erlöses gegen diese Reihe zirkulär wäre.
(5) Der Ansatz bewertet außerdem jedes Zeitintervall unabhängig, während die Ladezustandsbilanz die Intervalle bindend koppelt.
(6) Die Kopplung über den Ladezustand wiegt bei einem Energieinhalt je Leistung von 2,5 Stunden schwer, denn eine Reservierung von einer Megawattstunde je Megawatt bindet einen erheblichen Teil des Speichers.
(7) Der ermittelte kurative Reservierungspreis ist deshalb opportunitätskostenbasiert und enthält keinen Optionswert.
(8) Die Vergütungsstruktur der Festlegung trägt den Optionswert ohnehin nur dann, wenn er den anteiligen Werteverbrauch übersteigt, weil sie sich aus den Erzeugungsauslagen und dem höheren der beiden übrigen Bestandteile zusammensetzt.
(9) Anders als Anlage 5 der Festlegung, die von gesperrter Leistung ausgeht, bleibt die Anlage unter der kurativen Reservierung handlungsfähig, weshalb der ermittelte Preis unter dem Ausgleich nach der Festlegung liegen kann.
(10) Den Energieanteil eines Abrufs, den der Preis der kurativen Reservierung mit abdeckt, bildet das Modell nicht ab.
(11) Die Höhe der Pönale bestimmt die Untersuchung nicht, weil das Modell die daraus folgende Risikoprämie nicht trägt.
(12) Der ermittelte kurative Reservierungspreis ist damit der opportunitätskostenbasierte Teil des Gebots und nicht das Gebot.

Kommentar:

## 3.3 Validierung des Modells

## 3.3.1 Vergleichsmaßstab

Offene Vorschläge aus der Durchsicht: F24.

### 3.3.1 Absatz 1

(1) Als Vergleichsmaßstab dient der Erlösindex der Battery Charts der RWTH Aachen, der für ein BESS am deutschen Markt einen marktübergreifenden Erlös ausweist.
(2) Anders als die Prüfungen der Umsetzung, die das Modell mit sich selbst vergleichen, misst die Validierung an einer Referenz von außen.
(3) Geprüft wird die Plausibilität des Erlösniveaus des ungebundenen Fahrplans, also einer Zwischengröße des Modells.
(4) Nicht geprüft werden der kurative Reservierungspreis und die Frage, ob die Implementierung das formulierte Problem korrekt löst.
(5) Der ungebundene Erlös ist eine Zwischengröße und kein Ergebnis der Arbeit.
(6) Die Validierung nennt ihre Zahlen deshalb schon hier und nimmt kein Ergebnis vorweg.

Kommentar:

### 3.3.1 Absatz 2

(1) Der Index führt FCR, aFRR-Leistung, aFRR-Arbeit und den kontinuierlichen Intraday-Handel, kennt jedoch keinen DA.
(2) Dem Index steht deshalb der Erlös des Modells aus beiden Energiemärkten zusammen gegenüber.
(3) Der Index bedient die Märkte nacheinander und teilt Leistung, Speicherinhalt und Zyklen nach fest gesetzten Anteilen zu, während das Modell alle Märkte eines Liefertages gemeinsam entscheidet.
(4) Die Bezugsanlage des Index hält eine Megawattstunde je Megawatt, also einen Energieinhalt je Leistung von einer Stunde, die Modellanlage 2,5 Stunden.
(5) Der Index wird als gleitender Mittelwert über 365 Tage veröffentlicht und ist deshalb nur am Jahresende mit einem Kalenderjahr vergleichbar.
(6) Die Validierung umfasst darum das Jahr 2025.
(7) Verglichen wird in zwei Stufen, marktübergreifend und für jeden Markt allein, wobei im zweiten Fall alle übrigen Märkte im Modell abgeschaltet sind.

Kommentar:

## 3.3.2 Unterschiede in Vorausschau und Marktumfang

Offene Vorschläge aus der Durchsicht: F7.

### 3.3.2 Absatz 1

(1) Vor dem Vergleich der Zahlen ist zu klären, welche Abweichung zwischen Index und Modell zu erwarten ist, denn beide rechnen nach verschiedenen Regeln.
(2) Der Index bildet erreichbaren Handel ab und erhebt nach eigener Darstellung nicht den Anspruch, den höchsten erzielbaren Erlös zu treffen.
(3) Der Intraday-Handel des Index folgt einem rollierenden Verfahren, das in jedem Schritt gegen die bis dahin bekannten Preise optimiert und über künftige Preise nichts voraussetzt.
(4) Das Modell kennt dagegen alle Preise des Liefertages, und dieser Unterschied allein macht rund zehn Prozent des Erlöses im kontinuierlichen Intraday-Handel aus.
(5) Der größere Energieinhalt je Leistung der Modellanlage erhöht den Erlös in den Leistungsmärkten, denn er lässt mehr Leistung mit dem geforderten Energievorhalt zu.
(6) Auch der sichere Zuschlag erhöht den Erlös dort, denn das Modell übernimmt die veröffentlichten Preise und setzt jede angebotene Leistung als bezuschlagt.
(7) Die Degradationskosten senken den Erlös dagegen in den Energiemärkten, denn das Modell verrechnet dort jeden Zyklus mit Kosten, während der Index nur eine Zyklengrenze führt.
(8) Das Modell soll den Index nicht treffen, denn es ist als Obergrenze gebaut.
(9) Erwartet wird eine Abweichung, deren Richtung je Markt aus den genannten Unterschieden folgt.
(10) Das Prüfkriterium lautet, dass der Jahresgang übereinstimmt, dass das Modell in den Leistungsmärkten über dem Index liegt und dass es in den Energiemärkten darunter bleibt.
(11) Trägt eine Abweichung die entgegengesetzte Richtung, liegt ein Fehler der Umsetzung nahe und nicht eine Eigenschaft des Modells.
(12) Abbildung N stellt beide Reihen über das Jahr 2025 gegenüber.

Kommentar:

### 3.3.2 Absatz 2

(1) Über das Jahr 2025 liegt der Index im Mittel bei 259,7 Tausend Euro je Megawatt und Jahr, das Modell bei 348,3 Tausend Euro je Megawatt und Jahr.
(2) Das Verhältnis beider Reihen beträgt im Median 1,33 bei einer Spanne von 1,06 bis 1,54, und das Modell liegt in allen zwölf Monaten über dem Index.
(3) Die beiden Reihen korrelieren mit einem Koeffizienten von 0,97, sodass das Modell den Jahresgang des Index abbildet und gleichmäßig darüber liegt.
(4) Je Markt allein ist das Bild nicht einheitlich, wie Anhang X zeigt.
(5) In der FCR erreicht das Modell das 1,24-Fache des Index und in der aFRR das 1,52-Fache.
(6) Am DA erreicht das Modell das 0,86-Fache des Index und im IDC das 0,89-Fache.
(7) Das Modell ist damit nicht durchgängig überhöht, denn wo es Degradationskosten verrechnet, bleibt es hinter der Referenz zurück.
(8) Der Aufschlag entsteht in den Leistungsmärkten, wo der größere Energieinhalt je Leistung und der sichere Zuschlag wirken.
(9) Den größten Teil des Faktors bei der aFRR erklärt die vorgehaltene Leistung, denn der Index reserviert nach seiner Methodik nur ein Viertel der Anschlussleistung für die aFRR-Leistung.
(10) Das Modell hält dagegen im Jahresmittel 81 MW in positiver und 72 MW in negativer Richtung von 100 MW vor.
(11) Alle drei Teile des Prüfkriteriums sind damit erfüllt.

Kommentar:

