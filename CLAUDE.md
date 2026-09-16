# Auftrag an Claude Code

Diese Datei liegt im Wurzelverzeichnis des Repositorys der Schriftfassung und ist
zu Beginn jeder Sitzung zu lesen. Sie bindet dich für alle Arbeiten an diesem
Repository.

Stand 14.09.2026. Sie ersetzt die Fassung vom 08.09.2026 vollständig. Anlass
sind die Kommentare des Betreuers zur PDF-Fassung, aus denen die Stilregeln in
Abschnitt 4 abgeleitet sind, und der Wechsel der Arbeitseinheit vom Satz auf
den Absatz, der in `WORKFLOW.md` geregelt ist. Die alte Fassung steht in der
Git-Historie unter 38739f0.

---

## 1 Gegenstand

Masterarbeit am IAEW der RWTH Aachen mit dem Titel *Ausgestaltung eines
Marktmechanismus für kurative Systemführung zur Engpassbehebung*. Abgabe am
15.10.2026, Kolloquium am 12.10.2026. Deutschsprachig, LaTeX mit KOMA-Script und
biblatex.

Die Arbeit entwirft die kurative Reservierung als Produkt und bestimmt den
kurativen Reservierungspreis, also den Betrag, den ein BESS für die Reservierung
mindestens fordern muss, um mit ihr genauso viel zu verdienen wie ohne sie.

```
main.tex                          Rahmen, Kapitel 4 bis 6 auskommentiert
chapters/chapter_1.tex bis chapters/chapter_6.tex
extras/attachment.tex             Anhang A, modifizierter Weber-Ansatz
extras/attachment_thermik.tex     Anhang B, zulaessige Ueberlastdauer, seit 15.09.2026
extras/attachment_modell.tex      Anhang C, vollstaendiges Optimierungsproblem
extras/attachment_validierung.tex Anhang D, Validierung je Markt
extras/abbreviations.tex          Abkuerzungsverzeichnis
literature/literature.bib         Literaturdatei
literature/PDFs, literature/txt   Volltexte, nicht versioniert
figures/                          Abbildungen, PDF
tools/pruefen.py                  Pruefsuite
tools/quellencheck.py             Volltextsuche in den Quellen
ENTSCHEIDUNGSPROTOKOLL.md         Nachweis aller Entscheidungen, nur anhaengen, nie ganz lesen
WORKFLOW.md                       Vorgehen fuer Korrektur, Neufassung und Kommentardurchgang
DURCHSICHT_KAP1_3.md              Offene Vorschlaege der Durchsicht vom 15.09.2026, Liste F
KOMMENTARE_KAP3.md                Kommentardatei, nicht genutzt, der Verfasser kommentiert im Chat
analysen/                         Eigene Auswertungen mit Daten und Skripten als Belege
archiv/                           Umgesetzte Arbeitsdokumente, nur zum Nachschlagen:
                                  AENDERUNGEN_KAP1_2.md, AENDERUNGEN_KAP3.md,
                                  KUERZUNGEN_KAP1_2.md, STRUKTUR.md, ANWEISUNG_KOMMENTARE.md
```

Am 16.09.2026 aufgeraeumt. Die vier Arbeitsdokumente in `archiv/` sind
vollstaendig umgesetzt, ihre Entscheidungen stehen im Protokoll. Verweise
auf sie in dieser Datei und in `WORKFLOW.md` gelten als Verweise auf das
Archiv. Aktiv sind allein `DURCHSICHT_KAP1_3.md` und `KOMMENTARE_KAP3.md`.

Build in dieser Reihenfolge, biber und nicht bibtex. Vor jeder Durchsicht am
PDF neu bauen.

```
pdflatex main
biber main
pdflatex main
pdflatex main
```

---

## 2 Rollen

Der Verfasser gibt den Inhalt vor und entscheidet. Du schreibst nach dem
Absatzplan, den der Verfasser freigegeben hat, und nicht frei.

**Ohne Rückfrage.** Belege prüfen, Rechnungen nachvollziehen, Widersprüche zwischen
Kapiteln melden, Terminologie und Einheiten kontrollieren, Lücken benennen, die
Prüfungen aus Abschnitt 6 fahren, Kommentare aktualisieren, den Protokolleintrag
nach Abschnitt 9 schreiben, Absatzpläne vorlegen.

