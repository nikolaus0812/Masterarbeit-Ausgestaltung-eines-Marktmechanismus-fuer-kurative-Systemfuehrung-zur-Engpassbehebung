# Kommentare der Freunde zur PDF-Fassung, Stand 30.09.2026

Quelle sind zwei kommentierte PDF-Dateien in `sciebo/Masterarbeit/Nils_Feedback/`.
Die Anmerkungen sind mit pymupdf ausgelesen, markierter Text und Kommentartext
unverändert übernommen, und jeder Stelle ist die Zeile in der aktuellen
Kapiteldatei zugeordnet. Die Spalte *Entscheidung* bleibt leer, bis der
Verfasser entschieden hat. Die Spalte *Einordnung* ist meine Vorsortierung
gegen `CLAUDE.md` und trägt keine Entscheidung.

| Leser | Datei | Stand des PDF | Umfang | Anmerkungen |
|---|---|---|---|---|
| Luca (`lucah`) | `..._LD.pdf` | Build vom 28.09.2026, Kapitel 1 bis 6 mit Anhängen, 129 Seiten | Kurzfassung, Kapitel 1, einzelne Stellen in 3, 4 und 6 | 19, davon drei Markierungen zur Kurzfassung unter L1 zusammengefasst, deshalb keine L2 und L3 |
| Julius (`Julius.Klupp`) | `..._jkl.pdf` | Build vom 21.09.2026, nur Kapitel 1 bis 3, 85 Seiten | Kapitel 1 und 2.1 bis 2.1.4, gelesen bis 2.1.5 | 50, davon 12 Lob ohne Auftrag |
| Nicht benannt, vom Verfasser am 30.09.2026 aus dem Chat übernommen | keine Datei | unbekannt | Kapitel 1 und alle Abbildungen | 2 allgemeine Kommentare, Kennung C, Abschnitt 8 |

**Achtung beim Julius-PDF.** Es ist neun Tage älter als der aktuelle Text.
Alle Zitate sind gegen die Kapiteldateien geprüft, jede kommentierte Stelle
steht noch im Text. Eine Ausnahme ist L8, dort ist das markierte Wort seither
geändert, siehe Einordnung.

Kennung: L = Luca, J = Julius, laufend nummeriert. Kategorien: **Wort** (ein
Wort oder eine Wendung), **Satz** (Satzbau, Trennung, Zeichensetzung),
**Verständnis** (ein Leser versteht die Stelle nicht), **Aufbau** (Reihenfolge
von Sätzen, Absätzen oder Abschnitten), **Inhalt** (Aussage, Beleg, Zahl),
**Zitierweise**, **Lob** (kein Auftrag, zeigt aber, was trägt).

---

## 1 Vorab entscheidbar, weil eine Regel aus `CLAUDE.md` betroffen ist

Diese Kommentare treffen Stellen, die eine Vorgabe des Verfassers so vorschreibt.
Sie sind nur mit einer Änderung der Regel umzusetzen.

| Nr. | Stelle | Kommentar | Betroffene Regel | Entscheidung |
|---|---|---|---|---|
| J21 | 1.2, `chapter_1.tex:117` | *nämlich* gestrichen | Stilregel 16: Listeneinleitungen mit *nämlich* oder *folgende*. Der Text trägt 49 Stellen mit *nämlich*. | |
| J34 | 2.1.2, `chapter_2.tex:145` | *nämlich* gestrichen | wie J21 | |
| L15 | 4.1, `chapter_4.tex:23` | *fällt Folgendes auf.* Doppelpunkt? | Stilregel 16: Doppelpunkt sparsam und nur für These mit Erklärung. Die Form *Folgendes.* ist im Text mehrfach so gesetzt, in 4.1, 4.2 und 4.6.4. | |
| L14 | 4.1, `chapter_4.tex:17` | *zwischen null und 200 €/(MW·h)* irritiert, Zahl ausschreiben ist zwar üblich | Keine Regel in `CLAUDE.md`. Gleiche Form in Anhang F fünfmal in Bildunterschriften. Wenn geändert, dann überall. | |

---

## 2 Kurzfassung

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| L1 | Kurzfassung, `extras/abstract.tex:37` | BESS, FCR, aFRR | „Ich weiß nicht ob man auch hier Abkürzungen ohne vorige Erklärung nutzen sollte." | Zitierweise | Die drei stehen als `\acs`, EnWG dagegen als `\ac` mit Langform. Uneinheitlich. Die Kurzfassung steht vor dem Abkürzungsverzeichnis, ein Leser der Kurzfassung allein kennt die drei nicht. Der Abstract schreibt alle drei aus. | |
| L19 | Kurzfassung, `extras/abstract.tex:41` und 6, `chapter_6.tex:34` | *zwei Fünftel* | „40 % ?" | Wort | 4.4 sagt an derselben Stelle *rund 40 Prozent*. Zwei Schreibweisen für dieselbe Zahl, nämlich *zwei Fünftel* in Kurzfassung und Kapitel 6, *40 Prozent* in 4.4. | |

---

## 3 Kapitel 1 Einleitung

### 3.1 Kapiteleinleitung, `chapter_1.tex:4` bis `9`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J1 | Zeile 4 | `[BUN26a]` | „Zitiert ihr so? Max hat nur die Zahl stehen, ich hatte die ganzen Autoren, irgendwie komisch" | Zitierweise | Vorlage des Instituts, alphanumerischer Stil von biblatex. Kein Handlungsbedarf, nur Auskunft. | |
| J2 | Zeile 5 | *bewegt seither Mengen* | „Mengen von was" | Verständnis | Stilregel 5, unbestimmte Nominalphrase ohne Attribut. Gemeint sind Energiemengen im Redispatch. | |
| J3 | Zeile 8 | *Regime des Redispatch* | „würd ich erklären" | Verständnis | Redispatch ist erst in Zeile 22 erklärt, also in 1.1 Absatz 2, wie in `CLAUDE.md` Abschnitt 5 vorgesehen. Die Kurzform in der Kapiteleinleitung steht vor der Definition. Hängt mit J9 zusammen. | |
| J4 | Zeile 8 | *nur wenige Anlagen* | „Stromerzeugungsanlagen?" | Verständnis | Stilregel 5. | |
| J5 | Zeile 9 | *Eine Lösung könnte darin liegen* | „formuliers anders. Ist kurative Systemführung die Lösung des Problems und es geht nur um die Umsetzung? Selbst wenn es alternative Lösungsansätze gibt, würd ich schreiben, dass dies ein Lösungsansatz ist und noch Herausforderungen bestehen." | Inhalt | Der Folgesatz nennt die Herausforderungen schon. Es geht um die Behauptungsstärke des ersten Satzes, Stilregel 11. | |

