# Theorems and complete proofs — 2026-11-14

Status label: **audited argument (internal), pending independent adversarial review**
(see `docs/reviews/PROOF_REVIEW.md` once written). Supersedes the proof sketch in
`PROOF_AUDIT.md` for Theorem A: the two-branch reduction is now exact on the trimmed
annulus, so no O(Nw²) band-approximation error is needed.

## Setting

D closed unit disk. 0<α<π/2, β=α/π ∉ Q, a=cos α ∈ (0,1), Q=sin α.
p_j=(cos 2jα, sin 2jα); Γ_N=⋃_{j<N}[p_j,p_{j+1}] (N complete finite chords).
Chord j has unit normal u_j at angle θ_j=(2j+1)α, supporting line u_j·x=a, endpoints at
angles θ_j±α. w=c/N, c>0 fixed. V_N(c)=π⁻¹|{x∈D: dist(x,Γ_N)>w}|.

Angular gaps g_{N,0..N-1} of {θ_j mod 2π : j<N} (sum 2π). Circle vacancy

  m_N(s) = (2π)⁻¹ Σ_j (g_{N,j} − 2s/N)_+,  s ≥ 0,

which is exactly the normalized measure of points at circular distance > s/N from every θ_j.
Put Ṽ_N(c) = a² + 2∫_0^Q q·m_N(c/q)² dq  (= a² + 2∫_a^1 r·m_N(c/√(r²−a²))² dr).

## Theorem A (spatial dephasing)

For fixed irrational β∈(0,1/2) and fixed c>0, V_N(c) − Ṽ_N(c) → 0 as N→∞ (full sequence).

### A.1 Exact two-branch structure on a trimmed annulus

Fix ε∈(0,(1−a)/3). Let I_ε=[a+ε,1−ε] and N ≥ N_0(ε,c) so that w<min(ε/2,a) and
(1−ε)²−(a−w)² < Q² (possible since (1−ε)²−a² < 1−a² = Q²).

For x=re^{iφ}, r∈I_ε, and δ=φ−θ_j reduced to (−π,π]:
dist(x, line_j) = |r cos δ − a|. Hence dist(x,line_j) ≤ w ⇔ cos δ ∈ [(a−w)/r,(a+w)/r]
⇔ |δ| ∈ [d₋(r),d₊(r)], d_∓=arccos((a±w)/r) (well defined: (a+w)/r<1 because r ≥ a+ε > a+w).
On that set the tangential coordinate of x along chord j is r|sin δ| ≤ √(r²−(a−w)²) < Q, so
the foot of the perpendicular lies inside the chord; thus dist(x,chord_j)=dist(x,line_j).
Off that set dist(x,chord_j) ≥ dist(x,line_j) > w. Therefore, **exactly**,

  x covered ⇔ ∃j: φ−θ_j ∈ ±[d₋(r),d₊(r)] (mod 2π).

Write d̄_N(r)=(d₊+d₋)/2, h_N(r)=(d₊−d₋)/2, s_N(r)=N h_N(r). With
F_{N,s}(φ)=1{circ.dist(φ,θ_j)>s/N ∀j<N} (closed-arc covering, boundaries measure zero),
the uncovered angular fraction at radius r is

  U_N(r) = ∫ F_{N,s_N(r)}(φ−d̄_N(r)) F_{N,s_N(r)}(φ+d̄_N(r)) dφ/2π = C_{N,s_N(r)}(ψ_N(r)),

ψ_N=2d̄_N, C_{N,s}(t)=∫F_{N,s}(φ)F_{N,s}(φ+t)dφ/2π.

Uniform facts on I_ε (G(r,w)=arccos((a+w)/r) is real-analytic on the compact set
I_ε×[−ε/2,ε/2]): s_N(r) → c/q(r) uniformly, q(r)=√(r²−a²); ψ_N → ψ=2arccos(a/r) in C¹(I_ε);
ψ_N' ≥ κ_ε>0 and |(2r/ψ_N')'| ≤ K_ε for N ≥ N_0, since ψ'=2a/(rq) ≥ 2a/(1−ε) > 0.

### A.2 Layers

