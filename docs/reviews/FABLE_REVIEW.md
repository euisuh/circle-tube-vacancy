# Referee report: "Shrinking tubes around a circular billiard orbit" (draft of 14 Nov 2026)

Reviewer: Claude Fable 5.1, 2026-11-14. Independent pass; earlier reviews (`PROOF_REVIEW.md`,
`LITERATURE_REVIEW.md`) were not consulted before forming the verdicts below, only afterwards
for cross-checking citations. Every proof was checked against the text of `manuscript/main.tex`
(and the compiled PDF, 8 pages), not `docs/THEOREM.md`. Hand verification of all
inequalities and identities; no proof was delegated. Literature: 13 web searches (listed
in 3.1); no library access, so paywalled full texts were not read.

Labels used: **classical**, **audited argument** (I checked it and it holds), **gap**
(something a referee would require), **hypothesis**.

---

## 1. Summary of the claims (in my words)

Fix an irrational rotation number β = α/π ∈ (0,1/2) and take the first N chords of the
circular billiard orbit in the unit disk with reflection data α. All chords are tangent to the
caustic circle of radius a = cos α; their normals form a rotation orbit θ_j = (2j+1)α. Let
V_N(c) be the normalized area of the disk at distance > c/N from the union of the N finite
chords.

- **Theorem 1 (A, dephasing).** V_N(c) = a² + 2∫_0^Q q·m_N(c/q)² dq + o(1), where
  m_N(s) is the uncovered fraction of the circle by N arcs of half-length s/N centred at the
  θ_j, and Q = sin α. The planar observable reduces to the *square* of a one-dimensional gap
  functional; the square appears because a point at radius r is covered through two angular
  branches φ ± arccos(a/r), and radial integration over the lag 2arccos(a/r) kills all
  nonzero Fourier modes of the autocorrelation of the vacancy indicator. No rate.
- **Theorem 2 (C, envelope).** With V_δ(c) the value for equal gaps: liminf V_N(c) ≥ V_δ(c)
  always; equality (and in fact divergence of V_N for every c) when the partial quotients are
  unbounded; strict inequality when they are bounded and c < πQ. Corollary: for fixed
  c ∈ (0, πQ), β is badly approximable iff liminf V_N(c) > V_δ(c).
- **Theorem 4 (B, golden/noble).** For β = λ², the set of limit points of V_N(c) is the
  interval {V(x,c): x ∈ [0,λ]} indexed by the Fibonacci phase x = (N − F_m)/F_m; the minimum
  is attained at x = 0 (Fibonacci times) by a convex-order comparison of the three-atom gap
  laws; V_N(c) converges iff c ≥ c_* = πQ/(√5 λ³) ≈ 5.547, and then to a². Same for all noble
  β.
- Numerics: Monte Carlo (4·10⁶ points, 20 seeds) and a deterministic angular-union
  integrator agree with the limits to the expected O(1/N) finite-size offset; golden-angle
  constants are certified by interval arithmetic.

---

## 2. Correctness

### Theorem 1 (Section 2–3) — audited argument, holds.

- **Lemma 1 (two branches).** Correct. The computation dist(x, line_j) = |r cos δ − a|,
  the window |δ| ∈ [d_−, d_+], and the tangential bound r|sin δ| ≤ √(r² − (a−w)²) < Q are
  all right; the standing hypothesis (1−ε)² − (a−w)² < Q² is exactly what is needed and is
  achievable for large N. The "off that set" direction is also right. (One cosmetic point:
  (a−w)/r ≥ 0 is used implicitly in "here (a+w)/r < 1"; w < a guarantees it.)
- **Eq. (2) autocorrelation form.** Correct: uncovered ⇔ F(φ − d̄)F(φ + d̄) = 1 with
  s = N h; shift gives C_{N,s}(2d̄). Boundary sets have measure zero.
- **Uniform convergence s_N → c/q, ψ_N → ψ in C².** Correct by analyticity of
  arccos((a ± w)/r) on I_ε × [−ε/2, ε/2]; ψ' = 2a/(rq) ≥ 2a/(1−ε) is a valid (loose) bound.
  *Gap (minor):* the C² statement is asserted, not argued; one sentence (real-analytic in
  (r,w) on a compact set, so all r-derivatives converge uniformly as w → 0) should be
  written since the integration-by-parts constant B_ε depends on it.
