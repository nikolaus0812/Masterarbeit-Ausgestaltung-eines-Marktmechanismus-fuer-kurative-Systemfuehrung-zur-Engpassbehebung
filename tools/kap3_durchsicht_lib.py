import os
os.chdir(r"C:\GIT-HUB\Masterarbeit-Ausgestaltung-eines-Marktmechanismus-fuer-kurative-Systemfuehrung-zur-Engpassbehebung")
CRLF = "\r\n"
DATUM = "15.09.2026"

def lade(p):
    return open(p, encoding="utf-8", newline="").read().split(CRLF)

def speichere(p, z):
    open(p, "w", encoding="utf-8", newline="").write(CRLF.join(z))

class Datei:
    def __init__(self, p):
        self.p = p
        self.z = lade(p)

    def idx(self, prefix):
        t = [i for i, l in enumerate(self.z) if not l.lstrip().startswith("%") and l.lstrip().startswith(prefix)]
        assert len(t) == 1, (prefix[:70], t)
        return t[0]

    def satz(self, prefix, neu, grund):
        i = self.idx(prefix)
        ind = self.z[i][:len(self.z[i]) - len(self.z[i].lstrip())]
        self.z[i:i + 1] = [f"% DURCHSICHT {DATUM}, {grund}. Alte Fassung:", "%" + self.z[i]] + [ind + n for n in neu]

    def verbinde(self, prefix_a, prefix_b, grund):
        """Leerzeilen zwischen der Zeile a und der Zeile b durch Kommentar ersetzen, Absaetze verbunden."""
        a, b = self.idx(prefix_a), self.idx(prefix_b)
        assert a < b, (prefix_a[:40], prefix_b[:40])
        n = 0
        for i in range(a + 1, b):
            if self.z[i].strip() == "":
                self.z[i] = f"% ABSATZ VERBUNDEN {DATUM}, {grund}."
                n += 1
        assert n >= 1, ("keine Leerzeile", prefix_a[:40])

    def verschiebe(self, prefixes, nach_prefix, grund, neuer_absatz=False):
        """Zeilen (in dieser Reihenfolge) hinter die Zeile nach_prefix setzen, am Ursprung auskommentieren."""
        zeilen = []
        for p in prefixes:
            i = self.idx(p)
            zeilen.append(self.z[i])
            self.z[i] = f"% VERSCHOBEN {DATUM}, {grund}: " + self.z[i]
        j = self.idx(nach_prefix)
        block = ([""] if neuer_absatz else []) + [f"% HIERHER VERSCHOBEN {DATUM}, {grund}."] + zeilen
        self.z[j + 1:j + 1] = block

    def absatz_vor(self, prefix, grund):
        i = self.idx(prefix)
        self.z[i:i] = ["", f"% NEUER ABSATZ {DATUM}, {grund}."]

