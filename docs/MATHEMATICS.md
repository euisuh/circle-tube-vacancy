# Mathematical record

Evidence key: **classical** = established background; **internal derivation** = derivation checked here, not independent peer review; **historical claim** = inherited result without a complete new proof; **numerical** = consult saved results, not proof. No originality claim follows from these labels.

## Definitions and geometry

Let D={x∈R²:|x|≤1}, 0<α≤π/2, p_j=(cos(2jα),sin(2jα)), and Γ_N=⋃_{j=0}^{N−1}[p_j,p_{j+1}]. These are N complete finite chords, not an indefinitely extended line or a truncated flight. Set a=cos α, u_j=(cos((2j+1)α),sin((2j+1)α)). The supporting line is u_j·x=a. For c≥0 define

V_N(c)=π⁻¹ area{x∈D:dist(x,Γ_N)>c/N}.

Here c/N is tube **half-width**. Area boundaries have zero measure. Largest empty disks are open, tangency allowed.

The classical concentric caustic has radius a and area fraction a². A zero-width finite or countable ray has zero planar area: almost every point is untouched. This trivial statement differs from the largest central empty disk.

For coprime regular-star parameters (n,k), α=πk/n and central radius cos(πk/n). Even n can form stars, e.g. (8,3). The deliberately selected odd dense family k=(n−1)/2 has a=sin(π/(2n))→0: no universal positive central fraction.

## Shrinking tubes: spatial dephasing

Assume β=α/π irrational and 0<a<1. Write g_N,j for the circular gaps between the N normals, in radians, summing to 2π. For fixed c>0 and a<r<1 set q(r)=√(r²−a²) and

U_N(r)=(2π)⁻¹ Σ_j (g_N,j−2c/(Nq(r)))_+.

**Internal derivation, fully detailed in PROOF_AUDIT.md:**

V_N(c)=a²+2∫_a^1 r U_N(r)² dr+o(1).

The error is for N→∞ at fixed irrational α and fixed c; no uniform rate over α or c is supplied. The square comes from radial averaging of the two angular vacancy branches. It is not pointwise angular independence. No equidistribution of orbit pairs is assumed.

## Golden subsequences

Put λ=(√5−1)/2, β=λ², α=πβ, C=λ⁻²/√5. Fibonacci numbers use F_0=0,F_1=1. For fixed 0≤x≤λ choose N_m=F_m+⌊xF_m⌋. The proposed limiting scaled angular gaps N_m g are

L_j=2πC(1+x)λ^j, j=0,1,2,

with frequencies f=(λ−x, λ²+x, x)/(1+x). Zero-frequency classes are omitted. These constants pass the necessary identities Σf_j=1 and Σf_jL_j=2π. Their full arithmetic derivation from the three-gap theorem remains an external proof gate; numerical gap verification is a separate gate. Reflection/parity of Fibonacci rotations does not change gap lengths.

Conditional on this limiting empirical gap law, bounded convergence and the dephasing formula give

lim_m V_Nm(c)=a²+2∫_0^{sin α} q [Σ_j f_j(L_j−2c/q)_+/(2π)]² dq.

To evaluate: break q at 2c/L_j. On an interval with active set J write A=Σ_J f_jL_j/(2π), B=cΣ_J f_j/π. Its integrand is 2q(A−B/q)²; an antiderivative is A²q²−4ABq+2B²log q. Empty active sets contribute zero; never evaluate log 0.

Historical predictions (not observations): a²≈0.131315560961; x=0 versus x=1/3 yields approximately 0.336226129523 versus 0.338140371722 at c=1, and 0.156461653859 versus 0.162173010171 at c=2. Distinct **proved** limits would establish nonconvergence at one fixed irrational angle. Floating-point predictions and Monte Carlo alone do not establish strict inequality of exact limits; rigorous numerical bounds or analytic comparison remain desirable.

## Finite-prefix largest disk

Define ρ_N=max_{|z|≤1} min(1−|z|,dist(z,Γ_N)). For a>0 let h=2a/(1−a). An internally checked exact criterion is

ρ_N>a ⇔ ∃v∈S¹ such that every u_j·v lies in (−∞,0)∪(h,∞).

Proof: an open disk B(tv,r) inside D avoids a chord iff it avoids its supporting line. Any intersection with that line lies in D, hence on the chord. Thus |tu_j·v−a|≥r. If r>a, then t≤1−r<1−a, forcing each projection negative or greater than h. Conversely, finitely many strict inequalities give positive margins. Choose t slightly below 1−a and r slightly above a with t+r≤1; all line distances remain ≥r. The central disk gives ρ_N≥a.

Consequently irrational normals eventually give ρ_N=a exactly: the closed forbidden arcs {v:0≤u_j·v≤h} eventually cover S¹. For h≥1 each is a semicircle; otherwise each has nonempty interior, and density plus compactness gives a finite subcover. A sufficient maximum normal-gap bound is Δ_N≤arcsin(min(1,h)); endpoint equality needs careful coverage convention but holds because the forbidden arcs are closed. This defeats a proposed perpetual-decay research program: stabilization is finite, even if its time varies strongly with α.

## Fixed positive half-width baseline

For 0<w<a put h=a−w. The inherited baseline states: for sufficiently large N at irrational α/π, the uncovered set agrees up to its boundary with P_N=⋂_j{x:u_j·x<h}. Then, once all circular gaps are <π,

area(P_N)=h²Σ_j tan(g_N,j/2),

area(P_N)−πh²=(h²/24)Σ_j g_N,j³(1+O(Δ_N²)).

The expansion is uniform as Δ_N→0. Bounded continued-fraction coefficients imply gaps Θ(1/N), hence excess Θ(N⁻²). The eventual-set argument uses compactness and dense complete chords away from the caustic; actual chord endpoints must be retained in finite-N experiments. This baseline has not received the same complete new audit as shrinking-width dephasing. Rotation gaps and three-gap substitutions are established machinery, not an originality argument.

## Largest disk anywhere: odd complete stars

Historical formula, **not fully re-proved here**: for odd n, a=sin(π/(2n)), b=sin(3π/(2n)), r*=max(a,(b−a)/(1+b)). For n=3,5 the origin is reportedly unique; for odd n≥7 there are reportedly exactly n maximizers opposite vertices, z_j=−(1−r*)p_j. The reported proof classifies consecutive blocks of normals with u_i·z>a. Its completeness and uniqueness step remain open audit gates. Example reported exact values: n=7, r*≈0.2469796037; n=31, r*≈0.0875249066. Historical grid lower/upper bounds belong in the history ledger, not a theorem certificate. Older annular-billiard obstacle literature overlaps this geometry closely.
