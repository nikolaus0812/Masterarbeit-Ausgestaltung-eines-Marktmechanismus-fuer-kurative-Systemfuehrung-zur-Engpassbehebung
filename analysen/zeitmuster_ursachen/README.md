# Ursachen des Zeitmusters, eigene Auswertungen

**Angelegt am 23.09.2026.** Anlass ist die Vorgabe des Verfassers, auffällige
Perioden im Ergebnisteil nicht nur zu beschreiben, sondern aus den Daten zu
begründen.

Quelle aller Auswertungen ist `jahr_slots_2025.parquet` aus dem
Analyse-Repository `bess_dispatch_optimization`. Die Datei führt je
Viertelstunde des Jahres 2025 den kurativen Reservierungspreis beider
Richtungen, die im Referenzfall belegte Leistung je Markt und alle
Marktpreise. **Sie wird ausschließlich gelesen**, in das Analyse-Repository
schreibt keines der Skripte.

Aufruf mit dem Interpreter des Modellrepositorys:
`C:/ProgramData/anaconda3/envs/venv_mode/python.exe <skript>.py`

| Skript | Bericht | Frage |
|---|---|---|
| `ursachen.py` | `BEFUND.md` | Woran hängen die teuren Mittage und Abende, erste Annäherung über Rangkorrelationen |
| `ergaenzung.py` | `BEFUND_ERGAENZUNG.md` | Ist der hohe aFRR-Leistungspreis im Herbst ein Ereignis des ganzen Tages |
| `fuehrender_markt.py` | `BEFUND_FUEHRENDER_MARKT.md` | Welcher Markt stellt je Viertelstunde die größte Opportunität |
| `entladen_spread.py` | `BEFUND_ENTLADEN_SPANNE.md` | Dasselbe für die Entladerichtung, mit der Arbitragespanne statt des Preises |
| `arbitragepaare.py` | `BEFUND_ARBITRAGEPAARE.md` | Wie tief ist die Staffel der Preisspannen eines Tages |
| `sommerloch.py` | `BEFUND_SOMMERLOCH.md` | Trägt die Ferienzeit den Preisrückgang im Juli |
| `heatmap_struktur.py` | `BEFUND_HEATMAP.md` | Wie liegen die teuren Stunden über Tag und Jahr |

## Was in die Arbeit eingegangen ist

- **Abschnitt 4.4**, Ursachenabsatz: der Leistungspreis der aFRR trägt das
  Niveau, einzelne hohe Preisspannen tragen die Extrema. Belegt mit 82,2 gegen
  37,5 Euro je Megawatt und Stunde aus `BEFUND.md` und mit 179,0 gegen 112,8
  Euro je Megawattstunde aus `BEFUND_ARBITRAGEPAARE.md`.
- **Abschnitt 4.4**, Beschreibung der Heatmap: alle Zahlen aus
  `BEFUND_HEATMAP.md`.
- **Abschnitt 4.1**, Schlussfolgerungen: die Aussage, dass die aFRR-Leistung
  den kurativen Reservierungspreis setzt, steht seit dem 23.09.2026 auf der
  Rangkorrelation aus `BEFUND.md` und nicht mehr auf der
  Verdrängungsreihenfolge der fünf Analysetage.

## Zwei Vermutungen, die an den Daten gescheitert sind

- **Die Ferienzeit** trägt den Preisrückgang im Juli nicht. Geringere Last
  müsste die Mittagsdelle vertiefen; beobachtet ist das Gegenteil. Siehe
  `BEFUND_SOMMERLOCH.md`. Die Frage ist in `ANFRAGE_AFRR_HERBST_2025.md`
  Abschnitt 4 an den SMARD-Chat gegeben.
- **Die negativen Energiepreise** heben nicht das Niveau der Ladereservierung.
  Sie sind häufig, aber flach, nämlich im Median minus 7,8 Euro je
  Megawattstunde. Siehe `BEFUND_FUEHRENDER_MARKT.md` Abschnitt 3.

## Der Fehler, der alle Berichte dieses Ordners betrifft

> **Alle Berichte ausser `BEFUND_NEUBERECHNUNG.md` nehmen `be_pos` und
> `be_neg` als kurativen Reservierungspreis. Das ist die ERSTE Iteration**
> mit einem Median von 15,87 und 16,70 Euro je Megawatt und Stunde und
> einem Maximum von 488,48, naemlich dem Deckel der Bisektion. Die Arbeit
> weist die **zweite** Iteration aus, die als `be_full_pos` und
> `be_full_neg` in `heatmap_stunden_2025.parquet` steht.
>
> **Betroffen sind allein die Spalten mit dem Reservierungspreis.** Alle
> Aussagen ueber Marktpreise — der aFRR-Leistungspreis, die negativen
> Energiepreise, die Staffel der Arbitragepaare, der Juli — stehen in
> eigenen Spalten und bleiben richtig.
>
> **Massgeblich ist `BEFUND_NEUBERECHNUNG.md`**, das die Zahlen des Kapitels
> mit der zweiten Iteration neu rechnet und gegen ERGEBNISSE Abschnitt 7.1
> gegenprueft. `laden.py` fuehrt beide Quellen zusammen und liefert den
> Preis unter den Namen `res_ent` und `res_lad`; jede weitere Auswertung
> benutzt sie.

## Ein Fehler in der eigenen Rechnung

`fuehrender_markt.py` setzt für die **Entladerichtung** den Preis der Stunde
selbst als Opportunität an. Das überschätzt die Energiemärkte, denn wer
entladen will, muss die Energie vorher kaufen. **Abschnitt 2 von
`BEFUND_FUEHRENDER_MARKT.md` ist deshalb überholt**; maßgeblich ist
`BEFUND_ENTLADEN_SPANNE.md`, das mit der Spanne zum günstigsten Bezug
desselben Tages rechnet. Für die Laderichtung besteht das Problem nicht, weil
eine Ladung zu einem negativen Preis unmittelbar Geld einbringt.
