# L1 referee review

Reviewer: Claude Fable 5.1, 2026-11-20. Source: `manuscript/main.tex` + `manuscript/sections/*.tex` at HEAD (e888ae2), compiled three times with pdflatex to `/private/tmp/claude-501/L1/main.pdf` (28 pp., no `??`, no undefined references, one harmless underfull hbox in the Figure 3 caption). Every proof was re-derived line by line (Theorems A, B, C, 5.3 with its appendix proof, 7.3, 7.5, 7.7, Lemma B.1, all corollaries of Section 5, the table of Φ(x,s) in Step 2 of Theorem C, the explicit Vδ formula, and the numerical constants Qu ≈ 3.428, c_* ≈ 5.547, κ(√2−1) = 1 + 3√2/4, (2+λ)/(1+λ²) = 1+2/√5). No mathematical error was found; the findings below are bibliography, consistency and wording items.

Line numbers refer to the files as they are at HEAD.

## Findings

### 1. (must) `manuscript/main.tex:652` — wrong author list for `Leong17`
arXiv:1712.03758 has two authors, Victor Beresnevich and Nicol Leong. The entry lists only Leong.

Replace the line
```
\bibitem{Leong17} N.~Leong, Sums of reciprocals and the three distance theorem, arXiv:1712.03758.
```
by
```
\bibitem{Leong17} V.~Beresnevich and N.~Leong, Sums of reciprocals and the three distance theorem, arXiv:1712.03758.
```
Consequential text changes (same finding):
- `manuscript/sections/gaplemmas.tex:85` replace `\begin{remark}[Relation to Leong]` with `\begin{remark}[Relation to Beresnevich and Leong]`.
- `manuscript/sections/gaplemmas.tex:86` replace `Leong \cite[Thm.~3]{Leong17} treats` with `Beresnevich and Leong \cite[Thm.~3]{Leong17} treat`.

### 2. (must) `manuscript/main.tex:654` — uncited bibliography entry
`\bibitem{Ram14}` is never cited (`grep -r 'Ram14' manuscript/` finds only the bibitem). Delete line 654:
```
\bibitem{Ram14} F.~A.~Ram\'irez, Khintchine types of translated coordinate hyperplanes, arXiv:1405.7277.
```

### 3. (should) `manuscript/main.tex:642` — missing page numbers for `BI09`
Published version: Ann. Mat. Pura Appl. (4) 188 (2009), no. 2, 247–267. Replace the line by
```
\bibitem{BI09} C.~Bonanno and S.~Isola, A renormalization approach to irrational rotations, \emph{Ann. Mat. Pura Appl.} (4) \textbf{188} (2009), no.~2, 247--267; arXiv:0708.0048.
```

### 4. (should) `manuscript/main.tex:661` — `Zhao25` has appeared
The preprint is published in Ergodic Theory and Dynamical Systems (online 2025). Replace the line by
```
\bibitem{Zhao25} B.~Zhao, Almost sure convergence of cover times for $\psi$-mixing systems, \emph{Ergodic Theory Dynam. Systems}, published online 2025; arXiv:2412.17425.
```

### 5. (should) `manuscript/sections/dephasing.tex:161` — meaningless parenthetical in Step 0
The four layer bounds sum to 4ε + 2w; the clause "so that the total is also ≤ 6ε+2w" refers to nothing and the hypothesis w < ε/2 is not used in the displayed bound. Replace
```
Therefore, with $w<\varepsilon/2$ (so that the total is also $\le6\varepsilon+2w$),
```
by
```
Therefore
```

### 6. (should) `manuscript/sections/dispersion.tex:9` — "Recall" introduces new notation
G_N, 𝒟_N and L(β) are defined here for the first time (only γ_N and κ appear in Section 1). Replace
```
Recall the notation
```
by
```
Put
```

### 7. (should) `manuscript/sections/dispersion.tex:105` — stray parenthetical
Theorem 5.3 has no variable s; "(with t in place of s)" is a leftover from an earlier draft. Replace
```
By Theorem~\ref{gap:thm:three} (with $t$ in place of $s$), the blocks
```
by
```
By Theorem~\ref{gap:thm:three}, the blocks
```

### 8. (should) `manuscript/main.tex:361-372` — Lemma 6.1 restates Corollary 5.8 verbatim
Lemma 6.1 is word for word Corollary 5.8 and is "proved" by "This is Corollary 5.8". Remove the duplicate and cite the corollary directly.

Replace lines 361–372
```
\begin{lemma}\label{lem:golden}
Let $\beta=\lambda^2$, $m\ge3$ and $N=F_m+t$ with $0\le t<F_{m-1}$. The $N$ gaps of
$\{j\beta\bmod1\}_{j<N}$ are
\begin{align*}
\lambda^{m-2}&&(F_{m-1}-t\text{ times}),\\
\lambda^{m-1}&&(F_{m-2}+t\text{ times}),\\
\lambda^{m}&&(t\text{ times}).
\end{align*}
\end{lemma}

This is Corollary~\ref{gap:cor:golden}. We also verified it in exact arithmetic in
$\mathbb Z[\lambda]$ for every $2\le N\le3000$ (Appendix~\ref{app:repro}).
```
by
```
The gap law of the golden angle is Corollary~\ref{gap:cor:golden}: for $N=F_m+t$ with
$m\ge3$ and $0\le t<F_{m-1}$ the gaps are $\lambda^{m-2}$, $\lambda^{m-1}$, $\lambda^m$
with multiplicities $F_{m-1}-t$, $F_{m-2}+t$, $t$. We also verified it in exact
arithmetic in $\mathbb Z[\lambda]$ for every $2\le N\le3000$ (Appendix~\ref{app:repro}).
```
Then replace every remaining `\ref{lem:golden}` by `\ref{gap:cor:golden}`; there are two: `manuscript/main.tex:378` (`Lemma~\ref{lem:golden}` → `Corollary~\ref{gap:cor:golden}`) and `manuscript/main.tex:633` (`Lemma~\ref{lem:golden}` → `Corollary~\ref{gap:cor:golden}`).

### 9. (should) `manuscript/main.tex:190-191` — overstatement "along other times"
For Qu ≤ c < c_*, V(x,c) > a² holds only for phases x > c/(Qu) − 1 (Theorem C(3)), not for all non-Fibonacci times; at x = λ the limit is again a². Replace
```
covered along Fibonacci times, while along other times a positive area stays
uncovered.
```
by
```
covered along Fibonacci times, while along suitable other times a positive area stays
uncovered.
```

### 10. (should) Figure 3 marks πQ but the text discusses Qu
The paragraph before Figure 3 (`main.tex:462-466`) states that the dashed curve is positive exactly for c < Qu ≈ 3.428, yet the figure marks only c_* and πQ. Add a Qu marker so the figure shows the threshold the text names.
- `manuscript/make_figures.py:66`: after that line insert
```
    out.append(f'\\draw[gray, densely dotted] ({Q*math.pi/(math.sqrt(5)*LAM**2)*sx:.3f},0) -- ({Q*math.pi/(math.sqrt(5)*LAM**2)*sx:.3f},2.5) node[above, font=\\small] {{$Qu$}};')
```
- `manuscript/figures/threshold.tex`: after the line beginning `\draw[gray, densely dotted] (4.723,0)` insert
```
\draw[gray, densely dotted] (5.530,0) -- (5.530,2.5) node[above, font=\small] {$Qu$};
```
(5.530 = 3.4283 × 10/6.2; the two edits produce identical output, so either regenerate with the script or edit the `.tex` directly.)

VERDICT: FINDINGS 10
