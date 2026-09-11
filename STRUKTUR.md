# Struktur und Zuordnung

Stand 11.09.2026, nach der Auflösung von 3.1.3.
Arbeitsdokument. Es ersetzt weder CLAUDE.md noch das Entscheidungsprotokoll.

**F** heißt ausformulierter Fließtext, **S** heißt Stichpunktgerüst, **T** heißt
teilweise.

---

## Die bindende Randbedingung

Gemessen am Build vom 11.09.2026, 79 Seiten, 0 Fehler.

| | | |
|---|---|---|
| Kapitel 1 | S. 1 bis 5 | 5 Seiten |
| Kapitel 2 | S. 6 bis 34 | 29 Seiten, Zielwert war 25 |
| Kapitel 3 | S. 35 bis 52 | 18 Seiten, Zielwert 14. Davon 3.1 fünf Seiten, 3.2 elf, 3.3 zwei |

Damit die Ergebnisse vor Seite 50 anfangen, darf Kapitel 3 höchstens 14 Seiten
umfassen. Mit 18 Seiten liegt es vier darüber. Der Zuwachs stammt aus 3.2, das mit
den Abbildungen und dem neuen 3.2.5 elf Seiten füllt. Kürzbar sind 3.2 und
Kapitel 2, das seinen eigenen Zielwert ebenfalls um vier Seiten überschreitet.

Die Kapitel 4 bis 6 sind in `main.tex` auskommentiert.

---

## Kapitel 3

| | | Ziel | Stand |
|---|---|---|---|
| | Kapiteleinleitung | 0,3 | F |
| **3.1** | **Anforderungen und Produkt** | **5** | |
| 3.1.1 | Anforderungskatalog, jeder Eintrag mit Erläuterung | 1,5 | F |
| | danach die Einordnung des Marktdesigns | 0,5 | F, sieben Sätze |
| 3.1.2 | Die kurative Reservierung | 3 | F |
| **3.2** | **Optimierung des Speicherbetriebs** | **7** | |
| | Einleitung mit Preis, Lücke und Aufgabe, aus dem aufgelösten 3.1.3 | 0,5 | F, sechs Sätze |
| 3.2.1 | Ansatz und Lösungsverfahren | 1 | S |
| 3.2.2 | Eingangsdaten | 1 | S |
| 3.2.3 | Zielfunktion und Variablen, mit der Tabelle der Produktparameter | 1,5 | S |
| 3.2.4 | Nebenbedingungen | 2 | S |
| 3.2.5 | Bestimmung des kurativen Reservierungspreises | | S, neu von der zweiten Sitzung |
| 3.2.6 | Systemgrenzen und Abgrenzungen | 1,5 | S |
| **3.3** | **Validierung des Modells** | **2** | S |

### 3.1.2 im Einzelnen

| Block | Stand |
|---|---|
| Einleitung | F, zwei Sätze |
| Die Zusage | F, zwei Absätze mit acht und sechs Sätzen |
| Abruf und Erfüllung | F, ein Absatz mit elf Sätzen |
| Präqualifikation | F, sieben Sätze |
| Ausschreibung und Gebot | F, acht Sätze |
| Zuschlag | F, fünf Sätze |
| Abschluss | entfallen, 3.1.2 endet mit dem Zuschlag |

### Das frühere 3.1.3, aufgelöst am 11.09.2026

| Block | Stichpunkte | jetzt |
|---|---|---|
| Warum der Preis | 3 | Einleitung von 3.2, geschrieben |
| Die Lücke | 1 | Einleitung von 3.2, geschrieben |
| Diskutierte Anpassungen des Marktdesigns, in zwei Gruppen | 5 | hinter dem Katalog in 3.1.1, geschrieben |
| Aufgabe der Arbeit | 2 | Einleitung von 3.2, geschrieben |
| Wahlweise, Brücke nach Kapitel 5 | 1 | entfallen, Frage bleibt Kapitel 5 |

---

## Entschieden am 11.09.2026

- **Kurative Reservierung** ist der Name des Produkts. Dazu gelten *Wirkung* und
  *Reaktionszeit* als Begriffe, und die Katalogsätze sind gekürzt.
- **Reservierungspreis endogen wie im Code**, also K1. Fünf Stichpunkte in 3.2
  tragen den Vermerk ZU AENDERN NACH K1 und sind gemeinsam neu zu fassen.
  CLAUDE.md §9 Entscheidung 2 ist überholt, Entscheidung 3 und 4 sind in der
  Begründung berührt.
- **Definition des Preises.** Gemeint ist der Preis, bei dem ein Akteur eine
  Stunde voll reserviert. CLAUDE.md §1 ist vom Verfasser nachzuziehen.