- **Layers.** The stated bound 6ε + 2w is true but its derivation is not shown. My
  accounting: |(a−w)² − a²| ≤ 2w; ∫_{a−w}^{a} 2r dr ≤ 2w; annulus [a, a+ε] ≤ 2ε + ε²;
  [1−ε, 1] ≤ 2ε; total ≤ 4w + 5ε ≤ 6ε + 2w using w < ε/2. *Gap (minor):* write it out;
  the text's phrase "both for V_N and for the right-hand side" hides the inner-disk
  term (a−w)² vs a².
- **Low modes.** Correct and clean: symmetric difference of F and its 2α-shift has
  normalized measure ≤ 2s/(πN), hence |e^{−2ikα} − 1||F̂(k)| ≤ 2s/(πN), and irrationality
  gives F̂(k) → 0 uniformly in s ≤ S for fixed k ≠ 0. This is the only place where
  irrationality enters.
- **High modes.** Correct. Parseval Σ|F̂|² = m_N ≤ 1; absolute convergence justifies
  exchanging sum and integral; van der Corput-style bound B_ε/|k| for ∫_J 2r e^{ikψ_N} dr
  by one integration by parts; tail ≤ B_ε/K.
- **Unfreezing.** Correct: L¹-Lipschitz in s with constant 1/π, so both C and m² are
  2/π-Lipschitz; mesh η gives 8η/π. The order of limits in Remark 3 is consistent.

Verdict on Theorem 1: complete modulo the two minor write-up gaps above. The argument is
standard (almost-invariance + Riemann–Lebesgue/van der Corput + Parseval), and the author
says so.

### Theorem 2 (Section 4) — audited argument, holds; presentation gaps.

- **Lemma 5 (Jensen).** Correct, including the identity 2π(m_N − M_δ) = Σ(2s/N − g_j)_+.
- **Lemma 6 (two-gap times).** Stated without proof, attributed to Leong Thm 3 with the
  N' = N − 1 shift. I verified every case: N = rq_k + q_{k−1} with r ≥ 2 (Leong r' = r−1,
  s' = q_k − 1), with r = 1 (which requires *dropping one level*: Leong r' = a_k,
  s' = q_{k−1} − 1 at level k−1), and N = q_k for a_k ≥ 2 and a_k = 1 (again a level drop,
  using η_{k−2} = η_{k−1} + η_k). All counts and lengths agree. Also
  1/(a_{k+1}+2) < q_kη_k < 1/a_{k+1} is right (from 1/(q_{k+1}+q_k) < η_k < 1/q_{k+1} and
  q_{k+1}/q_k < a_{k+1}+1). *Gap (must):* this bookkeeping is not obvious and is the
  kind of index shift that silently goes wrong; the lemma needs a proof paragraph with
  the level-drop cases spelled out.
- **Part (2), unbounded.** Correct. At N = q_k both scaled gaps lie in
  (1 − 1/a_{k+1}, 1 + 1/a_{k+1}); uniform convergence of m_N to (1 − s/π)_+ follows from
  1-Lipschitz of (·)_+. At N = ⌈a_{k+1}/2⌉q_k + q_{k−1}: class η_k has frequency → 1 and
  scaled length → 1/2, the sparse class has total mass → 1/2 and scaled length → ∞, so
  m_N(s) → (1/2 − s/π)_+ + 1/2 pointwise; dominated convergence (m_N ≤ 1, integrand ≤ 2q)
  gives W(c). Strictness W > V_δ is correct: the integrands differ on s > π/2, which meets
  (c/Q, ∞) for every c.
