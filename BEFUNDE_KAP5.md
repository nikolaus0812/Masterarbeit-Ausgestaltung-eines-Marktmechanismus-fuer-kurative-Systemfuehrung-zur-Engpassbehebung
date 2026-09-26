# Befunde der Kontrollprüfung von Kapitel 5

**Angelegt am 26.09.2026.** Grundlage ist die Kontrollprüfung nach
`UEBERGABE_KAP5_PRUEFUNG.md`. Geprüft ist der Stand von `chapters/chapter_5.tex`
vom 26.09.2026, 123 Seiten.

**Stand 26.09.2026 nachts: alle Befunde erledigt**, siehe Abschnitte 0a bis 0c. Die Einzelbefunde darunter sind der Nachweis und bleiben stehen.

**Vorbehalt.** Der Verfasser schließt die Abschnitte 5.4 und 5.5 noch ab. Befunde
in diesen beiden Abschnitten können dadurch überholt sein und sind vor der
Umsetzung gegen den dann geltenden Text zu halten. Die Abschnitte 5.1 bis 5.3
und die Kapiteleinleitung sind davon nicht betroffen.

**Status.** `offen` bis der Verfasser entscheidet, dann `umgesetzt`,
`abgelehnt` oder `überholt`.

---

## 0 Prüfsuite und Build, Stand 26.09.2026

| Prüfung | Ergebnis |
|---|---|
| `python tools/pruefen.py --alle` | ohne Befund, 15 Dateien |
| `python tools/pruefe_stil.py` | Kapitel 5 ohne Verstoß, 21 Altbefunde Doppelpunkt in Kapitel 1 bis 3 |
| `python tools/absatzlaengen.py chapters/chapter_5.tex` | 5 Absätze außerhalb von 8 Sätzen |
| Build | 123 Seiten, Biber ohne Warnung, allein `ch:conc` undefiniert, weil Kapitel 6 auskommentiert ist |

Die fünf kurzen Absätze sind genau die in der Übergabe angekündigten, nämlich
die Kapiteleinleitung mit 7 Sätzen sowie in 5.5 der geltende Rahmen mit 6, der
Aufwand mit 7, die systemweite Ausrollung mit 6 und der Forschungsbedarf mit 6.

---

## 0a Erledigt am 26.09.2026

Der Verfasser hat die Absätze A1 und A2 des Abschnitts 5.4 gestrichen. Damit
sind **B6** und **B14** gegenstandslos. Die neun weiteren Absätze, die der
Verfasser in derselben Sitzung diktiert hat, sind noch nicht geschrieben; die
Fassungen liegen im Gespräch vor und im Protokolleintrag vom 26.09.2026.

**B29 neu.** `chapters/chapter_2.tex` Zeile 1295 gibt § 13c EnWG ohne Beleg
wieder. In Betracht kommt
`bundesministerium_der_justiz_energiewirtschaftsgesetz_2025`. Status offen.

**B30 neu.** `chapters/chapter_5.tex` Zeile 1399 doppelt die
Binnenmarktverordnung fast wortgleich gegen `chapters/chapter_2.tex`
Zeile 2587. Status offen.

---

## 0b Erledigt am 26.09.2026, zweiter Durchgang

5.4 und 5.5 sind abgeschlossen, 5.5 auf sechs Absätze umgebaut, der Nachweis
der Verfügbarkeit nach 5.1 verschoben, alle Zitate aus Kapitel 5 entfernt bis
auf Weber/Mahgoub und Consentec. Damit erledigt:

| Befund | Wie |
|---|---|
| B1 | Aufwand-Absatz gestrichen, *des Mechanismus* steht nicht mehr |
| B2 | 5.5 A1 neu, § 13c wird nicht mehr gebraucht |
| B5, Zeile 1272 | Satz gestrichen |
| B18 | *innerhalb der Regelzone* ergänzt |
| B30 | Binnenmarktverordnung gestrichen |
| Ableitung 5 der Übergabe | Satz zum Preisniveau der Zone zurückgenommen |