- **Basisfall.** 25 MW Mindestgröße, also MILP, beide Richtungen, Klasse zwei
  Minuten, Zeitscheibe eine Stunde, eine Megawattstunde je Megawatt. Die Stunden
  wählt das Modell. Das berührt die offenen Punkte zu LP oder MILP und zu den
  Dualvariablen.
- **Abrufdauer eine Stunde.** Im Code fehlt `"kur_t_res": 1.0` in `MARKET`. Alle
  bisherigen Ergebnisse beruhen auf einer Viertelstunde. Übernimmt der Verfasser
  mit der anderen Sitzung.
- **3.1.3 aufgelöst.** Preis, Lücke und Aufgabe öffnen 3.2, die Einordnung des
  Marktdesigns steht hinter dem Katalog. Der Einleitungssatz von 3.1 und der
  Kapitelüberblick in `chapter_1.tex` sind nachgezogen.
- **Entfallen.** Die Begründung der Klassen gegenüber InnoSys 2030, der Aufwand
  vor dem Zuschlag, die Kostenwälzung und der Schlusssatz von 3.1.2.

---

## Vorgemerkt, noch nicht im Text

1. **Ausschließlichkeit als Regel.** Steht in der Zusage nur als Beschreibung. 3.2
   setzt sie über die geteilte Anschlussleistung um.
2. **Wachstum des BESS-Bestands**, eigenes Argument des Verfassers, am Absatz zur
   Zusage vermerkt. Beleg fehlt über den Stand 2024 hinaus.
3. **Anlage 5 der Festlegung, Energieanteil eines Abrufs und Pönalehöhe** sind in
   3.2.6 vorgemerkt, bei den nicht modellierten Bestandteilen des Gebots.
4. **Ladezustandsband und A5.** Der Begriff setzt einen Speicher voraus.
5. **Entzug der Präqualifikation.** Die PQ-Bedingungen regeln ihn nicht, sie
   verweisen auf den Rahmenvertrag, Seite 10. Der liegt nicht im Repository.
6. **Tabelle der Produktparameter**, als Stichpunkt in 3.2.3. Die Prüfspalte ist
   offen.
7. **Eingriffe über Rahmenvorgaben**, erledigt am 11.09.2026. Satz 6 der Einordnung
   grenzt das Argument des Verfassers auf den Abruf ein, den die kurativen
   Klauseln nicht erfassen.
8. **Consentec 2024.** Der Literatureintrag datiert Februar, das PDF Mai. Seit dem
   11.09.2026 in der Einordnung nicht mehr zitiert.
9. **Verdrängung der Regelleistung.** Offen ist, ab welchem Preis die kurative
   Reservierung nicht mehr nur die Arbitrage, sondern auch die Regelleistung
   verdrängt. In 3.2 entfallen, die Frage bleibt Kapitel 5 überlassen.
10. **Einleitung von 3.2.** Die beiden Stichpunkte der zweiten Sitzung sagen
   kurative Bindung, nach Stilregel 5 heißt es kurative Reservierung.

---

## Geparkt

- Die sechs Sätze zu den Anpassungen des Marktdesigns, als Kommentar vor dem
  Anforderungskatalog. Abgelöst durch die Einordnung in 3.1.3. Die regionalen
  Gebiete für den Kurzfristhandel sind nicht übernommen, weil Hörsch 2017 und
  Einsiedler 2025 sie nicht tragen.
- Die Tabelle mit den 36 Bewertungen, als Kommentar erhalten, vorgesehen für 5.2.

---

## Offene Punkte außerhalb von 3.1

1. `chapter_5.tex:230` trägt F3 folgt aus A2 und A3, das ist die alte
   Nummerierung und heißt jetzt A3 und A4.
2. Abschnitt 4.4 führt noch Abrufhäufigkeit, Vergütungsniveau und Pönalehöhe, die
   nach den Entscheidungen 4, 5 und 6 entfallen.
3. Seit dem 11.09.2026 sind alle Volltexte lesbar, über PyMuPDF und bei den drei
   langen Dateinamen über den Langpfad-Präfix. Die inhaltliche Prüfung von
   `ehrhart_analysis_2025` steht aus.
4. Die Abbildung `fig:markt_zeitschiene` in Kapitel 2 führt pRD1, pRD2 und WAPP
   ohne Erklärung und ohne Eintrag im Abkürzungsverzeichnis.
5. Die Arbeitskopie enthält den uncommitteten Stand der zweiten Sitzung, nämlich
   Abbildungen in 3.2, den Ordner `figures/chapter_3` und ihren Protokolleintrag.
   Ob und wann committet wird, entscheidet der Verfasser.

---

## Nächste Schritte

1. Die Stichpunkte in 3.2 mit dem Vermerk ZU AENDERN NACH K1 gemeinsam neu fassen
2. Kapitel 3 auf 14 Seiten bringen
