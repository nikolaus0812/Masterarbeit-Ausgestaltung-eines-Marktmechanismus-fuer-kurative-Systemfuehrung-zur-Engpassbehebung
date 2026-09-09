# Workflow für das Ausformulieren der Kapitel

Stand 07.09.2026. Gilt für die Kapitel 3 bis 6 und für den Anhang. Er löst die
bisherige Regelung aus dem Übergabepapier nicht ab, sondern setzt sie um.

---

## 1 Die Arbeitseinheit ist ein Unterabschnitt

Nicht ein Kapitel, nicht ein Absatz, nicht eine Stichpunktliste. Ein
Unterabschnitt umfasst nach der jetzigen Planung zwischen einer halben und fünf
Seiten und trägt genau eine Aufgabe, die sich in einem Satz benennen lässt.

Drei Gründe. Erstens entspricht der Zuschnitt den vorhandenen Stichpunktlisten,
sodass beim Ausformulieren nichts neu sortiert werden muss. Zweitens bleibt der
Prüfaufwand je Runde bei einer Seite Lesen und nicht bei zwanzig. Drittens
bleibt bei einem Rückbau nur eine Einheit betroffen.

Ausnahmen sind die Einleitungen zu Abschnitten mit zwei bis vier Sätzen. Sie
werden zusammen mit dem ersten Unterabschnitt geliefert, weil sie allein zu
klein sind.

---

## 2 Der Zyklus, sechs Schritte

**Schritt 1, Freigabe.** Der Verfasser benennt den Unterabschnitt und übergibt
den Freigabezettel aus Abschnitt 4. Ohne Freigabe entsteht kein Fließtext.

**Schritt 2, Vorlage prüfen.** Claude liest die Stichpunkte, prüft die Belege
gegen das vorhandene Material, meldet Lücken, Widersprüche zu den Kapiteln 1 und
2 und offene Entscheidungen. Ergibt sich dabei, dass eine Vorentscheidung fehlt,
endet der Zyklus hier und geht mit der Entscheidungsfrage zurück.

**Schritt 3, Rohtext.** Claude schreibt den Fließtext für genau diesen
Unterabschnitt, setzt ihn in die Datei, lässt alle Kommentare und Marken
unberührt und liefert die vollständige Datei zurück. Dazu kommen die beiden
Zettel aus Abschnitt 5.

**Schritt 4, Prüfung.** `pruefen.py` läuft über die geänderte Datei. Befunde
werden vor der Übergabe behoben, nicht danach.

**Schritt 5, Durchsicht.** Der Verfasser liest das gerenderte PDF, nicht den
Quelltext. Rückmeldungen erfolgen satzweise oder absatzweise, in der bekannten
knappen Form. Eine Runde Korrektur gehört zum Zyklus, mehr als zwei Runden sind
ein Zeichen dafür, dass die Vorlage in Schritt 1 zu dünn war.

**Schritt 6, Protokoll.** Claude schreibt den Nachtrag für
`ENTSCHEIDUNGSPROTOKOLL.md`, mit den getroffenen Entscheidungen, den
eigenständigen Argumenten und den offen gebliebenen Punkten. Erst danach gilt
der Unterabschnitt als abgeschlossen und der nächste beginnt.

---

## 3 Dateihoheit, die wichtigste Regel

Zu jedem Zeitpunkt hat genau eine Seite die Datei. Entweder der Verfasser
arbeitet in Overleaf, oder Claude arbeitet an der hochgeladenen Fassung. Beides
gleichzeitig führt dazu, dass eine der beiden Fassungen verloren geht, und der
Verlust fällt erst zwei Sitzungen später auf.

Praktisch heißt das:

- Vor jeder Sitzung lädt der Verfasser die **aktuelle** Datei hoch, auch wenn er
  seit der letzten Lieferung nur eine Zeile geändert hat.
- Claude liefert immer die **vollständige** Datei zurück, nie ein Fragment, es
  sei denn, der Verfasser verlangt ausdrücklich einen Ausschnitt zum Einfügen.
- Während Claude arbeitet, ändert der Verfasser die Datei nicht.
- Nach der Übernahme in Overleaf ist die Overleaf-Fassung die gültige.

Für den Fall, dass es doch einmal auseinanderläuft, liefert Claude auf Zuruf
eine Liste der geänderten Stellen, sodass sich der Unterschied von Hand
zusammenführen lässt.

---

## 4 Freigabezettel, was der Verfasser liefert

Kurz halten, fünf Zeilen genügen. Vorlage:

```
Abschnitt:      3.2, Entwurf des kurativen Marktprodukts
Umfang:         5 Seiten
Stichpunkte:    alle, außer dem zur Pönale
Entscheidungen: E1 endogen, E3 Streichung
Nicht sagen:    keine Zahl zur Pönalehöhe, keine Obergrenze des Preises
```

Die Zeile *Nicht sagen* ist die wirksamste. Sie verhindert genau die
Grenzüberschreitungen, die in den Kapiteln 1 und 2 mehrfach zurückgenommen
werden mussten, nämlich vorweggenommene Ergebnisse, überdehnte Behauptungen und
Aussagen ohne Beleg.

Wenn der Verfasser eigene Formulierungen vorgibt, kennzeichnet er sie als
wörtlich zu übernehmen. Alles andere behandelt Claude als Inhaltsvorgabe.

---

## 5 Lieferung, was Claude zurückgibt

**Die Datei.** Vollständig, mit unverändertem Zeilenende und unveränderter
Kodierung, alle Kommentare erhalten. Ersetzte Formulierungen werden nicht
gelöscht, sondern als zurückgenommen im Kommentar vermerkt, damit eine spätere
Sitzung sie nicht wieder einführt.