**Nur nach Freigabe des Absatzplans.** Einen Absatz in eine Kapiteldatei
schreiben.

**Nie.** Kommentare oder Prüfmarken stillschweigend löschen, eine getroffene
Entscheidung umkehren, eine Zahl setzen, die weder aus dem Material noch aus
einer nachvollziehbaren eigenen Rechnung stammt, eine Aussage mit einer Quelle
belegen, die sie nicht trägt, in das entfernte Repository schreiben. Du
lieferst Änderungen zur Übernahme, du pushst nicht.

---

## 3 Arbeitsweise

Die Arbeitseinheit ist der Absatz. Ein Absatz trägt eine Kernaussage und
entsteht als Ganzes aus einem Absatzplan, der vor dem ersten Satz feststeht.
Das satzweise Vorgehen mit drei Fassungen je Satz ist seit dem 14.09.2026
abgelöst, weil es den Zusammenhang zwischen den Sätzen verloren hat. Der Ablauf
steht in `WORKFLOW.md`, dort auch der Absatzplan, die Fremdleser-Prüfung und
die Zettel, die du mit jedem Absatz lieferst.

Die Korrektur der Kapitel 1 bis 3 nach den Änderungslisten ist am 15.09.2026
abgeschlossen, die Listen liegen in `archiv/`. Seit dem 16.09.2026 gilt der
Kommentardurchgang nach `WORKFLOW.md` Abschnitt 7: Der Verfasser kommentiert
den Text in `KOMMENTARE_KAP3.md`, Claude arbeitet die Kommentare ein, und
die Kommentare haben Vorrang vor den offenen Vorschlägen in
`DURCHSICHT_KAP1_3.md`. Die Anweisung für die Sitzung, in der der Verfasser
seine Kommentare diktiert, steht in `ANWEISUNG_KOMMENTARE.md`.

**Subagenten nur nach Rückfrage.** Prüfagenten wie die Fremdleser-Prüfung
sind erwünscht, kosten aber Tokens, die der Verfasser steuern will. Vor jedem
Start eines Subagenten fragst du, ob er laufen soll, und nennst Zweck und
Zahl der Agenten. Vorgabe des Verfassers vom 16.09.2026.

---

## 4 Stilregeln

Die Regeln 1 bis 10 sind aus den 106 Kommentaren des Betreuers abgeleitet, die
Regeln 11 bis 16 sind aus der Fassung vom 08.09.2026 übernommen. Zwei alte
Regeln sind aufgehoben, nämlich das Verbot des Doppelpunkts und die Vorgabe
weniger Absatzumbrüche.

1. **Ein Absatz, eine Kernaussage.** Der Absatz beginnt mit seiner These und
   endet mit der Konsequenz. Vier bis acht Sätze. Ein Umbruch bei jedem
   Teilgedanken und nicht erst beim Themenwechsel.
2. **These und Begründung verbinden.** Die Begründung hängt mit *denn*, *weil*,
   *sodass*, *damit* oder mit einem Doppelpunkt an der These. Kein
   Behauptungssatz, dem unverbunden Erläuterungssätze folgen.
3. **Übergänge.** Der erste Satz eines Absatzes knüpft erkennbar an den vorigen
   Absatz an. Ein Themenwechsel, etwa von den Grundlagen zur Simulation,
   bekommt einen eigenen Überleitungssatz.
4. **Aussagen zu Ende führen.** Nach Befund und Erklärung steht, was daraus für
   Maßnahme, Mechanismus oder Netzbetrieb folgt.
5. **Bezüge ausschreiben.** Keine Pronominalisierung über die Satzgrenze.
   Pronomen und Demonstrativa wie *sie*, *er*, *es*, *diese*, *dieser*,
   *dafür* stehen nur, wenn der Bezug im selben Satz steht, sonst wird das
   Nomen wiederholt. Unbestimmte Nominalphrasen wie *der Bedarf*, *das Netz*,
   *der Mechanismus* tragen ihr Attribut. Die Wendungen *die vorliegende
   Arbeit* und *diese Arbeit* stehen nur in Abschnitt 1.2 und in den
   Kapiteleinleitungen, sonst nirgends. Vorgabe des Verfassers vom 15.09.2026.
6. **Begriffe vor der ersten Verwendung definieren**, einmal, und danach
   unverändert verwenden. Die Liste steht in Abschnitt 5.
