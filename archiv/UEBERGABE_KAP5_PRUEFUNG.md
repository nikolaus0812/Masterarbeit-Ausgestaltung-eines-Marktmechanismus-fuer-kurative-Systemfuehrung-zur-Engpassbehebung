# Übergabe: Kontrollprüfung von Kapitel 5

**Angelegt am 26.09.2026** zum Abschluss der Schreibsitzung vom 25.09.2026.
Diese Datei ist der Prompt für den neuen Chat, der Kapitel 5 prüft. Der
Verfasser kopiert den Abschnitt „Prompt" unten in den neuen Chat.

---

## Prompt

Du prüfst Kapitel 5 der Masterarbeit, also `chapters/chapter_5.tex` mit dem
Titel *Diskussion*. Das Kapitel ist am 24. und 25.09.2026 geschrieben und
Absatz für Absatz mit dem Verfasser durchgegangen worden. Es ist inhaltlich
fertig bis auf vier Absätze in Abschnitt 5.5.

**Lies zuerst, in dieser Reihenfolge:** `CLAUDE.md`, `HANDOFF.md` Abschnitt
1.0, `WORKFLOW.md` Abschnitt 10. Das Entscheidungsprotokoll ist über
1,2 Millionen Zeichen groß und **nicht ganz zu lesen**; die Einträge zu
Kapitel 5 vom 24. und 25.09.2026 stehen am Ende des Abschnitts
`## chapter_5.tex`.

**Deine Aufgabe ist Prüfen, nicht Umschreiben.** Du legst Befunde vor und
änderst erst nach dem Wort des Verfassers. Er entscheidet jede Formulierung.

### Was beim Schreiben bindend war

- **Acht Sätze je Absatz.** Der Verfasser hat am 25.09.2026 zweimal
  verlangt, die Absätze länger zu fassen. Acht ist die Obergrenze nach
  Stilregel 1. Mehr Länge geht nur über mehr Absätze. Prüfe mit
  `python tools/absatzlaengen.py chapters/chapter_5.tex --nur-kurze`.
- **Fast keine Zahlen.** Die Diskussion trägt Erkenntnisse und
  Schlussfolgerungen. Wo eine Größenordnung nötig ist, steht sie verbal,
  etwa *um ein Sechstel* statt *um 17,0 Prozent*.
- **Ein Hauptsatz und höchstens ein Nebensatz**, Stilregel 17.
- **Keine strukturellen Vor- und Rückverweise**, Stilregel 15. Sachverweise
  auf Abschnitte mit `\ref` sind an wenigen Stellen geblieben, etwa auf das
  Indifferenzprinzip. Prüfe, ob sie dort tragen.
- **Keine Pronomen über die Satzgrenze**, Stilregel 5.
- **Gesperrte Verstärkungen:** entscheidend, wesentlich, signifikant,
  deutlich, erheblich. Ebenso *perfekt* ohne Maßstab, Stilregel 11.

### Stand der Abschnitte

| Abschnitt | Absätze | Stand |
|---|---|---|
| Kapiteleinleitung | 1 zu 7 Sätzen | **ein Satz fehlt** |
| 5.1 Anforderungen und ihre Umsetzung im Produkt | 11 zu je 8 | durchgegangen |
| 5.2 Modellierung und ihre Annahmen | 7 zu je 8 | durchgegangen |
| 5.3 Wirtschaftlichkeit und Wirksamkeit | 6 zu je 8 | durchgegangen |
| 5.4 Die Rolle der BESS | 6 zu je 8 | durchgegangen |
| 5.5 Umsetzung, systemweite Ausrollung und Forschungsbedarf | 7, davon 3 zu je 8 | **vier Absätze offen** |

Offen in 5.5 sind der geltende Rahmen mit sechs Sätzen, der Aufwand mit
sieben, die systemweite Ausrollung mit sechs und der Forschungsbedarf mit
sechs.

### Was der Verfasser bestätigen muss

