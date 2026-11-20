# Adversarial review: docs/DISPERSION.md and manuscript/sections/dispersion.tex (2026-11-14)

Scratch: `checks/dispersion_review/` (common.py, t1-t5.py, t2_out.txt). Nothing else edited.

## Summary (<=200 words)
No counterexample found. Claim (1) and claim (2) are both CORRECT as proved, conditional on Theorem A (V_N - V~_N -> 0) and Theorem C(2), which I did not re-audit. The step-back argument is valid for every bounded-type beta: its constants depend only on A, never on k or on the block type (r), so the limsup being attained along different block types does no harm. Unbounded type is handled by Theorem C(2) plus L = infinity. The reduction lemma and the kappa formula are correct. Minimality (kappa >= 1+2/sqrt5, equality iff noble, kappa >= 2 otherwise) is a short, correct argument. Numerics I ran independently: max gap of {j beta} compared with the block formula for all N <= 4e5 at 14 angles (relative error ~1e-6, float noise); multiplicities of the three gap classes checked at 1010 (N, beta) pairs, 0 mismatches; analytic E_N(c) at stepped-back N for 7 angle types up to q_k ~ 1e20, constant in k for c < c_cov and exactly 0 for c > c_cov; 2.0M periodic words (period <= 8, digits 1..6) give min non-noble kappa = silver 2.0607. Literature: no primary source states (2). Closest are interval-metric only (Niederreiter 1984, Drobot 1986, Ji-Lu 1996, Tripathi 1993), so (2) stays "not found in literature", not "new". Only GAPs are dependencies and presentation, listed below.

## Item verdicts

| # | Item | Verdict |
|---|---|---|
| 1 | Lemma 1 (mass bounds, m_N(s)=0 iff s>=D_N) | CORRECT |
| 2 | Lemma 2 (E_N->0 iff m_N(c/Q+delta)->0 for all delta; limsup version) | CORRECT |
| 3 | Theorem 1(i) | CORRECT (given Theorem A) |
| 4 | Theorem 1(ii) | CORRECT (given Theorem A and item 8/9) |
| 5 | Three-gap block lemma | CORRECT; proof is by citation only: GAP (presentation) |
| 6 | Corollary / Lemma sup (kappa formula) | CORRECT |
| 7 | L = infinity for unbounded type | CORRECT |
| 8 | Prop. 3, bounded type (converse, step-back) | CORRECT |
| 9 | Prop. 3, unbounded type | CORRECT, depends on Theorem C(2) |
| 10 | Prop. 4 (min kappa, equality case, kappa>=2) | CORRECT |
| 11 | Remark on Niederreiter's interval constant | CORRECT numerics; literature claim appropriately hedged |
| 12 | Dependence on Theorem A / C(2) | GAP (not audited here) |

### Details
1. Each term (g_j - 2s/N)_+ lies in [0, (2/N)(D_N - s)_+] and n_N terms attain the top. Checked algebra with g = 2 pi h, D = N G/2.

2. Direction "m_N(c/Q+delta) >= eps => E >= eps^2 (Q^2 - q_delta^2)": since m_N is non-increasing, q >= q_delta gives c/q <= c/Q + delta, so m_N(c/q) >= eps. Correct. Converse: for q < q_delta, c/q > c/Q+delta so m <= m_N(c/Q+delta); for q in [q_delta, Q] bound m<=1 and take delta -> 0. Correct (needs c>0, which is assumed). Note the tex text says "contributes at most Q^2 m_N^2"; true, loose.

3-4. Logic of Theorem 1 is sound. (i): D_N <= L + delta/2 eventually, so m_N(c/Q+delta)=0, then Lemma 2. Includes c = c_cov exactly (delta arbitrary). (ii): c/Q < L <= Lambda gives m_N(c/Q+delta) not -> 0. Fine. If kappa=infinity, (i) is vacuous and (ii) holds for all c. Checked.

