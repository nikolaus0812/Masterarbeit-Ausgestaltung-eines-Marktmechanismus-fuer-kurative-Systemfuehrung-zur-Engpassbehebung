# LaTeX Thesis Template

This document does not claim to give all imaginable hints on how to use LaTeX. If you have problems with the template, you should look for help first on the Internet ([Google]({https://www.google.com/), [TeX Stack Exchange](https://tex.stackexchange.com/)), then with fellow students and then with your supervisor. If suggestions for corrections and additions to the LaTeX template are identified, we and the following generations of students will be grateful if valuable suggestions are incorporated into the central format template via the supervisor.

**Note:** If the thesis is written in German, it is recommended to use the newest German hyphenation patterns. This can be achieved by adding

    \usepackage[ngerman=ngerman-x-latest]{hyphsubst}
    
to the document's header. However, this often leads to the error

    Package hyphsubst Error: Unknown pattern `ngerman-x-latest'

when using the MiKTeX distribution and is therefore not included in this template by default. This error does usually not occur when using TeX Live.

## LaTeX Editors and Distributions

For offline use on the PC a LaTeX distribution (e.g. [TeX Live](https://www.tug.org/texlive/)) and an editor (e.g. [TeXStudio](https://www.texstudio.org/)) must be installed. The versions on the student computers are often outdated (if they exist at all) and should be reinstalled by our IT as a precaution. If MiKTeX is used as distribution instead of Tex Live, it must be allowed to download required packages from the internet. This can be done automatically or on demand. This template can be compiled as follows:

 - Download and unzip the LaTeX template
 - Start TeXstudio and open the file main.tex
 - Build and view (F5)

When using it for the very first time you should compile the main.tex first (with pdfLaTeX). In most cases the compilation of the bibliography ends with an error. Then Biber should be executed (Tools -> Commands -> Biber). Afterwards main.tex should be compiled again and everything should work. To bypass the manual execution of Biber, the standard bibliography program can be changed. In TeXstudio this is done via Options -> Configure TeXstudio -> Build. When compiling main.tex for the first time, errors may occur, but as soon as the setup runs through once without errors, usually no further (major) problems occur. If you change the language of this template, you usually have to compile two times, as the first compilation usually runs into an error.

**Note:** When installing, you should install the distribution first and use the suggested file path. If TeXstudio cannot find the paths with the required exe files (e.g. pdflatex.exe), they have to be set manually under Options -> Configure TeXstudio -> Commands.