r<a−w: dist(x,line_j) ≥ a−r > w for all j, so U_N=1; contribution 2∫_0^{a−w} r dr=(a−w)².
r∈[a−w,a+ε]∪[1−ε,1]: contribution ≤ 2(a+ε)(ε+w)+2ε. Same bounds hold for the
corresponding pieces of Ṽ_N since 0≤m_N≤1 and ∫_0^{a}2r dr=a². Hence

  |V_N − Ṽ_N| ≤ 6ε + 2w + |∫_{I_ε} 2r [C_{N,s_N(r)}(ψ_N(r)) − m_N(c/q(r))²] dr|.

### A.3 Low modes vanish (irrationality)

Rotating {θ_0..θ_{N−1}} by 2α gives {θ_1..θ_N}: one arc removed, one added. So
‖F_{N,s}(·−2α)−F_{N,s}‖_{L¹(dφ/2π)} ≤ 2·(2s/N)/(2π) = 2s/(πN), even with overlaps.
For k≠0: |e^{−2ikα}−1|·|F̂_{N,s}(k)| ≤ 2s/(πN). Since β∉Q, e^{−2ikα}≠1, so
sup_{s≤S} |F̂_{N,s}(k)| → 0 for every fixed k≠0 and S<∞. F̂(0)=m_N(s).

### A.4 High modes, frozen width

C_{N,s}(t)=Σ_k |F̂_{N,s}(k)|² e^{ikt}, absolutely convergent (Parseval: Σ|F̂|²=m_N(s) ≤ 1).
For a subinterval J⊂I_ε and k≠0, integration by parts with ψ_N' ≥ κ_ε gives
|∫_J 2r e^{ikψ_N(r)}dr| ≤ B_ε/|k| (B_ε from κ_ε, K_ε, endpoint terms; uniform in N ≥ N_0, J).
So for fixed s≤S:

  |∫_J 2r[C_{N,s}(ψ_N(r)) − m_N(s)²]dr| ≤ Σ_{0<|k|≤K}|F̂_{N,s}(k)|²·2 + B_ε/K.

Let N→∞ (first sum → 0 uniformly in s≤S by A.3), then K→∞.

### A.5 Unfreeze

|F_{N,s}−F_{N,t}|_{L¹} ≤ |s−t|/π, so |C_{N,s}(ψ)−C_{N,t}(ψ)| ≤ 2|s−t|/π and
|m_N(s)²−m_N(t)²| ≤ 2|s−t|/π, uniformly in N,ψ. Partition I_ε into bins J_1..J_L of mesh
small enough that c/q varies by <η on each, and pick s_i=c/q at a point of J_i.
For N large, |s_N(r)−c/q(r)|<η. Then the A.2 integral is ≤ (8η/π)·1 + Σ_i(A.4 error on J_i)
→ (8η/π) as N→∞ with L fixed (S=c/q(a+ε)+1). Let η→0, then ε→0. ∎

Limit order: α,c fixed → ε → mesh η (finite L) → K → N→∞ → K→∞ → η→0 → ε→0.
No rate is claimed; the A.3 rate depends on the Diophantine nature of β.

## Lemma B.1 (golden three-distance law, exact)

β=λ², λ=(√5−1)/2. For N=F_m+k, m≥3, 0≤k<F_{m−1}, the N gaps of {jβ mod 1: j<N} are
λ^{m−2}, λ^{m−1}, λ^m with multiplicities F_{m−1}−k, F_{m−2}+k, k.

Source: explicit three-distance theorem (Sós 1958; explicit counts e.g. Leong,
arXiv:1712.03758 Thm 3 — note Leong indexes N+1 points; Alessandri–Berthé 1998), applied
to rotation λ (β≡−λ mod 1; reflection preserves gaps) with q_k=F_{k+1}, ‖q_kλ‖=λ^{k+1},
all partial quotients 1. Sanity: Σ=F_{m−1}λ^{m−2}+F_{m−2}λ^{m−1}=1 (identity
F_jλ^{j−1}+F_{j−1}λ^j=1). Independent check: `certify.py` verifies the statement in exact
Z[λ] arithmetic for **every** 2≤N≤3000 (results/certify-golden.json). The angles θ_j are
a translate of {2πjβ}, so their gaps are 2π times these.

