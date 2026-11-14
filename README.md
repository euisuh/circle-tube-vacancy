# Circle Research

Standalone research continuity workspace. Created 2026-11-14 Asia/Seoul.
No research files belong in phd-prep. Start here, then read AGENTS.md.

**Current status (2026-11-14, Claude Code goal session):** three theorems with complete
proofs in [docs/THEOREM.md](docs/THEOREM.md), each passed an independent adversarial
review (no errors; small gaps fixed; [review](docs/reviews/PROOF_REVIEW.md)):
A spatial dephasing V_N(c)=a²+2∫q m_N(c/q)²dq+o(1); B golden/noble angle: exact limit
set, liminf along Fibonacci N (convex order), divergence iff c<c_*≈5.547; C all
irrationals: liminf V_N ≥ uniform-gap value V_δ(c), equality iff unbounded partial
quotients. Interval-certified constants (certify.py), exact three-distance check N≤3000,
independent deterministic integrator and 20-seed MC agree. Editable manuscript in
manuscript/ (PDF compiled). Independent literature rating: upper-end short note; key
risk: Coelho 2004 / Dzhalilov–Khomidov 2024 full texts unread. No novelty guarantee, no
submission. Final summary: [results/FINAL_REPORT.md](results/FINAL_REPORT.md).

## Read in order

- [History, all explored/rejected directions and corrections](docs/HISTORY.md).
- [Definitions and mathematical results, with evidence labels](docs/MATHEMATICS.md).
- [Theorems and complete proofs (current)](docs/THEOREM.md); [reviews](docs/reviews/).
- [Earlier proof audit](docs/PROOF_AUDIT.md).
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
python3 -m py_compile circle_research.py test_circle_research.py certify.py
python3 certify.py 3000            # exact three-gap check + interval limits
python3 manuscript/make_figures.py && (cd manuscript && pdflatex main.tex && pdflatex main.tex)
python3 circle_research.py --output results/smoke-reproduction
python3 circle_research.py --full --seed 20261115 --ns 4181 5574 --batch 100000 --cs 1 2 --output results/reproduction
python3 circle_research.py --full --ns 75025 100033 --seed 20261116 --output results/large-reproduction
```

Smoke uses 20,000 points; full uses 4,000,000 common disk points per pair.
Both c=1 and c=2 use those same points; they are correlated experiments.
Default batch 100,000. Interleaved radius/angle draws preserve samples across
batch sizes. `--help` lists flags. Outputs are JSON metadata/raw counts and CSV.
Do not overwrite old results when investigating changes: choose a new output stem.
Original per-point samples are regenerated from config, not stored.

Observed validation: 10 unittest tests passed, including brute finite-segment,
endpoint/caustic/periodic cases, analytical diameter, finite Fibonacci gap counts,
quadrature and paired SE. Current evidence is results/verified-checks.json and
results/verified-tests.log; earlier preexisting logs are retained separately.
Syntax compilation passed. No lint/typecheck config or tools available; these
checks were not run. No npm project or lint:slop:changed script exists here.

Current saved 4m-point paired experiment: c=2 gives vacancy 0.15617325 versus
0.16190950, difference 0.00573625 with paired SE 0.00010177224. See the observed
report for raw counts, source hashes, and the distinction from unsaved historical claims.

## Interpretation limits

Classical central caustic and standard three-gap arithmetic are not new research.
Altmann directly overlaps periodic-star eccentric-obstacle geometry; Coelho already
studies arithmetic hitting-time nonconvergence. Candidate contribution must be the
specific radial spatial-dephasing transformation and resulting spatial area limits.
Saved MC is evidence, not proof; SE covers sampling only. Floating-point calculations
are not interval certified. Full history includes earlier unsaved numbers separately.

Branch: codex/research-continuity. No remote, public posting, or author contact.