**Der Belegzettel.** Für jeden geschriebenen Absatz eine Zeile mit der Quelle
oder mit dem Vermerk, dass die Aussage Mechanismus, eigene Ableitung oder
unbelegt ist. Unbelegte Aussagen stehen nicht im Text, ohne dass der Verfasser
sie gesehen hat.

**Der Argumentzettel.** Jedes Argument, das nicht aus den Stichpunkten des
Verfassers stammt, wird einzeln aufgeführt und als eigenständiges Argument
gekennzeichnet. Der Verfasser prüft es, bevor es stehen bleibt. Diese Regel gilt
seit dem 02.09.2026 und hat sich bewährt, sie wird hier nur festgeschrieben.

---

## 6 Was ohne Rückfrage geschieht und was nicht

Ohne Rückfrage: Belege prüfen, Rechnungen nachvollziehen, Widersprüche melden,
Terminologie und Einheiten kontrollieren, Stichpunkte strukturieren, Lücken
benennen, die Prüfsuite laufen lassen, Kommentare aktualisieren.

Nur auf Aufforderung: Absätze schreiben, Formulierungen vorschlagen, Gliederung
ändern, Text in eine Kapiteldatei einfügen.

Nie: Kommentare oder TODO-Marken stillschweigend löschen, eine getroffene
Vorentscheidung umkehren, eine Zahl setzen, die nicht aus dem Material oder aus
einer eigenen Rechnung stammt.

---

## 7 Prüfung

`pruefen.py` läuft über eine oder mehrere Dateien und prüft Zeilenenden, Stil im
Fließtext, Klammer- und Dollarbilanz, Umgebungen, doppelte Leerzeilen, gesperrte
Begriffe, Akronympflicht, doppelte Marken, Zitatschlüssel gegen `literature.bib`
und Verweise ohne Marke.

```
python pruefen.py chapter_3.tex
python pruefen.py --bib literature.bib "chapter_*.tex" attachment.tex
```

Der Rückgabewert ist ungleich null, sobald ein Befund vorliegt, sodass sich das
Skript in einen Commit-Hook hängen lässt. Die Stilprüfung überspringt
Kommentare, Listenpunkte, Tabellenzeilen und Bildunterschriften, weil dort
Doppelpunkte und Gedankenstriche zulässig sind.

Was das Skript nicht kann und weiterhin von Hand geschieht, ist die inhaltliche
Belegprüfung, die Kontrolle der Behauptungsstärke und die Frage, ob ein Absatz
ein Ergebnis vorwegnimmt.

---

## 8 Reihenfolge und Zeit

Bis zur Abgabe am 15.10.2026 bleiben fünf Wochen und drei Tage. Zwei Dinge
liegen auf dem kritischen Pfad und sollten diese Woche fallen.

**E1 blockiert alles.** Die Entscheidung über die exogene oder endogene Bindung
bestimmt die Gleichungen in 3.3.3, den Umfang von 3.3.2, die
Sensitivitätsliste in 4.4 und die Begründung für den Verzicht auf Dualvariablen.
Solange sie offen ist, lässt sich weder 3.3 schreiben noch das Modell fertig
rechnen.

**Die Rechenläufe blockieren Kapitel 4.** Kapitel 4 lässt sich nicht
ausformulieren, bevor Ergebnisse vorliegen, und die Ergebnisse hängen an E1 bis
E3. Der Modelllauf sollte deshalb parallel zum Ausformulieren von 3.2 starten
und nicht danach.

Vorschlag für die Staffelung:

| Zeitraum | Schreiben | Parallel |
|---|---|---|
| 08.09. bis 14.09. | E1 bis E3 entscheiden, 3.1 abschließen, 3.2 | Modell nach E1 umbauen |
| 15.09. bis 21.09. | 3.3 und 3.4 | Rechenläufe Q4 2025 |
| 22.09. bis 28.09. | Kapitel 4 | Abbildungen erzeugen |
| 29.09. bis 05.10. | Kapitel 5 | Folgeänderungen aus dem Protokoll |
| 06.10. bis 12.10. | Kapitel 6, Verzeichnisse, Gesamtdurchsicht | Literaturdatei bereinigen |
| 13.10. bis 15.10. | Puffer und Abgabe | |

Die Woche für Kapitel 5 ist knapp bemessen, weil dort die Diskussion, die
adverse Selektion, der Gaming-Block D1 bis D5 und die kritische Würdigung der
Modellannahmen zusammenkommen. Wenn Zeit fehlt, wird sie dort fehlen, nicht in
Kapitel 3.

---

## 9 Wiederkehrende Fehlerbilder

Die Durchsichten der Kapitel 1 und 2 haben fünf Muster hervorgebracht. Der
Zyklus fängt sie an bestimmten Stellen ab.

**Ergebnisse werden vorweggenommen.** Abgefangen durch die Zeile *Nicht sagen*
im Freigabezettel und durch die Frage in Schritt 5, ob der Absatz eine Aussage
trifft, die erst ein späteres Kapitel belegt.

**Eine Quelle trägt weniger, als der Satz behauptet.** Abgefangen durch den
Belegzettel, der jede Zuordnung sichtbar macht, statt sie im Fließtext zu
verstecken.

**Ein Begriff wird eingeführt, nachdem er zum ersten Mal verwendet wurde.**
Abgefangen durch die Terminologieprüfung in Schritt 2, die die erste Verwendung
über alle Kapitel sucht.

**Eine Formulierung kehrt zurück, die schon einmal zurückgenommen war.**
Abgefangen dadurch, dass Rücknahmen als Kommentar in der Datei stehen und nicht
nur im Protokoll.

**Zwei Stellen sagen dasselbe.** Abgefangen in Schritt 2, weil die Prüfung der
Vorlage die Nachbarabschnitte mitliest.
