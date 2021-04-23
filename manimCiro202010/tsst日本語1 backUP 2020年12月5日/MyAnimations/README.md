# My objects and animatios of manim

In this repository you will find the code and files of my own animations of manim.

## Steps:

1. Copy this packages in manimlib/tex_template.tex

```latex
%------------New packages-----------
% \usepackage{emerald} % This fonts could be a problem on Linux & Mac
\usepackage{listings}
\usepackage{abraces}
\usepackage{multicol}
\usepackage{multirow}
\usepackage{pgfplots}
\usepackage{musixtex}
\usepackage{circuitikz}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,automata,positioning,decorations.pathmorphing}
\usetikzlibrary{arrows,shapes,trees}
\usetikzlibrary{intersections}
\usetikzlibrary{calc}
\usetikzlibrary{automata}
\usetikzlibrary{calendar}
\usetikzlibrary{er}
\usetikzlibrary{matrix}
\usetikzlibrary{folding}
\usetikzlibrary{patterns}
\usetikzlibrary{plothandlers}
\usetikzlibrary{shapes}
\usetikzlibrary{plotmarks}
\usetikzlibrary{snakes}
\usetikzlibrary{topaths}
\usetikzlibrary{babel}

\lstdefinestyle{basic}
{  
	basicstyle=\scriptsize\ttfamily,
	tabsize=4, % tab space width
	showtabs=true,
	showstringspaces=false, % don't mark spaces in strings
	numbers=left, % display line numbers on the left
	frame=single,
	numbers=left,
	numbersep=10pt,
	showstringspaces=false,
	breakatwhitespace=false,                 
	captionpos=t,abovecaptionskip=0pt,
	columns=fullflexible,    
	keepspaces=true,
	xleftmargin=10pt,
	framexleftmargin=17pt,
	framexrightmargin=0pt,
	framexbottommargin=0pt,
	framextopmargin=0pt,
	mathescape=false,escapechar=|,%
	framerule=0pt,
	breaklines=false,
}

\DeclareFontFamily{U}{matha}{\hyphenchar\font45}
\DeclareFontShape{U}{matha}{m}{n}{
	<5> <6> <7> <8> <9> <10> gen * matha
	<10.95> matha10 <12> <14.4> <17.28> <20.74> <24.88> matha12
}{}
\DeclareSymbolFont{matha}{U}{matha}{m}{n}
\DeclareFontSubstitution{U}{matha}{m}{n}

\DeclareFontFamily{U}{mathb}{\hyphenchar\font45}
\DeclareFontShape{U}{mathb}{m}{n}{
	<5> <6> <7> <8> <9> <10> <11> <12> gen * mathb
	<10.95> mathb10 <12> <14.4> <17.28> <20.74> <24.88> mathb12
}{}
\DeclareSymbolFont{mathb}{U}{mathb}{m}{n}
\DeclareFontSubstitution{U}{mathb}{m}{n}

\DeclareMathSymbol{\supa}{3}{mathb}{"F1}


\DeclareMathSymbol{\leftarrow}{3}{matha}{"D0}
\DeclareMathSymbol{\rightarrow}{3}{matha}{"D1}
\DeclareMathSymbol{\to}{3}{matha}{"D1}
\DeclareMathSymbol{\syx}{3}{matha}{"D8}
%------------------------------------
```
2. Copy the .svg files to SVG directory.
3. Copy the image files to raster_images directory.
4. Copy the audio files to sounds directory
