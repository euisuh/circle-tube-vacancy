# Shrinking tubes around a circular billiard orbit

Code, proofs and data for the paper *Shrinking tubes around a circular billiard orbit:
spatial dephasing and arithmetic oscillation of the uncovered area* (Euisuh Jeong).
PDF: [manuscript/main.pdf](manuscript/main.pdf).

Fix an irrational angle α and the first N chords of the circular billiard orbit in the
unit disk. V_N(c) is the normalized area at distance more than c/N from those chords.

- **Theorem A:** V_N(c) = a² + 2∫₀^{sin α} q·m_N(c/q)² dq + o(1), where m_N is the
  uncovered length of the circle by N arcs centred on the rotation orbit.
- **Theorem B:** liminf V_N(c) is at least the uniform-gap value V_δ(c), with equality
  (for c < π sin α) exactly when the partial quotients of α/π are unbounded.
- **Theorem C:** for the golden angle (and every noble angle), the limit set is an
  explicit interval, the liminf is attained at Fibonacci N, and V_N(c) converges iff
  c ≥ c* ≈ 5.547.
- **Section 7:** for every irrational angle, the annulus is asymptotically covered iff
  c ≥ π sin α·κ(β); noble angles minimize κ.

Status: proofs reviewed internally and by AI referees (see `docs/reviews/`); not yet
peer reviewed. AI assistance is disclosed in the paper.

## Layout

| Path | Contents |
|---|---|
| `manuscript/` | LaTeX source (`main.tex`, `sections/`, `figures/`), figure generators, PDF |
| `circle_research.py` | geometry, Monte Carlo with paired SE, limit formulas (NumPy) |
| `certify.py` | exact Z[λ] three-distance check, interval-certified limits (mpmath) |
| `test_circle_research.py` | unit tests |
| `independent/` | independently written exact-arc radial integrator |
| `checks/` | verification scripts used by the proof reviews |
| `results/` | saved outputs; `FINAL_REPORT.md` summary; `archive/` pre-revision outputs |
| `docs/THEOREM.md`, `docs/DISPERSION.md` | full proofs (working versions) |
| `docs/reviews/` | proof, literature and referee reports |
| `docs/HISTORY.md` | all explored and rejected directions |

## Reproduce

Python 3 with NumPy and mpmath (used: Python 3.14.7, NumPy 2.5.3, mpmath 1.3.0); pdflatex for the paper.

```sh
python3 -m unittest -v                     # 13 tests
python3 certify.py 3000                    # exact gap law for N<=3000 + interval limits
python3 circle_research.py --full --seed 20261115 --ns 4181 5574 --cs 1 2 --output results/reproduction
python3 manuscript/make_figures.py && python3 manuscript/make_geometry.py
(cd manuscript && pdflatex main.tex && pdflatex main.tex)
```

The full Monte Carlo run uses 4,000,000 common points for both N, so the paired standard
error is the right uncertainty for differences. Sampling error is not proof; floating-point
results are not certified except the interval computations in `certify.py`.

## Working notes

`AGENTS.md`, `docs/PLAN.md`, `docs/BIBLIOGRAPHY.md`, `docs/MATHEMATICS.md`,
`docs/PROOF_AUDIT.md`, `docs/EXPERIMENTS.md` and `HANDOFF-codex-1.md` record the research
process, including superseded statements; `docs/THEOREM.md` and the manuscript are current.
