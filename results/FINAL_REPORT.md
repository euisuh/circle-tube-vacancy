# Final research report — 2026-11-14 (Claude Code goal session)

## Outcome

The active candidate survived proof review and was strengthened into three theorems
(complete proofs: `docs/THEOREM.md`; manuscript: `manuscript/main.tex`, compiled `main.pdf`).

| Result | Statement (fixed irrational β=α/π, half-width c/N) | Status |
|---|---|---|
| A, dephasing | V_N(c) = a² + 2∫₀^Q q·m_N(c/q)² dq + o(1), m_N = circle vacancy of rotation orbit | Proof; adversarial review: no error, 2 gaps fixed |
| B, golden/noble | limit set = {V(x,c): x∈[0,λ]}; liminf = Fibonacci limit V(0,c) (convex order); limsup>liminf ⇔ c<c_*=πQ/(√5λ³)≈5.547; V_N→a² for c≥c_* | Proof; reviewed; noble extension checked numerically by reviewer |
| C, all irrationals | liminf V_N ≥ V_δ(c) (uniform gaps); = iff unbounded partial quotients (then divergence ∀c>0); strict for bounded type if c<πQ | Proof; round-2 review: no error, 2 cosmetic gaps fixed |

Strict separation of golden limits is now a theorem (B.3–B.4), not a float comparison.
Certified (mpmath interval, 50 digits): V(0,1)=0.336226129522972…, V(1/3,1)=0.338140371722238…,
V(0,2)=0.156461653859154…, V(1/3,2)=0.162173010171056…, c_*=5.547008255803426….

## Evidence

- `certify.py` → `results/certify-golden.json`: exact Z[λ] three-distance law for every 2≤N≤3000; interval limits.
- 13 unit tests pass (`results/goal-tests.log`), incl. 3 new (exact gap law, interval vs float, convex-order minimality).
- Independent integrator (`independent/`, `results/indep-REPORT.md`), written from spec: agrees with saved MC (|z|≤0.73); V_N−V(x_N,c) ≈ −0.72/N at c=1 (≈ −2ac/N caustic-disk deficit); block minimum at Fibonacci for m=20,21.
- 20-seed paired MC (`results/seedsweep/SUMMARY.md`): pooled z 0.91 (c=1), 1.43 (c=2) vs deterministic finite-N; an earlier 4-run +2.6σ flag was chance.
- Source hashes: `results/goal-hashes.txt`. `circle_research.py` unchanged (verified-full run still valid).

## Originality / significance (independent agent, `docs/reviews/LITERATURE_REVIEW.md`)

- Ingredients classical: three-distance counts (Leong Thm 3; Sós, Slater, van Ravenstein), uniform vs non-uniform fixed-angle laws (Coelho–de Faria 1996 Thm I), tightness ⇔ bounded type for hitting processes (Coelho 2004, abstract only), gap ratio ⇔ badly approximable (Ramírez §4).
- Dephasing argument routine for a specialist (almost invariance + Riemann–Lebesgue + Parseval).
- Not found in accessible literature: planar tube-vacancy formula, golden phase family with convex-order minimality and threshold, planar characterization of bounded type. Bounded search; not a novelty certificate.
- Rating: upper-end short note (e.g. Experimental Math / Monthly-type venue), not specialist paper. Drops to exposition if Coelho 2004 or Dzhalilov–Khomidov 2024 (unread) state the phase-x family.

## Remaining risks

1. Unread full texts: Coelho 2004, Dzhalilov–Khomidov 2024, Fan–Schmeling 2002, Alessandri–Berthé 1998.
2. Internal + agent review only; no human specialist has checked proofs.
3. No rate in Theorem A; bounded-type non-noble divergence open (block convex order fails numerically).
4. Floating-point numerics are evidence only; intervals certify only the golden constants.

## Next required decision (user)

Author metadata (manuscript has placeholder) and whether to pursue venue submission —
submission, posting and author contact need explicit approval. Before submitting, obtain the
two unread papers through library access.

## Revision round (same day, after user supplied author metadata)

- Author: Euisuh Jeong, Republic of Korea Air Force.
- Fable referee round 1: major revision (docs/reviews/FABLE_REVIEW.md); round 2 after revision:
  **minor revision** (docs/reviews/FABLE_REVIEW_2.md); its remaining must-fixes applied, except
  repository visibility (user decision).
- New theorem: coverage threshold for every irrational angle, V_N(c)→a² iff c≥πQκ(β);
  κ(β)≥1+2/√5 with equality iff noble (docs/DISPERSION.md; adversarial review
  docs/reviews/DISPERSION_REVIEW.md: no counterexample; not found in literature).
- Gap lemmas proved self-contained; Dzhalilov–Khomidov 2024 read: no overlap. Coelho 2004 still unread.
- Venues (Fable): Uniform Distribution Theory, then Monatshefte für Mathematik; Acta Arithmetica borderline.
- Repo: https://github.com/euisuh/circle-tube-vacancy (PRIVATE).
