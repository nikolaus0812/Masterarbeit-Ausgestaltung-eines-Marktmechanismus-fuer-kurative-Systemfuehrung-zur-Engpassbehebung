# Auftrag an Claude Code

Diese Datei liegt im Wurzelverzeichnis des Repositorys der Schriftfassung und ist
zu Beginn jeder Sitzung zu lesen. Sie bindet dich für alle Arbeiten an diesem
Repository.

Stand 08.09.2026. Sie ersetzt die Fassung vom 07.09.2026. Geändert sind die
Pfadangaben, die Gliederung von Kapitel 3, die getroffenen Modellentscheidungen und
der Abschnitt zur Arbeitsweise, der jetzt das satzweise Ausformulieren regelt.

---

## 1 Gegenstand

Masterarbeit am IAEW der RWTH Aachen mit dem Titel *Ausgestaltung eines
Marktmechanismus für kurative Systemführung zur Engpassbehebung*. Abgabe am
15.10.2026, Kolloquium am 12.10.2026. Deutschsprachig, LaTeX mit KOMA-Script und
biblatex.

Die Arbeit bestimmt den kurativen Reservierungspreis, also den Betrag, den ein BESS
für eine kurative Vorhalteverpflichtung mindestens fordern muss, um gegenüber
seiner besten alternativen Vermarktung indifferent zu sein.

Pfade, berichtigt am 08.09.2026.

```
main.tex                          Rahmen
chapters/chapter_1.tex bis chapters/chapter_6.tex
extras/attachment.tex             Anhang zum modifizierten Weber-Ansatz
literature/literature.bib         Literaturdatei
abbreviations.tex                 Abkuerzungsverzeichnis, Pfad pruefen
figures/                          Abbildungen, PDF aus SVG erzeugt
ENTSCHEIDUNGSPROTOKOLL.md         Nachweis aller Entscheidungen
CLAUDE.md                         diese Datei
WORKFLOW.md                       Vorgehen fuer das Ausformulieren
```

Build in dieser Reihenfolge, biber und nicht bibtex.

```
pdflatex main
biber main
pdflatex main
pdflatex main
```

Die gebaute `main.pdf` war am 08.09.2026 älter als `chapter_2.tex` und
`attachment.tex`. Vor jeder Durchsicht am gerenderten PDF neu bauen.

---

## 2 Rollenverteilung

Der Verfasser gibt den Inhalt vor und entscheidet. Du formulierst aus, aber nicht
frei, sondern nach Abschnitt 3.

**Ohne Rückfrage.** Belege prüfen, Rechnungen nachvollziehen, Widersprüche zwischen
Kapiteln melden, Terminologie und Einheiten kontrollieren, Lücken benennen, die
Prüfungen aus Abschnitt 5 fahren, Kommentare aktualisieren, den Protokolleintrag
nach Abschnitt 10 schreiben.

**Nur nach Auswahl durch den Verfasser.** Einen Satz in eine Kapiteldatei
schreiben.

**Nie.** Kommentare oder Prüfmarken stillschweigend löschen, eine getroffene
Vorentscheidung umkehren, eine Zahl setzen, die weder aus dem Material noch aus
einer nachvollziehbaren eigenen Rechnung stammt, eine Aussage mit einer Quelle
belegen, die sie nicht trägt, oder in das entfernte Repository schreiben. Du
lieferst Änderungen zur Übernahme, du pushst nicht.

---

## 3 Arbeitsweise, zwei Stufen

### 3.1 Stufe eins, die Form

Vor jedem Ausformulieren wird `chapters/chapter_3.tex` auf die Gliederung nach
Abschnitt 6 gebracht. Das umfasst Überschriften, Marken, Seitenziele, das
Verschieben der vorhandenen Stichpunktgerüste an ihre neue Stelle und das
Nachziehen der Kommentarblöcke. Kein Stichpunkt wird gelöscht, sondern nur
verschoben, und was entfällt, wird als Kommentar mit Datum und Grund vermerkt.

Danach läuft die Prüfsuite aus Abschnitt 5, und du berichtest das Ergebnis. Erst
wenn die Form steht, beginnt Stufe zwei.

### 3.2 Stufe zwei, Satz für Satz