**B31 neu.** *Lieferfähigkeit* in 5.1 A7 und A10 gegen *Verfügbarkeit* in
5.1 A11 und im Forschungsbedarf. Zu vereinheitlichen. Status offen.

**Zitate.** Alle entfernten Schlüssel sind in Kapitel 1 bis 4 weiter zitiert.
Die Aussage zur Wirksamkeit in 5.5 A6 trägt ohne Beleg jetzt *dürfte*.

Offen bleiben aus der Liste: B3, B4, B5 (Zeilen 802, 1006, 1008), B7 bis B13,
B15 bis B17, B19 bis B29, B31.

---

## 0c Abgearbeitet am 26.09.2026, dritter Durchgang

Alle verbliebenen Befunde sind auf Vorgabe des Verfassers umgesetzt oder
hingenommen. Die Liste ist damit **geschlossen**.

| Befund | Erledigung |
|---|---|
| B3, B23 | 5.1 A4: netzknotenscharfe Beschaffung mit beschränkter Präqualifikation, beide Anforderungen ziehen in dieselbe Richtung |
| B4 | Numerus |
| B5 | drei Stellen mit ausgeschriebenem Bezug |
| B7, B13, B15 | **hingenommen**, Regel 10 |
| B8, B11, B12 | Nebensätze in 5.1 gestrichen, Rückgriff statt Wiederholung |
| B9, B10 | 5.2 A1 kündigt nur an, 5.5 A6 greift zurück |
| B16 | 5.3 A4 eröffnet mit These statt mit Kapitel 4 |
| B17 | halbe Megawattstunde je Megawatt |
| B19 | der vorsichtigere Wert |
| B20 | relativ steigt, absolut sinkt |
| B21 | Kapitel 4: fast das ganze Jahr über |
| B22 | Bemessungsgegenstand und Preis im Gebot |
| B24, B25 | Kapiteleinleitung neu, acht Sätze |
| B26, B27 | datierte ERLEDIGT-Zeilen, nichts gelöscht |
| B28 | *Abrufdauer* bleibt zulässig, Entscheidung des Verfassers |
| B29 | Kapitel 2: Beleg für § 13c |
| B31 | Verfügbarkeit bei der Einplanung, Lieferfähigkeit im Fehlerfall |
| Ableitungen 1 bis 4 | vom Verfasser bestätigt, Marken datiert |

---

## 1 Harte Regelverstöße

### B1 „des Mechanismus" allein, Zeile 1394, Status erledigt am 26.09.2026

> Aus einer Frage der Menge wird damit eine Frage des Nachweises, sodass ein
> Verfahren zum Nachweis der Verfügbarkeit konstitutiver Bestandteil **des
> Mechanismus** ist.

CLAUDE.md Abschnitt 5 verlangt für den kurativen Marktmechanismus „danach immer
mit dem Adjektiv und nie *der Mechanismus* allein". Die einzige Stelle dieser Art
im ganzen Kapitel.

Vorschlag: *… konstitutiver Bestandteil des kurativen Marktmechanismus ist.*

In 5.5 A3, dem Absatz zum Aufwand, der ohnehin noch abzuschließen ist.

### B2 Absolute Feststellung ohne Beleg, Zeile 1364, Status erledigt am 26.09.2026

> Eine Vergütung der Bereithaltung mit einem Leistungspreis kennt das
> Engpassmanagement **allein** für systemrelevante Anlagen nach einer
> angezeigten Stilllegung, sodass der kurative Marktmechanismus an keine breit
> angelegte Beschaffungsform anschließen kann.

Das ist die erste der beiden inhaltlichen Umkehrungen vom 25.09.2026. Die
Aussage trägt sachlich, steht aber ohne Norm und ohne Quelle, obwohl der
Kommentar darüber § 13c EnWG nennt. Stilregel 8 verlangt hier den Beleg.

