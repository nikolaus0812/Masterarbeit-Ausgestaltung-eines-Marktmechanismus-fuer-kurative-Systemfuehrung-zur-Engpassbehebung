# Auftrag an das Analyse-Repository: Abbildungsstil vereinheitlichen

**Stand 22.09.2026.** Der Abschnitt *Der Text zum Kopieren* ist zum
Hineinkopieren in den Chat des Analyse-Repositorys gedacht. Anlass ist eine
Beobachtung des Verfassers, dass die Diagramme untereinander und gegenüber dem
Satzbild der Vorlage nicht einheitlich wirken und dass Abbildung 3.2 nicht
bündig mit dem Text steht. Die Prüfung bestätigt beides.

---

## Der Text zum Kopieren

Alle 28 eingebundenen Abbildungen sind auf Schriftfamilie, Schriftgröße und
Breite geprüft. Gemessen wurde die **wirksame** Größe im gesetzten Dokument,
also die Schriftgröße in der Datei mal dem Verhältnis aus gesetzter Breite und
Dateibreite.

**Die Breiten stimmen.** Die Dateien sind 453,5 pt breit, und das sind exakt
die 455,244 pt Textbreite der Arbeit, weil matplotlib mit 72 und TeX mit 72,27
Punkt je Zoll rechnet. Beim Einbinden mit `width=\textwidth` passt es physisch
1 : 1. Daran ist nichts zu ändern.

**17 Abbildungen sind die Referenz:** NimbusSanL, 8,00 pt Grundbeschriftung,
9,00 pt für Achsentitel und Feldtitel, volle Breite. Vier Gruppen weichen ab.

### 1 Die Sollvorgabe

Das Dokument ist KOMA-Script `scrbook`, Grundschrift 11 pt, serifenlos über
`\usepackage{helvet}` mit `\familydefault=\sfdefault`. Im PDF erscheint sie als
**NimbusSanL**, der freien Helvetica-Entsprechung von URW. Die Mathematik der
Arbeit läuft in Computer Modern; CM-Schnitte in Abbildungen mit Formelsatz
sind deshalb **richtig** und kein Befund.

| Merkmal | Soll |
|---|---|
| Schriftfamilie | **NimbusSanL**, nicht DejaVuSans |
| Grundbeschriftung (Ticks, Legende) | **8,0 pt** wirksam im Satz |
| Achsen- und Feldtitel | **9,0 pt** wirksam im Satz |
| Dateibreite | 453,5 pt, entspricht der vollen Textbreite |
| Einbindung | `width=\textwidth`, keine Stauchung |

In der Datei entspricht das 7,97 pt und 8,97 pt, weil TeX beim Einbinden um
72,27/72 hochskaliert. Wer über `text.usetex=True` oder das pgf-Backend setzt,
bekommt diese Werte automatisch — genau das tun die 17 richtigen Abbildungen.

### 2 Vier Abbildungen tragen die falsche Schriftfamilie

Sie sind in **DejaVuSans** gesetzt, also matplotlibs Voreinstellung. Die Größen
stimmen bei den ersten drei, allein die Familie weicht ab. Nebeneinander im
Dokument fällt das auf.

| Datei | Ziel | wirksam | Befund |
|---|---|---|---|
| `validierung_cross.pdf` | Kapitel 3 | 8,03 / 9,03 pt | nur Familie |
| `jahreslauf_reservierungspreis_redispatch_2025_median.pdf` | Kapitel 4 | 8,03 / 9,03 pt | nur Familie |
| `jahreslauf_reservierungspreis_redispatch_2025_mittel.pdf` | Kapitel 4 | 8,03 / 9,03 pt | nur Familie |
| `validierung_einzelmarkt.pdf` | Anhang | **7,03 / 8,03 pt** | Familie **und** eine Stufe zu klein |

### 3 Eine Abbildung wird im Satz gestaucht

`tatl_berechnung.pdf` (Kapitel 2) wird in voller Breite geliefert, aber mit
`width=0.72\textwidth` eingebunden. Die Schrift schrumpft dadurch mit:

| | Datei | wirksam im Satz |
|---|---|---|
| Grundbeschriftung | 7,97 pt | **5,76 pt** |
| größere Beschriftung | 8,97 pt | **6,48 pt** |

