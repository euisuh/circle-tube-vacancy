# Experiment protocol

All new results must be read from saved JSON/CSV, never copied from HISTORY.md.
Run commands from workspace root with Python 3 and installed NumPy. CLI help is
canonical for available flags. README lists observed commands for this revision.

## Geometry

Sample disk points with radius sqrt(U), angle 2pi V, U,V independent uniforms.
Compare two N values on identical points. A point is uncovered iff exact minimum
Euclidean distance to first N finite segments exceeds c/N. Disk boundary is not a
reflecting obstacle in the distance calculation; sample points already lie inside D.
Keep tube half-width explicit. Points below a-c/N are necessarily uncovered, but
that does not allow replacing all distances with infinite-line distances.

## Statistical reporting

For indicators I0,I1, estimate V0,V1 from sample means. Paired difference uses
D=I1-I0 in {-1,0,1}; estimated SE=sqrt(sample_variance(D)/M). Independent-error
addition would waste common random numbers and misstate paired uncertainty.
Store integer counts and sum D² so SE can be independently recomputed. Sampling
uncertainty says nothing about proof, novelty, deterministic bias or floating-point
certification. Bounds/tangency events have zero area but remain unit-test cases.

## Reproducibility and resource use

Save seed, RNG, sample count, batch size, N, c, alpha, software versions, elapsed
time and output paths. Uniform generation call order can differ with batching;
report whether changing batch size preserves samples. Floating arithmetic and NumPy
versions can affect last digits. No historical exact-digit match required.
Use bounded batches; no O(MN) full distance matrix for millions of points. Small
O(MN) brute reference remains essential for correctness tests.

## Prediction

Compute exact finite-N angular gap statistics independently of MC. Compare golden
scaled gap clusters/frequencies with limiting formulas; phase floor rounding creates
finite-N error. Integrate limiting vacancy square analytically by active thresholds,
then cross-check numerical quadrature. Numerical quadrature tolerance is not a
rigorous interval certificate. Historical predictions remain labeled historical
until observed new code reproduces them.

## Current verified artifact map

- `../results/verified-full.json`: complete metadata, raw integer counts, paired
  moments, finite gap checks, limiting predictions.
- `../results/verified-full.csv`: compact numerical rows.
- `../results/verified-full.stdout.log`: current CLI output.
- `../results/verified-checks.json`: observed test/compilation exit codes and
  code/test hashes, plus unavailable lint/typecheck status.
- `../results/verified-tests.log`: ten-test output.
- `../results/REPORT.md`: human-readable evidence and limits.

These files were newly observed in this archive task. Earlier output stems found
on disk remain preserved as preexisting artifacts; do not silently merge their
provenance with verified-full. New runs should use a unique stem and retain the
code hash; changing code after a run does not retroactively validate that run.

## Added 2026-11-14

- Deterministic exact-arc radial integrator: independent/geom.py (see results/indep-REPORT.md).
- Exact/interval certification: certify.py → results/certify-golden.json.
- Seed sweep 9001–9016: results/seedsweep/ (compare paired MC with deterministic finite-N, not limits).