### 3.2 Abschnitt 1.1, Absätze 1 bis 4, `chapter_1.tex:15` bis `49`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J6 | Zeile 15 | Absatz 1, Satz 1 | „örtliches Problem" | Aufbau | Julius liest die beiden ersten Sätze als Ort und Zeit. Randnotiz, kein Auftrag. | |
| J7 | Zeile 16 | Absatz 1, Satz 2 | „Zeitliches Problem. Die Info fehlt" | Verständnis | Er vermisst, dass der Satz die Zeit als zweite Dimension benennt. Der Absatz schließt mit *nicht stationär*, das trägt es nur implizit. | |
| J8 | Zeile 19 | Absatz 2, Satz 1 | „das ist ein Satz, teil das mal auf" | Satz | Stilregel 17. Der Satz trägt Doppelpunkt, Einschub mit *also* und Relativsatz. | |
| J9 | Zeile 22 | *Redispatch an, also eine Anpassung der Einspeisung einzelner Anlagen* | „da erklärst dus, würd ich nach oben nehmen" | Aufbau | Widerspricht der Festlegung in `CLAUDE.md` Abschnitt 5, Redispatch in 1.1 Absatz 2 zu definieren. Zusammen mit J3 entscheiden. | |
| L4 | Zeile 22 | *sagt … voraus* | „prognostiziert" | Wort | Stilregel 13 verlangt schlichtes Vokabular, *voraussagen* ist schlichter als *prognostizieren*. Geschmacksfrage. | |
| J10 | Zeile 23 | *eine Überlastung ab* | „Überlastung wovon?" | Verständnis | Stilregel 5. Betriebsmittel sind erst in Zeile 60 eingeführt. | |
| J11 | Zeile 24 | Absatz 2, letzter Satz | „gut!" | Lob | | |
| J12 | Zeile 33 | *Der Engpassmanagementbedarf ist hoch und von wenigen Wetterlagen geprägt* | „das zeigt die Abbildung aber nicht" | Inhalt | Trifft zu. Abbildung 1.1 zeigt Jahressummen, die Wetterlagen stehen erst in den Monatskosten im Text. Der Verweis *wie Abbildung 1.1 zeigt* deckt nur die erste Satzhälfte. | |
| L5 | Zeile 36 | Satz zum Dezember 2024 | markiert ohne Text | Inhalt | Gehört zu L6, Wiederholung in Zeile 53. | |
| J13 | Zeile 37 | *In einer solchen Wetterlage regelt der Redispatch Windstrom ab* | „der Satz muss vor den Absatz. Gut wäre: erst erklären, was bei einer kritischen Wetterlage passiert, dann mit dem Diagramm zeigen, dass das in Deutschland relevant ist, dann auf die Kosten überleiten" | Aufbau | Vorschlag für die Reihenfolge des Absatzes 3: Mechanismus, Menge, Kosten. Betrifft denselben Absatz wie J12 und L5. | |
| J14 | Zeile 47 | Absatz 4, NEP | „gut!" | Lob | | |

### 3.3 Abschnitt 1.1, Absätze 5 bis 7, `chapter_1.tex:53` bis `79`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| L6 | Zeile 53 | *Der Engpassmanagementbedarf ist ereignisabhängig, denn einzelne Wetterlagen wie die Windfront im Dezember 2024 prägen …* | „Wiederholung" | Inhalt | Trifft zu. Zeile 36 und Zeile 53 tragen denselben Befund mit derselben Quelle. Beide Leser stoßen sich daran, siehe J15. | |
| J15 | Zeile 53 | derselbe Satz | „den Satz würd ich nach oben zu der Redispatch-Erklärung ziehen" | Aufbau | Julius will die Wiederholung durch Verschieben lösen, Luca durch Streichen. Eine Entscheidung für beide. | |
| J16 | Zeile 56 | *ist damit das geeignete Mittel* | markiert ohne Text | Wort | Vermutlich Anstoß an *geeignet* ohne Vergleichsmaßstab, Stilregel 7. | |
| J17 | Zeile 57 | *ist deshalb um ein Instrument zu erweitern* | markiert ohne Text | Wort | Vermutlich die Folge aus J16, die Schlussfolgerung hängt am vorigen Satz. | |
| J18 | Zeile 60 | *Betriebsmittel* | „Also Anlage? Was ist hier ein Betriebsmittel?" | Verständnis | Betriebsmittel wird erst in 2.1 als *Leitungen und Transformatoren* erklärt, Zeile 11 in `chapter_2.tex`. In Kapitel 1 steht das Wort in Zeile 5 neben *Leitungen und Transformatoren* und ab Zeile 60 ohne Erklärung. Julius bestätigt das Fehlen in J26. | |
| L7 | Zeile 62 | *Dauergrenze* | „Mir ist nicht klar, was du damit meinst. Ist das Gesamtbelastung ohne N-1?" | Verständnis | Das Wort ist in Kapitel 1 nicht definiert, der PATL erst in 2.1.1. Der Vorsatz sagt *die Belastung, die jedes Betriebsmittel dauerhaft führen kann*. | |
| L8 | Zeile 63 | *thermische Reserve* | „Im Sinne von z. B. einem Kessel mit einer Trägheit, der kurzzeitig mehr Leistung schafft?" | Verständnis | Luca versteht *thermisch* als Kraftwerkseigenschaft, gemeint ist die thermische Trägheit des Betriebsmittels. Julius' PDF trägt hier noch *physikalische Reserve*, der Text ist seither auf *thermisch* geändert. | |
| L9 | Zeile 69 | *Fahrplanänderungen nach der letzten Vorschaurechnung gehen in keine Rechnung mehr ein, und gerade Anlagen …* | „Sätze trennen" | Satz | Stilregel 17, zwei Hauptsätze mit Nebensatz. | |
| J19 | Zeile 75 | Absatz 7, *Die kurative Systemführung vermeidet Engpässe nicht im Voraus* | „schöne Überleitung" | Lob | | |