Die Arbeitseinheit ist ein Satz. Ein Absatz entsteht Satz für Satz und nicht am
Stück. Für jeden Satz lieferst du in dieser Reihenfolge:

1. **Aufgabe des Satzes.** Ein Halbsatz, was er im Absatz leisten soll.
2. **Grundlage.** Woraus er folgt, also Beleg mit Zitatschlüssel, Mechanismus ohne
   Beleg, eigene Ableitung oder Setzung des Verfassers. Bei eigener Ableitung der
   ausdrückliche Vermerk, dass sie vom Verfasser zu prüfen ist.
3. **Drei Fassungen**, bezeichnet mit A, B und C.
4. **Ein Satz zum Unterschied**, also woran der Verfasser die Wahl festmacht.

Danach endest du und wartest. Du schreibst nichts in die Datei, bevor der Verfasser
gewählt hat.

**Die drei Fassungen unterscheiden sich in der Sache und nicht im Wortlaut.**
Brauchbare Achsen sind die Behauptungsstärke, also von der zurückhaltenden zur
vollen Aussage, der Umfang, also ob eine Nebenaussage mitgeführt wird, die
Reihenfolge, also welche Hälfte des Gedankens trägt, und der Anknüpfungspunkt, also
an welchen Vorsatz oder welche Quelle der Satz gebunden wird. Nicht brauchbar sind
Synonyme, umgestellte Nebensätze und dieselbe Aussage in drei Längen.

Fallen dir zu einem Satz keine drei Fassungen ein, die sich in der Sache
unterscheiden, sagst du das und lieferst eine oder zwei. Drei erfundene Varianten
sind schlechter als eine begründete.

**Nach der Wahl.** Der Verfasser wählt A, B oder C und ändert gegebenenfalls. Du
übernimmst die gewählte Fassung wörtlich, auch wenn du eine andere für besser
hältst. Hältst du sie für sachlich falsch oder für unbelegt, sagst du das einmal
und übernimmst sie danach trotzdem, mit einem Kommentar an der Stelle.

**Schreiben in die Datei.** Nicht nach jedem Satz, sondern nach jedem Absatz.
Solange ein Absatz läuft, führst du die gewählten Sätze im Gespräch mit. Ist er
fertig, schreibst du ihn als Ganzes in die Datei, ersetzt den zugehörigen
Stichpunkt und lässt die Kommentare stehen. Danach läuft die Prüfsuite.

**Vorschläge.** Du darfst vorschlagen, welcher Satz als nächster kommt, ob ein
Absatz zu Ende ist und wann ein Stichpunkt entfallen sollte. Entschieden wird das
vom Verfasser. Frage nicht mehr als einmal je Absatz nach.

**Länge.** Ein Satz je Fassung. Trägt eine Aussage einen unlösbaren Nebensatz, dann
zwei Sätze, und du sagst, weshalb sie nicht zu trennen sind.

---

## 4 Stilregeln

1. Beschreibung vor Bewertung.
2. Zurückhaltende Behauptungsstärke.
3. Klare Zuordnung der Akteure, kein Passiv bei bestimmtem Akteur.
4. Schlichtes Fachvokabular.
5. Begriffliche Konstanz, keine Synonyme für eingeführte Begriffe.
6. Wenige Absatzumbrüche, ein neuer Absatz nur bei echtem Themenwechsel.
7. Keine Doppelpunkte, Gedankenstriche oder Semikola im Fließtext.
8. Sparsame und gebündelte Zitate, eine Quelle je Absatz nur einmal.
9. Argumentative Sparsamkeit, keine strukturellen Vor- und Rückverweise.
   Sachverweise auf ein Modell oder eine Gleichung sind zulässig.
10. Nüchterner Ton ohne verstärkende Adjektive. Ausgeschlossen sind entscheidend,
    wesentlich, signifikant, deutlich und erheblich als bloße Verstärkung.

Listeneinleitungen kommen ohne Doppelpunkt aus, mit *nämlich* oder *folgende*. Kein
alleinstehendes `\\` als Absatztrenner.

---

## 5 Terminologie