Vorschlag: *… allein nach §\,13c \ac{EnWG} für systemrelevante Anlagen nach
einer angezeigten Stilllegung \cite{bundesministerium_der_justiz_energiewirtschaftsgesetz_2025}*.

In 5.5 A1, dem Absatz zum geltenden Rahmen, der noch abzuschließen ist.

---

## 2 Bezüge und Grammatik

### B3 Demonstrativum ohne Bezugswort, Zeile 191, Status offen

> Knotenscharfe Gebote und die Wirksamkeit am Netzknoten sind die
> Grundvoraussetzung dafür, dass der \ac{ÜNB} eine kurative Maßnahme überhaupt
> einplanen kann.
> Der Entwurf sieht **eine solche Beschaffung** vor.

Im Vorsatz steht keine *Beschaffung*. Der Befund ist ein Rückstand der Kürzung
vom 25.09.2026: die zurückgenommene Fassung enthielt „netzknotenscharfe
Beschaffung", und das Bezugswort ist mit ihr gefallen. Verstoß gegen Stilregel 5.

In 5.1 A4.

### B4 Numerusfehler, Zeile 1302, Status offen

> **Jede** dieser Verwendungen verlangt eine eigene Vergütung des Abrufs, denn
> **sie unterscheiden sich** in Häufigkeit und Dauer.

In 5.4 A5.

### B5 Pronomen über die Satzgrenze, Status offen

Alle drei verstoßen gegen Stilregel 5.

- Zeile 1006 „**Ihre** Zusage trägt zudem ein Risiko" und Zeile 1008 „so ist die
  kurative Reservierung **für sie** eine zusätzliche Erlösquelle". Bezug ist die
  Wind- oder Photovoltaikanlage aus Satz 1 beziehungsweise Satz 5 desselben
  Absatzes. In 5.3 A3.
- Zeile 1272 „Erzeugt **es** einen Engpass, so erhält **es** einen Erlös des
  \ac{ÜNB} statt einer Abregelung". Bezug ist das \ac{BESS} aus dem Vorsatz.
  In 5.4 A4.
- Zeile 802 „**Beide Mengen** von Stunden fallen nicht zusammen". Die zweite
  Menge ist über drei Sätze verteilt nur angedeutet. In 5.2 A6.

---

## 3 Dopplungen innerhalb von Kapitel 5

Status aller acht: offen. Nach `WORKFLOW.md` Regel 10 ist jeweils die Stelle
aufzulösen, die die Aussage für ihre Erklärung nicht braucht, und nicht die
erste Fundstelle.

| Nr | Aussage | Stellen | Vorschlag |
|---|---|---|---|
| B6 | Die Präqualifikation setzt auf der Regelleistung auf | 1121 in 5.4 A1, 1395 in 5.5 A3 | **erledigt am 26.09.2026**, 5.4 A1 ist gestrichen |
| B7 | Ein Zuschlag zeigt, dass die Anlage am Engpass wirkt | 314 in 5.1 A6, 1262 in 5.4 A4 | in 5.4 halten, in 5.1 streichen |
| B8 | Auf die \ac{aFRR} entfällt der größte Teil des Erlöses | 429 in 5.1 A9, 688 in 5.2 A3 | offen |
| B9 | Das Optimierungsmodell löst jeden Liefertag für sich | 538 in 5.2 A1, 807 in 5.2 A7 | in 5.2 A7 halten, in A1 streichen |
| B10 | Das Optimierungsmodell rechnet eine einzelne Anlage | 806 in 5.2 A7, 1415 in 5.5 A5 | offen |
| B11 | Abrufwahrscheinlichkeit und Pönale bleiben außer Betracht | 361 in 5.1 A7, 810 in 5.2 A7, 1443 in 5.5 A7 | 5.5 A7 ist der Forschungsbedarf und trägt sie eigens, zu prüfen sind 5.1 und 5.2 |
| B12 | Die kurative Ausschreibung liegt hinter der Regelleistung | 238 in 5.1 A5, 431 in 5.1 A9, 690 in 5.2 A3 | offen |
| B13 | Die Ablösung bestimmt die nötige vorgehaltene Energie | 1044 in 5.3 A5, 1408 in 5.5 A4 | in 5.5 A4 halten, weil dort die Ablösung der Gegenstand ist |