5,8 pt liegen deutlich unter der Referenz und an der Grenze der Lesbarkeit.
**Bitte flacher neu zeichnen**, also volle Breite von 453,5 pt bei geringerer
Höhe. Heute ist die Datei 453,5 mal 208,6 pt; damit der Platzbedarf im Satz
gleich bleibt, müsste sie auf etwa 453,5 mal 150 pt. Die Schriftfassung stellt
die Einbindung dann auf `width=\textwidth` um.

### 4 Abbildung 3.2 läuft nicht über die volle Textbreite

`reservierungspreis_bisektion.pdf` wird **schmal geliefert**, nämlich 371,9 pt
statt 453,5, und mit `width=0.82\textwidth` eingebunden. Das ist 1 : 1, die
Schrift ist mit 8,00 pt also **korrekt** — anders als bei Abschnitt 3 liegt
hier kein Schriftproblem vor.

Der Befund ist rein optisch: Die Abbildung steht als einzige im laufenden Text
nicht bündig mit dem Satzspiegel, und das fällt dem Leser auf. Sie war am
21.09.2026 bewusst auf 82 Prozent gebracht worden, damit unter ihr noch Text
steht.

**Bitte auch diese flacher und in voller Breite neu zeichnen**, heute 371,9 mal
275,2 pt, künftig 453,5 pt breit bei etwa 225 pt Höhe. Dann steht sie bündig,
behält ihre 8 pt und lässt weiterhin Text unter sich. Eine Nebensache dazu: die
größte Beschriftung liegt dort bei 10,0 pt statt 9,0 pt.

### 5 Fünf Abbildungen liegen eine Stufe zu klein

| Datei | wirksam | Soll |
|---|---|---|
| `dispatch_festpreis_2025-02-11_p5.pdf` | 7,00 / 9,00 pt | 8,0 / 9,0 |
| `dispatch_preisgitter_2025-02-11.pdf` und drei weitere Tage | 6,00 / 7,00 pt | 8,0 / 9,0 |

Bei den vier Preisgitterseiten mit je zehn Kacheln ist das nachvollziehbar und
bleibt eurer Entscheidung überlassen; falls es ohne Gedränge geht, wären auch
dort 8 pt schöner. Bei `dispatch_festpreis` spricht nichts gegen 8 pt.

### 6 Bitte in die Anweisung aufnehmen

Damit die Vorgabe bei künftigen Lieferungen nicht wieder auseinanderläuft,
bitte in `ANWEISUNG_LIEFERUNG_ABBILDUNGEN.md` einen festen Abschnitt mit der
Tabelle aus Abschnitt 1 aufnehmen. `AUFBAU_KAPITEL_4.md` nennt unter den
durchgehenden Regeln bereits Legende, Achsen nach DIN 461, Dezimalkomma und
Textbreite — Schriftfamilie und Schriftgröße fehlen dort, und genau daran ist
es auseinandergelaufen.

Zwei Punkte gehören ausdrücklich dazu:

1. **Keine Abbildung wird im Satz gestaucht.** Passt sie nicht, wird sie
   flacher gezeichnet und nicht kleiner gesetzt.
2. **Keine Abbildung wird schmaler als die Textbreite geliefert**, außer der
   Verfasser verlangt es für eine bestimmte Stelle.

---

## Was die Schriftfassung selbst tut

Nichts, bis die neuen Dateien vorliegen. Die Einbindungen mit
`width=0.72\textwidth` und `width=0.82\textwidth` bleiben so lange stehen, weil
ein bloßes Hochsetzen auf `\textwidth` die Seitenlage verschiebt, ohne das
Problem an der Wurzel zu lösen. Sobald die flacheren Fassungen da sind, wird
auf `width=\textwidth` umgestellt und die Seitenlage geprüft.

## Wie geprüft wurde

Alle eingebundenen Abbildungen mit `pdffonts` auf die eingebetteten Schriften
und mit `pdfinfo` auf die Seitengröße gelesen. Die Schriftgrößen stammen aus
den `Tf`-Operatoren der Inhaltsströme und sind mit dem Verhältnis aus gesetzter
Breite und Dateibreite verrechnet, sodass die Tabellen die **wirksame** Größe
im Dokument nennen. Die Textbreite von 455,244 pt stammt aus einem eigenen
LaTeX-Lauf gegen `extras/header.tex`. Auskommentierte Einbindungen und die
Logos der Titelseite sind ausgenommen.