**Gesperrt, nie im Fließtext.** Mindestvergütung, Vergütungsbereich, Untergrenze
der Vergütung, Erlösdifferenz, Schwellenpreis.

**Verbindlich.** Kurativer Reservierungspreis für die gesuchte Größe. Grenzpreis
und nicht Schwellenpreis. Kurative Systemführung als Oberbegriff für die kurative
Höherauslastung und den kurativen Redispatch. BESS und PSKW als Akronyme, keine
Pluralform mit `\acp`. IDA-1 für die Preisreihe der Strikepreise und nicht
Day-Ahead. Akteur für den Marktteilnehmer, Technologie für die Anlage, niemals
Aktor. Topologieschaltmaßnahmen einheitlich.

**Basispreis und Strikepreis, offen.** Der Ausdruck Basispreis steht elfmal in
Abschnitt 2.3.2, davon viermal in Tabellenzellen, während die Festlegung vom
Strikepreis spricht und der Anhang durchgehend Strikepreis führt. Bis zur
Entscheidung des Verfassers keine der beiden Stellen ändern und keinen der beiden
Ausdrücke in einem neuen Satz verwenden, ohne ihn zu benennen.

**Seitenbezeichnung, offen.** Vorgesehen sind Ausspeicherseite und
Einspeicherseite nach Anlage 1, im Text stehen Ausspeiseseite und Einspeiseseite.
Unabhängig von dieser Entscheidung sind die drei Stellen zu berichtigen, an denen
Einspeisung die Bezugsseite des Speichers meint, denn dasselbe Wort trägt an
anderen Stellen die Netzeinspeisung.

**Aktenzeichen, offen.** Text BK8-22-001-A nach dem Beschlussdeckblatt,
Literaturdatei und `extras/attachment.tex` noch BK8-22-0001-A aus der URL.

---

## 6 Prüfungen nach jeder Änderung

Führe sie aus und berichte das Ergebnis, bevor du eine geänderte Datei übergibst.
Behebe Befunde vor der Übergabe. Kommentarzeilen bleiben bei allen inhaltlichen
Prüfungen außer Betracht.

1. **Zeilenenden und Kodierung.** CRLF und UTF-8, beides unverändert.
2. **Stil im Fließtext.** Keine Doppelpunkte, keine Gedankenstriche, keine
   Semikola. Ausgenommen sind Kommentare, Listenpunkte, Tabellenzeilen und
   Bildunterschriften. Ein Prüfskript, das diese Ausnahme nicht kennt, berichtet zu
   viel, das ist kein Befund.
3. **Klammerbilanz und Dollarparität.**
4. **Umgebungen.** Jedes `\begin` hat sein `\end`.
5. **Doppelte Leerzeilen.**
6. **Gesperrte Begriffe** nach Abschnitt 5.
7. **Akronyme.** Batteriespeicher und Pumpspeicherkraftwerk kommen im Fließtext
   nicht ausgeschrieben vor. Jedes Akronym hat einen Eintrag in
   `abbreviations.tex`, und der verwendete Schlüssel ist der Eintragsschlüssel und
   nicht die Anzeigeform. `\ac{SO GL}` in `chapters/chapter_3.tex` ist ein Defekt
   und auf `\ac{SOGL}` zu ändern. Erstnennungen in Gleitumgebungen stehen als
   `\acs`.
8. **Marken.** Keine doppelt, jeder Verweis löst auf.
9. **Zitatschlüssel** gegen `literature/literature.bib`. Die letzte vollständige
   Prüfung deckte Kapitel 1, Kapitel 2 und den Anhang ab. Die Schlüssel von
   Kapitel 3 sind noch nicht abgeglichen, insbesondere `hull_options_2014`.
10. **Floats.** Jede `figure`- und `table`-Umgebung trägt eine Marke mit `fig:`
    beziehungsweise `tab:` und wird im Fließtext referenziert.

Was die Prüfungen nicht leisten und was du zusätzlich von Hand prüfst, ist die
inhaltliche Deckung der Belege, die Behauptungsstärke und die Frage, ob ein Absatz
ein Ergebnis vorwegnimmt, das erst ein späteres Kapitel trägt.

---

## 7 Gliederung von Kapitel 3, Stand 08.09.2026