Zu B7 ein eigener Hinweis: der Kommentar bei Zeile 1252 sagt ausdrücklich, der
Satz zur Auskunft über das Netz habe in 5.1 gestanden und passe in 5.4 besser.
Der Umzug ist am 25.09.2026 nicht zu Ende geführt worden, denn 5.1 hat ihn
behalten.

---

## 4 Dopplungen gegen die Kapitel 2, 3 und 4

### B14 Fast wörtlich aus Kapitel 2, Zeile 1122, Status erledigt am 26.09.2026

- Kapitel 5: *Ein \ac{BESS} vereint damit die Eigenschaften, die bei den
  übrigen Technologien einzeln auftreten.*
- `chapters/chapter_2.tex` Zeile 1037: *\ac{BESS} vereinen die Eigenschaften,
  die bei den übrigen Technologien einzeln auftreten: Sie wirken in beide
  Richtungen und erreichen die kürzesten Reaktionszeiten.*

5.4 A1 ist ein zusammenfassender Absatz, und nach Regel 10 darf ein
Zwischenfazit zusammenfassen. Der Wortlaut ist aber nahezu deckungsgleich.
In 5.4 A1.

### B15 Fast wörtlich aus Kapitel 3, Zeile 163, Status offen

- Kapitel 5: *Gegenstand dieser Vergütung sind die gelieferte Energie und die
  Nachlaufpflicht je Megawatt.*
- `chapters/chapter_3.tex` Zeile 93: *Die gesonderte Vergütung des Abrufs umfasst
  die gelieferte Energie und die Nachlaufpflicht je Megawatt.*

In 5.1 A2 wiederholen drei von acht Sätzen Kapitel 3, nämlich die Zeilen 158,
162 und 163. Das Nennen der Anforderung ist die Aufgabe von 5.1, die Zeilen 162
und 163 lassen sich aber zu einem Satz zusammenziehen und schaffen damit Platz
für die Diskussion.

### B16 Fast wörtlich aus Kapitel 4, Zeilen 1010 und 980, Status offen

- Kapitel 5 Zeile 1010: *Über das Jahr trifft der größte
  Engpassmanagementbedarf auf die günstigste Reservierung.*
- `chapters/chapter_4.tex` Zeile 864: *Das größte Potenzial liegt im Winter, denn
  dort trifft der größte Engpassmanagementbedarf auf die günstigste
  Reservierung.*
- Kapitel 5 Zeile 980 und `chapters/chapter_4.tex` Zeile 865 stimmen ebenso
  nahezu überein.

Die beiden Eröffnungssätze von 5.3 A4 sind der Schlussabsatz von Kapitel 4. Neu
in 5.3 A4 sind erst die Windfronten als Ursache und die Kombination eines
\ac{BESS} mit Anlagen der Windenergie.

---

## 5 Aussagen, die vom Beleg abweichen

### B17 Einheit verrutscht, Zeile 1045, Status offen

> Eine vorgehaltene Energie für **eine halbe Stunde** ist fast zum Preis **einer
> Viertelstunde** zu haben und verdoppelt die Zeit für eine solche Ablösung.

`chapters/chapter_4.tex` Zeile 1348 schreibt: *Eine halbe Megawattstunde je
Megawatt ist damit fast zum Preis einer viertel zu haben und verdoppelt die
Abrufdauer, über die der \ac{ÜNB} die kurative Maßnahme durch eine andere ablösen
kann.* Kapitel 5 rechnet die Energie in Stunden um. Über die Beschriftung der
Abbildung als zugehörige Abrufdauer ist die Umrechnung vertretbar, doch
*Viertelstunde* ist in dieser Arbeit die Zeiteinheit der Märkte und liest sich
hier als Laufzeit eines Produkts. CLAUDE.md Abschnitt 8 verlangt zudem, dass
jede Größe ihre Einheit einzeln trägt.