## Theorem B (golden / noble angle: full limit set, liminf, threshold)

Let β be golden (or any noble β∈(0,1/2), i.e. continued fraction eventually all 1's;
see B.6). u=π/(√5λ²) (=πC). For x∈[0,λ] let μ_x be the probability law with atoms
ℓ_i=u(1+x)λ^i, weights f=(λ−x, λ²+x, x)/(1+x), i=0,1,2; Σf_iℓ_i=π. Put
M_x(s)=π⁻¹ Σ_i f_i(ℓ_i−s)_+ and V(x,c)=a²+2∫_0^Q q M_x(c/q)² dq. Let c_*=Q·u/λ=πQ/(√5λ³).

For every c>0:
1. The set of subsequential limits of V_N(c) is {V(x,c): x∈[0,λ]} (a compact interval).
2. lim inf_N V_N(c) = V(0,c) = lim_m V_{F_m}(c).
3. V(x,c) ≥ V(0,c) for all x, with strict inequality iff 0<x<λ and c<Q·u(1+x).
   Hence lim sup > lim inf iff c<c_*; for c ≥ c_*, V_N(c) → a².
4. In particular for Q·u ≤ c < c_* (≈3.4282 ≤ c < 5.5470 at the golden angle),
   lim inf V_N(c)=a² (outer annulus asymptotically fully covered along F_m) but lim sup>a².

### B.2 Uniform reduction to x

For N=F_m+k put x_N=k/F_m∈[0,F_{m−1}/F_m). By B.1, N·(half-gaps) take values
πF_mλ^{m−2}(1+x_N)λ^i with frequencies (F_{m−1}−k, F_{m−2}+k, k)/N. Since F_mλ^{m−2}→1/(√5λ²)
and F_{m−1}/F_m→λ, F_{m−2}/F_m→λ², every atom and weight converges to its μ_{x_N} value
uniformly in k. As y↦(y−s)_+ is 1-Lipschitz and weights are bounded,
sup_{s≥0}|m_N(s)−M_{x_N}(s)|→0, hence Ṽ_N(c)−V(x_N,c)→0. With Theorem A: V_N(c)−V(x_N,c)→0.
[Review fix: F_{m−1}/F_m alternates around λ, so x_N may exceed λ by at most
|F_{m−1}/F_m−λ|=λ^m/F_m→0. The atom/weight formulas are polynomial in x on a neighbourhood
of [0,λ], so replacing x_N by x'_N=min(x_N,λ) changes M by o(1) uniformly; use x'_N.]
x↦V(x,c) is continuous on [0,λ] (dominated convergence; integrand ≤ 2q). The grids
{k/F_m} become dense in [0,λ] and x_N∈[0,λ], so the limit set is V([0,λ],c). Parts 1, 2
then follow from part 3 (V(F_m)=V(0,c)+o(1) since x=0).

### B.3 Convex-order lemma

Write D(x,s)=π(M_x(s)−M_0(s)). Ordering of atoms for 0≤x≤λ:
uλ²(1+x) ≤ uλ ≤ uλ(1+x) ≤ u ≤ u(1+x) (uses (1+x)λ ≤ 1). Using πM=E(ℓ−s)_+,
Eℓ=π, 1−λ=λ², 1/(1+λ)=λ:

| s range | πM_0(s) | D(x,s) |
|---|---|---|
| s ≤ uλ²(1+x) | π−s | 0 |
| [uλ²(1+x), uλ] | π−s | (x/(1+x))·(s−uλ²(1+x)) |
| [uλ, uλ(1+x)] | λ(u−s) | λ(λ−x)·(uλ − s/(1+x)) |
| [uλ(1+x), u] | λ(u−s) | (x/(1+x))·(1+λ)·(s−uλ(1+x)) |
| [u, u(1+x)] | 0 | (λ−x)(u − s/(1+x)) |
| s ≥ u(1+x) | 0 | 0 |

(Pieces agree at breakpoints; e.g. at s=uλ both middle rows give xuλ²(λ−x)/(1+x).)
So D ≥ 0, i.e. μ_x dominates μ_0 in convex order; for 0<x<λ, D>0 on
(uλ²(1+x), u(1+x)) \ {uλ(1+x)}, and D ≡ 0 for x∈{0,λ} (μ_λ=μ_0).

