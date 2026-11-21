# L4 fixes

1. Table 3 float: blank line inserted before `\begin{table}[ht]` in main.tex; the sentence "For m=12,...,21 ..." is no longer split.
2. z-score reference: sentence now states N=4181, 5574; V_N(1)=0.336056, 0.338011 (diff 0.001955); V_N(2)=0.156116, 0.161916 (diff 0.005800); z-scores computed against these differences (source results/indep-REPORT.md). No other number changed.
3. Bibliography: Coelho04 now precedes CdF96.

Compile (2 passes): 28 pp, 0 errors, 0 undefined, 0 overfull.
