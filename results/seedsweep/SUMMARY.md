# Seed sweep — 2026-11-14

Purpose: resolve the +2.6σ pooled c=2 paired-difference excess flagged in
results/indep-REPORT.md (4 runs). Command (repo root, source sha256 in each JSON):

    for s in $(seq 9001 9016); do python3 circle_research.py --full --seed $s \
      --ns 4181 5574 --output results/seedsweep/seed$s; done

Pooled with verified-full (seed 20261115) and indep-mc-seed777/778/779: 20 independent
4m-point paired runs. Reference = deterministic finite-N difference from
independent/ integrator (h=0.5; 6-digit rounding, error <=1e-6):
c=1 0.001955, c=2 0.005800.

| c | runs | mean paired diff | deterministic | pooled z | SD across runs | reported paired SE |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 20 | 0.001994 | 0.001955 | 0.91 | 1.70e-4 | 1.91e-4 |
| 2 | 20 | 0.005833 | 0.005800 | 1.43 | 1.15e-4 | 1.02e-4 |

Conclusion: no evidence of a discrepancy; the earlier 4-run excess is consistent with
chance, and the across-run spread matches the paired SE formula. Sampling only; not proof.
