# L2 referee review

Reviewer: Claude Fable 5.1, 2026-11-20. Source: `manuscript/main.tex` + `manuscript/sections/*.tex` at HEAD (441714c), compiled three times with pdflatex to `/private/tmp/claude-501/L2/main.pdf` (28 pp., no `??`, no undefined references or citations, one harmless underfull hbox in the Figure 3 caption).

L1 verification: all ten L1 items were checked against the source. Items 1, 2, 5–10 are applied exactly as specified (Beresnevich–Leong bibitem and remark; `Ram14` removed; Step 0 bound now `4ε+2w` with no stray clause; "Put" in Section 7; "(with t in place of s)" removed; Lemma 6.1 replaced by a pointer to Corollary 5.8 with both `\ref`s retargeted; "suitable other times"; `Qu` marker present in `figures/threshold.tex` and legible on p. 18). Items 3 and 4 are decided and not re-raised. No new problem was introduced by the fixes.

Mathematics: every proof was re-derived again (Theorems A, B, C, 5.3 with Appendix A, 7.3, 7.5, 7.7, Lemma B.1, all corollaries of Section 5, the Φ(x,s) table, the explicit V_δ, and the constants Qu ≈ 3.428, c_* ≈ 5.547, κ(√2−1) = 1+3√2/4, 1/(√5λ³) = 1+2/√5). The Monte Carlo and deterministic tables are internally consistent (N = 5574 = 4181+1393, N(V_N−V) column recomputed, Table 1 differences). No mathematical error found. Findings below are precision/consistency/copy-editing items.

Line numbers refer to the files at HEAD.

## Findings

### 1. (must) `manuscript/main.tex:539` — dangling colon; Table 3 floats into the next sentence
The paragraph ends `Selected values at $c=1$:` and relies on the `[ht]` table following immediately. In the compiled PDF (p. 23) the table floats and the text reads "Selected values at c = 1: For m = 12, …, 21 and [Table 3] c ∈ {0.5, 1, 2, 3} the log–log slope …". Neither `tab:mc` nor `tab:det` is referenced anywhere (`grep -r 'ref{tab:' manuscript/` finds only `tab:limits`).

Fix (a): replace at `main.tex:539`
```
sampling at every test point. Selected values at $c=1$:
```
by
```
sampling at every test point. Selected values at $c=1$ are given in Table~\ref{tab:det}.
```
Fix (b): replace at `main.tex:512-513`
```
four-candidate reduction of Lemma~\ref{lem:fourcand}. Common random numbers
give paired standard errors.
```
by
```
four-candidate reduction of Lemma~\ref{lem:fourcand}. Common random numbers
give paired standard errors (Table~\ref{tab:mc}).
```

### 2. (should) Figures 1 and 2 are never referenced in the text
`deph:fig-geometry` (Figure 1, p. 6) and `fig:phase` (Figure 2, p. 18) have no `\ref`. Journals require every float to be cited.

Fix (a): `manuscript/sections/dephasing.tex:9`, replace
```
Points of the disk are written $z=re^{i\varphi}$, and we set $q(r)=\sqrt{r^2-a^2}$.
```
by
```
Points of the disk are written $z=re^{i\varphi}$, and we set $q(r)=\sqrt{r^2-a^2}$.
Figure~\ref{deph:fig-geometry} shows the configuration.
```
Fix (b): `manuscript/main.tex:454`, replace
```
Figure~\ref{fig:threshold} shows the two quantities that Theorem~\ref{thm:C} controls. The
```
by
```
Figure~\ref{fig:phase} shows $x\mapsto V(x,c)-V(0,c)$ for three values of $c$.
Figure~\ref{fig:threshold} shows the two quantities that Theorem~\ref{thm:C} controls. The
```

### 3. (should) `manuscript/main.tex:173-174` — Theorem C(2) is stated with Fibonacci numbers, but "the same conclusions hold" for noble angles
For a noble β the extremal subsequence in part (2) is the sequence of convergent denominators q_k (this is what Step 4 of the proof, `main.tex:440-451`, actually shows), not F_m. As written, the transfer clause asserts lim_{m} V_{F_m}(c) = liminf V_N(c) for every noble β, which is not what is proved. The abstract (`main.tex:40-42`) has the same overstatement.

Fix (a): `main.tex:173-174`, replace
```
The same conclusions hold, with $a=\cos\pi\beta$ and $Q=\sin\pi\beta$, for every
noble $\beta\in(0,1/2)$, i.e.\ every $\beta$ whose partial quotients are eventually $1$.
```
by
```
The same conclusions hold, with $a=\cos\pi\beta$, $Q=\sin\pi\beta$ and the convergent
denominators $q_k$ in place of $F_m$ in (2), for every noble $\beta\in(0,1/2)$, i.e.\ every
$\beta$ whose partial quotients are eventually $1$.
```
Fix (b): `main.tex:40-42`, replace
```
of $V_N(c)$ is an explicit interval, its lower end is attained along Fibonacci times by a
convex-order argument, and $V_N(c)$ converges if and only if $c$ is at least an explicit
threshold.
```
by
```
of $V_N(c)$ is an explicit interval, its lower end is attained along Fibonacci times
(convergent denominators for noble angles) by a convex-order argument, and $V_N(c)$
converges if and only if $c$ is at least an explicit threshold.
```

### 4. (should) `manuscript/sections/gaplemmas.tex:42` — Khinchin is cited inline without a bibliography entry
The only classical source for \eqref{gap:eq:det}–\eqref{gap:eq:F2} is given as a parenthetical "(Khinchin, *Continued Fractions*, §§1–2)". It must be a proper reference.

Fix (a): `gaplemmas.tex:41-42`, replace
```
so that $\eta_{-1}=1$ and $\eta_0=\beta$. We use the classical facts
(Khinchin, \emph{Continued Fractions}, \S\S1--2):
```
by
```
so that $\eta_{-1}=1$ and $\eta_0=\beta$. We use the classical facts \cite[Ch.~I]{Khi64}:
```
Fix (b): `main.tex`, insert after line 643 (`\bibitem{FS02} …`), keeping alphabetical order:
```
\bibitem{Khi64} A.~Ya.~Khinchin, \emph{Continued Fractions}, University of Chicago Press, Chicago, 1964.
```

### 5. (should) `manuscript/sections/dispersion.tex:6` — hard-coded section number
`We keep the notation of Section~1:` is the only hard-coded cross-reference in the paper; the Introduction has no label.

Fix (a): `main.tex:51`, replace `\section{Introduction}` by `\section{Introduction}\label{sec:intro}`.
Fix (b): `dispersion.tex:6`, replace `We keep the notation of Section~1:` by `We keep the notation of Section~\ref{sec:intro}:`.

VERDICT: FINDINGS 5
