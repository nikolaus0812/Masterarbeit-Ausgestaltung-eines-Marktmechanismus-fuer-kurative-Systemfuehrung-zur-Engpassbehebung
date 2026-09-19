# Kontrollauftrag an Fable, 17.09.2026

Auftrag des Verfassers: eine unabhängige Kontrolle des ganzen Dokuments,
besonders auf kompakte Formulierung mit einem roten Faden in jedem Absatz und
auf inhaltliche Fehler. Der Auftrag ist eine Prüfung und keine Umsetzung.

---

## 1 Gegenstand

Geprüft wird die gebaute Fassung `main.pdf` mit 88 Seiten, Stand des Commits
`3849d22`, und der zugehörige Quelltext:

```
chapters/chapter_1.tex        Einleitung
chapters/chapter_2.tex        Grundlagen
chapters/chapter_3.tex        Marktmechanismus und Modellierung
extras/attachment.tex         Anhang A, modifizierter Weber-Ansatz
extras/attachment_thermik.tex Anhang B, zulässige Überlastdauer
extras/attachment_modell.tex  Anhang C, vollständiges Optimierungsproblem
extras/attachment_ablauf.tex  Anhang D, Ablauf der Preisbestimmung
extras/attachment_validierung.tex Anhang E, Validierung je Markt
extras/attachment_dispatch.tex Anhang F, Fahrplan ohne die Mindestgröße
```

Die Kapitel 4 bis 6 sind in `main.tex` auskommentiert und stehen nicht im
Dokument. Sie sind nicht Gegenstand der Prüfung. Wo ein Satz ein Ergebnis
vorwegnimmt, das erst Kapitel 4 oder 5 tragen kann, ist das dagegen ein Befund.

`chapter_3.tex` ist seit dem 17.09.2026 kommentarfrei. Der frühere
Kommentarbestand steht in `archiv/KOMMENTARBESTAND_KAP3.md`, die offenen Punkte
daraus als Liste G in `DURCHSICHT_KAP1_3.md`.

## 2 Maßstäbe

Verbindlich sind:

- `CLAUDE.md` Abschnitt 4, Stilregeln 1 bis 17, insbesondere ein Absatz mit
  einer Kernaussage, These mit angebundener Begründung, Satzlänge aus Hauptsatz
  und höchstens einem Nebensatz, keine Gedankenstriche und keine Semikola, keine
  Pronominalisierung über die Satzgrenze.
- `CLAUDE.md` Abschnitt 5, gesperrte und verbindliche Begriffe sowie die Liste
  der Begriffe, die vor der ersten Verwendung zu definieren sind.
- `CLAUDE.md` Abschnitt 7, die getroffenen Entscheidungen. Ein Satz, der einer
  davon widerspricht, ist ein Befund.
- `CLAUDE.md` Abschnitt 8, Einheiten und Formelzeichen. Euro je Megawatt und
  Stunde ist nicht Euro je Megawattstunde.
- `WORKFLOW.md` Abschnitt 4, Fremdleser-Prüfung.

## 3 Schwerpunkte

### 3.1 Kompakte Formulierung, roter Faden in jedem Absatz

Für jeden Absatz des Dokuments:

1. Trägt der Absatz eine Kernaussage, und steht sie im ersten Satz?
2. Hängt jede Begründung an ihrer These, oder folgen unverbundene
   Erläuterungssätze?
3. Knüpft der erste Satz erkennbar an den vorigen Absatz an?
4. Endet der Absatz mit der Konsequenz, oder bricht er ab?
5. Welche Sätze sagen nichts Neues? Benenne jeden Streichkandidaten mit Zitat
   und sage, welcher andere Satz die Aussage schon trägt.
6. Welche Sätze lassen sich ohne Verlust zu einem verbinden oder um mehr als
   ein Drittel kürzen? Gib die gekürzte Fassung in einem Satz an.

### 3.2 Inhaltliche Fehler

1. Zahlen, die sich widersprechen, innerhalb eines Abschnitts und über die
   Kapitel hinweg.
2. Einheiten, die nicht zur Größe passen, und Größen ohne Einheit.
3. Aussagen, die eine Quelle tragen, die sie nicht deckt, und absolute
   Feststellungen ohne Quelle.
4. Fachliche Fehler, besonders zum N-1-Kriterium, zum Grenzwertkonzept, zu PATL
   und TATL, zur kurativen Systemführung, zu den Regelleistungsmärkten und zum
   Intraday-Handel.
5. Begriffe, die im Dokument uneinheitlich verwendet werden oder vor ihrer
   Definition stehen.
6. Verweise auf Abbildungen, Tabellen und Gleichungen, die auf die falsche
   Stelle zeigen oder deren Aussage nicht tragen.

## 4 Form des Berichts

Schreibe den Bericht nach `KONTROLLE_FABLE.md` im Wurzelverzeichnis. Keine
andere Datei wird angefasst, insbesondere keine `.tex`-Datei.

Aufbau:

1. **Zusammenfassung**, höchstens zehn Zeilen, mit der Zahl der Befunde je Art
   und den drei gewichtigsten Befunden.
2. **Inhaltliche Befunde** als Tabelle mit den Spalten Nummer, Ort (Datei und
   Abschnitt, dazu die Seite im PDF), Zitat, Befund, Vorschlag in einem Satz,
   Gewicht (hoch, mittel, gering).
3. **Roter Faden und Kürzung** als Tabelle mit den Spalten Nummer, Ort, Befund
   nach den sechs Fragen aus 3.1, Vorschlag, erwartete Ersparnis in Zeilen.
4. **Streichkandidaten**, geordnet nach Ersparnis, mit dem Satz, der die Aussage
   schon trägt.
5. **Nicht geprüft oder nicht klärbar**, mit Angabe, warum.

Jeder Befund nennt seine Stelle so, dass sie eindeutig ist, also Dateiname und
die ersten Wörter des betroffenen Satzes.

## 5 Grenzen

- Ändere keine Datei außer `KONTROLLE_FABLE.md`.
- Erfinde keine Zahl und keine Quelle. Wenn eine Zahl nicht nachprüfbar ist,
  nenne sie als nicht klärbar.
- Führe keinen neuen Begriff ein. Ein Vorschlag verwendet die Begriffe aus
  `CLAUDE.md` Abschnitt 5.
- Kehre keine Entscheidung aus `CLAUDE.md` Abschnitt 7 um. Wenn eine
  Entscheidung inhaltlich fragwürdig erscheint, nenne sie als Befund mit
  Begründung, statt einen Gegenvorschlag zu schreiben.
- Bekannt und kein Befund sind drei undefinierte Verweise auf `ch:results`,
  `ch:discussion` und `ch:conc`, weil die Kapitel 4 bis 6 auskommentiert sind,
  sowie zwei Befunde der Prüfung 7 in `chapter_4.tex` und `chapter_5.tex`.
