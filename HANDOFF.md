# Übergabe an die nächste Sitzung, Stand 19.09.2026, abends

Diese Datei ersetzt die Fassung vom Vormittag des 19.09.2026 vollständig. Die
alte Fassung steht in der Git-Historie unter `854c4a7`.

**Lesereihenfolge zu Beginn der Sitzung.** `CLAUDE.md`, dann diese Datei, dann
`WORKFLOW.md` Abschnitt 7. `ENTSCHEIDUNGSPROTOKOLL.md` hat über 10 000 Zeilen
und wird nie ganz gelesen, sondern nur angehängt und gezielt durchsucht. Die
Einträge vom 19.09.2026 sind umfangreich und lohnen die gezielte Suche.

---

## 1 Was in dieser Sitzung zu tun ist

Der Verfasser geht das gesetzte PDF durch und veranlasst Änderungen. Der Ablauf
ist seit dem 16.09.2026 eingespielt:

1. Der Verfasser zitiert eine Stelle aus dem PDF, meist mit den Trennzeichen des
   Umbruchs, und schreibt dahinter, was daran nicht stimmt. Die Anweisung ist
   oft knapp und in Tippschreibweise.
2. Du suchst die Stelle in der Kapiteldatei, nicht im PDF, prüfst den
   Zusammenhang des ganzen Absatzes und setzt die Änderung um.
3. Danach: `python tools/pruefen.py <datei>`, Build, und du zeigst die neue
   Fassung im Chat, nicht das ganze Kapitel.
4. Committet wird **nur**, wenn der Verfasser *"commite"* schreibt. Nie pushen.