- **Part (3), bounded.** The three-gap statement for *every* N (gaps A, B, C with counts
  N − q_k, s, q_k − s in terms of the decomposition of N itself) is correct; I checked it
  against Leong's statement for N − 1 including the s = 0 edge cases (where class B is
  empty and the formula still returns the right multiset) and the sum identity
  (N − s)η_k + q_kB = 1. The frequency bound q_{k−1}/(q_{k+1}+q_k) ≥ ε uses
  q_{k+1} + q_k ≤ ((A_0+1)² + 1)q_{k−1} ≤ (A_0+1)(A_0+2)q_{k−1}; this one-liner is omitted
  (*gap, minor*). The ratio bounds 1/(A_0+2) ≤ η_{k+1}/η_k ≤ (1 + 1/(A_0+1))^{−1} are right
  (η_k/η_{k+1} = a_{k+2} + η_{k+2}/η_{k+1}). The three cases for E ∈ {B, C} are right.
  The mass lemma is right: (1+ε)(1 − ε²/4) ≥ 1 + ε/2 for ε ≤ 1, then
  ∫(π−ℓ)_+ = ∫(ℓ−π)_+ ≥ πε²/2 and ∫(π−ℓ)_+ ≤ πμ([0,π(1−τ)]) + πτ. The final bound
  m_N − M_δ ≥ ε⁴/32 on s ∈ [π(1−ε²/8), π] is right. Positivity of the q-set needs
  c/π < Q, i.e. c < πQ, as assumed.
  *Gap (must):* the "law of mean π" is never defined in the manuscript. The reader has to
  guess that μ_N = N^{−1}Σ_j δ_{Ng_j/2} and that π m_N(s) = ∫(ℓ − s)_+ dμ_N. Define it
  once (Section 4) and use it in Sections 4 and 5.