7. **Relative Angaben beziffern.** *Groß*, *klein*, *eng*, *spät*, *schnell*
   stehen nur mit Bezugsgröße, Zahl oder Vergleichsmaßstab.
8. **Belegen oder abschwächen.** Absolute Feststellungen tragen eine Quelle.
   Ohne Quelle wird zurückhaltend formuliert. Zahlen aus Pilotprojekten und
   Studien tragen ihre Randbedingungen.
9. **Keine fachlichen Pauschalisierungen.** Grenzwertkonzept, N-1-Kriterium,
   Vorbelastung und Witterung, Quelle und Senke werden differenziert
   dargestellt. Das deutsche Übertragungsnetz wird heute N-1-sicher betrieben,
   kein Satz darf das Gegenteil nahelegen.
10. **Handelnde Akteure als Subjekt.** Kapitel und Abschnitte handeln nicht.
    Verweise lauten *wie in Abschnitt X beschrieben* oder *in Abschnitt X wird
    X dargestellt*. Betrachtungsrahmen ausgesprochen, nämlich Deutschland gegen
    Europa, heutiger Stand gegen Planung, Zieljahr und Auswertungszeitraum.
11. Beschreibung vor Bewertung, zurückhaltende Behauptungsstärke.
12. Klare Zuordnung der Akteure, kein Passiv bei bestimmtem Akteur.
13. Schlichtes Fachvokabular. Wirtschaftlicher Jargon wie *Bindung*,
    *indifferent*, *Opportunitätskosten* wird beim ersten Auftreten erklärt.
    Prüfmaßstab ist ein fachfremder Leser.
14. Begriffliche Konstanz, keine Synonyme für eingeführte Begriffe.
15. Nüchterner Ton. Ausgeschlossen sind *entscheidend*, *wesentlich*,
    *signifikant*, *deutlich*, *erheblich* als bloße Verstärkung. Zitate
    gebündelt, eine Quelle je Absatz nur einmal. Keine strukturellen Vor- und
    Rückverweise, Sachverweise auf Modell, Gleichung, Abbildung und Tabelle sind
    zulässig.
16. **Zeichensetzung.** Doppelpunkt zulässig, sparsam und nur für These mit
    folgender Erklärung. Gedankenstriche und Semikola nicht. Listeneinleitungen
    mit *nämlich* oder *folgende*. Kein alleinstehendes `\\`. Tabellen und
    Abbildungen stehen unmittelbar bei der Stelle, die auf sie verweist.
17. **Satzlänge.** Ein Satz besteht aus einem Hauptsatz und höchstens einem
    Nebensatz. Zwei Hauptsätze sind die Ausnahme und tragen dann keinen
    Nebensatz mehr. Aufzählungen mit *nämlich* zählen nicht als Nebensatz.
    Vorgabe des Verfassers vom 15.09.2026, gilt für alle neu geschriebenen
    Absätze und rückwirkend für Kapitel 1 bis 3.

---

## 5 Begriffe

**Gesperrt, nie im Fließtext.** Mindestvergütung, Vergütungsbereich, Untergrenze
der Vergütung, Erlösdifferenz, Schwellenpreis, Aktor, Reichweite.

