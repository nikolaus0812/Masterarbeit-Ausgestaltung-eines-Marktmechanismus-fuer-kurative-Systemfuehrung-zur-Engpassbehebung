import os, re
os.chdir(r"C:\GIT-HUB\Masterarbeit-Ausgestaltung-eines-Marktmechanismus-fuer-kurative-Systemfuehrung-zur-Engpassbehebung")
out = os.environ.get("TEMP", ".")  # Ausgabe kap{n}_text.txt im Temp-Verzeichnis, 17.09.2026

def render(l):
    l = re.sub(r"\\acs?\{([^}]*)\}", r"\1", l)
    l = re.sub(r"\\acl\{([^}]*)\}", r"\1", l)
    l = re.sub(r"\\cite\{[^}]*\}", "[Quelle]", l)
    l = re.sub(r"\\(?:auto)?ref\{fig:[^}]*\}", "N", l)
    l = re.sub(r"\\(?:auto)?ref\{tab:[^}]*\}", "N", l)
    l = re.sub(r"\\(?:auto)?ref\{eq:[^}]*\}", "N", l)
    l = re.sub(r"\\(?:auto)?ref\{(sec|ch|anh):[^}]*\}", "X", l)
    l = re.sub(r"\\si\{([^}]*)\}", r"\1", l)
    l = l.replace("\\,", " ").replace("~", " ")
    l = re.sub(r"\\chapter\{([^}]*)\}", r"\n==== KAPITEL \1 ====", l)
    l = re.sub(r"\\section\{([^}]*)\}", r"\n=== \1 ===", l)
    l = re.sub(r"\\subsection\{([^}]*)\}", r"\n== \1 ==", l)
    l = re.sub(r"\\subsubsection\*?\{([^}]*)\}", r"\n= \1 =", l)
    l = re.sub(r"\\paragraph\{([^}]*)\}", r"\n- \1 -", l)
    l = re.sub(r"\\(textit|emph|textbf)\{([^}]*)\}", r"\2", l)
    l = re.sub(r"\\label\{[^}]*\}", "", l)
    l = re.sub(r"\\caption\{(.*)\}\s*$", r"[Bildunterschrift] \1", l)
    l = re.sub(r"\\item\[([^\]]*)\]", r"\1:", l)
    return l

SKIP = ("\\begin{figure}", "\\end{figure}", "\\centering", "\\includegraphics", "\\begin{table}", "\\end{table}",
        "\\begin{tabular}", "\\end{tabular}", "\\hline", "\\toprule", "\\midrule", "\\bottomrule", "\\small",
        "\\footnotesize", "\\setlength", "\\begin{description}", "\\end{description}", "\\begin{itemize}", "\\end{itemize}",
        "\\begin{equation}", "\\end{equation}", "\\multicolumn", "\\vspace", "\\noindent")
for n in (1, 2, 3):
    z = open(f"chapters/chapter_{n}.tex", encoding="utf-8", newline="").read().split("\r\n")
    lines = []
    for l in z:
        if l.lstrip().startswith("%"):
            continue
        s = l.strip()
        if s.startswith(SKIP) or ("&" in s and s.endswith("\\\\")):
            continue
        lines.append(render(l).strip())
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Absaetze nummerieren
    blocks = text.split("\n\n")
    outl = []
    k = 0
    for b in blocks:
        if b.startswith(("=", "-")) or not b.strip():
            outl.append(b)
            continue
        k += 1
        saetze = [s for s in b.split("\n") if s.strip()]
        outl.append(f"[Absatz {k}, {len(saetze)} Saetze]\n" + b)
    open(os.path.join(out, f"kap{n}_text.txt"), "w", encoding="utf-8").write("\n\n".join(outl))
    print(n, k, "Absaetze", len(text.split()), "Woerter")