- **Corollary.** Follows from (2) and (3). Note the restriction c < πQ is essential:
  for the golden angle and c ∈ [Qu, c_*) one has liminf V_N = a² = V_δ with bounded type.
  **The abstract omits this restriction** ("equality exactly when the angle has unbounded
  partial quotients") and is therefore false as stated for c ≥ πQ. *Must fix.*

### Theorem 4 (Section 5) — audited argument, holds; one lemma unproved.

- **Lemma 7 (golden gap law).** Correct; I rederived it from the three-distance theorem
  for rotation λ (β ≡ −λ, reflection preserves gaps): N = F_m + k has level k' = m − 2,
  r = 1, s = k, giving A = λ^{m−1} (F_{m−2}+k), B = λ^m (k), C = λ^{m−2} (F_{m−1}−k).
  Sum check (F_{m−1} − k)λ^{m−2} + (F_{m−2}+k)λ^{m−1} + kλ^m = 1 holds. *Gap (should):*
  the manuscript gives neither this derivation nor the Fibonacci indexing convention
  (F_1 = F_2 = 1 is implied); the `Z[λ]` check to N = 3000 is evidence, not proof, and the
  proof is three lines, so write it.
- **Reduction to the phase.** Correct. Atoms πF_mλ^{m−2}(1+x_N)λ^i → u(1+x)λ^i with
  u = π/(√5λ²); weights → (λ − x, λ² + x, x)/(1+x); mean Σf_iℓ_i = u(λ + λ³) = π (I
  checked λ + λ³ = √5λ²). The clamp x_N ↦ min(x_N, λ) handles |F_{m−1}/F_m − λ| = λ^m/F_m
  (verified). The weight f_0 = (λ−x)/(1+x) is rational, not "polynomial", in x; harmless.
  Limit set = continuous image of [0,λ] = interval: correct.
- **Convex order (table).** I recomputed all five nonzero pieces of D(x,s) and the
  agreement at the four breakpoints (e.g. at s = uλ both middle rows give
  xuλ²(λ−x)/(1+x); at s = u both give xuλ(1+λ)(λ−x)/(1+x) using (1+λ)λ = 1). The atom
  ordering uλ²(1+x) ≤ uλ ≤ uλ(1+x) ≤ u ≤ u(1+x) holds exactly for x ≤ λ. D ≥ 0 and
  the strictness set are right. Note that "μ_x dominates μ_0 in convex order" is stated
  but only the test functions (ℓ − s)_+ are used; that is sufficient (they generate the
  convex order for laws with equal means), but say so or drop the phrase.
- **Strictness/threshold.** Correct: positivity iff (c/Q, ∞) meets (uλ²(1+x), u(1+x)),
  i.e. c < Qu(1+x); sup over x < λ gives c_* = Qu(1+λ) = Qu/λ = πQ/(√5λ³) ≈ 5.547
  (numerically confirmed). For c ≥ c_* all M_x vanish on (0, Q].
- **Noble angles.** Correct bookkeeping: N = q_k + s = 1·q_{k−1} + q_{k−2} + s at level
  k−1 with a_k = 1 gives A = η_{k−1}, B = η_k, C = η_{k−2} with the stated counts;
  q_kη_{k−2} → 1/(λ + λ³) = 1/(√5λ²). The sentence "the argument applies verbatim" is
  acceptable once Lemma 7's proof is written in the general three-distance language
  (then the golden case becomes the special case rather than the other way round).

### Numerics (Section 6) — reproduced numerical evidence (by the author's own files);
I did not rerun anything.

- Values in the tables match `results/indep-REPORT.md` and `results/seedsweep/SUMMARY.md`.
  The 20-seed pooled z of 0.91/1.43 resolves the +2.6σ flag in the independent report; the
  manuscript should state the sample size per seed (4·10⁶) and that the reference is the
  deterministic finite-N difference, which it does only implicitly.
- "whose completeness we prove in the repository" (four-candidate reduction): a proof
  that the Monte Carlo is exact cannot live outside the paper. Either put a short lemma
  in the appendix or drop the claim and say the reduction was validated against brute
  force (which is what `indep-REPORT.md` actually documents).
- Figure 2 caption: the dashed curve V(0,c) − V_δ(c) is positive for c < Qu ≈ 3.43, not
  only for c < πQ ≈ 2.93; Theorem 2(3) guarantees the latter. Reword.
- The −2ac/N offset explanation is plausible and consistent with the data; fine as
  stated (labelled as observation).

### Errors found: none mathematical. Gaps a referee would demand: Lemma 6 proof, Lemma 7
proof, definition of μ_N, abstract overclaim, C² assertion, layer accounting, "proof in
repository".

---

## 3. Novelty and significance

Honest breakdown:

- **Routine / classical:** three-distance counts (Sós, Świerczkowski, Slater, van
  Ravenstein; Leong's explicit form); the Jensen bound; the two-gap-time computations in
  Theorem 2(2); the uniform-vs-nonuniform dichotomy along subsequences (Coelho–de Faria
  Thm I is the 1-D analogue); "gap ratios bounded iff badly approximable". Theorem 1's
  mechanism is routine for anyone who has done almost-invariance Fourier arguments; a
  specialist would reconstruct it in an afternoon once told the statement.
- **Not routine but short:** the exact two-branch reduction on the trimmed annulus (Lemma
  1 plus the layer control, replacing the band approximation of earlier drafts); the
  non-degeneracy lemma in Theorem 2(3) with an explicit ε(A_0); the convex-order table
  showing the Fibonacci law is the minimum of the whole phase family; the explicit
  threshold c_*.
- **Possibly new as statements:** (i) the planar formula with the square of the 1-D
  vacancy; (ii) the planar characterization of badly approximable β by an area
  observable; (iii) the full limit set for noble angles and the convex-order minimality.
  I did not find these in print (searches listed in 3.1), and the author's own 2-round
  search found nothing either. Caveat: Coelho (2004) and Dzhalilov–Khomidov (2024) remain
  unread by the author; Coelho's abstract (checked: Trans. AMS 356 (2004), "tightness
  occurs iff the rotation number is of bounded type") is the 1-D ancestor of Theorem 2
  and must be positioned honestly as such.
- **Already classical, and not recognised by the manuscript:** the convergence threshold
  in Theorem 4(3). Ṽ_N(c) = a² exactly when c ≥ πQ·N·d_N, where d_N is the **dispersion**
  (largest gap, in turns) of {jβ}_{j<N}. Hence for *every* irrational β the full-coverage
  threshold is c_cov(β) = πQ·limsup_N N d_N, and V_N(c) → a² for c > c_cov (fails for
  c < c_cov). For noble β, Lemma 7 gives limsup N d_N = F_{m+1}λ^{m−2} → 1/(√5λ³) =
  1 + 2/√5 ≈ 1.894, which is exactly the factor in c_* = πQ/(√5λ³). That
  limsup N d_N ≥ 1 + 2/√5 for all irrational α with equality precisely for golden-type α
  is Niederreiter's dispersion theorem (H. Niederreiter, "On a measure of denseness for
  sequences", Topics in Classical Number Theory, Colloq. Math. Soc. J. Bolyai 34 (1984);
  see also Niederreiter's QMC monograph, Ch. 6). *Classical; constant confirmed by my
  arithmetic from Lemma 7; the author should verify the exact bibliographic form.*
  Consequences: (a) the "V_N → a² iff c ≥ c_*" half of Theorem 4(3) is a one-line
  corollary of Theorem 1 plus Niederreiter and should be presented that way; (b) a
  general corollary is available for free and strengthens the paper — *for every
  irrational angle, V_N(c) fails to converge to a² for some c ≥ c_*, and c_* is the
  smallest possible threshold, attained exactly by noble angles* — this is a better
  headline than the golden-only statement; (c) what remains genuinely the author's in
  Theorem 4 is the limit set below the threshold and the Fibonacci minimality.
- **Closest prior objects, not cited:** Blank–Krikorian's three-length theorem for linear
  flow on the torus minus a slit and the Caglioti–Golse three-strip partition
  (E. Caglioti, F. Golse, Comm. Math. Phys. 236 (2003) 199–221, arXiv:math/0301300),
  where a fixed irrational direction produces strips whose *areas* are continued-fraction
  data — the same mechanism as the author's three-atom gap law feeding an area integral.
  The manuscript cites this paper but under the **wrong authors** (entry `MS03` lists
  Marklof–Strömbergsson and a 2004 CMP volume; the arXiv number and title belong to
  Caglioti–Golse). Must fix. Henk Don, "Polygons in billiard orbits", J. Number Theory
  132 (2012) 1151–1163, treats truncated billiard orbits in a *rectangle* and the
  three/four-gap structure of the polygons they cut out; different table, same
  "truncated orbit + three-gap" theme — cite for context. Dupain (Ann. Inst. Fourier 29
  (1979)) and Dupain–Sós (1984) on the discrepancy of {nφ}, with its Fibonacci-time
  structure, are the natural precedents for "extremal behaviour at Fibonacci N" and
  should be mentioned in one sentence next to the convex-order result. Fan–Schmeling,
  "Coverings of the circle driven by rotations" (Växjö Univ. Press 2003, pp. 7–15) is the
  rotation-driven Dvoretzky covering problem; no copy is online, but it must at least be
  cited since the manuscript's m_N is exactly a finite-N version of that covering.

### 3.1 What I searched (2026-11-14, web search only, no library access)

Don "Polygons in billiard orbits"; Fan–Schmeling rotation coverings; Coelho 2004 abstract
(AMS page); Dupain 1979 (Numdam page); Niederreiter dispersion of {nα} (not directly
retrieved; constant corroborated arithmetically); Blank–Krikorian / Caglioti–Golse strips
(Golse survey arXiv:0906.0191, Section 6); Signerska-Rynkowska curlicues (Geom. Dedicata
216 (2022); ε-neighbourhood area of orbit curves, different regime); "convex order" or
"majorization" of three-gap distributions (no hit); circular-billiard chord coverage (no
hit beyond textbook caustic facts); venue scope pages for Uniform Distribution Theory and
Monatshefte. Not accessed: Coelho 2004 full text, Dzhalilov–Khomidov 2024, Fan–Schmeling
text, Niederreiter 1984 text, Alessandri–Berthé full text.

Significance: a coherent short paper with one clean mechanism (dephasing ⇒ square of the
mean), one dichotomy (bounded type), and one fully explicit example (golden). It is not a
specialist-level paper: the hard questions (rates; non-noble bounded type; whether the
liminf is always at convergent times; other tables/caustics) are left open and the author
says so. Publishable as a short research article in a second-tier number theory/dynamics
journal after the revisions below. Not a note-only result: the three theorems together are
more than an observation.

---

## 4. Presentation against the standard of a mathematics paper

Structure is sound (intro with all theorems, geometry, proofs, numerics, open questions,
reproducibility appendix) and the paper is pleasantly short. Problems:

1. **Theorem labels.** Theorems are called A, C, B in the source and appear as Theorem 1,
   2, 4 in the PDF, with the golden theorem (B) stated after the envelope theorem (C). Pick
   one scheme; either number 1–3 in order of appearance or use `\newtheorem{thmA}`-style
   lettered theorems consistently. The current state reads as a draft.
2. **Motivation.** The introduction gives no reason to care about tubes of width c/N
   around billiard chords beyond "the scale at which the covered fraction is nontrivial".
   One paragraph on where this observable comes from (coverage/illumination of a cavity,
   Dvoretzky-type covering driven by rotations, the Lorentz-gas analogy already cited) would
   help an editor place it.
3. **Prior-work paragraph** contains sentences that do not belong in a published paper:
   "this is a bounded search", "(full text read)", "we could not read [Coelho04, DK24] in
   full". Read them (library access) and then either cite them precisely or remove the
   apology. Add Niederreiter (dispersion), Blank–Krikorian, Caglioti–Golse (correctly
   attributed), Dupain / Dupain–Sós, Fan–Schmeling, Don (2012, rectangular table).
4. **Notation.** μ_N (scaled half-gap law) undefined; "turn units" implicit; Fibonacci
   convention unstated; β vs α vs a vs Q vs λ vs u is a lot of single letters — a short
   notation table after the introduction would help. `\paragraph` headings inside sections
   are fine, but "Certified constants" and the numerics paragraphs should carry numbered
   tables with captions (the Monte Carlo and deterministic tables have none).
5. **Proof detail.** Theorem 1 and Theorem 2(3) are at the right level for a research
   paper if the small omissions in Section 2 are added. Lemmas 6 and 7 are not proved;
   see Section 2.
6. **Figures.** TikZ figures are clear and theme-free; fine. Figure 2 caption needs the
   Qu/πQ correction. Figure 1 could mark Qu and c_* for consistency with Figure 2.
7. **Numerics section.** Acceptable for a math journal if the "proof in repository"
   sentence is fixed. State explicitly that Monte Carlo and the integrator are both
   double-precision and independent of the proofs (it does, at the end — good).
8. **Bibliography.** No DOIs; inconsistent entries: BI09 lacks pages; **MS03 has the wrong
   authors** (it is Caglioti–Golse, CMP 236 (2003) 199–221; Marklof–Strömbergsson's
   free-path work is Ann. of Math. 172 (2010) and Nonlinearity 21 (2008)); Leong17, Ram14 (published: Acta Arith. 170 (2015)),
   Zhao25 are arXiv-only where journal versions exist or should be checked; DK24 lacks
   volume/pages. Use amsplain/BibTeX with DOIs.
9. **Missing front/back matter:** MSC 2020 codes (suggest primary 11K06, secondary 37E10,
   11J70, 37C83, 52C15); keywords; author e-mail; acknowledgements; funding statement;
   **data/code availability with a persistent public link** — the appendix says "the
   accompanying repository" but the repository has no remote (I checked `git remote -v`:
   none), so there is currently nothing a reader can access; **AI-use disclosure**: the
   proofs, code, literature review, "independent verifier" and "independently written
   integrator" referenced in Section 6 were produced by AI agents according to the
   repository's own records (`AGENTS.md`, `results/FINAL_REPORT.md`). Most journals now
   require a statement; phrases like "an independent verifier" without saying what it was
   would be read as misleading once discovered. Also "Draft of ..." in `\date` must go.
10. Overfull hbox at lines 119–121 (Theorem 4(3)); fix the line.

---

## 5. Venue recommendations (ranked by fit × realistic acceptance)

1. **Uniform Distribution Theory** (Sciendo / Slovak Acad. Sci., open access; scope
   explicitly lists distribution of {nα}, Diophantine approximation, continued fractions,
   "dynamics emerging from sequences"). Best fit; acceptance realistic after revision.
2. **Monatshefte für Mathematik** (Springer; general scope with a strong uniform
   distribution/Hlawka tradition; Q2). Good fit for a short, clean paper; moderate chance.
3. **Journal of Number Theory** (Elsevier). Don (2012) on circular billiard chords and
   three gaps appeared there, which makes it a natural home; moderate-to-low chance given
   the modest depth.
4. **Journal of Statistical Physics** or **Nonlinearity**. The coverage observable and the
   Lorentz-gas/hitting-time context (DMS 2017 appeared in JSP) fit; a referee there will
   ask for physical motivation, which the paper currently lacks. Lower chance.
5. **Experimental Mathematics**. Fits the certified-constants/numerics angle, but the
   paper is proof-driven; would need the numerics expanded (non-noble angles, rates) to
   be a natural fit. Lower chance as is.
6. **Archiv der Mathematik** or **Bull. Aust. Math. Soc.** (short-paper venues) as
   fallbacks.

Not recommended: Ergodic Theory Dynam. Systems, Acta Arithmetica, Proc. AMS (depth and
novelty insufficient; likely desk reject).

arXiv: primary **math.DS**, cross-list **math.NT**; MSC as in Section 4.9.

---

## 6. Prioritized revisions

**Must**
1. Fix the abstract: "(i) ... equality exactly when unbounded partial quotients, *for
   c < π sin α*"; the Corollary already has the restriction.
2. Prove Lemma 6 (two-gap times) including the r = 1 and N = q_k level-drop cases, and
   prove Lemma 7 from the same three-distance lemma (three lines); state the Fibonacci
   convention.
3. Define the scaled gap law μ_N = N^{−1}Σ_j δ_{Ng_j/2} in Section 4 and write
   π m_N(s) = ∫(ℓ−s)_+ dμ_N; use it in the mass lemma and in Section 5.
4. Remove "we prove in the repository"; either add the four-candidate completeness lemma
   to the appendix or describe the Monte Carlo as validated against brute force.
5. Connect Theorem 4(3) to dispersion: state Ṽ_N(c) = a² iff c ≥ πQ·N d_N, cite
   Niederreiter's theorem limsup N d_N ≥ 1 + 2/√5 (equality iff golden-type), derive the
   general corollary "convergence to a² for c > πQ·limsup N d_N, never for c below it;
   c_* is the minimal threshold over all irrationals, attained exactly by noble angles",
   and present the golden threshold as the special case. Correct the `MS03` entry to
   Caglioti–Golse; cite Blank–Krikorian and Fan–Schmeling; obtain and read Coelho (2004),
   Dzhalilov–Khomidov (2024) and rewrite the prior-work paragraph without the "could not
   read" language. Mention Dupain / Dupain–Sós next to the Fibonacci-minimality result.
6. Add a public repository link (or Zenodo DOI) and a code/data availability statement;
   add an AI-assistance disclosure covering proofs, code and the "independent verifier".
7. Unify theorem numbering/order (A,B,C vs 1,2,4).

**Should**
8. Write the one-sentence C² justification for ψ_N and the explicit layer accounting
   (≤ 4w + 5ε) in Section 3.
9. One-line proof of q_{k+1} + q_k ≤ (A_0+1)(A_0+2) q_{k−1} in Theorem 2(3).
10. Fix Figure 2 caption (positive for c < Qu; Theorem 2(3) gives c < πQ).
11. Add MSC 2020, keywords, e-mail, acknowledgements; remove "Draft of"; BibTeX with DOIs
    and journal versions (Ramírez, Acta Arith. 2015; Marklof–Strömbergsson 2004).
12. Number and caption the two numerics tables; state sample size per seed.
13. A short motivation paragraph in the introduction (why c/N tubes; coverage of a
    cavity; relation to the Lorentz-gas strip areas).

**Nice**
14. Remark that α ∈ (π/2, π) reduces to the stated case by reflection.
15. Mark Qu and c_* on Figure 1; add one non-noble bounded-type example (e.g. silver) to
    the numerics to illustrate the open question in Section 7.
16. Replace "dominates in the convex order" by the weaker statement actually used, or add
    the one-line justification that (ℓ−s)_+ test functions suffice for equal-mean laws.
17. Consider a rate for Theorem 1 under a Diophantine condition on β (the low-mode step
    gives it immediately); it would strengthen the paper materially.

---

## 7. Verdict to the editor

**Major revision** (not reject). The mathematics is correct: I checked every step of
Theorems 1, 2 and 4 in the manuscript itself and found no error. The results are a tidy,
self-contained package — a planar coverage observable reduced exactly to a 1-D gap
functional, a bounded-type dichotomy, and a fully explicit golden-angle limit set with a
convex-order minimum and a sharp convergence threshold — and I did not find them in
print. But the manuscript is not submittable as is: two lemmas on which everything rests
are unproved index-shift statements, a key object (μ_N) is undefined, the abstract
overstates the Corollary, a proof is outsourced to a repository that has no public
address, one reference carries the wrong authors, the convergence threshold is presented
as a golden-angle discovery when it is πQ times Niederreiter's classical dispersion
constant (and a stronger all-angle corollary is available for free), and required
front/back matter (MSC, keywords, availability, AI disclosure) is missing. All of this is
fixable in a single round; the revisions are mostly mechanical and one of them
(dispersion) improves the main result. After them I would recommend acceptance at a venue
of the level of Uniform Distribution Theory or Monatshefte.
