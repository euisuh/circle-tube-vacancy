# Research history and rejected directions

Recorded 2026-11-14 Asia/Seoul from delegated conversation continuity. This is a
faithful reconstruction, not an original transcript. Earlier experiment artifacts
were absent. Numbers in this file are HISTORICAL reports unless explicitly linked
to new results. Seed 20261115 is a reproducibility parameter, not an execution date.

## User objective and progression

Initial question: circular billiard star ray and untouched central circle radius/area.
Then: genuinely new, potentially publishable research idea with experiments/results.
Then: standalone Documents folder, comprehensive continuity including failures,
research plan, reproducible code and meaningful tests; use agents autonomously.
Folder name explicitly Circle Research, without question mark. No novelty or
publication guarantee was established. No author contact/publication authorized.

## 1. Classical central caustic — solved, not novelty

Vertices p_j=(cos(2j alpha),sin(2j alpha)); normal u_j at (2j+1)alpha;
chord line u_j·x=cos alpha=a. Central open empty disk radius a, area fraction a².
Periodic star (n,k), gcd(n,k)=1: a=cos(pi k/n). Odd densest family
k=(n-1)/2 gives a=sin(pi/(2n)) -> 0. No universal positive fraction.
Correction: even n CAN form stars, e.g. (8,3). Odd family chosen, not required.
Zero-width finite/countable rays miss full area measure: trivial, distinct from
largest central empty disk. Geometric tubes here are not diffraction/physical beams.

## 2. Largest empty disk anywhere, complete odd stars — high overlap risk

Historical geometry agent derived a=sin(pi/(2n)), b=sin(3pi/(2n)),
r*=max(a,(b-a)/(1+b)). Origin unique for n=3,5; n>=7 has n centers
c_j=-(1-r*)v_j. Fraction r*². Argument classifies consecutive normal blocks;
r>a forces block size (n-1)/2, bounds r<=bt-a and r<=1-t, attained at
 t=(1+a)/(1+b). Full proof must be checked; see audit.

Historical grid h=.004 on [-1,1]² plus exact center: objective Lipschitz 1,
grid gap <=h/sqrt(2). Floating arithmetic, NOT interval certification.

| n | central | grid lower | grid upper |
|---|---:|---:|---:|
|3|.5|.5|.5028284271|
|5|.3090169944|.3090169944|.3118454215|
|7|.2225209340|.2463433970|.2491718242|
|9|.1736481777|.2167248249|.2195532520|
|11|.1423148383|.1922277549|.1950561820|
|13|.1205366803|.1724306775|.1752591046|
|15|.1045284633|.156|.1588284271|
|17|.0922683595|.1419871600|.1448155872|
|19|.0825793455|.1305020574|.1333304845|
|21|.0747300936|.1204273765|.1232558036|
|23|.0682424134|.1120377058|.1148661329|
|25|.0627905195|.1047464554|.1075748825|
|27|.0581448289|.0981385310|.1009669581|
|29|.0541389086|.0922248119|.0950532390|
|31|.0506491688|.0874529642|.0902813914|

Formula reports: n7 .2469796037, n31 .0875249066.
Altmann et al. 2008 directly considers unchanged periodic stars avoiding an
eccentric obstacle. Standalone novelty risk HIGH; exact optimum not located.

## 3. Finite-prefix largest disk — finite stabilization, rejected main direction

rho_N=max_{|z|<=1} min(1-|z|,dist(z,Gamma_N)). Historical agent proved:
irrational alpha/pi, a>0 -> eventually rho_N=a, not indefinite gradual decay.
Sufficient maximum normal gap Delta_N<=arcsin(min(1,2a/(1-a))).
Exact reported criterion rho_N>a iff some unit v has every u_j·v<0 OR >h,
h=2a/(1-a), where OR applies separately to each j. Stabilized iff arcs
{v:0<=u_j·v<=h} cover circle. Radius>a forces |z|<1-a and each projection
outside [0,2a]; converse via perturbation. Boundary/equality audit required.
Likely routine rotation-cover corollary; retain baseline, no novelty assertion.

