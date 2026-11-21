# L3 referee review

Reviewer: Claude Fable 5.1, 2026-11-20. Source: `manuscript/main.tex` + `manuscript/sections/*.tex` + `manuscript/figures/*.tex` at HEAD (ee44841), compiled three times with pdflatex to `/private/tmp/claude-501/L3/main.pdf` (28 pp., no `??`, no undefined references or citations, one harmless underfull hbox in the Figure 3 caption, two harmless hyperref "math shift" warnings from the `$N$` in the Section 5.2 heading; the bookmark renders correctly).

L2 verification: all five L2 items are applied exactly as specified. Item 1: `main.tex:516` and `:542` now reference `tab:mc` and `tab:det`; the dangling colon is gone and the Table 3 sentence reads correctly on p. 23. Item 2: `dephasing.tex:10` references Figure 1; `main.tex:456` references Figure 2. Item 3: `main.tex:174-176` and `:40-42` carry the convergent-denominator clause. Item 4: `\cite[Ch.~I]{Khi64}` at `gaplemmas.tex:41`, bibitem at `main.tex:647`. Item 5: `\label{sec:intro}` and `\ref` at `dispersion.tex:6`. No new problem was introduced by the fixes.

Mathematics: every proof was re-derived again (Theorems A, B, C, 5.3 with Appendix A, 7.4, 7.6, 7.7, Lemma B.1, all corollaries of Section 5, the Φ(x,s) table, the explicit V_δ, the certified-constants primitive, and the numbers Qu ≈ 3.428, c_* ≈ 5.547, 1+2/√5 = 1/(√5λ³), κ(√2−1) = 1+3√2/4, (1+3/√5)/2 ≈ 1.1708, the Figure 3 marker abscissae, the Table 3 offsets N(V_N−V) and the decomposition N = 5574 = 4181+1393). No mathematical error found. Findings below are copy-editing items.

Line numbers refer to the files at HEAD.

## Findings

### 1. (must) `manuscript/figures/geometry.tex:28` — Figure 1 labels the point `$x$`, the caption and text call it `$z$`
The caption (`dephasing.tex:29-31`) says "a point $z$ at radius $r>a$ ... from $z$ to the caustic", and the whole paper writes $z=re^{i\varphi}$; the figure node reads `$x$` (visible on p. 6). Same symbol mismatch is in the generator and the stale comment block.

Fix (a): `manuscript/figures/geometry.tex:28`, replace
```
\node[font=\small, fill=white, inner sep=1pt] at (-2.4961,2.4248) {$x$};
```
by
```
\node[font=\small, fill=white, inner sep=1pt] at (-2.4961,2.4248) {$z$};
```
Fix (b) (keeps the figure regenerable): `manuscript/make_geometry.py:51`, replace `{{$x$}}` by `{{$z$}}`; and in `make_geometry.py:18` and `figures/geometry.tex:2-3` replace `a point x at radius r > a. The two tangent lines from x` by `a point z at radius r > a. The two tangent lines from z`.

### 2. (should) `manuscript/main.tex:637-648` — `Leong17` is out of alphabetical order after the L1 author correction
The bibliography is ordered by first-author surname (Caglioti–Golse, key `MS03`, sits under C). After L1 changed the entry to "V. Beresnevich and N. Leong" it stayed at the L position (ref. [15], between Khinchin and Niederreiter). Move it to the B position.

Fix: delete `main.tex:648`
```
\bibitem{Leong17} V.~Beresnevich and N.~Leong, Sums of reciprocals and the three distance theorem, arXiv:1712.03758.
```
and insert the identical line immediately after `main.tex:634` (`\bibitem{AB98} …`), i.e. before `\bibitem{BK93}`. Citation keys are unchanged; numbering shifts automatically.

### 3. (should) `manuscript/main.tex:278` — the proof of Theorem B sits inside Subsection 5.3 "Corollaries"
`sections/gaplemmas.tex` opens three `\subsection`s (5.1–5.3) and never closes the last; the "Idea of the proof" paragraph and the full proof of Theorem B (`main.tex:278-359`, pp. 13–14) therefore run under the heading "5.3. Corollaries". A reader navigating by the bookmarks or headings cannot find the proof of a main theorem.

Fix: at `main.tex:278`, insert before `\emph{Idea of the proof.}`
```
\subsection{Proof of Theorem~\ref{thm:B}}\label{sec:proofB}
```
(New Subsection 5.4; no existing cross-reference changes.)

VERDICT: FINDINGS 3
