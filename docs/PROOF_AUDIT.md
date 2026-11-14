# Proof audit — 2026-11-14

> Superseded for Theorem A by docs/THEOREM.md (exact two-branch reduction; adversarially
> reviewed, see docs/reviews/PROOF_REVIEW.md). Golden gates 1–3 below are now closed there:
> three-distance law cited (Leong Thm 3) and exactly verified N≤3000; strict separation
> proved by convex order (THEOREM.md B.3–B.4) and digits interval-certified.

This is a new internal audit of inherited reasoning. It is not an external referee report, formal verification, or novelty certificate. No historical Monte Carlo output was used to validate a proof. Scope: dephasing limit exchanges and geometric reductions; conditional golden-limit evaluation; bounded review of earlier directions.

## Audit outcome

- Shrinking-width dephasing: a complete internal argument is given below. The previously vague high-frequency step can be justified uniformly with Parseval after freezing width on radial bins.
- Golden gap constants: normalization and conditional integration checked algebraically. A complete continued-fraction derivation is still required; empirical gap agreement cannot replace it.
- Finite-prefix exact stabilization: criterion checked using empty disks contained in D, so chord-versus-line replacement is valid there.
- Fixed-width polygon: inherited derivation is plausible; complete independent proof not supplied here.
- Odd-star largest disk and uniqueness: historical candidate, not fully independently proved here.
- Novelty: unresolved. Literature mismatch or exclusion from a comparison theorem's hypotheses is insufficient.

## Detailed spatial-dephasing argument

All angular L¹ norms/integrals below use normalized Haar measure dφ/(2π). Fix α/π irrational, 0<a=cos α<1, c>0. Let θ_j=(2j+1)α modulo 2π. For s≥0 define the vacancy function

f_N,s(φ)=1{φ has circular distance >s/N from every θ_j}.

Its mean is m_N(s)=(2π)⁻¹Σ_j(g_N,j−2s/N)_+. This formula is exact: within each gap, remove s/N at either end; overlapping intervals leave no vacancy.

### 1. Trim the geometric boundary layers

Fix ε>0 small enough that a+ε<1−ε and work on I_ε=[a+ε,1−ε]. For a point x=r(cos φ,sin φ), distance to supporting line j is |r cos(φ−θ_j)−a|. At radius r, its width-w band has two angular components near φ−θ_j=±d(r), d(r)=arccos(a/r). Their half-width is w/q(r)+O_ε(w²), and each center differs from ±d(r) by O_ε(w²), uniformly in r; Taylor expansion of arccos on this compact domain proves this bound.

For w=c/N, the union of N angular bands differs in normalized measure from the ideal intervals by O_ε(Nw²)=O_ε(1/N). On I_ε and for sufficiently small w, every perpendicular projection associated with a point in a line band lies strictly inside its chord: its tangential coordinate is near ±q(r), whereas chord endpoints have tangential coordinate ±sin α and q(1−ε)<sin α. Thus line bands equal finite-segment tubes on this annulus for large N. Endpoint caps cannot enter it, since every endpoint has radius 1 and cap radius w<ε.

The ideal angular vacancy is f_N,s(r)(φ−d(r)) f_N,s(r)(φ+d(r)), with s(r)=c/q(r). Averaging φ yields the autocorrelation

C_N,s(r)(ψ(r)), where C_N,s(t)=∫f_N,s(φ)f_N,s(φ+t)dφ/(2π), ψ(r)=2d(r).

The core |x|<a−w is entirely uncovered. The discrepancy from assigning core area πa² is O(w). Omitted annular layers near a and 1 have area O(ε), uniformly in N. These elementary area bounds permit taking ε→0 only after N→∞.

### 2. Fixed Fourier modes vanish uniformly over frozen widths

Write θ=2α. Rotating the union of target intervals by θ removes one interval and adds one interval. Therefore

||f_N,s(·+θ)−f_N,s||_1 ≤ 2s/(πN).

This bound is valid even when intervals overlap, since the symmetric difference is contained in the two changed intervals. For k≠0,

|1−exp(ikθ)| |f̂_N,s(k)| ≤ 2s/(πN).

Irrationality makes the factor on the left nonzero for every fixed integer k. Hence each fixed nonzero coefficient tends to zero, uniformly for s in any bounded interval. No bound uniform over all k is asserted or needed. The dependence on the irrational angle precludes an arithmetic-uniform convergence rate.

### 3. Freeze width, then control high modes uniformly

For fixed s, the autocorrelation has the absolutely convergent Fourier expansion

C_N,s(t)=Σ_{k∈Z}|f̂_N,s(k)|² exp(ikt),

because Parseval gives Σ_k|f̂_N,s(k)|²=||f_N,s||²_2≤1. This summability justifies interchanging sum and a radial integral. The zero mode is m_N(s)².

For a fixed radial bin J⊂I_ε and k≠0, integration by parts gives

|∫_J 2r exp(ikψ(r))dr| ≤ C_ε/|k|.

