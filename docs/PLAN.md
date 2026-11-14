# Research plan and acceptance gates

## Core question

At one fixed irrational billiard angle, can uncovered spatial area fail to
converge when tube half-width is c/N? Separate three tasks: geometry, arithmetic,
and literature originality. Success in one does not establish the other two.

## Gate A — definitions and geometric computation

Use unit disk and first N complete chords. Exact point-to-segment brute reference
must agree with fast computation for randomized angles, periodic angles, repeated
vertices, endpoints, boundary, caustic and near-degenerate cases. Reject line-only
shortcuts without finite endpoint treatment. Validate inputs and memory batching.
Tests must include independently known one-chord/diameter geometry. Preserve failures.

## Gate B — arithmetic prediction

Check normal gap sum 2pi, nonnegative frequencies and sum fL=2pi. Compare empirical
scaled lengths and counts on increasing Fibonacci and intermediate subsequences.
Check piecewise analytical integral against independent numerical quadrature,
including inactive and threshold regimes. A mismatch blocks claimed constants.

## Gate C — numerical evidence

Smoke: small deterministic run, saved metadata, bounded batches. Full baseline:
4m common area-uniform disk points, seed20261115, N4181/5574, c=1,2. Record raw
counts, paired difference variance/SE, Python/NumPy/platform, elapsed time and config.
Sampling SE quantifies Monte Carlo error, not finite-N bias or algorithm error.
No normal-approximation confidence claim when discordance counts too small.
Compare predictions and explain discrepancies only with evidence. Independent seeds
and increasing N are next experiments, not automatic proof requirements.

## Gate D — proof audit

Verify finite endpoints disappear on trimmed annulus, angular width approximation
summed error, irrational rotation low-mode annihilation, frozen-width L1 continuity,
Parseval uniform tail, nonstationary phase and boundary layer removal. Write a complete
argument with quantifier order eps -> bin mesh -> frequency cutoff -> N. Independent
human/expert review still needed before theorem/publication claims. Other historical
results retain their own audit status; do not let main-candidate audit certify them.

## Gate E — originality and significance

Compare fixed-rotation shrinking targets/entrance laws, affine-lattice integrable-flow
limits, spatial chord/strip coverage, convex approximation, annular billiard obstacle
avoidance. Inspect forward/back citations for closest primary papers. Ask whether
radial integration/autocorrelation dephasing is already implicit in known results.
Write an exact overlap table and potential theorem statement. No originality claim
until an expert can inspect that record. Do not contact authors without authorization.

## Next experiments after baseline

1. Independent seeds; larger Fibonacci pairs; report paired SE and finite-N trend.
2. Sweep phase x through [0,lambda] and c through thresholds, saved tables.
3. Other bounded-type angles and a large-partial-quotient example; determine which
   features depend on golden arithmetic. Do not generalize from one example.
4. Deterministic radial/angular integration with resolution error bounds, if needed
   to separate finite-N bias from Monte Carlo error.

## Stop / pivot conditions

A counterexample to dephasing -> retain it, repair theorem assumptions before more
large runs. Existing matching theorem -> reposition as application/explicit example,
not new general theorem. Merely different notation or fixed-angle hypothesis gap is
not enough. No physical-optics claim; no manuscript until evidence gates reviewed.

## Deliverables and continuity

README/status, complete historical ledger, definitions/derivations/audit, primary
bibliography, executable code/tests, JSON/CSV results, experiment protocol and observed
report. No PDF, external service, paid compute, or publication in this stage.

## Current handoff: concrete remaining work

The current 4m paired rerun and ten tests are saved and passed; see
`../results/REPORT.md`. Do not repeat that full run solely because a new model
starts. Repeat only after code changes, a failed check, an independent-seed
question, or a planned finite-N scaling experiment.

Priority order:

1. Supply a written finite Fibonacci gap-length/count derivation. Existing tests
   check selected indices, including phase rollover, but do not prove all cases.
2. Independently review the radial dephasing argument, particularly finite-chord
   endpoints and the order of caustic/mesh/Fourier cutoffs.
3. Establish strict inequality between the two c=2 limiting integrals with exact
   algebra or rigorous interval bounds; ordinary float precision is insufficient
   for a mathematical certificate.
4. Audit full fixed-frequency hitting-time literature and deterministic spatial
   coverage. Test whether the radial dephasing identity is an immediate known
   corollary. Record exact source theorem/hypothesis mapping if it is.
5. Only if the preceding gates survive, package a short-paper claim: fixed-action
   spatial coverage law plus explicit unequal subsequential spatial area limits.
   Keep elementary caustic and standard three-gap facts as background.

A manuscript is deliberately not created in this archive request. The user asked
for durable research continuity; the absence of a manuscript is not permission
to omit any proof or novelty gap from later reports.

## Status update — 2026-11-14 (Claude Code goal session)

Gates A–D passed (see docs/THEOREM.md, docs/reviews/PROOF_REVIEW.md, results/indep-REPORT.md,
results/certify-golden.json, results/seedsweep/SUMMARY.md). Gate E: independent literature
review rated A+B+C an upper-end short note (docs/reviews/LITERATURE_REVIEW.md). Manuscript
draft exists (manuscript/main.tex, main.pdf).

Remaining, in priority order:
1. Read Coelho 2004 (Trans. AMS) and Dzhalilov–Khomidov 2024 in full (library access);
   check whether the golden phase-x family / convex-order minimality is stated there.
2. Author metadata (placeholder in manuscript) and target venue — user decision.
3. Open math: divergence for every bounded-type non-noble β below its coverage threshold;
   is liminf attained at two-distance times? (block-wise convex order fails; needs new idea.)
4. Optional: rate in Theorem A (numerics suggest O(1/N), dominated by −2ac/N).