5. I checked the lemma independently of the author's script: (a) block-wise max gap = eta_{k-1} - (r-1) eta_k at every N<=4e5 for 14 angles (golden, silver, random {1,2}, {1,3}, early-large-then-1, pi-digit-like), worst relative error 1.5e-6 (float64 accumulation); (b) at 1010 random (k,r,t) with q_k<=3000, the multiplicity of the largest class equals q_k - t and the other two classes match. 0 mismatches. The tiling claim (block (k,a_{k+1}) ends at q_{k+1}+q_k-1, next block starts at q_{k+1}+q_k) is right. Presentation GAP: the lemma is not proved in the text; it is only cited (Sos; Alessandri-Berthe; Leong) plus computer checks up to N<=2500. Since Prop. 3 uses the multiplicity q_k - t >= 1 and the exact largest-gap value, a one-paragraph derivation or an exact page/theorem number in the citation would remove the dependency.

6. N_{k,r} l_{k,r} = ((r+1)+s_k) q_k l - l, q_k l = (1-(r-1)t_k) q_k eta_{k-1}, q_k eta_{k-1} = 1/(1+s_k t_k) (from q_k eta_{k-1} + q_{k-1} eta_k = 1). Correct. Monotone in N inside a block because l is fixed. The max over N is at the block end. The `-1` correction vanishes. Silver check: (2+s)/(1+st) with s=t=sqrt2-1 gives 2.06066; r=2 gives 1.707. Matches.

7. r = ceil(a/2): (r+1+s) >= a/2, 1-(r-1)t > 1 - (a/2)/a = 1/2, denominator <= 2, so bracket >= a/8. Correct. limsup a_{k+1} = infinity iff unbounded.

8. Step-back: N' = N_{k,r} - j with j = ceil(eps q_k) stays in the block (t' = q_k - 1 - j >= 0, needs eps<1/2 and q_k large), largest gap unchanged, multiplicity j+1. D_{N'} >= (1-eps) D_{N_{k,r}} needs j/N_{k,r} <= eps, i.e. (eps q_k + 1)/(2 q_k - 1) <= eps, true for q_k >= (1+eps)/eps. Frequency n/N' >= eps/(A+2) since N' <= (A+1) q_k + q_{k-1} <= (A+2) q_k. Therefore m_{N'}(sigma) >= (eps/(pi(A+2)))((1-eps)(L-eps)-sigma) uniformly in (k,r). Every constant depends only on A and eps, so it is irrelevant whether the limsup is attained at one block type, several block types, or only along a subsequence of phases: the proof only needs infinitely many (k,r) with D_{N_{k,r}} >= L-eps, which the limsup gives. No counterexample. The remark that the converse "needs bounded N/q_k" is right.

   Numeric check (t2.py, exact class counts, quadrature in q): for golden, silver, [2,(1,2)^inf], [2,(1,3)^inf], [3,1,1,(2,2,1)^inf], [2,9,8,7,1,1,...], [2,(4,1,2,1)^inf], max over stepped-back N of E_N(c), k from 20 to 60 (q_k up to ~1e20):
   - c = 0.90 c_cov: E = 0.7e-6 to 1.5e-6, identical across k (no decay).
   - c = 0.99 c_cov: E = 1e-12 to 1e-11, identical across k (positive, tiny, non-decaying).
   - c = 1.01, 1.05 c_cov: E = 0 exactly at all sampled N.
   For the period-4 case blocks k and k+1 alternate between extremal and non-extremal phases (E = 0 at non-extremal k), as predicted by a limsup rather than lim.

9. Unbounded: Theorem C(2) gives limsup V_N >= W(c) > V_delta(c) >= a^2 for every c>0 (V_delta = a^2 for c>=pi Q, so strictness comes from W>V_delta). With Theorem A and Lemma 2, limsup m_N(c/Q+delta) > 0 for some delta, hence m_N(sigma) not -> 0 for every sigma, Lambda = infinity. Correct, but it rests on Theorem C(2)/C.3 (not re-audited here; see PROOF_REVIEW.md).