Indeed ψ'(r)=2a/(rq(r)) is positive, smooth, bounded away from zero on I_ε; 2r/ψ'(r) has bounded derivative there. Endpoint terms are included in C_ε. Thus the contribution of all |k|>K is ≤C_ε/K, uniformly in N and s. For the finitely many 0<|k|≤K the previous step gives convergence to zero. Taking N→∞ then K→∞ proves, for every fixed bin and frozen s,

∫_J 2r[C_N,s(ψ(r))−m_N(s)²]dr→0.

The crucial point is the square-summable Fourier origin of the correlation: treating an arbitrary bounded oscillatory function would not supply this uniform tail estimate.

### 4. Unfreeze without assuming smooth dependence on N

For any s,t≥0, changing N target half-widths changes their union by normalized measure at most |s−t|/π. Hence

||f_N,s−f_N,t||_1≤|s−t|/π,

|C_N,s(ψ)−C_N,t(ψ)|≤2|s−t|/π,

|m_N(s)²−m_N(t)²|≤2|s−t|/π.

These bounds are uniform in N and ψ. Since s(r)=c/q(r) is uniformly continuous on I_ε, a finite partition with sufficiently small mesh makes all freezing errors arbitrarily small, uniformly in N. Apply step 3 to that finite partition, then send the mesh to zero. This yields the dephasing identity on I_ε. Finally remove its boundary layers by step 1 and 0≤U_N≤1. Result:

V_N(c)−a²−2∫_a^1rU_N(r)²dr→0.

### Limit-order ledger

Keep α,c fixed → fix ε → choose finite radial mesh → fix Fourier cutoff K → send N→∞ → send K→∞ → refine mesh → send ε→0. Equivalently use a tolerance-based nested choice in that order. No interchange of an N-dependent infinite Fourier tail, caustic singularity, and N limit is needed.

## Golden subsequences: remaining gates

The supplied f_j,L_j satisfy Σf_j=1 and Σf_jL_j=2π for every 0≤x≤λ. With the claimed empirical scaled-gap convergence, mean vacancy converges for every q>0 because y↦(y−2c/q)_+ is continuous; bounded normalized vacancy permits dominated convergence in q. At q=0 define vacancy zero; this single point does not affect the integral. The piecewise antiderivative in MATHEMATICS.md follows by expanding 2q(A−B/q)².

What remains before announcing a proved nonconvergence example:

1. Derive exact finite Fibonacci/intermediate gap lengths and counts, including the floor and all parity cases, from a primary three-gap statement or a self-contained argument.
2. Establish the resulting empirical law analytically, beyond saved gap histograms.
3. Bound the two explicit integral values far enough apart with certified arithmetic, or prove their strict inequality symbolically. Ordinary double precision is strong experimental evidence but not an interval certificate.
4. Obtain independent mathematical review of the complete dephasing argument and its relation to prior work.

## Avoided invalid shortcuts

- Dense normals alone do not imply pointwise independence of two vacancy branches.
- Equidistribution at fixed angular scale does not prove shrinking-target statistics.
- A candidate accelerated distance routine is not trusted merely because line distance is easy; finite-segment endpoints matter near ∂D.
- Fixed positive w and w=c/N are different limits; the eventual central-polygon result cannot be substituted into the shrinking regime.
- Finite-prefix largest disks stabilize exactly; their apparent transient decay is not an asymptotic research theorem.
- A numerical separation with many standard errors quantifies sampling uncertainty, not discretization error, implementation bias, mathematical correctness, or originality.

## Independent audit of four-neighbor segment-distance reduction

Reviewed `fast_distances` and its docstring against actual finite chords. The reduction is mathematically valid for points inside D, in exact arithmetic, for 0<α≤π/2. It does not extend without proof to points outside D.

Rotate one chord to normal angle 0. Its endpoints are (a,±b), b=sin α. For a point r(cos δ,sin δ), choose absolute angular difference δ∈[0,π]. If r sin δ≤b, perpendicular projection lies on the segment and distance is |r cos δ−a|. Otherwise the closest endpoint is (a,b), giving squared distance r²+1−2r cos(δ−α).

For r>a, the continuous minimum occurs at d=arccos(a/r)≤α. On [0,d] the projection is interior because r sin d=√(r²−a²)≤b; line distance decreases. For δ>d, interior line distance increases. Any endpoint regime has δ≥arcsin(b/r)≥α and δ−α<π, so its squared distance derivative 2r sin(δ−α) is nonnegative. The formulas join continuously. Thus distance increases throughout [d,π]. For r≤a the same reasoning gives nondecreasing distance throughout [0,π], with minimum at 0. At r=0 all distances equal a.

On the circle of normal angles, there are at most two minima θ_point±d, separated by two monotone arcs on either side (with maxima at θ_point and θ_point+π when d>0). A minimum over any finite set of normals must therefore be a predecessor or successor of one of those minima. `searchsorted` with cyclic wrap selects exactly these four candidates; actual clipped finite-segment distances, rather than line distances, are evaluated. Duplicate normals and coincident minima merely repeat candidates. This proves candidate completeness, while brute-force comparisons test floating-point implementation and indexing. Trigonometric argument reduction and segment arithmetic remain ordinary floating-point operations, not certified bounds.