**Verbindlich.** *Kurativer Reservierungspreis* für die gesuchte Größe.
*Kurative Reservierung* für das Produkt, seit dem 11.09.2026. *Kurative Bindung* für die
Reservierung eines Leistungsbandes und, bei Speichern, eines Ladezustandsbandes,
definiert in 2.1.2, entschieden am 16.09.2026. *Bindung* ohne Adjektiv nur im
allgemeinen Sinn. *Referenzfahrplan* und *Referenzerlös* für den Fahrplan und den
Erlös ohne kurative Bindung, Lauf mit Preis null, statt *ungebundener
Fahrplan*, entschieden am 16.09.2026. *Kurativer
Marktmechanismus* für das Verfahren, mit dem der ÜNB die Vorhaltung marktlich
beschafft, einmal in 1.2 erklärt, danach immer mit dem Adjektiv und nie *der
Mechanismus* allein. Der Mechanismus dient der Erkenntnis über Einflüsse auf den
Preis und ist kein Marktdesign mit prognostizierten Preisen, Vorgabe des
Verfassers vom 15.09.2026. *Grenzpreis* und
nicht Schwellenpreis. *Kurative Systemführung* als Oberbegriff für die kurative
Höherauslastung und den kurativen Redispatch. *BESS* und *PSKW* als Akronyme,
keine Pluralform mit `\acp`. *IDA-1* für die Preisreihe der Strikepreise.
*Akteur* für den Marktteilnehmer, *Technologie* für die Anlage.
*Topologieschaltmaßnahmen* einheitlich. *Der PATL* und *der TATL*, maskulin, nach
InnoSys 2030 und dem Grenzwertkonzept, entschieden am 15.09.2026. *Energieinhalt je Leistung* in Stunden für das Verhältnis von
Speicherkapazität zu Nennleistung, nicht C-Wert oder C-Rate, denn die C-Rate ist der
Kehrwert. Definiert in 2.1.3, Wertebereiche in Tabelle 2.1 aus einer eigenen
Auswertung des Marktstammdatenregisters vom 15.09.2026 in
`analysen/mastr_speicher`, Eintrag `bundesnetzagentur_mastr_2026`. PSKW 3 bis
9 Stunden, BESS 1 bis 2 Stunden mit steigender Tendenz.

**Vor der ersten Verwendung zu definieren.** Die Spalte Ort nennt die Stelle,
an der die Definition nach `AENDERUNGEN_KAP1_2.md` stehen soll. Bis sie dort
steht, gilt der Begriff als undefiniert.

| Begriff | Ort |
|---|---|
| Redispatch, Kurzform | 1.1 Absatz 2 |
| Kurative Vorhaltung, kurativer Marktmechanismus, kurative Reservierung | 1.2 Absatz 1 |
| Bindung, Bindungsdauer, Reaktionszeit, kurativer Reservierungspreis | 1.2 Absatz 2 |
| Engpassmanagement, Redispatch, Ausfallvariante, Ausfallvariantenliste, Befund, Engpass | Einleitung 2.1 |
| N-1-Kriterium, präventive und kurative Systemführung | Einleitung 2.1 |
| PATL, TATL, zulässige Überlastdauer | 2.1.1 Absatz 1 |
| Planungshorizont, Ersatz für Reichweite | 2.1.1 Absatz 3 |
| Kurative Höherauslastung, kurativer Redispatch | 2.1.1 Absatz 5 |
| Kurativer Akteur | 2.1.2 Absatz 1 |
| Einplanung, Scharfschaltung, Auslösung, Abruf, Umsetzung, Reaktionszeit, Bindungsdauer | 2.1.2 Absatz 2, seit 16.09.2026 nach InnoSys 2030 |
| Quelle und Senke | 2.1.2 Absatz 3 |
| Bemessungsgrundlage | 2.1.3 Absatz 1 |
| Arbitrage | 2.3.5 Absatz 1, seit 16.09.2026 |

**Handlung des Akteurs.** Der Akteur *setzt* die Leistungsänderung *um*, das
Leitsystem des ÜNB *löst* die Maßnahme *aus*. *Aktivieren* und *Aktivierung*
stehen nur in Zitaten aus SOGL und InnoSys. Entschieden am 14.09.2026, V4.

**Offen, nicht stellvertretend entscheiden.** Basispreis gegen Strikepreis,
Aktenzeichen BK8-22-001-A gegen BK8-22-0001-A in der Literaturdatei. Bis zur
Entscheidung keine der Stellen ändern und keinen der Ausdrücke in einem neuen
Satz verwenden, ohne ihn zu benennen. Der Stand von V1 bis V13 steht in
`AENDERUNGEN_KAP1_2.md` Abschnitt 0.

---

## 6 Prüfungen nach jeder Änderung

`tools/pruefen.py` führt die Prüfungen 1 bis 10 aus. Führe es aus und berichte
das Ergebnis, bevor du eine geänderte Datei übergibst. Behebe Befunde vor der
Übergabe. Kommentarzeilen bleiben bei allen inhaltlichen Prüfungen außer
Betracht.

```
python tools/pruefen.py chapter_1.tex chapter_2.tex
python tools/pruefen.py --alle
```

1. Zeilenenden und Kodierung, beides unverändert. Die Kapiteldateien liegen
   im Arbeitsverzeichnis mit CRLF, die Markdown- und Python-Dateien mit LF,
   `.gitattributes` normiert alles auf LF im Repository. Eine Datei wird mit
   den Zeilenenden zurückgegeben, mit denen sie gelesen wurde.