### 3.4 Abschnitt 1.2, `chapter_1.tex:84` bis `119`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| L10 | Zeile 94 | *mit dem präventiven Redispatch mithält* | „ugs., lieber *konkurrenzfähig ist*" | Wort | Die Kurzfassung sagt schon *konkurrenzfähig*. | |
| J20 | Zeile 96 | Absatz 3, *Für die Vorhaltung von Leistung besteht keine Vergütung …* bis *… verbindet damit beide Logiken* | „das ist alles Stand der Technik, weiß nicht, was das in deiner Zielsetzung macht" | Aufbau | Grundsätzlicher Einwand gegen den halben Absatz. Der Absatz begründet, warum ein Optimierungsmodell die Antwort gibt, und holt dafür die Rechtslage und die Regelleistung vor. Betrifft denselben Absatz, den der Betreuerdurchgang bereits gekürzt hat. | |
| J22 | Zeile 112 | Kapitelübersicht | „gut! bisschen lang, aber gut!" | Lob | | |
| J21 | Zeile 117 | *nämlich* | gestrichen | Wort | siehe Abschnitt 1 dieser Datei | |

---

## 4 Kapitel 2 Grundlagen und Stand der Technik

### 4.1 Kapiteleinleitung und 2.1, `chapter_2.tex:3` bis `20`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J23 | Zeile 4 | *dargelegt, und daraus wird begründet* | „Punkt." | Satz | Stilregel 17. | |
| J24 | Zeile 6 | *Zuletzt wird geprüft* | „du prüfst doch nicht im zweiten Kapitel irgendwas. Das ist das Grundlagen- und Erklär-Kapitel!!" | Wort | 2.3.3 prüft tatsächlich die Übertragbarkeit der Festlegung, insofern trägt das Wort. Julius liest es als Vorgriff auf Kapitel 3. | |
| J25 | Zeile 3 bis 6 | Kapiteleinleitung als Ganzes | „in dem kleinen Absatz fehlt komplett der rote Faden. Warum kurative Systemführung zuerst, warum der Rest danach, wieso ist das wichtig für meine Arbeit" | Aufbau | Stilregel 3, Überleitung. Die Einleitung zählt die drei Teile auf, ohne die Reihenfolge zu begründen. | |
| J26 | Zeile 11 | *Betriebsmitteln wie Leitungen und Transformatoren* | „ahh das sind Betriebsmittel. aiaiai" | Verständnis | Bestätigt J18, die Erklärung kommt zu spät. | |
| J27 | Zeile 20 | Ende von 2.1 | „gutes Kapitel bis hier!" | Lob | | |

### 4.2 Abschnitt 2.1.1, `chapter_2.tex:24` bis `86`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J28 | Zeile 41 | Verweis auf Abbildung 2.1 | „gut eingebunden!" | Lob | | |
| J29 | Zeile 65 | *denn der Kohle- und Kernenergieausstieg reduziert die steuerbare konventionelle Kapazität* | „vielleicht noch um einen Satz weiter ausführen? Warum passiert das gerade durch den Kohleausstieg?" | Inhalt | Ein Satz zur Ursache, Stilregel 4. Belegbar mit InnoSys 2030, das schon zitiert ist. | |
| J30 | Zeile 66 | *Volumen und Kosten … nicht proportional zueinander* | „sehr gut" | Lob | | |
| J31 | Zeile 77 | *Pumpspeicherkraftwerk (PSKW)* | „Mehrzahl" | Wort | Erstnennung über `\ac{PSKW}` liefert den Singular aus `abbreviations.tex`. `CLAUDE.md` Abschnitt 5 schließt `\acp` aus. Änderbar nur über den Satz oder den Eintrag im Verzeichnis. | |

### 4.3 Abschnitt 2.1.2, `chapter_2.tex:90` bis `147`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J32 | Zeile 104 | Absatz mit den Begriffen Scharfschaltung, Auslösung, Abruf, Umsetzung, Reaktionszeit, kurative Bindung, Bindungsdauer | „find ich sehr eklig zu lesen den ganzen Absatz, dabei ist die Grafik eigentlich ganz sauber" | Aufbau | Der Absatz ist eine Begriffsliste nach InnoSys 2030, so in `CLAUDE.md` Abschnitt 5 verlangt. Form bleibt offen, etwa eine Tabelle oder Definitionen je Phase im Folgeabsatz. | |
| J33 | Zeile 112 | *State Estimation* | „deutsch noch dahinter?" | Wort | Der Satz erklärt es bereits mit *also der aus Messwerten geschätzten Netzsituation*. Vielleicht den deutschen Begriff *Netzzustandsschätzung* voran. | |
| J35 | Zeile 126 | *Last [INN21], wobei sich …* | „Punkt. Würd auch nicht mitten im Satz zitieren" | Satz | Stilregel 17 und 15. Der Satz trägt nach dem Zitat noch einen Nebensatz mit *wobei*. | |
| J36 | Zeile 128 | *stellt sich die Frage nach Vorhaltung und Vergütung* | „bis dahin guter Absatz. *stellt sich die Frage* ist nicht gut formuliert. *muss beachtet werden* vielleicht?" | Wort | Sein Vorschlag ist Passiv, Stilregel 12. Alternative ohne Passiv nötig. | |
| J37 | Zeile 142 | *Situation, und damit der ÜNB …* | „puuuuuunkt" | Satz | Stilregel 17. Der Satz trägt *denn*, *und*, *damit*. | |
| J34 | Zeile 145 | *nämlich* | gestrichen | Wort | siehe Abschnitt 1 dieser Datei | |