## 4. Fixed positive half-width — useful baseline, rejected main direction

For 0<w<a, h=a-w: eventually uncovered set (up to boundary conventions) is
P_N=intersection_j {u_j·x<h}. No offcenter pockets. Historical proof chooses
h<b<min(a,sqrt(h²+sin²alpha)); dense chords cover |x|>=b, chord projections
valid inside b; eventually P_N inside b. Exact polygon area
A_N=h² sum tan(g_j/2). Excess A_N-pi h²=(h²/24)sum g_j³(1+O(max g_j²)).
Bounded continued fractions -> Theta(N^-2). Golden phase limits likely routine
three-gap substitutions. Do not package standard arithmetic as main contribution.

## 5. Generic gap/hitting laws — rejected novelty shortcuts

Rotation gaps, continued fractions and rate exponents already known. Fixed-angle
exclusion from DMS hypotheses is not evidence of originality. No exact web match
is not proof of novelty. Literature must compare observables, not titles alone.

## 6. Active candidate: shrinking half-width c/N

Claim to audit: V_N(c)=a²+2 integral_a^1 r U_N(r)² dr+o(1),
U_N(r)=(1/(2pi))sum_j (g_N,j-2c/(N sqrt(r²-a²)))_+.
Potential contribution: radial spatial dephasing plus explicit distinct area limits
at one fixed irrational angle. See mathematics/audit for current status.

Golden beta=alpha/pi=(3-sqrt5)/2=lambda², lambda=(sqrt5-1)/2,
C=lambda^-2/sqrt5. N_m=F_m+floor(xF_m), 0<=x<=lambda.
Scaled angular gap lengths L_j=2pi C(1+x)lambda^j (j=0,1,2),
frequencies (lambda-x,lambda²+x,x)/(1+x).
Predicted limit a²+2 integral_0^sin(alpha) q[(1/(2pi))sum f_j(L_j-2c/q)_+]²dq.
Primitive on active interval: A²q²-4ABq+2B²log q.

Historical predictions x=0 versus x=1/3:

|c|x=0|x=1/3|difference|
|---|---:|---:|---:|
|1|.336226129523|.338140371722|.00191424219927|
|2|.156461653859|.162173010171|.00571135631190|

Historical a²=.131315560961. Constants require independent checking.

## Historical numerical reports — artifacts absent

4 million common area-uniform disk points, NumPy default_rng seed20261115,
N4181 and5574, true finite-segment distances reportedly accelerated by neighboring
normal-angle roots and endpoints. These are NOT newly observed outputs:

|c|N4181|N5574|paired diff|SE|
|---|---:|---:|---:|---:|
|1|.335985|.3378805|.0018955|.00019091386|
|2|.156013|.161780|.005767|.00010164244|

Reported significance ~9.93SE,56.74SE. Claimed 200 point brute-force agreement;
insufficient without endpoint/periodic/caustic/adversarial coverage. Individual
prediction discrepancies not explained merely by saying sampling/finite N.
Earlier independent 1m sweep c1: Fibonacci N610 .335336,987 .335757,
1597 .336111,2584 .335917,4181 .335910; intermediate N813 .337933,
1316 .337670,2129 .338309,3445 .337809. Sampling design details unavailable.
New implementation may consume RNG differently: matching historical digits is
not an acceptance criterion. Save new config, actual outputs and uncertainty.

## Permanent pitfalls

Complete chords versus collision points; half-width versus full width; normalized
area versus physical area; open empty disk tangencies; radians versus turns;
finite segments versus infinite lines; finite N evidence versus asymptotic proof;
fixed positive w versus c/N; fixed irrational versus averaged frequencies; grid
bound versus exact optimizer; model reports versus independent audit; bibliographic
search absence versus originality; numerical agreement versus proof correctness.

## 7. Parked variants and why they were not promoted