**Der Verfasser stellt häufig Verständnisfragen** ("was heißt das?", "den Satz
verstehe ich nicht"). Das ist keine Bitte um Erklärung im Chat, sondern der
Befund, dass die Stelle im Text zu verdichtet ist. Erkläre die Sache kurz und
schlage sofort eine klarere Fassung vor.

**Der Verfasser prüft inhaltlich mit.** Am 19.09.2026 hat er mehrere Sachfehler
gefunden, die dem Text seit Wochen anhaften, unter anderem die falsch
zugeordnete State Estimation und die verdrehte Kausalität bei der
Sicherheitsmarge. Nimm seine Einwände ernst und prüfe sie an der Quelle nach,
bevor du umsetzt; mehrfach hat die Nachlese den Einwand bestätigt und zusätzlich
einen zweiten Fehler zutage gefördert.

Kapitel 1, die Einleitung von 2.1, 2.1.1, 2.1.2, 2.1.5 und 2.2 sind auf diesem
Weg überarbeitet. **Der Verfasser war zuletzt in 2.2**, unmittelbar nach der
Auflösung des Unterabschnitts zu den Dispatchmodellen.

---

## 2 Stand des Dokuments

Letzter Commit `0375f87`. Build sauber, **94 Seiten**. Zwölf Commits am
19.09.2026.

| Teil | Umfang |
|---|---|
| Kapitel 1 Einleitung | PDF-Seite 9 bis 13, fünf Seiten, **keine Reserve** |
| Kapitel 2 Grundlagen und Stand der Technik | PDF-Seite 14 bis 37 |
| Kapitel 3 Marktmechanismus und Modellierung | PDF-Seite 38 bis 56 |
| Kapitel 4 Exemplarische Anwendung | ab PDF-Seite 57, Gerüst |

Logische Seitenzahl ist PDF-Seite minus acht.

`main.tex` bindet die Kapitel 1 bis 4 ein, die Kapitel 5 und 6 sind
auskommentiert. Die beiden Warnungen zu `ch:discussion` und `ch:conc` sind
deshalb normal. `python tools/pruefen.py --alle` meldet einen Altbefund in
`chapters/chapter_5.tex` Zeile 91, der zum auskommentierten Kapitel gehört.

### Gliederung von Kapitel 2, Stand jetzt

Die Nummerierung hat sich am 19.09.2026 verschoben, weil der Unterabschnitt
*Selbstdispatch und Zentraldispatch* aufgelöst worden ist.

```
2.1  Kurative Systemführung
     2.1.1 Präventive und kurative Systemführung im Engpassmanagement
     2.1.2 Prozessablauf und Zeitanforderungen
     2.1.3 Technologien kurativer Akteure
     2.1.4 Herausforderungen der Umsetzung
     2.1.5 Rechtlicher Rahmen
2.2  Marktrahmen und Systemdienstleistungen
     2.2.1 Marktzeithorizonte und Handelsgelegenheiten   (war 2.2.2)
     2.2.2 Systemdienstleistungen                        (war 2.2.3)
2.3  Vergütungslogiken für Systemdienstleistungen
     2.3.1 bis 2.3.5 unverändert
2.4  Zwischenfazit
```

Die Marke `sec:dispatch_models` ist entfallen, sie wurde nirgends referenziert.
`sec:market_horizons` bleibt, weil Anhang A sie braucht.

---

## 3 Entscheidungen des 19.09.2026, die beim Schreiben binden

Ausführlich im Protokoll unter `chapter_2.tex` und unter den übergreifenden
Entscheidungen, jeweils Einträge vom 19.09.2026.

- **Stilregel 1 ist geändert.** Ein Absatz trägt **mindestens eine halbe Seite**.
  Ein Umbruch steht nur bei einem Wechsel der Kernaussage und **nie innerhalb
  einer Aufzählung**. Die Obergrenze von acht Sätzen ist entfallen. Gemessen:
  eine Textseite trägt rund 40 Zeilen, ein Satz nach Stilregel 17 rund 1,9
  Zeilen, eine halbe Seite also zehn bis zwölf Sätze. `CLAUDE.md` Abschnitt 4
  ist an dieser Stelle noch nicht nachgezogen.
- **Aufzählungen wie erstens, zweitens, drittens sind aufzulösen**, wenn die
  Punkte inhaltlich zusammenhängen. In 2.1.1 ist das geschehen.
- **Neue Vorgabe zu Abbildungen.** Abbildung und Verweis gehören auf dieselbe
  Seite. Das Prüfskript liegt im Sitzungsverzeichnis und ist **noch nicht** in
  `tools/pruefen.py` aufgenommen; es liest das PDF mit `pdftotext`, löst
  Trennstriche am Zeilenende auf und meldet den Seitenabstand. Aktuell 14
  Befunde, davon elf mit einer Seite Abstand, also gewöhnlicher Gleitsatz.
- **Das Aktenzeichen lautet `BK8-22-001-A`** mit drei Ziffern. Die Quelle
  schreibt es durchgehend so, die vierstellige Form stand nur in der
  BNetzA-URL und in Dateinamen. In `literature.bib` sind drei Stellen
  nachgezogen, URL und Dateipfade bleiben vierstellig. Der offene Punkt in
  `CLAUDE.md` Abschnitt 5 ist damit erledigt.
- **KuPilot erprobt die kurative Höherauslastung.** Das ist eine Einordnung des
  Verfassers gegen den Wortlaut beider greifbarer Quellen, die von kurativem
  Redispatch sprechen. Ein Folgesatz im Text nennt deren Bezeichnung
  ausdrücklich, damit die Quelle keine Aussage belegt, die sie nicht trägt.
  Nicht stillschweigend zurückdrehen.
- **Der kurative Marktmechanismus ist technologieoffen auszugestalten.** Die
  Binnenmarktverordnung schützt nicht die BESS vor einem Ausschluss, sie
  beschränkt den Zuschnitt des Produkts.
- **BESS gelten als schnell**, die sehr schnelle Klasse unter zehn Sekunden ist
  eine zu prüfende Fähigkeit. InnoSys 2030 definiert die Klasse, untersucht das
  Potenzial aber nur für die schnelle und die langsame Klasse.
- **Die Vergütungsstruktur von KuPilot wird nicht dargestellt.** Es bleibt
  dabei, dass die Bereitstellung auf einer bilateralen Vereinbarung für dieses
  Projekt beruht. Die veröffentlichte Struktur ist bekannt und bewusst
  ausgelassen, siehe Protokoll.
- Die Entscheidungen vom 18.09.2026 gelten unverändert, insbesondere das
  Trendjahr 2032 des NEP, die gestrichenen drei Teilfragen, Begriffe als
  Apposition statt im Definitionsabsatz, kein Absatzauftakt mit einem
  Literaturanker und keine Fußnoten in Kapitel 2.

---

## 4 Arbeitstechnik, die sich bewährt hat

- Änderungen an Kapiteldateien **immer über ein Python-Skript**, das die Datei
  mit `open(pfad, encoding="utf-8", newline="")` liest und mit CRLF
  zurückschreibt. Das Skript bricht ab, wenn ein Anker nicht genau einmal
  greift. Ersetzter Fließtext bleibt als Kommentar mit Datum und Grund über der
  neuen Fassung stehen.
- **Achtung bei Ankern.** Viele Sätze stehen doppelt in der Datei, einmal als
  Fließtext und einmal als auskommentierte alte Fassung. Anker deshalb auf
  Gleichheit der ganzen Zeile prüfen oder Kommentarzeilen ausschließen, sonst
  greift die Ersetzung an der falschen Stelle. Das ist am 19.09.2026 mehrfach
  passiert.
- **Skripte mit Backslashes oder Umlauten nur über das Write-Werkzeug anlegen**
  und dann ausführen. Bash-Heredocs und `python -c` verstümmeln `\c`, `\a`,
  `\t` und `\u`. Bei der Ausgabe auf die Konsole `sys.stdout` auf UTF-8
  umstellen, sonst bricht der Druck an Umlauten ab.
- **Gegenprobe nach jeder Umstellung.** Die Fließtextzeilen vor und nach der
  Änderung vergleichen und die Differenz ausgeben. Eine reine Zählung genügt
  nicht; am 19.09.2026 ist so ein doppelt gesetzter Satz entdeckt worden, den
  die Zählung nicht gezeigt hätte.
- Layoutprüfung ohne PDF-Betrachter: `pdftotext -layout main.pdf -`, die Ausgabe
  an `\f` in Seiten teilen und Trennstriche am Zeilenende auflösen, sonst werden
  umbrochene Wörter wie "Abbil-dung" nicht gefunden.
- Build: `pdflatex main; biber main; pdflatex main; pdflatex main`. `biber` nur
  nötig, wenn sich Zitate geändert haben.
- **Nicht jede Quelle ist maschinell lesbar.** Die TenneT-Mitteilung zu KuPilot
  ist eine reine Bilddatei ohne Schriften. Die FfE-Quelle zum Sägezahn und die
  FAQ Stromspeicher der Bundesnetzagentur tragen Type-3-Schriften ohne
  ToUnicode-Tabelle. Bei diesen dreien liefert `pdftotext` nur Zeichensalat.
  Prüfe mit `pdffonts`, bevor du einem leeren Ergebnis traust, und sage dem
  Verfasser, wenn eine Aussage deshalb nicht an ihrer Quelle prüfbar ist.
- **Subagenten nur nach Rückfrage**, mit Zweck und Anzahl. Am 19.09.2026 haben
  fünf Leseagenten die Zahlenprüfung von Kapitel 2 getragen; das hat sich
  bewährt und vier Sachfehler gefunden.
- Zu jedem Abschnitt, an dem gearbeitet wurde, gehört ein Protokolleintrag nach
  `CLAUDE.md` Abschnitt 9, mit den zurückgenommenen Formulierungen im Wortlaut
  und mit jeder eigenständigen Ableitung als solcher gekennzeichnet.

---

## 5 Dateien im Repository

Aktiv im Wurzelverzeichnis: `CLAUDE.md`, `WORKFLOW.md`, `HANDOFF.md`,
`ENTSCHEIDUNGSPROTOKOLL.md`, `DURCHSICHT_KAP1_3.md` (allein Liste G ist noch
aktuell), `KAPITEL_4_AUFBAU.md` (gehört der parallelen Sitzung), `README.md`.

`archiv/` ist Nachschlagewerk und wird nicht fortgeschrieben.
`quellencheck_bericht.md` erzeugt `tools/quellencheck.py` neu und ist in
`.gitignore`.

---

## 6 CLAUDE.md ist an sechs Stellen überholt

Der Verfasser zieht `CLAUDE.md` selbst nach, Claude ändert die Datei nicht
stellvertretend. Offen sind:

1. **Abschnitt 4, Stilregel 1.** Statt *vier bis acht Sätze* gilt seit dem
   19.09.2026 *mindestens eine halbe Seite, Umbruch nur bei Wechsel der
   Kernaussage, nie innerhalb einer Aufzählung*.
2. **Abschnitt 5, Begriffe.** Als Ort der Definition von PATL und TATL steht
   dort "2.1.1 Absatz 1"; nach der Umstellung ist es Absatz 3.
3. **Abschnitt 5, offene Punkte.** Das Aktenzeichen ist entschieden,
   `BK8-22-001-A`, und kann dort gestrichen werden.
4. **Abschnitt 5, Begriffe.** Die Abgrenzung "kein Marktdesign mit
   prognostizierten Preisen" bezieht sich auf einen am 18.09.2026 gestrichenen
   Satz.
5. **Abschnitt 7, Entscheidung 4.** Dort steht das Jahr 2030 als qualitativer
   Rahmen; der Rahmen ist seit dem 18.09.2026 das Trendjahr 2032 des NEP.
6. **Abschnitt 1, Dateiliste.** `KOMMENTARE_KAP3.md` steht dort noch im
   Wurzelverzeichnis, liegt aber seit dem 19.09.2026 in `archiv/`. Abschnitt 10
   gilt für `chapters/chapter_3.tex` weiterhin mit der Ausnahme, dass die Datei
   kommentarfrei bleibt.

---

## 7 Offene Punkte

**Aus dem Durchgang vom 19.09.2026**

- Der belegte Befund von Consentec, die Vergütungslogik der freiwilligen
  Selbstverpflichtung KuPilot sei "teilweise nicht vollständig in der aktuell
  regulatorisch geltenden Kostenerstattungssystematik im Redispatch abbildbar",
  ist vorgemerkt und nicht verwendet. Er stützt die Fragestellung unmittelbar.
- Ob die Betriebsplanungsprozesse WAPP, pRD1, pRD2/DACF und IDCF oder die
  Ausfallapproximation in den Text sollen. `leeuwen_integration_2020` nennt die
  Prozesse und in einer Fußnote den AC-SCOPF, kennt aber weder den Begriff
  Ausfallapproximation noch ein synthetisches Netzmodell.
- Ob ein Satz ergänzt wird, wonach die Arbeit mit dem BESS den Preis **eines
  Anbieters** bestimmt und nicht den Zuschnitt des Produkts. Das folgt aus der
  technologieoffenen Ausgestaltung und passt zu `CLAUDE.md` Abschnitt 5.
- Die Aussage, dass die Vorhaltung keine Vergütungsregel kennt, steht in 2.1.5
  dreimal, nämlich als Rahmung, als Schluss der Analyse und als Überleitung zu
  den flexiblen Netzanschlüssen. Ob dort gekürzt wird, ist offen.
- Ob Kapitel 1 dieselbe Vorwegnahme trägt, ist ungeprüft.
- Zwei bib-Einträge sind verwaist, nämlich `bundesnetzagentur_beschluss_2019`
  und `bundesministerium_der_justiz_netzausbaubeschleunigungsgesetz_2025`.
- Ob die Näheprüfung als elfte Prüfung in `tools/pruefen.py` aufgenommen wird,
  und ob die beiden Abbildungen mit zwei Seiten Abstand angefasst werden,
  nämlich Abbildung 1.2 und Abbildung 3.2.

**Ältere Punkte, unverändert**

- Der Ausdruck *Marge* ohne Attribut steht noch in 2.1.5 und in
  `chapters/chapter_1.tex` Zeile 209. Die Stelle in Kapitel 1 trägt zusätzlich
  dieselbe Kausalitätsverdrehung, die am 19.09.2026 in 2.1.1 behoben worden ist,
  nämlich die Gleichsetzung von Marge und Eingriff.
- Der Ausdruck *kurative Verfügbarkeit* steht noch in 2.4 und ist durch
  *kurative Vorhaltung* zu ersetzen.
- Die Abgrenzung, dass der eingesparte Engpassmanagementbedarf nicht Gegenstand
  ist, weil dafür ein Netzmodell nötig wäre, ist am 18.09.2026 aus 1.2
  gestrichen worden und steht seither nirgends. Vorschlag: 3.2.1 oder Kapitel 5.
- Der Absatz zu den Vergütungslogiken in 1.2 hat rund vierzehn Sätze, der
  Zielabsatz neun. Nach der neuen Stilregel 1 ist das kein Befund mehr.
- `KAPITEL_4_AUFBAU.md` stützt sich auf die drei gestrichenen Teilfragen.
- Der angekündigte Vergleich der marktlich beschafften Vorhaltung mit dem
  präventiven Redispatch ist in den Kapiteln 4 und 5 nicht eingeplant.
- `DURCHSICHT_KAP1_3.md` Liste G, vierzehn Punkte aus Kapitel 3, nichts
  umgesetzt. Darunter G5 (Degradationskosten von 8 Euro je Megawattstunde ohne
  Quelle), G7 (ausgeschriebene aFRR-Menge von 2000 MW ohne Beleg) und G13 (vor
  Abgabe prüfen, ob eine Mitteilung der Beschlusskammer zu Batteriespeichern
  ergangen ist). Die Listen A bis F sind durch die seitherigen Überarbeitungen
  teilweise überholt.
- Preisreihen in Kapitel 3 zitieren noch SMARD, die Umstellung auf
  energy-charts oder EPEX wartet auf eine Entscheidung.

**Eine Zahlenprüfung für Kapitel 3 steht aus.** Die Prüfung von Kapitel 2 am
19.09.2026 hat bei 17 geprüften Angaben vier Sachfehler und sechs nicht
tragende Belege gefunden. Für Kapitel 3 ist dasselbe Vorgehen angezeigt.

---

## 8 Für Kapitel 3 und 5 vorgemerkt

Aus der Zahlenprüfung vom 19.09.2026, im Protokoll belegt:

- Anlage 1 der Festlegung, Seite 13: "Jedenfalls erachtet die Beschlusskammer
  eine Anwendung der Vorgaben zur Vergütung von Pumpspeicherwerke auf
  Batteriespeicher (auch ohne weitere Anpassungen) als zulässig." Das ist der
  Quellenbeleg dafür, dass die am PSKW entwickelte Bemessung auf BESS
  übertragen werden darf.
- Ebenda: "§ 13a Abs. 2 EnWG gibt ausdrücklich einen kostenbasierten Redispatch
  vor und die Einführung eines marktbasierten Redispatches ist schon aufgrund
  des gesetzlichen Rahmens nicht möglich."
- Die 30 Tage der Standardabweichung sind nicht mit den 90 Tagen zu verwechseln,
  die Anlage 1 für die Schätzung des IDA-Ergebnisses vor 14:30 Uhr nennt.
- Der Auftraggeber des Weber-Gutachtens ist in den Quellen widersprüchlich. Das
  Deckblatt der Anlage 2 sagt EnBW, die Festlegung sagt in Fußnote 1 BDEW. Der
  bib-Eintrag folgt dem Deckblatt und bleibt vorerst so.
- Anlage 1 der Festlegung liegt doppelt in `literature/PDFs`.

---

## 9 Modellrepository

`C:/GIT-HUB/bess_dispatch_optimization`, Interpreter mit matplotlib:
`C:/ProgramData/anaconda3/envs/venv_mode/python.exe`.

Der Verfasser hat dort eigene ungesicherte Änderungen in mehreren Dateien. Vor
jedem Zugriff `git status` lesen und fremde Änderungen nicht anfassen.

**Abbildungen.** Größe und Seitenverhältnis werden **im Erzeugungsskript**
gesetzt, über `ts.subplots(breitenanteil=..., seitenverhaeltnis=...)` mit
`TEXTWIDTH = 16 cm`, und **niemals** über `\includegraphics` skaliert. Die
Skripte liegen unter `analysen/code/schrift/`, die fertigen PDF werden nach
`figures/chapter_<n>/` kopiert.

**Eigene Auswertungen.** `analysen/mastr_speicher` für den Energieinhalt je
Leistung, `analysen/mfrr_leistungspreise` für die mittleren Leistungspreise des
Jahres 2025, `analysen/vollreservierung_pruefung`. Die vier Leistungspreise sind
am 19.09.2026 nachgerechnet und bestätigt, die Einheit Euro je Megawatt und
Stunde ist richtig. Die mFRR-Rohdateien liegen nicht im Repository.

Der Quelltext des Erlösindex der ISEA Battery Charts liegt lokal unter
`C:/GIT-HUB/battery_revenue_index-main`.
