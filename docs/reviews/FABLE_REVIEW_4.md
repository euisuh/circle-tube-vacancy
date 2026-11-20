# Fourth-round review: layout rewrite (bfd47da → HEAD)

Reviewer: Claude Fable 5.1, 2026-11-20. Sources: `git diff bfd47da HEAD -- manuscript/main.tex manuscript/sections/*.tex` (read in full), `docs/reviews/STYLE_GUIDE.md`, compiled `manuscript/main.pdf` (28 pp., built 17:31 KST, same minute as the last source edit; `pdftotext` shows no `??`). Page map: §1 pp. 1–3, §2 p. 4, §3 pp. 5–7, §4 pp. 8–9, §5 pp. 10–18 (§5.2 three-distance pp. 11–14, §5.3 corollaries pp. 14–18), §6 pp. 19–21, §7 pp. 22–25, §8 p. 26, §9 + App. A p. 27, refs p. 28.

Labels: **classical**, **audited argument**, **hypothesis**, as in earlier rounds. Every changed statement and proof step was compared line by line against bfd47da; no numerics rerun.

---

## 1. Mathematical equivalence (audited argument)

Known intentional changes confirmed: thm:B/thm:C label swap (all `\ref`s, the notation table, `related.tex`, both figure captions and the dispersion file header follow); Lemma 3.2(1) "s_N/c is the mean of −∂_tζ" (correct: s_N = (c/2w)∫(−∂_tζ)dt); Theorem C(3)/(4) split with "This is (3)… This is (4)" in the proof and "(2) follows from (3)" still valid; Table 1 truncated to 12 decimals, caption says so.

Other changes found, none altering a conclusion:

| Where | Change | Verdict |
|---|---|---|
| Thm B proof, Step 4 | Case analysis replaced by a citation of Cor. 5.7(iii), ratio bound stated as 1+1/(A_0+1) ≥ 1+ε. bfd47da argued the first two cases via η_{k+1}/η_k ≥ 1/(A_0+2), i.e. a weaker 1+1/(A_0+2). | Equivalent and now sharper; Cor. 5.7(iii) (unchanged since bfd47da) already proves the stronger bound via (i). Fine. |
| Thm B proof, Step 3 | Frequency bounds now cited from Cor. 5.7(ii) with the explicit guard "for large N we have k ≥ 1". | Cor. 5.7 assumes k ≥ 1; the guard was implicit before. Improvement. |
| Thm B proof, Step 5 | Claim (eq:mass) isolated; "if (eq:mass) fails the larger atom exceeds π(1+ε/2)" retained; Jensen(3) rewritten as (1/π)∫(s−ℓ)_+dμ_N. | Checked: (1+ε)(1−τ) ≥ 1+ε/2 for ε<1; τ·πτ/2 /π = τ²/2 = ε⁴/32. Same constants as before. |
| Thm C proof, Step 4 | "η_k/η_{k−1} → λ" became "= λ (k ≥ k_0)". | True and already in Cor. 5.9(ii) (ξ_k = [0;1,1,…] exactly). Strengthening of a side remark, not of a hypothesis. |
| Lemma 3.2 statement | Constant c'_ε added to the list of constants. | Was used but undeclared in bfd47da. Fix. |
| §7 after Lemma 7.2 | "By Cor. 5.5, q_kη_{k−1} = 1/(1+ω_kξ_k), ξ_k < 1/a_{k+1}". | First identity is Cor. 5.5(i) divided by q_kη_{k−1}; the bound ξ_k < 1/a_{k+1} is from (gap:eq:xi), not from Cor. 5.5. Harmless mis-citation; change "By Corollary 5.5" to "By Corollary 5.5(i) and (5.x)" (the ξ display). |
| §7 Thm 7.3 proof (ii) | "(ii) follows from Λ ≥ L" became "follows once we know Λ = L", with "Λ ≤ L is trivial" kept. | Equivalent. |
| §7 Prop 7.5 proof | "(1−ε)(L−ε) > σ" etc. displayed; "since q_k is large" added to j/N_{k,r} ≤ ε. | The largeness was already assumed ("Fix one with q_k large"); now explicit. |
| Thm 5.3 Step 1(b), third range | Inner variable renamed d → d'. | Avoids clash with the outer d. Fine. |
| §5.2 preamble | p_{k+1} recursion written out; (F1)/(F2) split into four numbered displays (gap:eq:det, sign, rec, F2). | Classical; all later `(F1)`/`(F2)` citations now point to the right numbered equation (checked each). |
| Remark 7.7 (Niederreiter) | Definition of d_N removed, replaced by a pointer to §2 where it is displayed. | §2 does display it. Fine. |
| Fig. 2 caption | Positivity ranges moved from caption to a paragraph after the proof of Thm C. | Same claims, same justification (Thm B(3) for c<πQ, V(0,c)>a² on [πQ,Qu)). |