| Nr | Überschrift | Seiten |
|---|---|---|
| 3.1 | Anforderungen an einen kurativen Marktmechanismus | 2,5 |
| 3.2 | Der kurative Reservierungspreis als offene Größe | 1,5 |
| 3.3 | Rahmen des kurativen Marktprodukts | 3,5 |
| 3.4 | Modellierungsansatz und Systemgrenzen | 2,5 |
| 3.5 | Mathematische Formulierung des Optimierungsproblems | 5 |
| 3.6 | Abgrenzung gegenüber dem modifizierten Weber-Ansatz | 1,5 |
| 3.7 | Validierung des Modells | 2,5 |

**3.1** trägt den Anforderungskatalog A1 bis A6 und den Forschungsbedarf. Der
Unterabschnitt zum Abgleich bestehender Marktdesignansätze steht zur Streichung,
siehe Abschnitt 9. Bis zur Entscheidung bleibt er unverändert stehen.

**3.2** nimmt den Absatz zur Bewertungsaufgabe auf, der am 04.09.2026 aus dem
Zwischenfazit 2.4 entfernt wurde, und zerlegt ihn in seine drei Bestandteile,
nämlich den entgangenen Deckungsbeitrag der besten alternativen Vermarktung, die
Pfadabhängigkeit des Ladezustands und die parallelen Erlösquellen. Jeder Bestandteil
erzeugt eine Anforderung an das Modell, und damit begründet 3.2 die Wahl in 3.4.
Der Wortlaut steht im Protokoll unter chapter_3.tex. Zwei Eingriffe sind dort
vermerkt, nämlich der Wegfall des Halbsatzes zum eigenen Kapitel und die Ersetzung
der Wendung Wert der aufgegebenen Vermarktungsoption, weil sie den Optionsbegriff
als eigene Grundlage einführte.

**3.3** stellt die Fragen des Produktentwurfs und beantwortet sie mit einem Rahmen,
nicht mit einer fertigen Ausgestaltung. Die Form jeder Rahmenantwort steht in
Abschnitt 8.

**3.4** trägt die Marktauswahl, die Einzelanlagenbetrachtung, die deterministische
Optimierung, die Auflösung von 96 Viertelstunden, den Szenariorahmen 2030 als
qualitative Einordnung und die nicht abgebildeten Größen.

**3.5** trägt Mengen, Parameter, Variablen, Zielfunktion und jede Nebenbedingung
einzeln, jeweils mit einem Satz zu ihrer Aufgabe.

**3.6** trägt die drei methodischen Gründe gegen eine Einbettung des Verfahrens in
das eigene Modell. Die inhaltlichen Gründe gegen die Anwendbarkeit auf ein BESS
stehen in Abschnitt 2.3.3 und werden hier nicht wiederholt.

**3.7** trägt die Validierung gegen den marktübergreifenden Erlösindex der ISEA
Battery Charts. Sie prüft den unrestringierten Fahrplan und nicht den
Reservierungspreis. Weil der unrestringierte Erlös eine Zwischengröße des Modells
und kein Ergebnis der Arbeit ist, darf dieser Abschnitt Zahlen tragen, obwohl das
Kapitel vor den Ergebnissen steht. Der Abschnitt sagt diese Begründung selbst.
Zugleich bindet die Validierung die Marktauswahl in 3.4, denn das Modell muss
dieselben Märkte führen wie der Index.

---

## 8 Form einer Rahmenantwort in 3.3

Jede Rahmenantwort trägt vier Teile in dieser Reihenfolge. Erstens die Setzung.
Zweitens die Begründung aus einer Anforderung A1 bis A6 oder aus einem Befund in
Kapitel 2. Drittens die Bandbreite, innerhalb derer eine spätere Ausgestaltung
abweichen kann. Viertens das Kriterium, an dem sich die Wahl innerhalb dieser
Bandbreite entscheidet.

Der vierte Teil ist der tragende. Eine Bandbreite ohne Kriterium ist keine Antwort.
Fehlt dir das Kriterium, sagst du das, statt eines zu erfinden.

Die Fragen zerfallen in vier Gruppen, und die Behandlung unterscheidet sich.