2. Stil im Fließtext. Keine Gedankenstriche, keine Semikola. Der Doppelpunkt
   wird seit dem 14.09.2026 nicht mehr gemeldet. Ausgenommen sind Kommentare,
   Listenpunkte, Tabellenzeilen und Bildunterschriften.
3. Klammerbilanz und Dollarparität.
4. Umgebungen, jedes `\begin` hat sein `\end`.
5. Doppelte Leerzeilen.
6. Gesperrte Begriffe nach Abschnitt 5.
7. Akronyme. Batteriespeicher und Pumpspeicherkraftwerk kommen im Fließtext
   nicht ausgeschrieben vor. Jedes Akronym hat einen Eintrag in
   `extras/abbreviations.tex`, der Schlüssel ist der Eintragsschlüssel.
   Erstnennungen in Gleitumgebungen stehen als `\acs`.
8. Marken, keine doppelt, jeder Verweis löst auf.
9. Zitatschlüssel gegen `literature/literature.bib`.
10. Floats. Jede `figure`- und `table`-Umgebung trägt eine Marke mit `fig:`
    beziehungsweise `tab:` und wird im Fließtext referenziert.

Von Hand und je Absatz prüfst du zusätzlich die inhaltliche Deckung der
Belege, die Behauptungsstärke, die Frage, ob der Absatz ein Ergebnis
vorwegnimmt, das erst ein späteres Kapitel trägt, und die Stilregeln 1 bis 10.
Die Fremdleser-Prüfung nach `WORKFLOW.md` Abschnitt 4 läuft je Abschnitt.

---

## 7 Entscheidungen

Wortlaut und Begründung stehen im Protokoll, die Gliederung von Kapitel 3 in
`STRUKTUR.md`. Hier steht nur, was beim Schreiben bindet.

### Getroffen, nicht umkehren

1. Der modifizierte Weber-Ansatz ist kein Bestandteil des Optimierungsmodells
   und bleibt Referenz für die Abgrenzung in 3.2.4.
2. **Der kurative Reservierungspreis ist endogen** wie im Code, Entscheidung K1
   vom 11.09.2026. Gemeint ist der Preis, bei dem ein Akteur eine Stunde voll
   reserviert. Die frühere Entscheidung zur exogenen Bindung mit zwei Läufen je
   Tag ist damit überholt.
3. **Basisfall.** Lineares Programm mit stetiger Reservierung, beide
   Richtungen, Reaktionszeitklasse etwa zwei Minuten, Zeitscheibe eine Stunde,
   eine Megawattstunde je Megawatt, Abrufdauer eine Stunde. Die Stunden wählt
   das Modell. Die Mindestgröße von 25 MW macht das Modell gemischt-ganzzahlig
   und ist eine Sensitivität, wie im Code mit USE_KUR_BINAER = False.
   Berichtigt am 15.09.2026, W1. Die Reaktionszeitklassen folgen InnoSys 2030,
   nämlich unter zehn Sekunden, etwa zwei Minuten und bis 15 Minuten,
   entschieden am 15.09.2026, W3.
4. **Auswertungszeitraum ist das ganze Jahr 2025.** Das Jahr 2030 ist ein
   qualitativer Rahmen, gerechnet wird mit beobachteten Preisen.
5. **Nicht modelliert** sind die Abrufwahrscheinlichkeit und die Pönale. Beide
   stehen unter den nicht abgebildeten Größen. Der ermittelte Preis ist der
   opportunitätskostenbasierte Teil des Gebots und nicht das Gebot.
6. Das Vergütungsniveau ist keine Sensitivität, sondern die gesuchte Größe.
7. Netzentgelte liegen außerhalb des Untersuchungsrahmens, Speicher sind nach
   § 118 Abs. 6 EnWG befreit.
8. Die Teilnahme am Redispatch ist keine Erlösquelle, die Vergütung folgt dem
   Indifferenzprinzip.
9. Für den kurativen Reservierungspreis wird keine Obergrenze angegeben, auch
   nicht verneinend.
10. Die Vergütungsstruktur der Festlegung lautet nach Anlage 1 Seite 14
    Erzeugungsauslagen zuzüglich des Maximums aus anteiligem Werteverbrauch und
    Opportunität.
