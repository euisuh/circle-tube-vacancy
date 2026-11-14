# Second-round referee report: "Shrinking tubes around a circular billiard orbit" (revision of 14 Nov 2026)

Reviewer: Claude Fable 5.1, 2026-11-14. Sources checked: `manuscript/main.tex` (417 lines),
`manuscript/sections/{related,dephasing,gaplemmas,dispersion}.tex`, `manuscript/figures/geometry.tex`,
the compiled `manuscript/main.pdf` (17 pages, built 18:09 after the last source edit; `main.log` read),
`docs/reviews/DISPERSION_REVIEW.md`, `docs/reviews/LIT_ROUND3.md`, `docs/DISPERSION.md`, and the live
state of the GitHub remote (`gh repo view`, `git ls-tree origin/...`). Every new proof (Theorem 5.3,
Corollaries 5.5–5.9, Lemmas 7.1–7.5, Propositions 7.6 and 7.8) was re-derived by hand; nothing was rerun.

Labels: **classical**, **audited argument**, **gap**, **hypothesis**, as before.

Correction to my first report, acknowledged up front: I wrote that c_* equals πQ times
Niederreiter's dispersion constant. That was wrong. Niederreiter's d_N lives on [0,1] with the
Euclidean metric and the golden value is (1+3/√5)/2 ≈ 1.1708; the manuscript's κ is the circular
largest-gap constant, 1+2/√5 ≈ 1.8944 for noble angles. The revision handles this correctly: it
defines κ(β) on the circle, proves the minimality statement itself (Proposition 7.8) from the
three-gap block formula, and states in Remark 7.10 that the two constants differ. That is the right
treatment and it strengthens the paper: the all-angle threshold (Theorem 7.3) is now a theorem,
not a citation.

---

## 1. Status of the first-round items

### Must

| # | Item | Status | Where / what remains |
|---|---|---|---|
| 1 | Abstract overclaim (restriction c < πQ) | **resolved** | abstract (i) now reads "for 0<c<π sin α" |
| 2 | Prove Lemma 6 (two-gap times) and Lemma 7 (golden law); state Fibonacci convention | **resolved** | `sections/gaplemmas.tex`: Theorem 5.3 (self-contained three-distance proof in the N-point convention, level drop avoided by allowing s=0), Cor. 5.6, Cor. 5.8 (F_1=F_2=1 stated), Cor. 5.9. I re-derived Steps 1–3 of Theorem 5.3 (successor analysis, lattice/Cramer argument, both s≥1 and s=0 branches) and all corollaries: correct. |
| 3 | Define μ_N, write π m_N(s)=∫(ℓ−s)_+ dμ_N | **resolved** (with duplication) | Section 5.1 / Lemma 5.2. It is defined a second time in the preamble of Section 7 (`dispersion.tex` lines 7–17); delete the second copy. |
| 4 | Remove "whose completeness we prove in the repository" | **not resolved** | `main.tex` line 289–291, Section 8 "Monte Carlo" paragraph, unchanged |
| 5 | Dispersion connection; fix MS03 authors; cite BK, FS; read Coelho/DK; drop "could not read"; mention Dupain | **mostly resolved** | New Section 7 (correct, see §2). `MS03` now Caglioti–Golse. BK93, FS02, Don12, Dup79, Nie84, Dro86, Tab05 added. DK24 read (LIT_ROUND3). Remaining: (a) `related.tex` line 50 still says "This reflects a bounded search" and line 31 says the constant 1+2/√5 is "a value recomputed numerically" although Prop. 7.8 now proves it; (b) `dispersion.tex` Remark 7.10 ends "We did not read \cite{Nie84}; we do not claim..." — apology language of the kind I asked to remove; (c) Coelho04 is still cited from its abstract only (LIT_ROUND3: full text not retrieved); the sentence in Section 2 is consistent with the abstract, so acceptable, but Dupain is cited only in passing and not next to the Fibonacci-minimality result. |
| 6 | Public repository link; AI-use disclosure | **partially** | AI disclosure present and adequate. The URL `https://github.com/euisuh/circle-tube-vacancy` resolves, but **the repository is PRIVATE** (`gh repo view --json visibility` → `PRIVATE`) and the only pushed branch is `codex/research-continuity` (no `main`). A reader cannot access it. Make public (or Zenodo DOI) before submission. |
| 7 | Unify theorem numbering | **resolved** | Theorems A (dephasing), B (envelope), C (golden) in order of appearance; Theorem 7.3 and Props. 7.6/7.8 section-numbered. Source labels are swapped (`thm:C` = Theorem B, `thm:B` = Theorem C) — maintenance hazard only. |

