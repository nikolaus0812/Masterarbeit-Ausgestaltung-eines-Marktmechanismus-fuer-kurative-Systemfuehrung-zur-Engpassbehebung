"""Absatzlaengen einer Kapiteldatei auszaehlen.

Angelegt am 26.09.2026. Anlass ist die Vorgabe des Verfassers vom
25.09.2026, die Absaetze in Kapitel 5 auf acht Saetze zu fuehren. Acht ist
die Obergrenze nach Stilregel 1 in CLAUDE.md Abschnitt 4, und
tools/pruefen.py prueft die Absatzlaenge nicht.

Kommentarzeilen, Marken und LaTeX-Befehlszeilen bleiben ausser Betracht,
ebenso Gleitumgebungen, weil deren Text kein Absatz des Fliesstextes ist.

    python tools/absatzlaengen.py chapters/chapter_5.tex
    python tools/absatzlaengen.py chapters/chapter_5.tex --nur-kurze
"""
import re
import sys

GRENZE = 8


def absaetze(pfad):
    """Liefert je Absatz die Ueberschrift, die Nummer und den Text."""
    with open(pfad, encoding='utf-8', newline='') as f:
        zeilen = f.read().replace('\r\n', '\n').split('\n')

    abschnitt = ''
    puffer = []
    nr = 0
    in_float = 0
    for z in zeilen:
        z = z.strip()
        if z.startswith(r'\begin{figure}') or z.startswith(r'\begin{table}'):
            in_float += 1
            continue
        if z.startswith(r'\end{figure}') or z.startswith(r'\end{table}'):
            in_float = max(0, in_float - 1)
            continue
        if in_float:
            continue
        if z.startswith(('\\chapter', '\\section', '\\subsection')):
            if puffer:
                nr += 1
                yield abschnitt, nr, ' '.join(puffer)
                puffer = []
            abschnitt = z
            nr = 0
            continue
        if not z or z.startswith('%') or z.startswith('\\'):
            if not z and puffer:
                nr += 1
                yield abschnitt, nr, ' '.join(puffer)
                puffer = []
            continue
        puffer.append(z)
    if puffer:
        nr += 1
        yield abschnitt, nr, ' '.join(puffer)


def saetze(text):
    """Zaehlt die Saetze. Abkuerzungen mit Punkt zaehlen nicht mit."""
    ohne = re.sub(r'\b(?:Abs|Nr|bzw|z|B|ca|vgl|Art|S|Kap)\.', '', text)
    ohne = re.sub(r'\\ac[sp]?\{[^}]*\}', 'X', ohne)
    return len(re.findall(r'[.!?](?:\s|$)', ohne))


def main():
    pfade = [a for a in sys.argv[1:] if not a.startswith('--')]
    nur_kurze = '--nur-kurze' in sys.argv
    if not pfade:
        print(__doc__)
        return 1

    befund = 0
    for pfad in pfade:
        kopf = ''
        for abschnitt, nr, text in absaetze(pfad):
            n = saetze(text)
            kurz = n < GRENZE
            lang = n > GRENZE
            if nur_kurze and not (kurz or lang):
                continue
            if abschnitt != kopf:
                kopf = abschnitt
                print()
                print(kopf)
            marke = ''
            if kurz:
                marke = '  <-- unter %d' % GRENZE
                befund += 1
            if lang:
                marke = '  <-- UEBER %d' % GRENZE
                befund += 1
            print('  A%-2d %d Saetze%s  %s' % (nr, n, marke, text[:70]))
    print()
    print('%d Absaetze ausserhalb von %d Saetzen.' % (befund, GRENZE))
    return 0


if __name__ == '__main__':
    sys.exit(main())