Diese fünf Aussagen stammen aus Vorgaben des Verfassers, sind aber nicht
gerechnet und stehen in keinem Kapitel. Sie sind im Quelltext als
`EIGENSTAENDIGE ABLEITUNG` markiert. Lege sie ihm einzeln vor.

1. Der Zeitpunkt der Anweisung bestimmt die Kosten einer Redispatchmaßnahme
   mit. In 5.3, erster Absatz.
2. Ein Gebot für einige aneinander anschließende Stunden liegt unter dem
   ermittelten Wert. In 5.3, Absatz zum Zuschnitt des Produkts.
3. Der ÜNB verteilte die Kosten der Vorhaltung auf mehrere Verwendungen.
   In 5.4, Absatz zur Mehrfachnutzung.
4. Ein zusätzliches Produkt mit längerem Zeitfenster übernähme die Ablösung.
   In 5.5, Absatz zur Ablösung.
5. Ein Gebotszonensplit senkte den Bedarf an Engpassmanagement, und der
   kurative Reservierungspreis hinge danach am Preisniveau der Zone.
   In 5.5, Absatz zum Marktrahmen.

### Was bewusst nicht gesetzt ist

Diese Aussagen hat der Verfasser genannt, sie sind aber nicht belegbar. Wenn
er sie haben will, braucht es eine Quelle oder eine Rechnung.

- **Die Regelleistung ist teuer.** Die Kapitel 1 bis 4 tragen keine Aussage
  zu den Kosten der Regelleistung. Belegbar wäre das aus
  `analysen/afrr_herbst_2025`, das wäre dann aber eine Zahl für Kapitel 4.
- **Das Niveau des kurativen Reservierungspreises liegt leicht über den
  Regelleistungspreisen.** Ein solcher Vergleich steht in keinem Kapitel.
  Der Text sagt stattdessen das Belegte aus Abschnitt 4.4, nämlich dass der
  Leistungspreis der aFRR das Niveau trägt.
- **Die kurative Vorhaltung ist von jeglichen Eingriffen ausgeschlossen.**
  Abschnitt 3.1.2 sagt allein, dass Fahrplanänderungen nach der letzten
  Vorschaurechnung die Vorhaltung nicht mehr aufheben.
- **Der Revenue-Index rechnet ebenfalls mit dem gemittelten
  Leistungspreis.** Abschnitt 3.3 sagt das nicht. Der Revenue-Index stammt
  zudem vom ISEA mit der enspired GmbH und nicht vom IAEW.

### Zwei inhaltliche Umkehrungen, die zu prüfen sind

1. **Der kurative Marktmechanismus kann an keine breit angelegte
   Beschaffungsform anschließen.** Bis zum 25.09.2026 stand dort das
   Gegenteil, gestützt auf den Begriff *kapazitätsbasierter Redispatch*.
   Dieser Begriff ist entfernt, weil er in keinem Kapitel definiert ist und
   im Kern die kurative Systemführung selbst wäre. Das Engpassmanagement
   kennt eine Vergütung der Bereithaltung mit einem Leistungspreis nach
   Abschnitt 2.1 allein in § 13c EnWG für systemrelevante Anlagen nach
   angezeigter Stilllegung. In 5.5, erster Absatz.
2. **Der kurative Marktmechanismus wird mit wachsendem Bestand an BESS nicht
   ohne Weiteres wettbewerbsfähiger.** Abschnitt 4.6.4 zeigt, dass der
   Markterlös um 17,0 Prozent nachgibt, die Zahlung bei vollständiger
   Verdrängung aber nur um 16,0 Prozent, sodass der Aufschlag von 23,3 auf
   24,8 Prozent steigt. Der Text sagt deshalb nur, dass der Markterlös
   absolut fällt und ein Betreiber nach weiteren Erlösquellen sucht, und
   nennt die Wettbewerbsfähigkeit als Bedingung für beide Seiten. In 5.4,
   letzter Absatz.

### Offene Arbeit

- **Der letzte Absatz von 5.5** ist mit dem Verfasser noch durchzugehen,
  ebenso die drei übrigen kurzen Absätze in 5.5 und die Kapiteleinleitung.