### 4.4 Abschnitt 2.1.3, `chapter_2.tex:151` bis `226`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J38 | Zeile 162 | *der Anlagenbestand mit seiner Entwicklung* | „versteh ich nicht. Die Entwicklung des Bestandes?" | Verständnis | Gemeint ist der Zubau bis 2037. Das Pronomen *seiner* steht im Satz, also regelkonform, aber unklar. | |
| J39 | Zeile 164 | *Der Vergütungspfad betrifft nicht die Eignung …, also eine Regel, nach der der Ausgleich …* | „vielleicht noch einen Einschub mit Komma in den Satz einbauen?" | Satz | Ironisch, der Satz ist zu verschachtelt. Stilregel 17. | |
| J40 | Zeile 198 | *allein ein Abregelpotenzial* | „lediglich?" | Wort | *allein* ist im Text durchgehend für *nur* gesetzt, 84 Stellen in Kapitel 1 bis 6. Eine einzelne Änderung bräche die Konstanz, Stilregel 14. | |
| J41 | Zeile 199 | Absatz Wind und Photovoltaik | „schöner Absatz" | Lob | | |
| J42 | Zeile 205 | *eine über Stunden reichende Bindung* | „anhaltende" | Wort | | |
| J43 | Zeile 206 | *Im Pilotbetrieb von KuPilot ist ein PSKW bereits eingesetzt worden, dort allerdings auf eine Stunde begrenzt. … Die Zahl der PSKW ist jedoch begrenzt …* | „hier irgendwo noch ne Quelle" | Inhalt | Trifft zu. Der Absatz zu PSKW trägt keinen Beleg, obwohl er KuPilot nennt. TEN25 ist erst in 2.1.4 zitiert. Stilregel 8. | |
| J44 | Zeile 211 | *Ein BESS stellt anders als ein konventionelles Kraftwerk und eine Windenergieanlage auch aus dem Stillstand in beide Richtungen.* | „… Leistung bereit? Da fehlt doch noch was" | Verständnis | *stellen* ist Fachjargon für *den Betriebspunkt verändern*, in 1.1 als *Stellpotenzial* eingeführt. Ohne Objekt liest ein Fachfremder den Satz als unvollständig. Zusammen mit J45. | |
| J45 | Zeile 213 | *kann in dieser Richtung nicht weiter stellen* | „ist das Strom-Slang?" | Wort | siehe J44 | |
| J46 | Zeile 216 | *anders als konventionelle Kraftwerke* | „im Gegensatz zu" | Wort | Der Satz beginnt schon mit *Anders als PSKW*, die Wiederholung im selben Satz stört. | |
| J47 | Zeile 221 | Absatz Energieinhalt gegen Leistung | „gut erklärt!" | Lob | | |

### 4.5 Abschnitt 2.1.4 und 2.1.5, `chapter_2.tex:228` bis `260`

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| J48 | Zeile 228 | Überschrift *Herausforderungen der Umsetzung* | „boah, würd ich mir überlegen, ob das schon in Stand der Technik kommen sollte und nicht erst in Methodik" | Aufbau | Grundsätzlich. Der Abschnitt trägt die vier Hindernisse aus den Pilotprojekten, also Stand der Technik, und die Anforderungen A1 bis A8 in 3.1.1 bauen darauf auf. Eine Verschiebung zöge die Struktur von Kapitel 3 nach sich. | |
| J49 | Zeile 242 | *Die Ausgestaltung der Redundanz ist nicht Gegenstand der Untersuchung.* | „gerade der Satz darf in Kapitel 2 eigentlich nicht fallen" | Aufbau | Abgrenzung der Arbeit in einem Grundlagenkapitel. Verschiebbar nach 1.2 oder zu den nicht abgebildeten Größen in 3.2.1. | |
| J50 | Zeile 260 | Überschrift 2.1.5 | „hab bis hier gelesen" | Hinweis | Julius' Kommentare enden hier. | |

---

## 5 Kapitel 3 und 4

| Nr. | Stelle | Markiert | Kommentar | Kategorie | Einordnung | Entscheidung |
|---|---|---|---|---|---|---|
| L11 | 3.2.1, `chapter_3.tex:166` | *relative Optimalitätslücke von 0,01 Prozent* | „Stimmt das? Nicht dass du eigentlich 1 % meinst" | Inhalt | **Text und Code weichen ab.** `bess_dispatch_optimization/optimizer.py:465` setzt `MIPGap = 0.0`, mit dem Kommentar, ein Gap von 1e-4 entschiede mit darüber, ob eine Stunde als voll reserviert gilt. Der Text nennt 0,01 Prozent, also 1e-4, den Vorgabewert von Gurobi. Der Satz in 3.2.1 ist zu berichtigen, unabhängig davon, wie die Frage von Luca gemeint war. | |
| L12 | 3.3, `chapter_3.tex:409` | Überschrift *Validierung des Optimierungsmodells* | „Gehören die Ergebnisse der Validierung nicht eher in Kapitel 4?" | Aufbau | Die Gliederung ist am 13.09.2026 entschieden, siehe `archiv/STRUKTUR.md`. Die Validierung prüft das Werkzeug, Kapitel 4 trägt die Ergebnisse der Fragestellung. | |
| L13 | 3.3.1, `chapter_3.tex:440` | *taugt damit nicht als Maßstab* | „ugs." | Wort | Stilregel 15, nüchterner Ton. | |
| L14 | 4.1, `chapter_4.tex:17` | *zwischen null und 200* | siehe Abschnitt 1 | Wort | | |
| L16 | 4.1, `chapter_4.tex:19` | *Der 06.05.2025 tritt daneben* | „ugs., lieber *wird zusätzlich betrachtet*" | Wort | Sein Vorschlag ist Passiv, Stilregel 12. | |
| L17 | 4.1, `chapter_4.tex:20` | *macht die kurative Reservierung für den Betreiber lohnender* | markiert ohne Text | Wort | Vermutlich derselbe Anstoß, Stilregel 13 oder 15. | |
| L15 | 4.1, `chapter_4.tex:23` | *fällt Folgendes auf.* | siehe Abschnitt 1 | Satz | | |

---

## 6 Übergreifende Befunde aus beiden Durchsichten

Diese Punkte tragen mehrere Kommentare zugleich und sind vor den Einzelstellen
zu entscheiden.

1. **Begriffe vor der Definition in Kapitel 1.** *Redispatch* (J3, J9),
   *Betriebsmittel* (J10, J18, J26), *Dauergrenze* (L7), *thermische Reserve*
   (L8), *stellen* (J44, J45). Beide Leser stolpern in Kapitel 1 über
   Fachbegriffe, die erst in 2.1 erklärt sind. Die Liste in `CLAUDE.md`
   Abschnitt 5 legt die Orte fest, sie deckt *Betriebsmittel* und
   *Dauergrenze* nicht ab.
2. **Wiederholung der Windfront im Dezember 2024** in 1.1 Absatz 3 und 5
   (L5, L6, J15). Beide Leser unabhängig voneinander.
3. **Satzlänge** (J8, J23, J35, J37, J39, L9). Sechs Stellen gegen Stilregel
   17, alle in Kapitel 1 und 2.1, die schon zweimal durchgesehen sind.
