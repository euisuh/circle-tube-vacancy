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