These were discussed, not established research gaps. Preserve them so a future
model does not restart the same novelty loop.

| Direction | What was learned | Status / useful next discriminator |
|---|---|---|
| Finite beam width, central disk only | For a geometric distance tube of fixed half-width w, protected central radius is max(0,a-w); its area fraction is the square. | Elementary extension; rejected as standalone novelty. This is not the propagation law of an optical beam. |
| Near-rational stabilization time | Near a rational star with offcenter holes, irrational finite-prefix disk stabilization may take very long; a candidate scale is inverse distance to the rational angle. | Unproved; finite-hole survivor papers already analyze near-periodic neighborhoods. Needs a theorem beyond standard rotation hitting times. |
| Shrinking width w=c/N | Total trace length grows like N while width decreases like 1/N; nontrivial macroscopic spatial vacancy survives. | Active direction. Radial dephasing, not single-target gap arithmetic, is the candidate additional result. |
| Shrinking width w=c/N² / caustic boundary layer | Chord sagitta from angular gaps of order 1/N is of order 1/N². Near r=a+y/N², local line distance scales like abs(a*z²/2-y)/N². | Scaling heuristic only; global tube area tends to zero at this width, so a rescaled local observable is needed. No theorem or experiment saved. |
| Bounded reflection-angle errors | Could ask worst-case protected area or robustness of a caustic. | No precise nontrivial model or contribution established; no experiments. Distinguish adversarial errors, independent noise, and actual rough boundaries. |
| Multiple rays / variable initial cone | Extra rays or an angular beam can change coverage. | Chernov–Galperin already treats eventual search-light illumination. No finite-time quantitative gap established here. |
| Other regular stars (n,k), even counts | Even counts can form connected stars when gcd(n,k)=1. General jump classification could be studied. | Not excluded mathematically, but broad obstacle-avoidance literature overlaps. Odd maximal-jump family was a scope choice. |
| Largest empty disk allowed to move | Introduced to escape the elementary central caustic question. | Exact odd-family formula internally derived, strong Altmann overlap. Retain as baseline, not confirmed new theorem. |
| General-purpose largest-empty-circle algorithm | Voronoi and segment-site geometry already provide established methods. | Reimplementing an optimizer is not research novelty. |

## 8. Source and communication corrections

Early voice replies claimed formulas/notes had been displayed, literature had been
checked, and simulations had run without visible supporting tool artifacts in the
retained conversation. Later numerical reports and agent derivations were supplied,
but original raw outputs were not retained. Do not upgrade those early statements
into verified observations. This archive distinguishes historical claims from
saved files and command outputs observed during reconstruction.

The user explicitly corrected repeated offers and either/or questions: pursue
proof, novelty checks, and experiments in parallel when authorized; report concrete
progress and durable results. This is a project-specific authorization, not authority
to contact authors, publish, submit, or purchase compute.

A literature result found after the first search materially changed the picture:
Dettmann–Fain modifies the orbit by a collision, whereas Altmann et al. directly
studies unchanged regular stars avoiding an eccentric obstacle. Therefore the earlier
statement that the closest literature necessarily changes the orbit was incomplete.

DMS f-regularity excludes a single fixed frequency from that particular theorem.
Coelho–de Faria and Coelho nevertheless establish fixed-frequency entrance-time
laws. Hypothesis exclusion alone was explicitly rejected as a novelty argument.

## 9. Archive-task verification recorded on 2026-11-14

The current geometry executor preserved the existing implementation, added a
finite Fibonacci gap-count test, and saved a new 4m paired run under
`results/verified-full`. The documentation executor read the saved JSON and test
outputs. Ten tests and syntax compilation exited 0. Current c=2 vacancy difference
is 0.00573625, paired SE 0.000101772241; this is newly observed numerical evidence,
not the unsaved historical 0.005767 claim. Full metadata and limits are in
`results/REPORT.md`. Lint/typecheck unavailable; no publication or author contact.