Vorschlag: *Eine vorgehaltene Energie von einer halben Megawattstunde je
Megawatt ist fast zum Preis einer viertel zu haben.*

In 5.3 A5.

### B18 Handelsschluss verallgemeinert, Zeile 1206, Status erledigt am 26.09.2026

> Der Handel am \ac{IDC} läuft deshalb bis fünf Minuten vor Lieferbeginn und
> nimmt der Regelleistung diesen Ausgleich ab.

`chapters/chapter_2.tex` Zeile 1649: der Handelsschluss tritt gestaffelt ein,
nämlich 60 Minuten vor Lieferbeginn für den grenzüberschreitenden Handel, 30
Minuten für den Handel zwischen den Regelzonen und 5 Minuten für den
regelzoneninternen Handel. Kapitel 5 nennt allein die kürzeste Frist.

Vorschlag: Ergänzung *innerhalb der Regelzone*.

In 5.4 A3.

### B19 Gemessene Spanne, Zeile 580, Status offen

> Der ausgewiesene kurative Reservierungspreis ist damit die vorsichtigere Seite
> **einer gemessenen Spanne**.

Kapitel 4 weist keine Spanne aus, sondern einen Wert je Stunde. Der Absatz
begründet allein, dass ein globales Minimum nicht über dem ausgewiesenen Preis
läge.

Vorschlag: *… ist damit der vorsichtigere Wert.*

In 5.2 A2.

### B20 Aufschlag relativ gegen absolut, Zeile 1341, Status offen

> Der kurative Reservierungspreis gibt dabei weniger nach als der Markterlös,
> sodass die kurative Bindung gegenüber dem Markt nicht günstiger wird.

`chapters/chapter_4.tex` Zeile 1404: der Aufschlag gegenüber dem Markterlös
steigt relativ von 23,3 auf 24,8 Prozent, **fällt aber absolut** von
79,4 auf 70,3 TsdEurMWa. Der Satz trägt in der relativen Lesart. Für den
\ac{ÜNB} sinkt die Differenz absolut, was die zweite Umkehrung vom 25.09.2026
teilweise abschwächt.

Vorschlag: den Vergleich ausdrücklich als relativen kennzeichnen oder den
absoluten Rückgang mit einem Halbsatz aufnehmen.

In 5.4 A6, dem letzten Absatz des Abschnitts.

### B21 Befund in Kapitel 4, nicht in Kapitel 5, Status offen

`chapters/chapter_4.tex` Zeile 863 sagt, die kurative Vorhaltung bleibe im
Tagesmittel „das ganze Jahr über" unter der Bezugslinie, während Zeile 844
362 von 365 Tagen in der Entlade- und 364 von 365 Tagen in der Laderichtung
ausweist. Kapitel 5 Zeile 965 formuliert mit „fast das ganze Jahr" richtiger als
Kapitel 4. Der Befund liegt damit in Kapitel 4 und nicht in Kapitel 5.

---

## 6 Logikbrüche

### B22 Unbegründetes „damit", Zeile 161, Status offen

> Eine Bemessung an der gelieferten Energie träfe deshalb den falschen
> Gegenstand, weil die Vorhaltung auch ohne Abruf Erlöse kostet.
> Über die Vergütung der Vorhaltung entscheidet **damit** der Markt.

Das *damit* folgt nicht aus dem Vorsatz. Zwischen dem falschen
Bemessungsgegenstand und der marktlichen Preisbildung fehlt ein Glied. Verstoß
gegen Stilregel 2 und Stilregel 4. In 5.1 A2.

