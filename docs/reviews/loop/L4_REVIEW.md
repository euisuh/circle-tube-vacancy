# L4 referee review

Reviewer: Claude Fable 5.1, 2026-11-21. Source: `manuscript/main.tex` + `manuscript/sections/*.tex` + `manuscript/figures/*.tex` at HEAD (5a6c772), compiled three times with pdflatex to `/private/tmp/claude-501/L4/main.pdf` (28 pp., no `??`, no undefined references or citations, no overfull boxes; the one underfull hbox in the Figure 3 caption and the two hyperref "math shift" warnings from the `$N$` in the Section 5.2 heading are unchanged from L3 and harmless).

L3 verification: all three L3 items are applied exactly as specified, with no regression. Item 1: `figures/geometry.tex:32` and `make_geometry.py` now label the point `$z$`; the rendered Figure 1 (p. 6) and its caption agree. Item 2: `Leong17` is `main.tex:636`, between `AB98` and `BK93`, and renders as [2]; all citation keys resolve. Item 3: `\subsection{Proof of Theorem~\ref{thm:B}}` at `main.tex:278` renders as "5.4. Proof of Theorem B" (p. 13) and the bookmark is present; 5.3 "Corollaries" now ends at Corollary 5.9. Theorem/lemma/equation numbering is unchanged from L3.

Mathematics: every proof was re-derived once more (Theorems A, B, C, 5.3 with Appendix A, 7.3, 7.5, 7.7, Lemmas 3.1, 3.2, 5.1, 5.2, 7.1, 7.2, 7.4, B.1, Corollaries 5.5-5.9, the Φ(x,s) table including slopes and breakpoint values, the explicit V_δ, the certified-constants primitive, and the numbers Qu ≈ 3.428, c_* ≈ 5.547, 1+2/√5 = (2+λ)/(2−λ) = 1/(√5λ³), κ(√2−1) = 1+3√2/4, (1+3/√5)/2 ≈ 1.1708, the Figure 3 marker abscissae, N = 5574 = 4181+1393, the Table 3 values of N and of N(V_N−V), the Table 2 paired differences, and −2ac ≈ −0.725). No mathematical error found. Findings below are copy-editing items.

Line numbers refer to the files at HEAD.

## Findings

### 1. (should) `manuscript/main.tex:543-544` — Table 3 float splits a sentence
`\begin{table}[ht]` at `:544` sits inside the paragraph that continues at `:558` with "For $m=12,\dots,21$ and $c\in\{0.5,1,2,3\}$ ...". LaTeX places the float after the current line, so on p. 23 the reader sees "Selected values at c = 1 are given in Table 3. For m = 12, . . . , 21" / [Table 3] / "and c ∈ {0.5, 1, 2, 3} the log–log slope ...". The sentence is cut in two by the table.

Fix: insert one empty line between `main.tex:543` and `main.tex:544`, i.e. make `:543-545` read
```
sampling at every test point. Selected values at $c=1$ are given in Table~\ref{tab:det}.

\begin{table}[ht]
```
Verified in a scratch compile: the table then sits between the two paragraphs, "For $m=12,\dots,21$ and ..." starts a new paragraph intact, page count unchanged (28), no new warnings.

### 2. (should) `manuscript/main.tex:533-534` — "the deterministic finite-$N$ values below" points at values that are not in the paper
The pooled $z$-scores are computed against deterministic values at $N=4181$ and $N=5574$ (c = 1, 2). Table 3, the only deterministic data "below", lists $m=15,18,21$ ($N=610,2584,10946$ and $813,3445,14594$) and only $c=1$; the reference values ($V_{4181}(1)=0.336056$, $V_{5574}(1)=0.338011$ in `results/REPORT.md:97`) appear nowhere in the manuscript. A referee cannot check the stated $z$-scores against anything in the text.

Fix (minimal, no new data): at `main.tex:533-534` replace
```
verifier), the pooled $z$-scores of the paired differences against the deterministic
finite-$N$ values below are $0.91$ ($c=1$) and $1.43$ ($c=2$), and the spread across runs
```
by
```
verifier), the pooled $z$-scores of the paired differences against the deterministic
finite-$N$ values at $N=4181$ and $5574$ (exact-arc integrator, described next; not
tabulated) are $0.91$ ($c=1$) and $1.43$ ($c=2$), and the spread across runs
```

### 3. (should) `manuscript/main.tex:641-642` — bibliography order: single-author Coelho after Coelho–de Faria
The list is alphabetical by first author; the standard convention (AMS, Chicago) puts a single-author entry before coauthored entries by the same first author. Currently [7] is Coelho–de Faria (1996) and [8] is Coelho (2004).

Fix: swap `main.tex:641` and `main.tex:642`, i.e. make them read
```
\bibitem{Coelho04} Z.~Coelho, The loss of tightness of time distributions for homeomorphisms of the circle, \emph{Trans. Amer. Math. Soc.} \textbf{356} (2004), 4427--4445.
\bibitem{CdF96} Z.~Coelho and E.~de Faria, Limit laws of entrance times for homeomorphisms of the circle, \emph{Israel J. Math.} \textbf{93} (1996), 93--112.
```
Citation keys unchanged; the numbers [7]/[8] swap automatically.

VERDICT: FINDINGS 3
