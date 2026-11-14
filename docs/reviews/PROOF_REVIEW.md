# Adversarial review of docs/THEOREM.md and certify.py

Reviewer: Claude Sonnet 5.5, 2026-11-14. Scratch scripts: `docs/reviews/proof_review_scratch/` (s1..s6).
Labels: CORRECT / GAP (fixable) / ERROR. No ERROR found.

## Item verdicts

1. **A.1 exact two-branch structure: CORRECT, one GAP in N_0.**
   - Algebra checked: line distance `|r cos δ - a|`, arcs `±[d₋,d₊]`, and the `F(φ-d̄)F(φ+d̄)` reduction, including `φ-θ_j ∈ ±[d₋,d₊]` ⇔ `|φ∓d̄-θ_j| ≤ h`.
   - Wrap-around at δ near ±π is harmless: cos δ < 0 there, so it lies outside `[(a-w)/r,(a+w)/r]`.
   - s1_foot.py compared brute finite-segment distance against the two-arc rule at 6 radii each for 5 (α,N,c) cases, on 20000 angles per radius. There were 0 mismatches for every radius with r > a+w and w < ε/2. The only mismatches were at r ≤ a+w or w ≥ ε/2, outside the stated regime.
   - GAP: the bound `r|sin δ| ≤ √(r²-(a-w)²)` uses d₊ ≤ π/2, i.e. w ≤ a. N_0 enforces only w < ε/2, and ε < (1-a)/3 does not force ε/2 < a. Example: a = 0.05, ε ≈ 0.3167, w = 0.158 gives a-w < 0. If d₊ > π/2 the maximum of `r sin δ` is r, not `√(r²-(a-w)²)`. Fix: add `w < a` (and `1-ε < Q`) to N_0. This is asymptotically vacuous.
   - Nit: the condition `(1-ε)²-(a-w)² < Q²` is exactly what is needed for `sup r|sin δ| < Q`. It is correct and, given w < a, sufficient.

2. **A.2 layers: CORRECT.**
   - U_N = 1 for r < a-w holds since `|r cos δ - a| ≥ a-r > w`.
   - Total bound: the actual constant is `4ε+4w`, since `2(a+ε)(ε+w) ≤ 2(ε+w)` and the r < a pieces differ by `a²-(a-w)² ≤ 2w`. With w < ε/2 this is ≤ 6ε, so the stated `6ε+2w` holds.

3. **A.3 L¹ almost-invariance: CORRECT.**
   - `θ_j+2α = θ_{j+1}`, so only the arcs at θ_0 (removed) and θ_N (added) change. The bound `2s/(πN)` is right, including overlaps.
   - Fourier convention: `F(·-2α)^(k) = e^{-2ikα}F̂(k)` with `F̂(k) = ∫F e^{-ikφ}dφ/2π`. The factor `e^{-2ikα}-1 ≠ 0` iff `kβ ∉ Z`. This uses only irrationality of β, with no Diophantine input.

4. **A.4 Parseval and integration by parts: CORRECT.**
   - `C(t) = Σ|F̂(k)|² e^{ikt}` holds for real F.
   - `Σ|F̂|² = ∫F² = ∫F = m_N(s)`, and `F̂(0) = m_N(s)`.
   - Integration by parts: `ψ_N' = Σ` of two positive terms `(a±w)/(r√(r²-(a±w)²)) > 0`, and ψ_N'' is bounded by analyticity on the compact set. B_ε is therefore uniform in N, J and k. The tail bound `Σ_{|k|>K}|F̂|² B/|k| ≤ B/K` is valid.