**A, Gegenstand der Verpflichtung.** Was beschafft wird, in welcher Richtung, ob
gesperrt oder gebunden, ob die Erfüllung binär ist. Diese vier bekommen eine
Entscheidung und keine Bandbreite, weil alles Weitere auf ihnen aufsetzt.
Festgelegt ist, dass die Anlage nicht gesperrt, sondern in Leistung und
Ladezustandsband gebunden wird und weiterhandeln darf. Das ist der Unterschied zu
Anlage 5 der Festlegung und der Grund, weshalb der ermittelte Preis unter dem
dortigen Ausgleich liegen kann.

**B, Parameter, die das Modell als Eingang braucht.** Vorgehaltene Leistung,
gebundenes Ladezustandsband, Bindungsdauer, Reaktionszeit und Vergütungsform. Diese
fünf bekommen den vollen Vierschritt und laufen in eine Tabelle mit den Spalten
Größe, Basisfall und in Kapitel 5 zu prüfen. Jede Zeile erhält in 3.5 ein Symbol.
Sobald eine Zahl gesetzt ist, hängt jedes Ergebnis in Kapitel 4 an ihr, und das ist
einmal offen zu sagen.

**C, Fragen, die erst die Ergebnisse beantworten.** Welche Bindungsdauer, welche
Leistung und welche Reaktionszeitklasse vertretbar sind und ab welchem Punkt die
kurative Vorhaltung die Regelleistung statt nur die Arbitrage verdrängt. Diese vier
stehen in 3.3 als Fragen und werden dort nicht beantwortet. Sie sind die Brücke
nach Kapitel 5.

**D, Beschaffung und Durchsetzung.** Beschaffungszeitpunkt, Ausschreibender und
Turnus, Zuschlagsverfahren, räumliche Auflösung, Präqualifikation, Pönale und das
Verhältnis zum Redispatch. Diese bekommen den Rahmen ohne Zahl. Bei zwei Fragen
sagt der Text ausdrücklich, dass die Arbeit sie nicht entscheidet, nämlich bei der
Pönalehöhe, weil das Modell sie nicht trägt, und beim Konflikt zwischen
knotenscharfer Beschaffung nach A2 und Diskriminierungsfreiheit nach A4, weil er
die netzweite Beschaffungsmenge voraussetzt, die außerhalb der Systemgrenzen liegt.

Zwei Vorlagen aus Kapitel 2 sind unmittelbar verwendbar. Die aFRR zeigt, dass sich
die Gebotspflicht auf die bezuschlagte Leistung beschränken lässt, ohne den Zugang
zum Abruf zu verengen. Und § 13k zeigt eine Bindung im Voraus mit Sanktion,
allerdings mit umgekehrter Zahlungsrichtung und mit einer Menge statt einer
Fähigkeit als Gegenstand.

---

## 9 Entscheidungen und offene Punkte

### Getroffen, nicht umkehren

1. Der modifizierte Weber-Ansatz ist kein Bestandteil des Optimierungsmodells und
   bleibt Referenz für die Kritik in 3.6.
2. **Die kurative Bindung ist exogen.** Sie steht als Flag im Modell und nicht als
   Entscheidungsvariable. Der Reservierungspreis ist die Differenz der
   Zielfunktionswerte zweier Läufe, einmal mit gesetztem und einmal mit gelöschtem
   Flag, für das vierte Quartal 2025 also 92 Tagespaare. Entschieden am 08.09.2026.
3. **Einheit.** Aus 2 folgt der Wert je Leistung und Zeit, also Euro je Megawatt
   und Stunde, nämlich die Differenz geteilt durch das Produkt aus gebundener
   Leistung und Bindungsdauer. Die Aggregation auf Tages- oder Quartalsbeträge ist
   eine Darstellungsfrage. Der frühere offene Punkt zur Einheit ist damit erledigt.
4. **Abrufwahrscheinlichkeit.** Nicht modelliert. Sie steht wieder unter den nicht
   abgebildeten Größen in 3.4, und die Sensitivität der Abrufhäufigkeit in
   Abschnitt 4.4 entfällt. Folgt aus 2, weil ohne Vergütung im Modell nichts
   dagegen zu verrechnen ist.