### Should

| # | Item | Status |
|---|---|---|
| 8 | C² justification for ψ_N; explicit layer accounting | **resolved** (Lemma 3.2 with real-analyticity on the compact K; Step 0 itemized, 4ε+2w) |
| 9 | One-line proof of q_{k+1}+q_k ≤ (A_0+1)(A_0+2) q_{k−1} | **resolved** (Cor. 5.7(ii)) |
| 10 | Figure 3 caption: dashed curve positive for c<Qu, not c<πQ | **not resolved** (`main.tex` line 279; the plot itself shows the dashed curve vanishing near 3.4, after the πQ marker at 2.93, so the caption contradicts its own figure) |
| 11 | MSC, keywords, e-mail, remove "Draft of", DOIs, journal versions | **partially**: MSC and keywords added; `\date{Draft of 14 November 2026}` still there; no e-mail; no DOIs; Ram14 still arXiv-only (Acta Arith. 170 (2015) exists); Leong17 arXiv-only |
| 12 | Number/caption the two numerics tables; state sample size per seed | **not resolved** (both tables in Section 8 are bare `center` environments; "Four million points" is stated for the main run only) |
| 13 | Motivation paragraph | **not resolved** |

### Nice

14 (α∈(π/2,π) reflection): not done. 15: Figure 3 now marks πQ and c_* (good); Qu not marked; no silver example in Section 8 (silver appears only in Section 7.1 and Remark 7.9). 16 (convex-order phrase): unchanged. 17 (rate): not attempted, fine.

---

## 2. Correctness of the new material

### Section 5 (gap lemmas) — audited argument, holds.

- Theorem 5.3. Uniqueness of (k,r,s): the intervals I_k=[q_k+q_{k−1}, q_{k+1}+q_k) tile [1,∞); checked. Step 1(a): d_++d_- ≥ N, both sign cases; checked. Step 1(b): the three successor ranges and the four "no shorter forward step" arguments; checked, including the boundary claim that the candidate (d_+−d_-)β has fractional part Δ_++Δ_- < 1. Step 2: b_1=(q_k,ση_k), b_2=(d_ρ,−σw), determinant −σ, Cramer m=dw+d_ρe, n=η_kd−q_ke; the two sign cases; checked. Step 3: s≥1 with ρ=r (needs N ≤ d_r+q_k, true since s ≤ q_k−1) and s=0 with ρ=r−1 (d_ρ ≥ q_{k−1} ≥ 1 for k≥1); checked. Case k=0 separate; checked.
- Cor. 5.5: 1/(q_kη_k) = q_{k+1}/q_k + η_{k+1}/η_k; checked.
- Cor. 5.6(ii): N=q_k is (k−1, a_k, 0); k=1 falls under the k=0 case; checked.
- Cor. 5.7: (i) both bounds on θ_{k+1}; (ii) N−q_k ≥ q_{k−1} ≥ q_k/(A_0+1), N < (A_0+2)q_k; (iii) the three ratio cases; checked. The main-text proof of Theorem B(3) uses the weaker lower bound 1/(A_0+2) ≤ η_{k+1}/η_k, consistent.
- Cor. 5.8: β=λ²=[0;2,1,1,…], q_j=F_{j+2}, η_j=λ^{j+2}; m=3 base case and K=m−3 general case; checked.
- Cor. 5.9: K=k−1 with r=1=a_{K+1}; contraction |f(x)−λ| ≤ λ|x−λ| gives θ_j=λ exactly; limits q_kη_{k−1}→1/(1+λ²)=1/(√5λ), q_kη_{k−2}→1/(√5λ²); and the trailing paragraph matches the family μ_x (largest atom weight (q_{k−1}−s)/N → (λ−x)/(1+x)); checked.

