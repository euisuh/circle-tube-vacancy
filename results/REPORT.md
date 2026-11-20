# Observed experiment report — 2026-11-14

## Provenance

The geometry executor ran and saved `verified-full.json`, `verified-full.csv`,
`verified-full.stdout.log`, `verified-checks.json`, and `verified-tests.log` during
this archive task. The documentation executor read those saved outputs before
writing this report. Earlier `full`, `large`, `smoke`, and `theory_checks` files (now in `results/archive/`)
already existed when the executors inspected the folder; they are preserved but
are not the verification source for the current claim. Historical numbers from
voice replies are recorded separately in `../docs/HISTORY.md`.

No raw per-point samples are stored; regenerate them from the saved seed, RNG,
software versions, and command. The JSON stores integer totals and source hashes.
Seed names such as 20261115 are arbitrary RNG parameters, not execution dates.

## Command and environment

```sh
python3 circle_research.py --full --seed 20261115 --ns 4181 5574 --batch 100000 --cs 1 2 --output results/verified-full
```

- Four million common disk-area-uniform samples for both N values.
- Angle alpha=1.1999816148643268 radians, alpha/pi=(3-sqrt(5))/2.
- Tube half-width c/N, actual finite segments, unit outer disk.
- Python 3.14.7, NumPy 2.5.3, macOS arm64; elapsed 3.276 seconds in saved run.
- NumPy default_rng/PCG64, interleaved radius-angle draws; batch-invariant sample order.
- Both c rows share points and are correlated experiments.

## Newly observed results

All areas below are normalized by pi. Difference is vacancy at N5574 minus N4181.

| c | N4181 vacancy | N5574 vacancy | Paired difference | Paired SE | Predicted limiting difference |
|---|---:|---:|---:|---:|---:|
| 1 | 0.33615200 | 0.33818425 | 0.00203225 | 0.000191311694 | 0.001914242199 |
| 2 | 0.15617325 | 0.16190950 | 0.00573625 | 0.000101772241 | 0.005711356312 |

Observed paired differences are about 10.62 and 56.36 sampling SE above zero.
Those ratios characterize Monte Carlo sampling precision, not asymptotic proof
or originality. The predicted differences lie within one paired SE of observed
differences for this run. This agreement does not bound finite-N bias.

Individual limiting predictions are:

| c | Fibonacci-phase limit | Intermediate-phase limit |
|---|---:|---:|
| 1 | 0.336226129523 | 0.338140371722 |
| 2 | 0.156461653859 | 0.162173010171 |

Saved raw uncovered counts are 1,344,608 / 1,352,737 at c=1 and
624,693 / 647,638 at c=2. Paired signed sums are 8,129 and 22,945;
paired squared sums are 585,619 and 165,853. These suffice to recompute SE.

Historical 4m values differ because that earlier report had no saved artifacts
and the reconstructed implementation uses a specified interleaved RNG draw order.
Matching its digits is not an acceptance criterion; this report supplies a fresh
reproducible observation instead of retrospectively certifying it.

## Observed checks

`verified-checks.json` records exit 0 for:

```sh
python3 -m unittest -v
python3 -m py_compile circle_research.py test_circle_research.py
```

Ten tests passed. Coverage includes finite-segment brute reference versus fast
candidates, endpoints/caustic/periodic and adversarial points, an analytical
diameter case, parameter validation, batch reproducibility, paired statistics,
exact finite Fibonacci gap-count formulas at selected indices, and an independent
quadrature check of the limiting prediction primitive.

The gap-count tests are numerical implementation checks against explicit formulas,
not a written proof for every index. The general golden gap derivation and strict
separation of exact integral limits still require proof audit.

Lint and typecheck were **not run**: no configured linter/typechecker, ruff and
mypy unavailable. Syntax compilation is not typechecking. No npm project or
`lint:slop:changed` script exists here. No dependency installation was required.

## What this run establishes

The saved finite-N experiment reproduces a positive phase-pair vacancy difference
using one fixed irrational angle, true segments, a defined sampling protocol, and
reported paired uncertainty. It supports the proposed spatial-area limit formula.
It does not establish convergence, a universal error rate, interval-certified
constants, independent mathematical review, or novelty/publication suitability.

## Update — 2026-11-14 goal session

New evidence: results/certify-golden.json (exact/interval), results/indep-REPORT.md
(independent deterministic integrator), results/seedsweep/SUMMARY.md (20 seeds),
results/goal-tests.log (13 tests). Summary and risks: results/FINAL_REPORT.md.
The predicted-vs-observed comparison above used limits; finite-N deterministic values
(e.g. V_4181(1)=0.336056, V_5574(1)=0.338011) are the correct reference for MC z-scores.