### B23 Unbelegte Behauptung und Themenwechsel, Zeile 192, Status offen

> Aus genügend Geboten mit denselben Eigenschaften folgt am Ende ein Markt, der
> mit wenig Regulierung auskommt.

Unbelegt, und der Absatz behandelt die Diskriminierungsfreiheit und die
Lokationalität, nicht den Regulierungsumfang. In 5.1 A4, demselben Absatz wie B3.

---

## 7 Kapiteleinleitung

Neben dem fehlenden achten Satz zwei Befunde, Status beide offen.

### B24 Wortwiederholung

*Anschließend* steht zweimal, in Zeile 51 und in Zeile 53.

### B25 Ankündigung deckt 5.4 nur halb

Zeile 53 kündigt 5.4 an als *die künftige Rolle der \ac{BESS} im Strommarkt und
bei den Systemdienstleistungen*. Der Abschnitt heißt „Die Rolle der \acs{BESS} im
Engpassmanagement und am Markt", und seine Absätze 3 bis 5 behandeln die
Betriebsplanung und das Engpassmanagement. Die Ankündigung lässt die größere
Hälfte aus.

---

## 8 Zahlen über die Vorgabe hinaus, Status offen

Der Kopfkommentar in den Zeilen 22 bis 27 lässt allein die Reaktionszeitklasse
von etwa zwei Minuten, die Zeitscheibe der \ac{aFRR} von vier Stunden, die
halbe Stunde gegen die Viertelstunde und § 13a EnWG stehen und verlangt, jede
weitere Zahl beim Nachziehen einzeln zu begründen. Im Text stehen zusätzlich:

| Zahl | Zeile | Abschnitt |
|---|---|---|
| die drei Reaktionszeitklassen mit ihren Werten, zweimal | 98 und 102 f. | 5.1 A1 |
| 23.30 Uhr | 254 | 5.1 A5 |
| fünf Minuten vor Lieferbeginn | 1206 | 5.4 A3 |
| § 17 Abs. 2b EnWG | 315 | 5.1 A6 |
| um ein Sechstel | 1340 | 5.4 A6 |

Umgekehrt steht die im Kopfkommentar genannte Zeitscheibe der \ac{aFRR} von
vier Stunden **nicht** mehr im Text. Der Kopfkommentar ist insoweit
nachzuziehen.

---

## 9 Hygiene im Quelltext, Status offen

### B26 Drei überholte Marken `EIGENSTAENDIGE ABLEITUNG`

Im Quelltext stehen acht Marken, lebendig sind fünf.

| Zeile | Stand |
|---|---|
| 812 | überholt, die Pool-Ableitung ist am 25.09.2026 zurückgenommen |
| 846 | lebendig, Anweisungszeitpunkt als Kostenfaktor |
| 1028 | lebendig, Gebot für anschließende Stunden |
| 1175 | überholt, alle drei Ableitungen sind bestätigt oder zurückgenommen |
| 1279 | lebendig, Verteilung der Vorhaltekosten |
| 1372 | lebendig, Wirkungen eines Gebotszonensplits |
| 1401 | lebendig, zusätzliches Produkt für die Ablösung |
| 1424 | überholt, am 25.09.2026 bestätigt und präzisiert |

Die fünf lebendigen Marken decken sich genau mit der Liste in
`UEBERGABE_KAP5_PRUEFUNG.md`. Wer künftig nach der Marke greppt, findet
gleichwohl acht Treffer.

### B27 Kopfkommentar führt zwei erledigte offene Punkte

Die Zeilen 32 bis 37 führen zwei offene Punkte, beide erledigt. Der Begriff
*kapazitätsbasierter Redispatch* ist am 25.09.2026 entfernt, und die Begründung
in 5.1, warum der Betreiber unter vollständiger Bindung besser steht, steht
nicht mehr im Text.

### B28 Begriff `Abrufdauer`