11. Das vollständige Optimierungsproblem steht in Anhang C, seit dem neuen
    Anhang B vom 15.09.2026 nicht mehr in Anhang B. Kapitel 3 verweist auf
    die Gleichungen, statt sie zu wiederholen. Entschieden am 13.09.2026.
12. Der Vierschritt für Rahmenantworten gilt nicht durchgängig. Gesetzt wird
    allein, was für die Optimierung von Belang ist, der Ausdruck Bandbreite
    kommt im Text nicht vor. Entschieden am 14.09.2026.
13. Die Nachlaufpflicht wird nur benannt und nicht modelliert. Entschieden am
    14.09.2026.
14. **Ein Abruf wird gesondert vergütet**, nämlich die gelieferte Energie und
    die Nachlaufpflicht je Megawatt. Der kurative Reservierungspreis vergütet
    allein die Vorhaltung. Die Preise der Abrufvergütung werden nicht
    festgelegt, der Text sagt nur, dass sie eigens zu betrachten sind.
    Entschieden am 16.09.2026, ersetzt die Aussage, der Preis decke die
    Energie eines Abrufs mit ab.

### Offen, nicht stellvertretend entscheiden

Die offenen Punkte stehen im Protokoll unter *Offene Punkte* und in
`AENDERUNGEN_KAP1_2.md` Abschnitt 0 als V1 bis V13. Dazu gehören die Einheit
des Reservierungspreises, die Dualvariablen, die Behandlung unzulässiger Läufe,
der Eintrag für die ISEA Battery Charts und die Kürzungen A1 bis A7.

---

## 8 Zahlen, Einheiten und Formelzeichen

**Einheiten.** Preise in Euro je Megawattstunde, Werte je Leistung in Euro je
Megawatt, Werte je Leistung und Zeit in Euro je Megawatt und Stunde. Die letzte
Form ist nicht Euro je Megawattstunde. Jede Größe trägt ihre Einheit einzeln,
auch als zweites Glied einer Aufzählung und in Gleichungsblöcken. Tabellen
tragen die Einheit im Spaltenkopf oder in der Zeilenbezeichnung.

**Rundung.** Zwischenwerte werden ungerundet weitergerechnet und nur in der
Darstellung gerundet. Gedruckte Zahlengleichungen tragen so viele Stellen, dass
sich das ausgewiesene Ergebnis reproduzieren lässt.

**Belegte Formelzeichen.** g_T, g_P, X, d_T, d_P, V_C und V_P sind durch die
Darstellung des Weber-Ansatzes belegt. Im Speichermodell sind damit V, X und d
gesperrt, ebenso g für eine andere Größe als einen Grenzpreis. Prüfe jede neue
Symbolliste gegen `tab:weber_symbole` und gegen Anhang A und C.

---

## 9 Pflege des Entscheidungsprotokolls

`ENTSCHEIDUNGSPROTOKOLL.md` ist der Nachweis, warum eine Formulierung so und nicht
anders steht. Aufbau, nämlich Aufbau der Datei, übergreifende Entscheidungen,
je ein Abschnitt für `chapter_1.tex` bis `chapter_3.tex`, dann die Anhänge,
`literature.bib`, die offenen Punkte und zuletzt die beiden Anhänge mit dem
Kommentarbestand vom 28.08.2026.

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

Protokolliert wird je Abschnitt, nicht je Absatz. Der Eintrag nennt die
getroffenen Entscheidungen, die zurückgenommenen Formulierungen und jede
eigenständige Ableitung.

---

## 10 Dateihandhabung

- Ersetzungen über Python mit `open(pfad, encoding='utf-8', newline='')` und nicht
  über sed.
- Prüfe nach jeder Ersetzung, dass sie genau so oft gegriffen hat wie erwartet.
- Ersetzter Fließtext wird nicht gelöscht, sondern als Kommentar mit Datum und
  Grund über der neuen Fassung erhalten.
- Gib immer die vollständige Datei zurück, nie ein Fragment, es sei denn, der
  Verfasser verlangt ausdrücklich einen Ausschnitt.
- Zu jedem Zeitpunkt arbeitet nur eine Seite an einer Datei. Vor Beginn
  `git status` lesen und Dateien mit fremden ungesicherten Änderungen nicht
  anfassen.