### Section 7 (coverage threshold) — audited argument, holds; dependencies and presentation gaps.

- Lemma 7.1 (mass bounds) and the "m_N(s)=0 iff s ≥ D_N" statement: checked.
- Lemma 7.2 (reduction E_N ↔ m_N(c/Q+δ)): both directions, monotonicity of m_N used correctly; checked.
- Theorem 7.3: (i) D_N ≤ L+δ/2 < c/Q+δ eventually ⇒ m_N(c/Q+δ)=0; (ii) via Λ=inf{σ: m_N(σ)→0} and Prop. 7.6; Λ ≤ L trivial. Checked. Note (ii) only gives limsup V_N > a², not divergence; the paper says exactly that.
- Lemma 7.4 is a verbatim restatement of Theorem 5.3 with s renamed t. The sentence "indexing shifted by one point as in Theorem B and Theorem 5.3" is wrong: Theorem 5.3 is already in the N-point convention, no shift is involved. The computer check "for all N ≤ 2500" is superfluous once Theorem 5.3 is proved. Replace the lemma by "By Theorem 5.3, in the block (k,r) the largest gap is ℓ_{k,r}=η_{k−1}−(r−1)η_k with multiplicity q_k−s ≥ 1."
- Lemma 7.5: N h_N = N ℓ_{k,r} increases in N within a block; N_{k,r}=(r+1)q_k+q_{k−1}−1; the formula (r+1+s_k)(1−(r−1)t_k)/(1+s_kt_k) via q_kη_{k−1}=1/(1+s_kt_k); checked. Statement is phrased as a proof fragment ("Since … is attained at …, and"); restate as a lemma.
- Prop. 7.6, bounded type: step back j=⌈εq_k⌉ keeps the same largest gap with multiplicity j+1 ≥ εq_k; D_{N'} ≥ (1−ε)D_{N_{k,r}} requires q_k ≥ (1+ε)/ε (covered by "q_k large"); frequency ≥ ε/(A+2); the final bound is uniform in (k,r); checked. Unbounded type: the deduction from Theorem B(2) + Lemma 7.2 needs one sentence it does not have — for arbitrary σ take c=Qσ, obtain δ with limsup m_N(σ+δ)>0, and use monotonicity to get limsup m_N(σ)>0; and L=∞ via r=⌈a_{k+1}/2⌉ (bracket ≥ a_{k+1}/8); checked.
- Prop. 7.8: case a_{k+1} ≥ 2 infinitely often, r=1 gives (2+s_k)/(1+s_kt_k) > 2 using t_k < 1/2; noble case (2+λ)/(1+λ²)=1+2/√5; equality iff noble; checked. Remark 7.9 silver value 1+3√2/4: checked by hand (r=1 branch; r=2 gives (2+√2)/2 < it).
- Remark 7.10 (interval vs circle): correct, and consistent with LIT_ROUND3 and DISPERSION_REVIEW.
- Consistency: for golden, c_cov = πQ(1+2/√5) = πQ/(√5λ³) = c_* of Theorem C(3); Theorem C(3) "V_N → a² iff c ≥ c_*" agrees with Theorem 7.3. Abstract (iii) matches Theorem 7.3. Introduction's forward reference "Section 7 … Theorem 7.3 … Proposition 7.8" resolves correctly in the PDF.
- Dependency: Theorem 7.3 inherits the scope of Theorem A for every irrational β; Theorem A's proof in Section 4 is general (irrationality used once, Step 1), so no gap in the manuscript itself.

Errors found: none mathematical. Gaps: the one-sentence monotonicity step in Prop. 7.6 (unbounded case); Λ is defined inside a proof and then used in the statement of Prop. 7.6 — define it before Theorem 7.3.

---

## 3. New presentation issues

1. **Notation clash κ.** `main.tex` line 205 (proof of Theorem B(3), last sentence): "Ṽ_N(c)−V_δ(c) ≥ κ > 0" uses κ as a constant; Section 7 and the abstract use κ(β) for the largest-gap constant. Rename the constant (e.g. c_0 or γ).
2. **Internal repository paths in the paper.** Remark 5.4 cites `docs/reviews/gaplemmas_scratch/verify_output.txt`; Section 7.1 cites `docs/dispersion_scratch/disp_check.py` and `docs/DISPERSION.md`. These are working-notes paths (and the repo is private). Either move the verification mention into Appendix A with a stable path, or delete; a proved theorem does not need "we also checked it by computer".
3. **Duplication / length.** The paper grew from 8 to 17 pages. Duplicated statements: Lemma 6.1 = Cor. 5.8; Lemma 7.4 = Theorem 5.3; μ_N and the gap conventions defined in 5.1 and again at the start of Section 7; Lemma 5.2 and the display in the Section 7 preamble. Section 5.2 (2.5 pages proving the three-distance theorem) is classical material: keep the statement and the Leong remark in the body and move the proof to an appendix, or cite [AB98, vRav88] for Step 1 and prove only Step 2–3. With the duplicates removed and Section 7.1 folded into Section 8 the paper should return to about 13 pages.
4. **Apology language still present.** `related.tex` line 50 "This reflects a bounded search"; `dispersion.tex` Remark 7.10 "We did not read [15]". Replace by a plain statement: "We are not aware of a circular version of Niederreiter's minimality statement in the literature; Proposition 7.8 proves what is needed here."
5. **Stale claim.** `related.tex` line 31: 1+2/√5 "a value recomputed numerically" — it is proved in Proposition 7.8; say so and cross-reference.
6. **Tripathi** is cited in-text in Remark 7.10 ("see Tripathi, Acta Arith. 63 (1993)") without a bibitem. Add `A. Tripathi, A comparison of dispersion and Markov constants, Acta Arith. 63 (1993), 193–203`.
7. **Remark 7.7** last sentence ("No counterexample to the equivalence exists: the statement of Theorem 7.3 is an exact iff") is an internal note; delete.
8. **Section 9** should be updated against Section 7: what is open for non-noble bounded type is whether liminf V_N(c) < limsup V_N(c) for c < c_cov (Theorem 7.3 already gives limsup > a²), and whether the liminf is always at convergent denominators.
9. **Rendering** (PDF checked page by page): clean overall; Figure 1 (geometry) is legible and correct (two tangent directions φ∓d(r), stadium tube); Figure 3 now carries πQ and c_* markers. Minor: one underfull hbox in the Figure 3 caption (log line 774); two hyperref "Token not allowed in a PDF string" warnings from the `\\` in the title — add `\texorpdfstring` or drop the forced break; Corollary 5.5's displayed `\dfrac` inside a run-in statement stretches the line (page 9) — use `\frac` or a display; `\paragraph` heads ("Prior work.", "Monte Carlo.", "Deterministic integration.", "Certified constants.") render as unemphasized run-in text in amsart — use `\subsection*` or `\emph`. Page 17 is a near-empty tail; fine.
10. **Front matter**: `\date{Draft of …}` still present; no e-mail; the address "Republic of Korea Air Force" with no department or e-mail will draw an editorial query.
11. Figure 3 caption error (Should 10 above) now contradicts the figure's own curve; fix the caption to "positive for c<Qu≈3.43 (Theorem C(3)); Theorem B(3) guarantees positivity for c<πQ".

---

## 4. Novelty and significance (update)

The dispersion revision changes the headline for the better. The paper now has: (a) the exact planar reduction (Theorem A); (b) the bounded-type dichotomy (Theorem B); (c) the all-angle coverage threshold c_cov(β)=πQ κ(β) as an exact iff (Theorem 7.3), with κ minimal exactly for noble angles (Prop. 7.8); (d) the full golden limit set and Fibonacci minimality (Theorem C). Item (c) is, as DISPERSION_REVIEW and LIT_ROUND3 record, not found in the literature in its circular form; the closest results are interval-metric (Niederreiter 1984, Drobot 1986, Tripathi 1993). The hedge that a specialist may consider Prop. 7.8 folklore is appropriate and is now stated in acceptable form once the "we did not read" sentence is rewritten. The three-distance proof in Section 5 is classical and adds nothing new; its value is only self-containment of the N-point convention.

---

## 5. Venue recommendation (update)

Unchanged in ranking, slightly stronger in fit:

1. **Uniform Distribution Theory** — best fit; the dispersion section lands squarely in scope (distribution of {nα}, dispersion, continued fractions). Realistic.
2. **Monatshefte für Mathematik** — good fit; Ji–Lu's dispersion paper appeared there (121 (1996)), which gives a natural hook.
3. **Journal of Number Theory** — Don (2012) precedent; moderate.
4. **Acta Arithmetica** — now borderline rather than desk-reject, because of Theorem 7.3/Prop. 7.8 and Tripathi (1993) precedent; still a long shot given the modest depth.
5. Nonlinearity / J. Stat. Phys. — lower, unchanged.

arXiv: math.DS primary, math.NT cross-list.

---

## 6. Verdict

**Minor revision.** The mathematics is correct: every new proof (Theorem 5.3 and corollaries; Lemmas 7.1–7.5; Propositions 7.6, 7.8) was re-derived and holds, and the dispersion treatment now correctly distinguishes the circular constant from Niederreiter's interval constant and proves what it uses. Five of my seven must-items are resolved. What blocks submission is mechanical: the private repository, the "prove in the repository" sentence, the κ clash, internal scratch paths and apology sentences in the text, the Figure 3 caption, and duplicated lemmas that inflate the paper. None of these require new mathematics.

### MUST before submission
1. `main.tex` line 205: rename the constant κ in the proof of Theorem B(3).
2. `main.tex` lines 289–291: delete "whose completeness we prove in the repository"; say the four-candidate reduction was validated against brute force (as `results/indep-REPORT.md` documents) or add a short lemma to Appendix A.
3. Make `github.com/euisuh/circle-tube-vacancy` public with a `main` branch (currently PRIVATE, only `codex/research-continuity` pushed), or deposit on Zenodo and cite the DOI.
4. `sections/gaplemmas.tex` Remark 5.4 and `sections/dispersion.tex` §7.1: remove the `docs/...` scratch paths and the "checked by computer" sentences, or relocate to Appendix A with stable repo paths.
5. `sections/dispersion.tex` Lemma 7.4: replace by a reference to Theorem 5.3; delete the wrong "indexing shifted by one point" clause.
6. `sections/dispersion.tex` Remark 7.10 last sentence and `sections/related.tex` line 50: remove "We did not read" / "bounded search"; `related.tex` line 31: replace "recomputed numerically" with a reference to Proposition 7.8.
7. `main.tex` line 279: Figure 3 caption, c<Qu not c<πQ.
8. `main.tex` line 22: remove "Draft of".

### SHOULD
9. Define Λ before Theorem 7.3; add the monotonicity sentence in the unbounded case of Prop. 7.6; restate Lemma 7.5 as a statement.
10. Delete Lemma 6.1 (cite Cor. 5.8 directly), the duplicate μ_N definition in Section 7, Remark 7.7's last sentence; move the proof of Theorem 5.3 to an appendix.
11. Add Tripathi (1993) bibitem; DOIs; Ramírez journal version; e-mail.
12. Number and caption the Section 8 tables; state points per seed.
13. Update Section 9 against Theorem 7.3; one motivation paragraph in Section 1.