Not found: any change to a hypothesis, quantifier, strict/non-strict inequality, index range or constant beyond the above. The abstract's dropped formulas (a², Vd(c), c_* value, κ ≥ 1+2/√5) are all restated in §1.

## 2. Readability vs the style guide

Display counts (`\[`, align, equation, multline): main 12→52, dephasing 11→41, dispersion 7→40, gaplemmas 4→75. Rules R1–R6 now hold everywhere I checked; the three-distance proof and Corollaries 5.6–5.9 are no longer formula walls, and every reused estimate is numbered. Density is now at or below the S1/S8/S9 band.

Over-correction, concrete (recombine into prose; each saves 2–3 lines):
- `dispersion.tex`: `V_N(c)−a²−E_N(c)→0`, `Λ = L ,`, `Λ=L(β);` (statement of Prop 7.5; the "that is" clause is the real content), `κ(β) ≥ 2 .` (Prop 7.6(ii)), `c ≥ c_cov(β),`, `q_δ = c/(c/Q+δ).`, `j := ⌈εq_k⌉, N' := N_{k,r}−j`, `D_N = max supp μ_N` (duplicates "largest atom" in the preceding words).
- `main.tex`: Thm B(1) and (3) one-relation displays are defensible under R7 but Thm B could read as in bfd47da for (1); `V(0,c) > a² = Vd(c).`; `{V(x,c): x∈[0,λ]}.` in Thm C(1); `A²q²−4ABq+2B²log q .`
- `gaplemmas.tex`: `(N−q_k)+t+(q_k−t)=N.`, `N=q_k=a_kq_{k−1}+q_{k−2},`, the two `e = mη_k − nν ≥ η_k` / `≤ −ν` displays (one inline each would do), Thm 5.3 Step 3's two 2×2 aligns (prose was fine).
- `dephasing.tex`: `q(r)=√(r²−a²).` ; Lemma 3.2 items (1)–(3) each a bare display inside an `enumerate` (three items, three displays, 12 lines for what was 3).

Remaining dense spots: Thm 5.3 Step 2 "Consequently, for d∈[1,N−1], {dβ} ∉ cases …" plus the following cases display: correct but two stacked `cases` for one sentence; a 2×2 table would be shorter. §1 "Prior work" paragraph and §2 unchanged (pass).

## 3. Length

28 pp. in amsart 11pt/1.1in. UDT and Monatshefte reformat to their own class (Monatshefte ~ 10pt Springer, UDT ~ 10pt); expect ~20–22 pp. there. Not a hard problem, but 28 invites a "too long for the content" remark. Cuts, in order of pages saved at zero readability cost:
1. Move §5.2 (Thm 5.3 proof, pp. 11–14, ≈3.5 pp.) to an appendix, keep the statement and Remark 5.4 in §5. Saves nothing in total but moves 3.5 pp. out of the main line; referees reading UDT know the theorem.
2. Recombine the ~20 trivial displays listed in §2: ≈1 page.
3. Drop `[margin=1.1in]` and 11pt in favour of the class default (amsart 10pt, default margins): ≈4–5 pp. Journals reset this anyway; the author's PDF is only for the referees.
4. Remark 5.4 (Leong) and the "Equivalently, one may apply the theorem to λ…" paragraph after Cor. 5.8: ½ page together; both are optional.
Items 2–3 alone bring the author's PDF to ≈22 pp. without touching mathematics.

## 4. Verdict

Ready for the author's proof check. Mathematics is unchanged apart from the listed intentional corrections and two harmless strengthenings. Before submission: fix the Cor. 5.5 mis-citation in §7 (one word), recombine the trivial displays in §2, and decide on item 3 of §3. No rewrite needed.