5. **A.5 unfreezing and limit order: CORRECT.**
   - `‖F_s-F_t‖₁ ≤ |s-t|/π`, the factor 2 for C, and the factor 2 for m² are all right.
   - No hidden uniformity in s is needed. The bin values s_i are finitely many fixed numbers, so A.3 is applied only at fixed s. `sup_{s≤S}` in A.3 is stronger than required.
   - The limit order is legitimate: L is fixed before K and N, and the constants (η, B_ε) do not depend on N.
   - Numerics (s6_thmA.py, brute 2D area vs Ṽ_N, c = 2): the difference is `-0.034,-0.023,-0.015` at N = 34, 55, 89 (golden), and similar for non-golden β. It decays roughly like 1/N, consistent with the theorem (no rate is claimed).

6. **B.1 three-distance law and certify.py: CORRECT.**
   - Counts sum to N, and the lengths sum to 1 via `λ^{m-2} = λ^{m-1}+λ^m`.
   - The rotation matches: θ_j is a translate of `2π{jβ}`, β = λ² ≡ -λ, and reflection preserves gaps.
   - certify.py was audited:
     - `sign` was tested on 200000 random (p,q) against 80-digit mpmath, with 0 mismatches, including `sign(0,0) = 0`.
     - `frac_point` matches mpmath for all j tested, and the floor identity `⌊(t-j)/2⌋` with `t = ⌊j√5⌋` is valid for j ≥ 1.
     - The wrap gap and the Fibonacci index (`m = max{i: F_i ≤ n}`) are right.
     - Equality is on exact `(p,q)` tuples, and `want` merges equal powers.
   - The check is not vacuous: two mutants (wrong gap power, one perturbed point) were both caught, and `three_gap_exact(600)` passes. I did not rerun N = 3000.
   - The citation "Leong arXiv:1712.03758 Thm 3" could not be verified offline. Exact verification up to 3000 plus the sum identity is the actual evidence, and a proof for all N would need an induction or a citation.

7. **B.2 uniform convergence and limit set: CORRECT, one GAP.**
   - Atoms `πF_mλ^{m-2}(1+x)λ^i → u(1+x)λ^i` and weights `(λ-x, λ²+x, x)/(1+x)` match. `m_N(s) = π⁻¹Σ f_i(ℓ_i-s)_+` is exact. `E ℓ = π` was confirmed symbolically.
   - GAP: `x_N < F_{m-1}/F_m`, and this ratio alternates around λ. So x_N can slightly exceed λ, where `λ-x` is slightly negative. Fix: extend M_x continuously to `[0,λ+δ]`, or note that the weights are exact in finite N and the error is o(1).
   - The limit set is exactly `V([0,λ],c)`: the x_N are dense in [0,λ], V is continuous, and the image of the compact interval is an interval.

8. **B.3 D(x,s) table: CORRECT.**
   - Every row was recomputed symbolically with sympy (s2_D.py), exact identities all reducing to 0. Numeric spot checks at 7 values of x and 3 points per row gave 0 mismatches.
   - Breakpoints are continuous. D ≥ 0 on all rows for `0 ≤ x ≤ λ` (row 3 needs `s ≤ uλ(1+x)`, true on its interval).
   - The atom ordering for `0 ≤ x ≤ λ` is correct: `(1+x)λ ≤ 1` ⇔ `x ≤ λ`.
   - `μ_λ = μ_0` is correct.

9. **B.4 strictness and threshold: CORRECT.**
   - Strict iff `0<x<λ` and `c < Qu(1+x)`, since `M_x+M_0 > 0` on `s < u(1+x)`.
   - `c_* = Qu(1+λ) = Qu/λ` because `1/λ = 1+λ`. Numerically `Qu = 3.42824` and `c_* = 5.54701`.
   - For `c ≥ c_*`, `V(x,c) = a²` for all x, so `V_N → a²`.
   - Part 4: `V(0,c) = a²` iff `c ≥ Qu`.
   - The certified values in B.5 match an independent mpmath quad (s5_limit.py) to 20 digits.
   - `certified_limit` was checked analytically: primitive `A²q²-4ABq+2B² ln q`, correct active-set selection, and the guards for undecidable breakpoints.