4. **Aufbau von 1.1 Absatz 3** (J12, J13): Der Verweis auf Abbildung 1.1
   deckt die Wetterlagen nicht, und der Mechanismus der Windfront steht am
   Ende statt am Anfang.
5. **Kapiteleinleitung 2** (J23, J24, J25): roter Faden und *geprüft*.
6. **Grenzziehung Kapitel 2 gegen 3** (J48, J49, L12): drei Stellen, an
   denen ein Leser den Inhalt in einem anderen Kapitel erwartet.
7. **Umgangssprache** (L10, L13, L16, L17): vier Stellen.
8. **Zahlen und Zeichen mit Regelbezug** (J21, J34, L14, L15, L19): siehe
   Abschnitt 1, plus die zwei Schreibweisen für 40 Prozent.
9. **Zahl gegen den Code** (L11): Der Text sagt 0,01 Prozent, der Code setzt
   die Lücke auf null. Einzige Stelle, die unabhängig von jeder Entscheidung
   zu berichtigen ist.
10. **Beleg fehlt** (J43): PSKW im Pilotbetrieb.
11. **Länge und Inhalt von Kapitel 1** (C1, J20, J3, J18, L7, L8): Ein
    Leser will in der Einleitung nur Problem, Relevanz und Aufbau, die
    Erklärungen zu Netz, Markt und Redispatch erst in Kapitel 2. Die
    Einzelkommentare zu Begriffen vor der Definition (Punkt 1) sind die
    Folge desselben Aufbaus. Einzelheiten in Abschnitt 8.
12. **Bildunterschriften** (C2): alle 43 Bildunterschriften sind Titel in
    einem Satz, keine erklärt Achsen, Legende oder Aussage. Einzelheiten in
    Abschnitt 8.

## 7 Was die Leser loben

J11, J14, J19, J22, J27, J28, J30, J41, J47: der Zusammenhang Marktdesign und
Engpass, der NEP-Absatz, die Überleitung zur kurativen Systemführung, die
Kapitelübersicht, 2.1 als Ganzes, die Einbindung von Abbildung 2.1, die
Nichtproportionalität von Volumen und Kosten, der Absatz zu Wind und
Photovoltaik und der Absatz zum Energieinhalt. Diese Absätze sind beim Schliff
nicht anzufassen.

---

## 8 Allgemeine Kommentare aus dem Chat, 30.09.2026

Zwei Kommentare ohne Stelle im PDF, vom Verfasser im Wortlaut übermittelt.
Der Leser ist nicht benannt.

### C1 Länge und Inhalt der Einleitung

Wortlaut: „Ich find die Motivation/Einleitung sehr lang. Da erklärst du schon
sehr viel, was eigentlich eher in Kapitel 2 gehört. Ist sicherlich ein
bisschen Geschmackssache, aber ich möchte da nur wissen, wo das Problem
liegt, welches du mit der Arbeit lösen möchtest, warum das relevant ist und
wie du deine Arbeit aufgebaut hast. Die ganzen Erklärungen, wie die Märkte,
Netze, Redispatch und Co. funktionieren, können ruhig später kommen."

Kategorie: Aufbau. Was der Kommentar am Text trifft, in Zahlen:

| Absatz | Zeilen in `chapter_1.tex` | Sätze | Wörter | Trägt |
|---|---|---|---|---|
| Kapiteleinleitung | 4 bis 10 | 7 | 168 | Problem |
| 1.1 Absatz 1, Transportaufgabe | 15 bis 17 | 3 | 85 | Problem |
| 1.1 Absatz 2, Marktdesign | 19 bis 24 | 6 | 140 | Problem, mit Erklärung des dezentralen Dispatch |
| 1.1 Absatz 3, Bedarf und Kosten | 33 bis 38 | 6 | 147 | Relevanz |
| 1.1 Absatz 4, NEP | 47 bis 51 | 5 | 92 | Relevanz |
| 1.1 Absatz 5, Ereignisabhängigkeit | 53 bis 57 | 5 | 109 | Relevanz, Folgerung |
| 1.1 Absatz 6, präventive Systemführung | 59 bis 64 | 6 | 118 | **Erklärung**, (N-1)-Kriterium, Dauergrenze, thermische Reserve |
| 1.1 Absatz 7, Vorschauprozesse und Handelsfenster | 66 bis 73 | 8 | 175 | **Erklärung**, Rechenläufe, Handelsschluss, Netzsicherheitsrechnung |
| 1.1 Absatz 8, kurative Systemführung | 75 bis 79 | 5 | 100 | **Erklärung**, dann Wahl der BESS |
| 1.2 Absatz 1, Ziel | 86 bis 94 | 9 | 214 | Ziel |
| 1.2 Absatz 2, Vergütung und Modell | 96 bis 110 | 15 | 279 | **Erklärung**, § 13a, Regelleistung, dann Modell und Rahmen |
| 1.2 Absatz 3, Aufbau | 112 bis 119 | 8 | 150 | Aufbau |

Einordnung: Die vier fett markierten Absätze tragen 672 von 1777 Wörtern,
also gut zwei Fünftel des Kapitels, und genau dort liegen die Begriffe, an
denen beide anderen Leser gestolpert sind, nämlich Betriebsmittel,
Dauergrenze, thermische Reserve und Redispatch. Julius sagt zu 1.2 Absatz 2
dasselbe in J20. Der Kommentar deckt sich also mit sechs Einzelkommentaren.

Gegen eine Kürzung steht: Die Betreuerkommentare vom 14.09.2026 verlangten
den roten Faden von der Physik zur Vorhaltung, die Absätze 6 bis 8 sind die
Antwort darauf, und die Länge von fünf Seiten ist am 28.09.2026 bewusst
wiederhergestellt worden, siehe Commit `2bceb4e`. Eine Kürzung braucht
deshalb eine Entscheidung, was aus den Absätzen 6, 7 und 1.2 Absatz 2 nach
2.1.1, 2.2.1 und 2.3 wandert und was als ein Satz je Absatz in Kapitel 1
bleibt. Die Erklärung des dezentralen Dispatch in 1.1 Absatz 2 steht
bereits in 2.2, die Vorschauprozesse aus Absatz 7 in 2.2.1, die
Rechtslage aus 1.2 Absatz 2 in 2.1.5. Eine Kürzung streicht damit
überwiegend Dopplungen und keine Aussagen.

