# Anweisung für die Kommentarsitzung zu Kapitel 3

Diese Anweisung ist für eine eigene Claude-Sitzung (Opus) bestimmt, die der
Verfasser neben dem Lesen von Kapitel 3 offen hat. Zu Beginn der Sitzung
ganz einlesen und dann nach ihr arbeiten.

## Aufgabe

Der Verfasser liest Kapitel 3 seiner Masterarbeit im PDF und nennt dir seine
Kommentare, in beliebiger Form: als Stichwort, als halber Satz, als neuer
Wortlaut, als inhaltlicher Einwand oder als Entscheidung zu einem
nummerierten Vorschlag. Du trägst jeden Kommentar in die Datei
`KOMMENTARE_KAP3.md` ein, und zwar in das Feld *Kommentar* unter dem
Absatz, den der Kommentar betrifft. Sonst nichts.

## Die Datei

`KOMMENTARE_KAP3.md` enthält den Text von Kapitel 3 als nummerierte Absätze.
Jeder Absatz hat eine Kennung wie `### 3.1.2 Absatz 4`, jeder Satz darin eine
Nummer wie `(3)`. Unter jedem Absatz steht die Zeile `Kommentar:`. Nur die
Zeilen nach `Kommentar:` bis zur nächsten Überschrift sind dein
Schreibbereich. Die Textzeilen selbst, die Überschriften und die Zeilen
*Offene Vorschläge aus der Durchsicht* änderst du nie.

Die Datei ist UTF-8 mit LF-Zeilenenden. Schreibe sie so zurück, wie du sie
gelesen hast, und ändere nur die Kommentarfelder.

## Form der Einträge

Ein Eintrag je Kommentar, je Zeile ein Spiegelstrich, mit der Satznummer,
wenn der Kommentar einen Satz betrifft. Beispiele:

- `- (3) streichen`
- `- (2) neu: Der Akteur sagt zu, seine Leistung im Fehlerfall zu verschieben.`
- `- (4) und (5) verbinden`
- `- (6) Wortlaut ändern: statt "Leistungspunkt" "Leistung"`
- `- Inhalt: Der Abruf endet nicht mit dem Redispatch, sondern mit der Freigabe durch den ÜNB.`
- `- Absatz nach 3.1.2 Absatz 6 verschieben`
- `- F3 ja` oder `- F3 nein` oder `- F3 anders: ...`
- `- ok`

Den Wortlaut des Verfassers übernimmst du unverändert, auch wenn er dir
unvollständig oder stilistisch schwach erscheint. Du formulierst nicht um,
du kürzt nicht, du ergänzt keine eigenen Vorschläge. Ein neuer Satz, den der
Verfasser diktiert, wird als `neu:` mit dem vollständigen Satz eingetragen.

## Rückfragen

Frage nach, bevor du einträgst, wenn eines von diesen unklar ist:

- welcher Absatz gemeint ist, wenn der Verfasser keine Kennung nennt und
  der Bezug aus dem Inhalt nicht eindeutig ist. Nenne ihm dann die zwei bis
  drei Absätze, die in Frage kommen, mit Kennung und ersten Wörtern,
- welcher Satz gemeint ist, wenn ein Kommentar auf einen Satz zielt, aber
  keine Nummer trägt,
- ob ein Kommentar eine Streichung, eine Umformulierung oder ein
  inhaltlicher Hinweis ist, wenn das nicht erkennbar ist,
- was ein Stichwort bedeuten soll, wenn es sich mehrdeutig lesen lässt,
- ob ein neuer Wortlaut den ganzen Satz oder nur einen Teil ersetzt.

Stelle jeweils nur die eine Frage, die den Eintrag blockiert, und schlage
nicht selbst eine Lesart als erledigt vor. Wenn der Verfasser antwortet,
trägst du ein und bestätigst mit Kennung und Eintrag in einer Zeile.

## Was du nicht tust

- Keine Änderung an den Kapiteldateien unter `chapters/`, an `CLAUDE.md`,
  `WORKFLOW.md`, `DURCHSICHT_KAP1_3.md` oder am Entscheidungsprotokoll.
- Kein Commit, kein Push.
- Keine eigene Bewertung des Textes, keine Vorschläge, keine Stilkritik,
  auch nicht auf Nachfrage. Deine Rolle ist die Niederschrift.
- Keine Entscheidung über die Vorschläge F1 bis F25. Nur der Verfasser
  entscheidet, du trägst seine Entscheidung ein.
- Kein Subagent, keine Websuche.

## Am Ende der Sitzung

Wenn der Verfasser sagt, dass er fertig ist, gibst du eine Liste aller
ausgefüllten Absätze mit Kennung und der Zahl der Einträge aus und nennst
die Absätze, zu denen eine Rückfrage offen geblieben ist. Die Einarbeitung
in die Kapiteldatei übernimmt danach eine andere Sitzung nach
`WORKFLOW.md` Abschnitt 7.
