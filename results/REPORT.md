# Observed experiment report

Executed during workspace creation, 2026-11-14 Asia/Seoul. Exact completion UTC timestamps, platform, source SHA256 and versions are in each JSON. These are newly observed outputs, distinct from historical reports.

## Saved Monte Carlo evidence

|Run / N pair|c|V first|V second|paired difference|paired SE|predicted difference|difference / SE|
|---|---:|---:|---:|---:|---:|---:|---:|
|full: 4181/5574|1|0.33615200|0.33818425|0.00203225|0.00019131|0.00191424|10.62|
|full: 4181/5574|2|0.15617325|0.16190950|0.00573625|0.00010177|0.00571136|56.36|

full: 4,000,000 points, seed 20261115, batch 100,000, observed runtime 3.205s (machine-specific).

|large: 75025/100033|1|0.33603325|0.33804100|0.00200775|0.00019099|0.00191424|10.51|
|large: 75025/100033|2|0.15640800|0.16205675|0.00564875|0.00010159|0.00571136|55.60|

large: 4,000,000 points, seed 20261116, batch 100,000, observed runtime 4.429s (machine-specific).

Each row pair uses common points; c values share samples. Runs use independent seeds. Predicted difference is the conditional asymptotic formula, not a finite-N identity. All four observed differences are positive and within one paired SE of the predicted difference. This supports the candidate, not its proof. Individual values can differ from limits due to sampling and finite-N effects; this experiment does not identify their separate contributions.

## Analytical and geometry checks

- 9 unittest tests passed; exact log: [tests.log](tests.log).
- `python3 -m py_compile circle_research.py test_circle_research.py` exited 0.
- Fast finite-segment distances checked against brute reference over six angles, five N values, 500 random points per case plus boundary/endpoint/caustic/midpoint cases; diameter and center have independent analytical checks.
- Internal audit supplies angular-neighbor candidate proof; no interval-certified arithmetic.
- 24 analytical primitive versus Gauss quadrature comparisons across phase and c passed tolerance 1e-11; [theory_checks.json](theory_checks.json). Quadrature shares gap constants but independently integrates the vacancy function.
- Empirical gaps checked at 4181/5574/75025/100033. At N5574 maximum scaled-length discrepancy is about 0.001173, consistent with a finite approximation but not a proof of the limiting gap law.
- Paired counts, sum D and sum D² saved in JSON. Unit test independently replays samples and recomputes SE with brute distances.
- Batch-size invariant RNG sequence tested. Historical RNG draw layout unknown, so historical exact digit match not expected.
- Lint/typecheck not run: ruff, mypy, pyright unavailable; no project lint/typecheck config, package.json or lint:slop:changed script. Syntax compilation is not a typecheck.

## Reproduction artifacts

- [full.json](full.json), [full.csv](full.csv): requested baseline.
- [large.json](large.json), [large.csv](large.csv): larger pair, independent seed.
- [smoke.json](smoke.json), [smoke.csv](smoke.csv): fast run.
- Source/config hashes and raw counts allow auditing against code; per-point data deliberately regenerated from seed to limit disk use.

## Research decision

Continue narrowly with spatial dephasing and fixed-angle shrinking-width spatial area. Do not claim novelty of caustics, gaps or generic arithmetic nonconvergence. Internal dephasing audit resolved the high-frequency uniformity argument using frozen radial bins and Parseval. Exact golden gap derivation, certified separation, external proof review and broader prior-art comparison remain gates. Odd-star largest-disk uniqueness and fixed-positive-width baseline retain their separate incomplete audit statuses. No publication, remote repository or author contact.

## Run commands

```sh
python3 -m unittest -v
python3 -m py_compile circle_research.py test_circle_research.py
python3 circle_research.py --output results/smoke
python3 circle_research.py --full --output results/full
python3 circle_research.py --full --ns 75025 100033 --seed 20261116 --output results/large
```