In Kapitel 5 kommt *Abrufdauer* nicht mehr vor. In
`chapters/chapter_4.tex` Zeile 1293 steht der Begriff noch als eigene Größe,
nämlich *Die vorgehaltene Energie folgt aus der Abrufdauer, also aus der Zeit,
über die eine kurative Maßnahme wirken muss*, ebenso in Zeile 1348 und im Label
`sec:sensi_abrufdauer`. Entscheidung des Verfassers nötig: bleibt *Abrufdauer*
als Name der Zeitdauer zulässig, oder ist Kapitel 4 nachzuziehen?

---

## 10 Geprüft, kein Befund

- **`regelleistung_ausschreibungsdaten_2026` ist nicht verloren.** Der Schlüssel
  steht siebenmal in den Kapiteln 2, 3 und 4, und
  `chapters/chapter_4.tex` Zeile 1043 trägt die Anonymisierung der
  Ergebnislisten. Die Aussage in 5.2 zu den Gebotsstrategien braucht ihn nicht.
  Der offene Punkt aus `HANDOFF.md` Abschnitt 1.0 ist damit erledigt.
- **Keine gesperrten Verstärkungen** aus Stilregel 15 und kein *perfekt*.
- **Keine Gedankenstriche und keine Semikola.**
- **Keine Pronomen am Satzanfang.**
- **Keine gesperrten Begriffe** nach CLAUDE.md Abschnitt 5, kein *Abrufdauer*,
  kein *Sanktion*, kein *Redispatchplanung*, kein *kapazitätsbasierter
  Redispatch*.
- ***diese Arbeit*** steht allein in der Kapiteleinleitung, Zeile 48, und damit
  regelkonform.
- **Zeitliches Muster belegt.** Zeile 969 *nachts am niedrigsten und mittags am
  höchsten* deckt sich mit `chapters/chapter_4.tex`, wonach der Median der Summe
  beider Richtungen von 9,6 EurMWh um Mitternacht auf 79,3 EurMWh um 14 Uhr
  steigt. Zeile 968 *Entladereservierung am Vormittag und am Abend teuer* deckt
  sich mit dem Füllgrad der ersten Iteration, der für die Entladereservierung um
  8, 18 und 19 Uhr am niedrigsten liegt.
- **Kein zweiter sachlicher Fehler der Art vom 25.09.2026.** 5.4 sagt richtig,
  dass zwei \ac{BESS} ein bilanziell ausgeglichenes Maßnahmenset bilden, und
  nennt dafür keinen gemeinsamen Netzknoten.

### Zur Bestätigung durch den Verfasser

Zeile 1041 *Eine Zeitscheibe von einem Tag bindet die Stunden unvollständig und
kostet dennoch beinahe den vollen Preis* stützt sich auf Kapitel 4 zur **ersten
Iteration** der Preissuche, nämlich 97,6 Prozent der Zahlung bei einem Füllgrad
von 85,9 Prozent entladend und 89,6 Prozent ladend. Die Gleichsetzung von
erster Iteration und Zeitscheibe von einem Tag ist eine Deutung und nicht der
Wortlaut von Kapitel 4. Sie trifft die Sache, weil die erste Iteration einen
Preis je Tag setzt, ist aber eine Bestätigung wert.

---

## 11 Offene Arbeit, unverändert aus der Übergabe

- **Vier kurze Absätze in 5.5** und die Kapiteleinleitung.
- **Ein Satz muss noch nach 5.5:** *Eine Vergütung der kurativen Vorhaltung
  verlangt eine eigene Struktur, zumal für die kurative Reservierung bislang
  kein Vergütungsrahmen besteht.* Er passt in 5.5 A1, den Absatz zum geltenden
  Rahmen, der bei sechs Sätzen liegt und damit Platz für zwei hat. Dort liegt
  auch B2.
- **Fünf eigenständige Ableitungen** sind dem Verfasser einzeln vorzulegen,
  nämlich die Marken in den Zeilen 846, 1028, 1279, 1372 und 1401.