5. **Pönale.** Nicht modelliert. Abschnitt 3.3 sagt das offen und begründet es
   damit, dass die Pönale eine Risikoprämie erzeugt, die neben den
   Opportunitätskosten steht. Der ermittelte Preis ist der
   opportunitätskostenbasierte Teil des Gebots und nicht das Gebot. Die
   Sensitivität der Pönalehöhe in 4.4 entfällt.
6. **Vergütungsniveau** ist keine Sensitivität, sondern die gesuchte Größe. Von der
   Liste in 4.4 bleiben die Produkt- und die Anlagenparameter.
7. Netzentgelte liegen außerhalb des Untersuchungsrahmens, Speicher sind nach
   § 118 Abs. 6 EnWG befreit.
8. Die Teilnahme am Redispatch ist keine Erlösquelle, die Vergütung folgt dem
   Indifferenzprinzip.
9. Für den kurativen Reservierungspreis wird keine Obergrenze angegeben, auch nicht
   verneinend.
10. Das Jahr 2030 ist ein qualitativer Rahmen, gerechnet wird mit historischen
    Preiszeitreihen. Das vierte Quartal 2025 ist der gültige Auswertungszeitraum,
    weil die Umstellung des Day-Ahead-Produktschnitts am 01.10.2025 einen
    Regimebruch darstellt.
11. Die Vergütungsstruktur der Festlegung lautet nach Anlage 1 Seite 14
    Erzeugungsauslagen zuzüglich des Maximums aus anteiligem Werteverbrauch und
    Opportunität.

### Offen, nicht stellvertretend entscheiden

1. **Lineares oder gemischt-ganzzahliges Problem.** Nach Entscheidung 2 ist die
   kurative Bindung ein Parameter. Ob das Modell ganzzahlig bleibt, hängt jetzt
   allein daran, ob eine Binärvariable gleichzeitiges Laden und Entladen
   ausschließt. Davon hängen der Zuschnitt der Methodendarstellung in 3.5, die
   Nennung von Gurobi und die Begründung für den Verzicht auf Dualvariablen ab.
2. **Dualvariablen.** Ihre Entfernung war damit begründet, dass ein
   gemischt-ganzzahliges Problem sie nicht liefert. Diese Begründung hängt jetzt am
   offenen Punkt 1. Bei einem linearen Programm steht der Schattenpreis der
   Vorhalterestriktion zur Verfügung, also der Grenzwert der Bindung in Euro je
   Megawatt, während die Differenz der Zielfunktionswerte den Gesamtwert liefert.
   Melde das, entscheide es nicht.
3. **Unzulässige Läufe.** Der gebundene Lauf kann unzulässig werden, wenn die
   kurative Bindung zusammen mit den zugesagten Regelleistungsbändern die Anlage
   überzeichnet. Zu entscheiden ist, ob eine Schlupfvariable mit Strafkosten
   eingeführt wird. Diese Fälle sind kein Rechenfehler, sondern das Ergebnis, dass
   ein BESS diese Kombination von Produktparametern nicht anbieten kann, und damit
   die Grenze, an der A6 kippt.
4. **Abgleich bestehender Marktdesignansätze in 3.1.** Vier der sechs Zeilen sind
   in Kapitel 2 bereits abgehandelt, und die 36 eigenen Bewertungen wären je
   einzeln zu begründen. Vorgeschlagen ist die Streichung, wobei zwei Sätze in
   3.1.3 die beiden nächstliegenden Alternativen benennen, nämlich den
   kapazitätsbasierten Redispatch und den Netzbooster, und der vollständige
   Abgleich samt Matrix nach Kapitel 5 wandert, wo er zugleich den Einwand der
   adversen Selektion trägt.
5. **Formelzeichen.** Der Anhang führt g_T und g_P für die Grenzpreise, X für den
   Strikepreis und d_T und d_P, die Symboltabelle in 2.3.2 führt X_C und X_P sowie
   d_C und d_P. Der Anhang trennt Seite und Optionsart, 2.3.2 vermengt beides. Die
   Entscheidung bindet auch die Symbolliste in 3.5.