### B.4 Strictness and threshold

V(x,c)−V(0,c)=2∫_0^Q q(M_x−M_0)(M_x+M_0)(c/q) dq ≥ 0. Substituting s=c/q, the integrand is
positive exactly for s>c/Q inside the set where D>0. That set meets (c/Q,∞) in positive
measure iff 0<x<λ and c/Q<u(1+x). Taking x↑λ gives strictness for some x iff c<Qu(1+λ)=c_*.
For c ≥ c_*: c/Q ≥ u(1+x) ≥ every atom, so M_x(c/q)=0 for all q≤Q and V(x,c)=a² ∀x;
by B.2 V_N(c)→a². Part 4: M_0(s)=0 for s ≥ u, so V(0,c)=a² iff c ≥ Qu. ∎

### B.5 Certified values (results/certify-golden.json; mpmath interval, 50 digits)

V(0,1)=0.336226129522972286713858…, V(1/3,1)=0.338140371722238948759490…,
V(0,2)=0.156461653859154412145164…, V(1/3,2)=0.162173010171056514663865…,
c_*=5.547008255803426524554994…, a²=0.131315560960840049240879….
Strictness itself is proved by B.4; intervals only certify the digits.

### B.6 Noble extension

If β has partial quotients a_{k+1}=1 for all k ≥ k_0, the same three-distance theorem
gives, for N=q_k+s, 0≤s<q_{k−1}, gaps η_{k−1},η_k,η_{k−2} with counts N−q_{k−1}, s,
q_{k−1}−s (η_j=‖q_jβ‖). With q_{k−1}/q_k→λ, η_k/η_{k−1}→λ and q_kη_{k−1}+q_{k−1}η_k=1
one gets q_kη_{k−2}→1/(√5λ²), so x_N=s/q_k yields the same family μ_x; Theorem B holds with
a=cos πβ, Q=sin πβ. (Index bookkeeping here is checked against B.1 only for golden; the
numerical check for a non-golden noble β is listed as an open verification item.)

## Theorem C (all irrational angles: uniform-gap envelope detects bounded type)

β∈(0,1/2) irrational, partial quotients a_k, convergent denominators q_k, η_k=‖q_kβ‖.
Define the **uniform-gap value**

  V_δ(c) = a² + 2∫_0^Q q (1 − c/(πq))_+² dq
         = a² + Q² − 4cQ/π + 3(c/π)² + 2(c/π)² log(πQ/c)   for 0<c<πQ,
         = a²                                               for c ≥ πQ.

For every c>0:
1. lim inf_N V_N(c) ≥ V_δ(c).
2. If (a_k) is unbounded: lim inf_N V_N(c) = V_δ(c), and lim sup_N V_N(c) ≥ W(c) > V_δ(c),
   W(c)=a²+2∫_0^Q q[(1/2 − c/(πq))_+ + 1/2]² dq. So V_N(c) diverges for **every** c>0.
3. If a_k ≤ A₀ for all k and 0<c<πQ: lim inf_N V_N(c) ≥ V_δ(c)+κ with κ=κ(A₀,c,α)>0.
Corollary: for any fixed c∈(0,πQ), β is badly approximable ⇔ lim inf V_N(c) > V_δ(c).

### C.1 Finite-N Jensen bound (exact)
Σ_j(g_j − 2s/N)_+ ≥ max(0, Σ_j(g_j − 2s/N)) = (2π−2s)_+, so m_N(s) ≥ M_δ(s):=(1−s/π)_+ for
every N, s. Hence Ṽ_N(c) ≥ V_δ(c) exactly, and part 1 follows from Theorem A. For s ≤ π,
2π(m_N(s) − M_δ(s)) = Σ_j(2s/N − g_j)_+ (mean-gap identity).