- **Ein Satz muss noch nach 5.5:** *Eine Vergütung der kurativen Vorhaltung
  verlangt eine eigene Struktur, zumal für die kurative Reservierung bislang
  kein Vergütungsrahmen besteht.* Er ist am 25.09.2026 aus 5.3 entfernt
  worden und gehört zum geltenden Rahmen in 5.5.

### Worauf du inhaltlich achten sollst

- **Dopplungen zwischen den Abschnitten.** Am 25.09.2026 sind mehrere
  gefunden worden, etwa der Erlösanteil der aFRR, der dreimal stand. Prüfe
  das systematisch, auch gegen die Kapitel 3 und 4.
- **Belege.** Jede absolute Feststellung trägt eine Quelle oder ist
  zurückhaltend formuliert. Beim Zusammenziehen von Absätzen ist ein Beleg
  verloren gegangen, nämlich `regelleistung_ausschreibungsdaten_2026` in
  5.2. Prüfe, ob die dortige Aussage zu den Gebotsstrategien ihn noch
  braucht.
- **Sachliche Fehler.** Am 25.09.2026 stand in 5.4, eine bilanziell
  ausgeglichene Vorhaltung sei an einem Netzknoten möglich. Das ist falsch,
  weil sich die Wirkung beider Richtungen dort aufhebt. Suche nach
  ähnlichen Fehlern.
- **Begriffe** nach CLAUDE.md Abschnitt 5. *Abrufdauer* heißt seit dem
  23.09.2026 *vorgehaltene Energie je Abruf*, *Sanktion* heißt *Pönale*,
  *Redispatchplanung* heißt seit dem 25.09.2026 *Planung des
  Engpassmanagements*.

### Prüfungen, die du fahren musst

```
python tools/pruefen.py --alle
python tools/pruefe_stil.py
python tools/absatzlaengen.py chapters/chapter_5.tex --nur-kurze
pdflatex main && biber main && pdflatex main && pdflatex main
```

Stand am 26.09.2026: 123 Seiten, `pruefen.py --alle` ohne Befund,
`pruefe_stil.py` ohne Verstoß in Kapitel 5, Biber ohne Warnung. Die drei
Doppelpunkt-Meldungen in `chapter_3.tex` sind Altbefunde, denn der
Doppelpunkt ist seit dem 14.09.2026 zulässig.

### Arbeitsweise

- **Ersetzungen über Python** mit `open(pfad, encoding='utf-8', newline='')`,
  nicht über sed. Die Kapiteldateien liegen mit CRLF.
- **Skripte mit dem Write-Werkzeug anlegen**, nicht als Bash-Heredoc. Ein
  Heredoc hat am 24.09.2026 Backslashes zerstört und Steuerzeichen in den
  Text geschrieben, die `pruefen.py` nicht findet. Jedes Skript prüft am
  Ende, dass keine Steuerzeichen außer CR und LF in der Datei stehen.
- **Ersetzter Fließtext wird nicht gelöscht**, sondern als Kommentar mit
  Datum und Grund über der neuen Fassung erhalten.
- **Nach jeder Anpassung den ganzen Absatz zeigen**, nicht nur den
  geänderten Satz. Vorgabe des Verfassers vom 24.09.2026, `WORKFLOW.md`
  Regel 8a.
- **Nicht pushen.** Du lieferst Änderungen zur Übernahme. Committen nur auf
  das Wort des Verfassers.
- **Subagenten nur nach Rückfrage**, mit Nennung von Zweck und Zahl.

---

## Hinweis zum Push

Acht Commits stehen beim Verfasser zum Push aus, beginnend mit `2fc1be7`
vom 24.09.2026. Für diesen Commit hat GitHub am 24.09.2026 mit einem
Internal Server Error geantwortet, Request ID
`8320:1105C9:74AA1:8229B:6AB53586`. Die Objekte wurden vollständig
übertragen, allein die Referenz ließ sich nicht setzen.