6. Seitenbezeichnung, Basispreis und Aktenzeichen nach Abschnitt 5.
7. **Protokoll.** Die Einträge der Quellenprüfung vom 07.09.2026 fehlen in der
   eingecheckten Fassung von `ENTSCHEIDUNGSPROTOKOLL.md`. Sie stehen dort als
   offener Punkt 1.
8. **Literaturdatei.** Der Eintrag für die ISEA Battery Charts fehlt, obwohl 3.7
   den Vergleichsmaßstab darauf stützt.

---

## 10 Zahlen, Einheiten und Formelzeichen

**Einheiten.** Preise in Euro je Megawattstunde, Werte je Leistung in Euro je
Megawatt, Werte je Leistung und Zeit in Euro je Megawatt und Stunde. Die letzte
Form ist nicht Euro je Megawattstunde. Jede Größe trägt ihre Einheit einzeln, auch
als zweites Glied einer Aufzählung und in Gleichungsblöcken. Tabellen tragen die
Einheit im Spaltenkopf oder in der Zeilenbezeichnung.

**Rundung.** Zwischenwerte werden ungerundet weitergerechnet und nur in der
Darstellung gerundet. Gedruckte Zahlengleichungen tragen so viele Stellen, dass
sich das ausgewiesene Ergebnis reproduzieren lässt. Im Berechnungsbeispiel von
2.3.2 ist das derzeit nicht der Fall, siehe den Protokolleintrag vom 08.09.2026.

**Belegte Formelzeichen.** g_T, g_P, X, d_T, d_P, V_C und V_P sind durch die
Darstellung des Weber-Ansatzes belegt. Im Speichermodell sind damit V, X und d
gesperrt, ebenso g für eine andere Größe als einen Grenzpreis. Prüfe jede neue
Symbolliste gegen `tab:weber_symbole` und gegen den Anhang.

---

## 11 Pflege des Entscheidungsprotokolls

`ENTSCHEIDUNGSPROTOKOLL.md` ist der Nachweis, warum eine Formulierung so und nicht
anders steht. Aufbau seit dem 08.09.2026, nämlich Aufbau der Datei, übergreifende
Entscheidungen, je ein Abschnitt für `chapter_1.tex` bis `chapter_3.tex`, dann
`attachment.tex`, `literature.bib`, die offenen Punkte und zuletzt die beiden
Anhänge mit dem Kommentarbestand vom 28.08.2026.

- Ein Eintrag je Sitzung und Datei, überschrieben mit Datum und kurzer Sache, ans
  Ende des jeweiligen Dateiabschnitts.
- Eine Änderung, die mehrere Dateien betrifft, steht unter den übergreifenden
  Entscheidungen und nicht mehrfach.
- Jede zurückgenommene Formulierung wird im Wortlaut festgehalten, mit dem Vermerk,
  dass sie nicht wieder aufzunehmen ist.
- Jedes Argument, das nicht vom Verfasser stammt, wird als eigenständiges Argument
  gekennzeichnet.
- Jede unbelegte Aussage wird als offener Punkt geführt, mit dem Hinweis, welche
  Quelle in Betracht kommt.
- Der Wortlaut früherer Einträge wird nicht geändert. Ein überholter Befund erhält
  einen neuen Eintrag.

Beim satzweisen Arbeiten wird nicht jeder Satz protokolliert. Protokolliert werden
je Absatz die getroffenen Entscheidungen, die verworfenen Fassungen, soweit sie
eine Aussage enthielten, die nicht wieder auftauchen soll, und jede eigenständige
Ableitung.

---

## 12 Dateihandhabung

- Ersetzungen über Python mit `open(pfad, encoding='utf-8', newline='')` und nicht
  über sed.
- Prüfe nach jeder Ersetzung, dass sie genau so oft gegriffen hat wie erwartet.
  Eine Ersetzung, die null- oder zweimal greift, ist ein Fehler und kein Zufall.
- Gib immer die vollständige Datei zurück, nie ein Fragment, es sei denn, der
  Verfasser verlangt ausdrücklich einen Ausschnitt.
- Zu jedem Zeitpunkt arbeitet nur eine Seite an einer Datei.

Das Vorgehen für das gemeinsame Ausformulieren steht in `WORKFLOW.md`.
