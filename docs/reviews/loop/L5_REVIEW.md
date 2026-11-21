# L5 referee review

Reviewer: Claude Fable 5.1, 2026-11-21. Source: `manuscript/main.tex` + `manuscript/sections/*.tex` + `manuscript/figures/*.tex` at HEAD (f2ba808), compiled three times with pdflatex to `/private/tmp/claude-501/L5/main.pdf` (28 pp., no `??`, no undefined references or citations, no overfull boxes; the one underfull hbox in the Figure 3 caption and the two hyperref "math shift" warnings from the `$N$` in the Section 5.2 heading are unchanged from L3/L4 and harmless).

L4 verification: the commit touches only `main.tex` (plus the review/fix logs and the PDF); all three L4 items are applied exactly as specified, with no regression.

- Item 1: blank line before `\begin{table}[ht]` at `main.tex:547-548`; on p. 23 Table 3 now sits between "Selected values at c = 1 are given in Table 3." and the intact paragraph "For m = 12, ..., 21 and c in {0.5, 1, 2, 3} ...".
- Item 2: `main.tex:532-538` states the reference values. Checked against `results/indep-REPORT.md:15` (V_N(1) = 0.336056 / 0.338011, V_N(2) = 0.156116 / 0.161916 at N = 4181 / 5574, h = 0.5) and `results/seedsweep/SUMMARY.md` (deterministic differences 0.001955 and 0.005800; 20 runs = seed 20261115 + 9001-9016 + three verifier seeds; pooled z 0.91 and 1.43; SD across runs 1.70e-4 / 1.15e-4 vs paired SE 1.91e-4 / 1.02e-4). Differences recompute correctly (0.338011 - 0.336056 = 0.001955; 0.161916 - 0.156116 = 0.005800), and the values are consistent with Table 3 (N = 4181 lies between the m = 18 and m = 21 rows, with N(V_N - V(0,1)) = 4181 x (0.336056 - 0.336226) = -0.71 and 5574 x (0.338011 - 0.338140) = -0.72, matching the -0.7 offsets) and with Table 2 (single-N Monte Carlo values within 0.4-0.7 SE of the deterministic ones). The sentence is grammatical and renders on one paragraph (p. 23).
- Item 3: `Coelho04` at `main.tex:645` precedes `CdF96` at `:646`; rendered as [7] Coelho (2004), [8] Coelho-de Faria (1996). All 23 bibitems cited; all citation keys resolve.

Mathematics: every proof was re-derived once more (Theorems A, B, C, 5.3 with Appendix A including the k = 0 case, the Cramer's-rule claim and both t >= 1 / t = 0 branches of Step 3; Theorems 7.3, 7.5, 7.7; Lemmas 3.1, 3.2, 5.1, 5.2, 7.1, 7.2, 7.4, B.1; Corollaries 1.1, 5.5-5.9; the Phi(x,s) table including slopes and breakpoint values; the mass inequality (26) with tau = eps^2/4; the explicit V_delta; the certified-constants primitive; the constants Qu = 3.428, c_* = 5.547, 1 + 2/sqrt5 = (2+lambda)/(2-lambda) = 1/(sqrt5 lambda^3), kappa(sqrt2 - 1) = 1 + 3 sqrt2/4, a^2 = 0.131316, the Table 1 differences, the Table 2 limit differences, N = 5574 = 4181 + floor(4181/3), and the bound |F_{m-1} - lambda F_m| = lambda^m). No mathematical error found. Numbering, cross-references, figures (pp. 6, 16-17 re-rendered and inspected), tables and bibliography are consistent; no typo requiring correction was found.

## Findings

None.

VERDICT: NONE