10. Case split "a_{k+1}>=2 infinitely often" vs "a_k = 1 eventually" is exhaustive. First case: t_k < 1/a_{k+1} <= 1/2 and s_k in (0,1) (q_{k-1}<q_k for all k>=1 since a_1>=2), so (2+s)/(1+st) > 2 for every such k; the limsup is >= 2. Second case: beta noble, t_k = lambda exactly, s_k = [0;1,...,1,a_j,...] -> lambda, only r=1, limit (2+lambda)/(1+lambda^2) = (2+lambda)/(2-lambda) = 1+2/sqrt5 = 1.894427. So kappa = 1+2/sqrt5 iff noble, else >=2. The identity c_*(beta)/(pi Q) = 1/(sqrt5 lambda^3) = 1.894427 checks numerically. Brute force (t1.py) golden sup_{N>8000} N h_N = 1.89474, approaching from above as expected. The bound kappa>=2 is not sharp: a scan over 2,015,530 non-noble periodic words (period<=8, digits 1..6) gives min kappa = 2.060660 (silver and its repeats), so the true non-noble minimum is conjecturally silver, 2.0607 (not proved). Optional improvement only.

11. Interval constant at golden: brute force for N in [4181, 6765) gives sup N d_N = 1.17065 (target (1+3/sqrt5)/2 = 1.17082) and circular sup N*maxgap = 1.89415 (target 1.89443). Agrees with the document. The remark that Niederreiter's constant is not kappa/2 is correct (end segments, no wrap).

12. Theorem 1 uses Theorem A for every irrational beta and fixed c. THEOREM.md A.1 itself flags that index bookkeeping was checked "only for golden" and non-golden noble as an open item; the new result inherits that. Not a flaw of the new text, but the claim "every irrational beta" is only as strong as Theorem A. Also the md carries Theorem A label as "audited argument"; whether that covers all beta is outside this review.

## Literature (WebSearch / WebFetch, secondary only)
- Niederreiter 1984 (Colloq. Math. Soc. Janos Bolyai 34) and Drobot, "On dispersion and Markov constants", Acta Math. Hungar. 47 (1986) 89-93: interval dispersion D(alpha) = limsup N d_N; Drobot proves M(alpha) <= 4D(alpha) - 2 <= M(alpha) + 1/M(alpha) (M = Markov constant), gives a method for quadratic irrationals, and a counterexample to monotonicity of D vs M. Interval metric, not circular. Source: https://link.springer.com/article/10.1007/BF01299639 (abstract unavailable; relation as quoted from a secondary description in search results). Related: Ji-Lu, Monatsh. Math. 121 (1996) 69-77; Tripathi, Acta Arith. 63 (1993) 193-203.
- Aequat. Math. 97 (2023) 683-705, "Deviation from equidistance for one-dimensional sequences" (https://link.springer.com/content/pdf/10.1007/s00010-023-00958-x.pdf, text extracted): treats the circle and the max gap as dispersion, uses the three-gap theorem, but no limsup N*max-gap constant and no golden minimality statement (grepped full text: no match).
- arXiv 2404.16352 (one-dimensional quasi-uniform Kronecker sequences): badly approximable iff low dispersion / bounded mesh ratio; cites Niederreiter 1992 and Drobot 1986. No explicit 1+2/sqrt5. (PDF text extracted; mesh ratio bound 2+2 sup a_j is a different quantity.)
- Ramshaw (Indag. Math. 40 (1978) 527-541, "On the gap structure of sequences of points on a circle"), Schoissengeier, and a direct search for 1+2/sqrt5 returned nothing retrievable. Not read; cannot be excluded.
- Conclusion: no primary source found proving (2). That is not novelty certification. Risk: Drobot's method for D(alpha) plausibly adapts to the circular max-gap in a few lines; a referee who knows that literature may call Prop. 4 folklore. Recommend keeping the existing hedge ("we do not claim novelty; Nie84 / Drobot not read") and, if possible, reading Drobot 1986 and Ramshaw 1978 from a library copy before submission.

## Remaining actionable points (none change a truth value)
1. Add a short proof or exact theorem number for the multiplicity statement of the three-gap lemma.
2. State explicitly that Theorem 1 inherits the scope of Theorem A (incl. its non-golden noble bookkeeping note).
3. Optionally record that the sharp non-noble minimum appears to be the silver value 2.0607 (computational, period<=8, digits<=6).
4. Optionally say that in Prop. 3 the requirement eps in (0,1/2) and q_k >= (1+eps)/eps are what make the step-back stay in the block and lose at most the factor 1-eps.