Files already existed when this documentation executor arrived. They were
inspected and preserved; this pass enriched the ledger, hypothesis comparison,
protocol, plan, and observed report rather than claiming authorship or fresh
verification of every preexisting artifact. Git commits were left to the owning
executor to avoid conflicting with concurrent work.

## 10. Claude Code goal session — 2026-11-14 (Asia/Seoul)

Goal prompt: CLAUDE_GOAL.md. Lanes: independent literature agent
(docs/reviews/LITERATURE_REVIEW.md), adversarial proof agent (docs/reviews/PROOF_REVIEW.md),
independent deterministic-numerics agent (independent/, results/indep-*). Main thread wrote
docs/THEOREM.md, certify.py, three new tests, manuscript/.

Discoveries (labels: audited argument unless stated):
- Theorem A two-branch reduction is EXACT on the trimmed annulus (no band approximation).
  Adversarial review: no error; gaps fixed (need w<a; x_N may exceed λ by λ^m/F_m).
- Golden convex order: every phase-x gap law dominates the Fibonacci law in convex order,
  so liminf V_N(c)=V(0,c) (Fibonacci times) and limit set = V([0,λ],c). Divergence iff
  c<c_*=πQ/(√5λ³)≈5.547; for c≥c_* V_N→a². Strict separation is now a proof, not a float
  comparison. Extends to noble β (reviewer checked two noble examples numerically).
- Theorem C (all irrationals): Jensen gives m_N(s)≥(1−s/π)_+, so liminf V_N≥V_δ(c);
  equality iff unbounded partial quotients (then divergence for every c>0); bounded type
  gives strict gap for c<πQ. Round-2 review: no error; two cosmetic index/exposition gaps fixed.
- certify.py: exact Z[λ] verification of the golden three-distance law for all N≤3000;
  50-digit interval enclosures reproduce the historical predictions to 12+ digits.

Rejected in this session:
- Block-wise convex-order domination for non-golden angles: FAILS numerically (silver,
  √3-type, e-type, π−3). So the golden liminf argument does not extend; open conjecture:
  liminf attained at convergent-type two-distance times for all bounded-type β.
- Literature verdict: dephasing is a routine Fourier argument for a specialist; gap laws
  classical; Coelho–de Faria / Dzhalilov–Khomidov full texts unread (risk that golden
  hitting-time laws already tabulated). Rating: short note, not specialist paper, unless
  broadened (Theorem C partly answers this).
- Numerics flag: independent verifier saw +2.6σ pooled c=2 paired excess over 4 seeds;
  16 more seeds (results/seedsweep/) gave pooled z=1.43 over 20 → chance. Comparison must
  use deterministic finite-N values, not limits (offset ≈ −2ac/N).
- Literature round 2: Coelho–de Faria full text read (no phase-x continuum/convex order);
  rating upper-end short note. Manuscript created (author placeholder; no submission).

## 11. Revision round — 2026-11-14 (user: name Euisuh Jeong, Republic of Korea Air Force)

Fable referee (docs/reviews/FABLE_REVIEW.md): major revision, no math errors. Parallel lanes:
gap lemmas proved in N-point convention (49 angles verified); related work (LIT_ROUND3:
Dzhalilov–Khomidov 2024 read in full, no overlap; Coelho 2004 still unread; MS03 citation
was wrong → Caglioti–Golse CMP 236 (2003)); expanded dephasing proof + geometry figure; NEW
coverage-threshold theorem for every irrational (V_N→a² iff c≥πQκ(β), κ=limsup N·maxgap) and
κ≥1+2/√5 with equality iff noble (docs/DISPERSION.md; adversarial review: no counterexample,
minimality not found in literature). Rejected: Fable's "c_* = πQ × Niederreiter constant"
(Niederreiter dispersion is on [0,1]; golden 1.1708 vs circular 1.894). Private GitHub repo
euisuh/circle-tube-vacancy created (not public; flip at submission only with user approval).