10. **B.6 noble extension: CORRECT, no index errors.**
    - Tested β = [0;3,1,1,...] (0.2764) and [0;2,2,1,1,...] (0.4198) with N = q_k+s, s up to 0.99 q_{k-1}, k up to 10 or 11 (s3_noble.py).
    - Exact gap counts `η_{k-1}: N-q_{k-1}`, `η_k: s`, `η_{k-2}: q_{k-1}-s` held in every case. Here `η_j = ‖q_jβ‖` with `q_0 = 1`.
    - `sup_s|m_N-M_{x_N}|` decays by about 1/λ² per k, from about 5e-3 to about 1e-5, so the same μ_x is the limit.
    - The identity `1+λ² = √5λ` gives `q_kη_{k-2} → 1/(√5λ²)`, as claimed.
    - Wording nit: the golden case in B.1 is β = λ² only (not λ > 1/2). The noble statement for a_1 ≥ 2 is B.6 and is correct.

11. **Other.**
    - Closed vs open sets: V_N uses `dist > w` (open uncovered set), F uses strict `>`. The boundary has measure zero, so this is consistent.
    - c = 0: V_N = 1 = Ṽ_N trivially. Theorem A needs c > 0 only for the asymptotics.
    - α near π/2 (a small): fine at fixed α; the constants degrade, which is the same w < a issue as item 1. No uniformity in α is claimed.

## Overall verdict

Theorem A and Theorem B, with the B.6 extension, are correct as stated. I found no ERROR, and the proof structure and constants stand. The only GAPs are two small regularity conditions:
- Add `w < a` and `1-ε < Q` to N_0 (A.1).
- Handle `x_N` slightly above λ in B.2.

Also unverified: the Leong citation, and the all-N proof of B.1, which currently rests on the N ≤ 3000 exact check.


---

# Round 2: Theorem C (uniform-gap envelope)

Scratch: `proof_review_scratch/r2_c2.py`, `r2_lemma.py`, `r2_W.py`, `r2_unb.py`. No ERROR. Three cosmetic GAPs.

1. **Closed form of V_δ(c), c < πQ: CORRECT.** With k = c/π, `2∫_k^Q q(1-k/q)² dq = Q²-4kQ+3k²+2k² ln(Q/k)`. This matches the stated formula, and a 200001-point quadrature agrees to 1e-11 (c = 0.3, 1, 2). V_δ = a² for c ≥ πQ.
   - C.1 is correct: Jensen gives `Σ(g-2s/N)_+ ≥ (2π-2s)_+`, so `m_N ≥ (1-s/π)_+`. The mean-gap identity is correct, and the monotone integrand gives `Ṽ_N ≥ V_δ`.

2. **C.2 two-distance formulas: CORRECT, one convention GAP.**
   - Verified in exact 80-digit arithmetic for 319 (β,k,r,s) cases over four types: [0;2,1,1,…], [0;3,1,5,1,9,…], [0;2,7,3,12,1,20,2,40,…] and [0;3,2,2,…].
   - Checked for `N = rq_k+q_{k-1}` (A: `N-q_k`, C: `q_k`), `N = q_k`, and the three-class law. The three-class law is `N = rq_k+q_{k-1}+s`, 0 ≤ s < q_k, with A = η_k (count `N-q_k`), B = η_{k-1}-rη_k (count s) and C = A+B (count `q_k-s`). There were 0 failures. The sum identity also holds.
   - GAP (cosmetic): THEOREM.md C.4 and manuscript §5 write "N-1 = rq_k+q_{k-1}+s'". If s' ∈ [0,q_k), this gives s = s'+1 ∈ [1,q_k], so the s = 0 two-distance times drop out of the stated range, and s = q_k is the next r. Everything is consistent if the ranges are stated as in my convention, and the lemma holds for all s. Fix: state "N = rq_k+q_{k-1}+s, 0 ≤ s < q_k" (all N ≥ q_1+q_0 are covered).