Entscheidung:

### C2 Bildunterschriften

Wortlaut: „Grundsätzlich brauchst du längere Bildunterschriften. Jede
Abbildung muss mit der Bildunterschrift voll verständlich sein, du schreibst
meistens nur eine Überschrift in den Abbildungstext."

Kategorie: Aufbau. Befund über alle 43 Bildunterschriften in Kapitel 1 bis 6
und den Anhängen, Tabellen eingeschlossen:

- Kürzeste 3 Wörter (Tabelle C.2), längste 25 (Abbildung 3.2), im Mittel 17.
- 29 von 43 bestehen aus einem einzigen Satz, der den Gegenstand nennt.
- 14 tragen einen zweiten Satz. Er nennt die Quelle (Abbildung 1.1, 1.2,
  Tabelle 2.2, A.1), eine Darstellungsregel (Ordinate ab 50 Prozent, Preisachse
  logarithmisch, Zeitumstellung steht schwarz, Whisker am oberen Ende) oder
  die Iteration (zweite Iteration). Keine erklärt, was die Abbildung zeigt,
  welche Größe auf welcher Achse steht oder was der Leser ablesen soll.
- Die Legenden stehen in den Abbildungen selbst, die Einheiten meist im
  Achsentitel.

Einordnung: `CLAUDE.md` trägt keine Regel zur Länge, nur die Ausnahme der
Bildunterschriften von den Zeichensetzungsregeln in Stilregel 16 und die
Vorgabe, dass jede Abbildung unmittelbar bei der Stelle steht, die auf sie
verweist. Der erklärende Satz steht heute im Fließtext vor oder nach der
Abbildung, etwa zu Abbildung 4.4 der Absatz zur Farbskala. Eine längere
Bildunterschrift wiederholte diesen Satz. Umsetzbar in zwei Stufen, nämlich
ein zweiter Satz je Bildunterschrift mit Achsen und Aussage bei den 22
Abbildungen in Kapitel 1 bis 4, oder nur bei den Ergebnisabbildungen in
Kapitel 4, die ein Leser ohne den Text am ehesten einzeln ansieht. Die
Tabellen brauchen ihn nicht, ihre Spaltenköpfe tragen die Einheit.

Entscheidung:

---

## 9 Stufen und Gewichtung, nachgetragen am 07.10.2026

Dieselben drei Stufen wie in `KOMMENTARE_BETREUER_KAP4_5.md`, mit zwei
Vorgaben des Verfassers vom 07.10.2026: Die Kommentare der Freunde haben
weniger Gewicht als die des Betreuers, und strukturelle Änderungen werden
auf ihre Kommentare hin nicht vorgenommen. Wo ein struktureller Kommentar
eine leichte Variante zulässt, steht sie bei B, der strukturelle Kern bei
C mit der Empfehlung *zurückstellen*. Die Spalte *Länge* wie dort, ±0 ist
Wortersatz.

| Stufe | Anzahl | Bedeutung |
|---|---|---|
| A | 31 | Wortersatz oder Satztrennung, automatisch, Verfasser sieht den Diff |
| B | 8 | Ein leichter Satz oder Halbsatz, Wortlaut wird vorgelegt |
| C | 8 | Strukturell, Empfehlung zurückstellen, leichte Variante genannt |
| entfällt | 21 | Lob, Auskunft, Markierung ohne Text, Regelkonflikt, Doppelung mit dem Betreuer |

### 9.1 Stufe A

| Nr. | Stelle | Umsetzung | Länge | Entscheidung |
|---|---|---|---|---|
| L1 | `extras/abstract.tex:37` | BESS, FCR und aFRR bei der ersten Nennung in der Kurzfassung ausschreiben, wie im Abstract. `\acs` bleibt, Langform davor. | +1 | |
| L19 | `extras/abstract.tex:41`, `chapter_6.tex:34` | *zwei Fünftel* durch *rund 40 Prozent* ersetzen, wie 4.4. | ±0 | |
| J2 | `chapter_1.tex:5` | *bewegt seither Energiemengen*. | ±0 | |
| J4 | `chapter_1.tex:8` | *nur wenige Erzeugungsanlagen*. | ±0 | |
| J18, J26 | `chapter_1.tex:5` | Begriff bei der ersten Nennung einführen: *Überlastungen von Betriebsmitteln, also Leitungen und Transformatoren*. Zeile 60 bleibt dann verständlich. | ±0 | |
| J10 | `chapter_1.tex:23` | *eine Überlastung eines Betriebsmittels ab*. Setzt J18 voraus. | ±0 | |
| J8 | `chapter_1.tex:19` | Satz in zwei trennen, Stilregel 17. Die EIV-Erklärung mit *also* wird eigener Satz. | ±0 | |
| J12 | `chapter_1.tex:33` | Verweis auf die Hälfte beziehen, die die Abbildung trägt: *Der Engpassmanagementbedarf ist hoch, wie Abbildung 1.1 mit dem jährlichen Maßnahmenvolumen zeigt, und von wenigen Wetterlagen geprägt.* | ±0 | |
| L5, L6, J15 | `chapter_1.tex:53` | Wiederholung auflösen, ohne zu verschieben: In Zeile 53 den Dezember 2024 und die Quelle streichen, der Satz lautet dann wie im Build vom 21.09.2026, *denn einzelne Wetterlagen prägen die Kosten eines Jahres stärker als die Jahresmenge*. Zeile 36 bleibt mit Beleg. | ±0 | |
| L7 | `chapter_1.tex:62` | *Dauergrenze* durch den Begriff des Vorsatzes ersetzen: *unter der dauerhaft zulässigen Belastung*. | ±0 | |
| L9 | `chapter_1.tex:69` | Satz am *und* trennen. | ±0 | |
| L10 | `chapter_1.tex:94` | *mit dem präventiven Redispatch konkurrenzfähig ist*. | ±0 | |
| J23 | `chapter_2.tex:4` | Satz am *und* trennen. | ±0 | |
| J33 | `chapter_2.tex:112` | *mit der Netzzustandsschätzung (State Estimation), also …* | ±0 | |
| J35 | `chapter_2.tex:126` | Punkt nach dem Zitat, *wobei*-Satz wird eigener Satz: *Die Maßnahmen unterscheiden sich darin, wer …* | ±0 | |
| J36 | `chapter_2.tex:128` | *Nur bei Eingriffen in Erzeugung, Last und Speicherung sind Vorhaltung und Vergütung zu regeln, weshalb …* | ±0 | |
| J37 | `chapter_2.tex:142` | Satz am *und damit* trennen. | ±0 | |
| J38 | `chapter_2.tex:162` | *der Anlagenbestand mit seinem Zubau bis 2037*. | ±0 | |
| J39 | `chapter_2.tex:164` | Satz trennen: *Der Vergütungspfad betrifft nicht die Eignung der Technologie. Er betrifft die Frage, ob für sie eine Bemessungsgrundlage besteht, also eine Regel für die Berechnung des Ausgleichs.* | ±0 | |
| J42 | `chapter_2.tex:205` | *eine über Stunden anhaltende Bindung*. | ±0 | |
| J43 | `chapter_2.tex:206` | `\cite` auf TEN25 an den KuPilot-Satz, die Quelle ist in 2.1.4 schon zitiert und trägt die Aussage. | ±0 | |
| J44, J45 | `chapter_2.tex:211`, `213` | *stellt … Leistung in beide Richtungen bereit* und *kann ihre Leistung in dieser Richtung nicht weiter erhöhen*. | ±0 | |
| J46 | `chapter_2.tex:216` | *im Gegensatz zu konventionellen Kraftwerken*, weil der Satz schon mit *Anders als* beginnt. | ±0 | |
| L13 | `chapter_3.tex:440` | *eignet sich damit nicht als Maßstab*. | ±0 | |
| L14 | `chapter_4.tex:17` und Anhang F | *zwischen 0 und 200 €/(MW·h)*, an allen sechs Stellen gleich. Keine Regel in `CLAUDE.md`. | ±0 | |
| L17 | `chapter_4.tex:20` | *erhöht den Anreiz zur kurativen Reservierung*. | ±0 | |
| L11 | `chapter_3.tex:166` | Zahl an den Code angleichen, siehe Abschnitt 5. Wortlaut hängt an B unten. | ±0 | |

