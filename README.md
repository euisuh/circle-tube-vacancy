# Circle Research

Standalone research continuity workspace. Created 2026-11-14 Asia/Seoul.
No research files belong in phd-prep. Start here, then read AGENTS.md.

**Current status:** reproducible finite-chord experiments support distinct
subsequential shrinking-tube area limits at a fixed golden irrational angle.
An internal spatial-dephasing argument is recorded. The complete nonconvergence
example is not yet a certified theorem: exact golden gap derivation, rigorous
separation of integral values, independent proof review and originality audit remain.
No publication suitability or novelty guarantee. No manuscript/PDF produced.

## Read in order

- [History, all explored/rejected directions and corrections](docs/HISTORY.md).
- [Definitions and mathematical results, with evidence labels](docs/MATHEMATICS.md).
- [Detailed proof audit and remaining proof gates](docs/PROOF_AUDIT.md).
- [Annotated primary bibliography and overlap](docs/BIBLIOGRAPHY.md).
- [Research plan and acceptance gates](docs/PLAN.md).
- [Experiment protocol](docs/EXPERIMENTS.md).
- [Observed experiment report](results/REPORT.md).

## Reproduce

Python 3, NumPy required; existing environment used Python 3.14.7 / NumPy 2.5.3.
`requirements.txt` records the sole runtime dependency; no new installation made.
Run from this directory:

```sh
python3 -m unittest -v
python3 -m py_compile circle_research.py test_circle_research.py
python3 circle_research.py --output results/smoke
python3 circle_research.py --full --output results/full
python3 circle_research.py --full --ns 75025 100033 --seed 20261116 --output results/large
```

Smoke uses 20,000 points; full uses 4,000,000 common disk points per pair.
Both c=1 and c=2 use those same points; they are correlated experiments.
Default batch 100,000. Interleaved radius/angle draws preserve samples across
batch sizes. `--help` lists flags. Outputs are JSON metadata/raw counts and CSV.
Do not overwrite old results when investigating changes: choose a new output stem.
Original per-point samples are regenerated from config, not stored.

Observed validation: 9 unittest tests passed, including brute finite-segment,
endpoint/caustic/periodic cases, analytical diameter, quadrature and paired SE.
Syntax compilation passed. No lint/typecheck config or tools available; these
checks were not run. No npm project or lint:slop:changed script exists here.

## Interpretation limits

Classical central caustic and standard three-gap arithmetic are not new research.
Altmann directly overlaps periodic-star eccentric-obstacle geometry; Coelho already
studies arithmetic hitting-time nonconvergence. Candidate contribution must be the
specific radial spatial-dephasing transformation and resulting spatial area limits.
Saved MC is evidence, not proof; SE covers sampling only. Floating-point calculations
are not interval certified. Full history includes earlier unsaved numbers separately.

Branch: codex/research-continuity. No remote, public posting, or author contact.