### C.2 Two-distance times (from the three-distance theorem, our N-point convention)
For N = r q_k + q_{k−1}, 1≤r≤a_{k+1}: gaps η_k (count N−q_k) and η_{k−1}−(r−1)η_k
(count q_k). [Leong Thm 3 with Leong's N'=N−1=(r−1)q_k+q_{k−1}+(q_k−1); sum check
q_{k−1}η_k+q_kη_{k−1}=1.] Case r=a_k at level k−1 gives N=q_k: gaps η_{k−1}
(count q_k−q_{k−1}) and η_{k−1}+η_k (count q_{k−1}). Standard bounds:
1/(a_{k+1}+2) < q_kη_k < 1/a_{k+1}, q_kη_{k−1} = 1 − q_{k−1}η_k.

### C.3 Unbounded case
Along k with a_{k+1}→∞ and N=q_k: both scaled gaps Nη_{k−1}, N(η_{k−1}+η_k) lie in
(1−1/a_{k+1}, 1+1/a_{k+1}) (turn units), so sup_s|m_N − M_δ| → 0 and V_N(c)→V_δ(c).
Along N=r q_k+q_{k−1}, r=⌈a_{k+1}/2⌉: Nη_k → 1/2 with frequency (N−q_k)/N → 1, while the
other class has frequency q_k/N→0 and total length q_kη_{k−1}−(r−1)q_kη_k → 1/2, its
scaled length → ∞. Hence m_N(s) → (1/2 − s/π)_+ + 1/2 for each fixed s, and dominated
convergence in q gives V_N(c)→W(c). M_W ≥ M_δ with strict inequality on (π/2,∞),
which meets (c/Q,∞) for every c, so W(c)>V_δ(c).

### C.4 Bounded case
Non-degeneracy lemma: if a_k ≤ A₀ then for all large N the scaled gap law μ_N has two
atoms of frequency ≥ ε and length ratio ≥ 1+ε, ε=1/((A₀+1)(A₀+2)). [Three-distance, our N-point convention (review fix): every N has a unique form
N = r q_k + q_{k−1} + s, 1≤r≤a_{k+1}, 0≤s<q_k, with gaps A=η_k (count N−q_k),
B (count s), C=A+B (count q_k−s): class A has count N−q_k ≥ q_{k−1}, frequency
≥ q_{k−1}/(q_{k+1}+q_k) ≥ ε; classes B=η_{k+1}+(a_{k+1}−r)η_k and C=A+B have total
frequency q_k/N ≥ 1/(A₀+2), so one has frequency ≥ 1/(2(A₀+2)) ≥ ε. C/A ≥ 1+η_{k+1}/η_k
≥ 1+1/(A₀+2); B/A ≤ η_{k+1}/η_k ≤ (1+1/(A₀+1))⁻¹ if a_{k+1}=r, else B/A ≥ 1+1/(A₀+2).]
Mass lemma: a mean-π law with such two atoms has μ(ℓ ≤ π(1−ε²/4)) ≥ ε²/4. [If the
smaller atom is > π(1−ε²/4) the larger is ≥ π(1+ε/2), so ∫(π−ℓ)_+ = ∫(ℓ−π)_+ ≥ πε²/2,
while ∫(π−ℓ)_+ ≤ π·μ(ℓ≤π(1−τ)) + πτ with τ=ε²/4.]
Then for s∈[π(1−ε²/8), π]: π(m_N−M_δ)(s) ≥ (ε²/4)(s−π(1−ε²/4)) ≥ πε⁴/32. Since c/Q<π the
set of q with c/q ∈ [max(c/Q, π(1−ε²/8)), π] has positive length, giving
Ṽ_N(c) − V_δ(c) ≥ κ>0 for all large N; Theorem A transfers this to V_N. ∎

Numerical sanity (scratch, not evidence-grade): β=[0;3,1,5,1,9,1,17,…] excess over V_δ at
q_k before large a_{k+1} → 0, mid-block excess grows; β=[0;3,2,2,…] excess at q_k stable
≈3.3e−4 at c=1.

## What is not claimed

- No rate in Theorem A; no uniformity in α or c.
- No statement for non-noble β. Numerically (scratch exploration, not saved as evidence)
  the deepest minima of Ṽ_N occur at convergent denominators for silver, e, π−3, √3-type
  angles, but block-wise convex-order domination FAILS for those angles, so the B.3
  argument does not extend. Open: is lim inf V_N always attained along two-distance times?
- Not a physical-optics beam model; tubes are geometric.