### 9.2 Stufe B

| Nr. | Stelle | Vorzulegen | Länge | Entscheidung |
|---|---|---|---|---|
| L11 | `chapter_3.tex:166` | Der Code setzt die Lücke auf null, also exakte Lösung bis zur Zulässigkeitstoleranz. Der Satz muss das sagen, und der Verfasser bestätigt, dass die ausgewerteten Läufe mit dieser Einstellung gerechnet sind. | ±0 | |
| L8 | `chapter_1.tex:63` | Halbsatz, der *thermisch* auf das Betriebsmittel bezieht: *eine thermische Reserve der Leitungen und Transformatoren ungenutzt bleibt*. | ±0 | |
| J3, J9 | `chapter_1.tex:8` | Leichte Variante statt Verschieben der Definition: *Im bestehenden Engpassmanagement können nur wenige Erzeugungsanlagen so kurzfristig reagieren*. Der Begriff Redispatch fällt dann erst in Zeile 22 mit seiner Erklärung. | ±0 | |
| J5 | `chapter_1.tex:9` | *Ein Lösungsansatz ist die kurative Systemführung, die das Netz effizienter nutzt …* Behauptungsstärke nach Stilregel 11, der Folgesatz trägt die Hürden schon. | ±0 | |
| J24 | `chapter_2.tex:6` | *Zuletzt wird dargelegt, ob sich eine der bestehenden Vergütungslogiken …* Nimmt *prüfen* aus der Kapitelankündigung, 2.3.3 bleibt eine Prüfung. | ±0 | |
| J25 | `chapter_2.tex:3` bis `6` | Ein Satz zur Reihenfolge am Ende der Kapiteleinleitung: *Die Reihenfolge folgt dem Weg von der Maßnahme über den Markt zum Preis der Vorhaltung.* | +1 | |
| J29 | `chapter_2.tex:65` | Ein Satz zur Ursache, belegt mit INN21: steuerbare Kapazität fällt weg, die verbleibenden Anlagen laufen seltener und verlangen für ein Anfahren mehr. Geringes Gewicht, nur wenn die Länge es zulässt. | +1 | |
| J49 | `chapter_2.tex:242` | Den Abgrenzungssatz aus Kapitel 2 nehmen und in 3.2.1 zu den nicht abgebildeten Größen stellen, dort als Halbsatz. Kapitel 2 verliert eine Zeile, 3.2.1 gewinnt keine. | −1 | |

### 9.3 Stufe C, Empfehlung zurückstellen

| Nr. | Kommentar | Warum zurückstellen | Leichte Variante |
|---|---|---|---|
| C1, J20 | Einleitung kürzen, Erklärungen nach Kapitel 2 | Vier Absätze mit 672 Wörtern, Gegenposition des Betreuerdurchgangs vom 14.09.2026, Länge am 28.09.2026 bewusst gesetzt. | Allein die A-Stellen in Kapitel 1 oben, die die Begriffe an Ort und Stelle klären. Damit entfällt der Hauptgrund der Freunde, nämlich das Stolpern über Begriffe. |
| C2 | Längere Bildunterschriften | 43 Unterschriften, jede Ergänzung kostet Zeilen, und der Text neben der Abbildung erklärt sie schon. | Nur dort, wo auch der Betreuer fragt, nämlich die grauen Zahlen in Abbildung 4.7 bis 4.10 (N44). |
| J13 | 1.1 Absatz 3 umbauen, Mechanismus vor Menge vor Kosten | Absatzumbau im zweimal durchgesehenen Kapitel 1. | J12 oben stellt den Abbildungsverweis richtig, mehr nicht. |
| J32 | Begriffsabsatz in 2.1.2 als Liste oder Tabelle | Die Begriffsliste ist in `CLAUDE.md` Abschnitt 5 so verlangt, eine Tabelle kostet Platz. | Keine. |
| J48 | 2.1.4 nach Kapitel 3 | Die Anforderungen A1 bis A8 bauen auf den vier Hindernissen auf, Verschiebung zieht Kapitel 3 nach. | Keine. |
| L12 | Validierung nach Kapitel 4 | Am 13.09.2026 entschieden, siehe `archiv/STRUKTUR.md`. | Keine. |
| J31 | PSKW in der Mehrzahl | Erstnennung über `\ac`, Verzeichnis trägt den Singular, `\acp` ist nach `CLAUDE.md` ausgeschlossen. | Keine. |