3. **C.3 limits and W > V_δ: CORRECT.**
   - Along N = q_k, `q_kη_{k-1} = 1-q_{k-1}η_k`, and `q_{k-1}η_k < q_{k-1}/q_{k+1} < 1/a_{k+1}`, so `V_N → V_δ`.
   - Along `r = ⌈a/2⌉`, `rq_kη_k ∈ (r/(a+2), r/a) → 1/2`. The other class has total length `→ 1/2` and frequency `→ 0`, so `m_N(s) → (1/2-s/π)_+ + 1/2` pointwise in s. Dominated convergence is valid (integrand ≤ q).
   - Numerics with a_{k+1} = 400: `m_N = 0.4992, 0.4976` at s = 2, 3, against M_W = 0.5.
   - `M_W > M_δ` on (π/2, ∞), which meets (c/Q, ∞) for every c. This includes c ≥ πQ, where `W = a²+Q²/4 > a²`. So V_N diverges for every c > 0 in the unbounded case.

4. **C.4 non-degeneracy, mass lemma and κ: CORRECT, with slack.**
   - Frequency of A: `q_{k+1}+q_k ≤ ((A₀+1)²+1)q_{k-1} ≤ (A₀+1)(A₀+2)q_{k-1}`, so the frequency is ≥ ε. The total frequency of B and C is `q_k/N > 1/(A₀+2)`, since `N < q_{k+1}+q_k`.
   - The ratio claims are right.
     - `C/A = 1+B/A ≥ 1+η_{k+1}/η_k`.
     - `η_{k+1}/η_k ≥ 1/(A₀+1)`, and `η_k/η_{k+1} ≥ 1+1/(A₀+1)`.
     - In case B/A: if r = a_{k+1}, A/B ≥ 1+1/(A₀+1); otherwise B/A ≥ 1+1/(A₀+1).
   - Mass lemma: `(1+ε)(1-τ) ≥ 1+ε/2` uses `ε(1+ε) ≤ 2`, which is fine. The case where the smaller atom is ≤ π(1-τ) is trivial since its frequency is ≥ ε. The identity `π(m-M_δ)(s) = E(s-ℓ)_+` (valid for s ≤ π, since Eℓ = π) gives `≥ (ε²/4)(πε²/8) = πε⁴/32`.
   - Final κ: `(m+M_δ) ≥ (m-M_δ)` gives integrand ≥ (ε⁴/32)² on a q-interval of positive length (c < πQ), independent of N.
   - Numerics (r2_lemma.py, 40 random bounded-type β with A₀ ≤ 8, N up to 3000, step 7): 0 violations of "two atoms of frequency ≥ ε with ratio ≥ 1+ε". The mass was ≥ 75× the ε²/4 bound.
   - GAP (cosmetic): the manuscript's one-line statement "1/(A₀+2) ≤ η_{k+1}/η_k ≤ (1+1/(A₀+1))⁻¹; either class differs from A by ≥ 1+ε" omits the case split on r = a_{k+1} versus r < a_{k+1} and the C-versus-B choice. THEOREM.md has it. Add it to the manuscript.

5. **Corollary (badly approximable ⇔ liminf > V_δ for c ∈ (0,πQ)): fully justified.**
   - (⇒) is part 3.
   - (⇐) is the contrapositive of part 2: unbounded gives liminf = V_δ.
   - Theorem A is only needed to transfer liminf of Ṽ_N to V_N, and it holds for every irrational β.
   - The restriction to c < πQ is needed, since for c ≥ πQ, V_δ = a². The corollary does not claim that case.

6. **manuscript/main.tex §4–5 versus THEOREM.md: consistent.**
   - Statements, the formula for V_δ, W, ε, τ and the ε⁴/32 bound all match.
   - The only differences are the cosmetic points in 2 and 4 above.
   - The B.6 and B.2 patches (min(x_N, λ)) are reflected in §golden.

**Round 2 overall:** Theorem C is correct as stated. No ERROR.