### 9.4 Entfällt

- Lob: J11, J14, J19, J22, J27, J28, J30, J41, J47.
- Auskunft oder Hinweis ohne Auftrag: J1, J6, J7, J50.
- Markierung ohne Text, Anstoß nicht erkennbar: J16, J17.
- Regelkonflikt, nur mit Regeländerung: J21, J34 (*nämlich*, Stilregel 16),
  J40 (*allein*, Konstanz nach Stilregel 14), L4 (*prognostiziert* gegen
  Stilregel 13, Geschmack).
- Beim Betreuer bereits enthalten und dort zu entscheiden: L15 (C1 dort),
  L16 (N9 dort).

---

## 10 Umgesetzt am 07.10.2026

Freigabe des Verfassers vom 07.10.2026 für Stufe A, dazu L11 und J49 aus
Stufe B. Prüfsuite ohne Befund, Build geprüft: 129 Seiten, Kapitelanfänge
1, 6, 30, 49, 65, 77 und Literaturverzeichnis 81 wie im Stand `54048c6`.

| Nr. | Datei | Alt | Neu |
|---|---|---|---|
| J18, J26 | `chapter_1.tex:5` | Überlastungen von Leitungen und Transformatoren | Überlastungen von Betriebsmitteln, also von Leitungen und Transformatoren |
| J2 | `chapter_1.tex:5` | Mengen | Energiemengen |
| J4 | `chapter_1.tex:8` | Anlagen | Erzeugungsanlagen |
| J8 | `chapter_1.tex:19` | ein Satz mit Doppelpunkt, Einschub und Relativsatz | zwei Sätze: *liegt die Fahrplanbildung bei den Einsatzverantwortlichen (EIV), also den Marktrollen, die den Einsatz einer Anlage im Betrieb verantworten. Die EIV bestimmen die Erzeugungs- und Verbrauchsfahrpläne selbst und melden sie dem Netzbetreiber.* |
| J10 | `chapter_1.tex:24` | eine Überlastung | die Überlastung eines Betriebsmittels |
| J12 | `chapter_1.tex:34` | Verweis am Satzende | Verweis nach *hoch*, Wetterlagen danach |
| L5, L6, J15 | `chapter_1.tex:54` | *wie die Windfront im Dezember 2024* mit Zitat | gestrichen, Satz ohne Beleg wie am 21.09.2026 |
| L7 | `chapter_1.tex:63` | Dauergrenze | dauerhaft zulässigen Belastung |
| L9 | `chapter_1.tex:70` | ein Satz | zwei Sätze am *und* |
| L10 | `chapter_1.tex:95` | mithält | gegenüber dem präventiven Redispatch konkurrenzfähig ist |
| J23 | `chapter_2.tex:4` | ein Satz | zwei Sätze am *und* |
| J33 | `chapter_2.tex:113` | State Estimation | Netzzustandsschätzung (State Estimation) |
| J35 | `chapter_2.tex:127` | *, wobei sich die Maßnahmen …* | Punkt nach dem Zitat, eigener Satz |
| J36 | `chapter_2.tex:129` | stellt sich die Frage nach Vorhaltung und Vergütung | sind Vorhaltung und Vergütung zu regeln |
| J37 | `chapter_2.tex:143` | ein Satz | zwei Sätze am *und damit* |
| J38 | `chapter_2.tex:163` | mit seiner Entwicklung | mit seinem Zubau bis 2037 |
| J39 | `chapter_2.tex:165` | *, also eine Regel, nach der …* | eigener Satz *Eine Bemessungsgrundlage ist eine Regel …* |
| J42 | `chapter_2.tex:206` | reichende | anhaltende |
| J44 | `chapter_2.tex:212` | stellt … in beide Richtungen. | stellt … Leistung in beide Richtungen bereit. |
| J45 | `chapter_2.tex:214` | nicht weiter stellen | ihre Leistung in dieser Richtung nicht weiter erhöhen |
| J46 | `chapter_2.tex:217` | anders als konventionelle Kraftwerke | im Gegensatz zu konventionellen Kraftwerken |
| J49 | `chapter_2.tex:242` → `chapter_3.tex:175` | Satz in 2.1.4 | gestrichen, in 3.2.1 neu: *Ebenso bleibt die Ausgestaltung der Redundanz in der Wirkungskette aus Abschnitt 2.1.4 außer Betracht.* |
| L11 | `chapter_3.tex:167` | Optimalitätslücke von 0,01 Prozent | Optimalitätslücke von null, also bis zum Nachweis der Optimalität |
| L13 | `chapter_3.tex:441` | taugt | eignet sich |
| L14 | `chapter_4.tex:17`, Anhang F fünfmal | null | 0 |
| L17 | `chapter_4.tex:20` | lohnender | attraktiver. Die längere Fassung *erhöht den Anreiz des Betreibers* schob eine Abbildung und kostete in Kapitel 4 eine Seite, deshalb verworfen. |
| L19 | `chapter_6.tex:34`, `abstract.tex:41` | zwei Fünftel | 40 Prozent |

Nicht umgesetzt, obwohl in Stufe A:

- **L1**, Abkürzungen in der Kurzfassung ausschreiben. Am 07.10.2026 nach
  Freigabe doch gesetzt: *Batteriespeichersystem (BESS)*, *Primärregelleistung
  (FCR)* und *Sekundärregelleistung (aFRR)*. Dafür gestrichen, weil die
  Kurzfassung sonst um eine Zeile auf zwei Seiten lief: *Die Einplanung hängt
  deshalb an der Zeit ebenso wie am Engpassmuster im Netz.* Nicht wieder
  aufzunehmen. Kurzfassung wieder eine Seite, Build mit 129 Seiten geprüft.
- **J43**, Beleg für den KuPilot-Satz. Die Pressemitteilung ist ein Scan ohne
  Textebene, und die Begrenzung auf eine Stunde ist ein Hinweis des Betreuers,
  nicht Inhalt der Mitteilung. So im Protokoll festgehalten, Zeile 1266. Ein
  Zitat trüge die Aussage nicht, Regel aus `CLAUDE.md` Abschnitt 2.

Offen aus Stufe B, Wortlaut in Abschnitt 9.2: L8, J3/J9, J5, J24, J25, J29.
