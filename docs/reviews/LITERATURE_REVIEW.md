# Independent literature review: radial dephasing (A) and golden-angle area oscillation (B)

Reviewer pass dated 2026-11-14. Read/search only; no one contacted, nothing paid. `docs/BIBLIOGRAPHY.md` was read as a lead list only; its conclusions were not trusted. Absence of a search hit is not evidence of novelty, and this is a bounded web search, not a systematic survey. I did not verify the proofs of (A) or (B); I only assessed overlap with literature (plus a short plausibility sketch of (A), labelled as mine).

Retrieval legend: FT = full text read (via pdftotext of the fetched PDF); ABS = abstract/landing page only; META = bibliographic metadata/snippets only.

## 1. Sources

### 1.1 Explicit three-distance theorem with counts

| Source | Data | Retrieved | Relevance |
|---|---|---|---|
| Leong, "Sums of reciprocals and the three distance theorem", arXiv:1712.03758 (also N. Leong's White Rose thesis, eprint 17431) | **Theorem 3** (eq. 16-21) | **FT** | Best citable explicit statement found. See below. |
| Alessandri & Berthé, "Three distance theorems and combinatorics on words", L'Enseignement Math. (2) 44 (1998), 103-132 | survey; closest published version per Leong Remark 2 ("[1]", reference not resolved by me) | META only (no full text; ResearchGate says none) | Cite for the theorem, but page/theorem numbers NOT verified. |
| Marklof & Strömbergsson, "The three gap theorem and the space of lattices", Amer. Math. Monthly (2017) | arXiv/author PDF at people.maths.bris.ac.uk/~majm/bib/threegap.pdf | **FT** | States only "at most three gaps" and gives a lattice proof; it gives **no counts or multiplicities** in the text I read. It cites Sós 1957/58, Slater 1967 (Proc. Camb. Phil. Soc. 63, 1115-1123), van Ravenstein (J. Austral. Math. Soc. A 45), Biringer-Schmidt (Geom. Dedicata). Not a source for the N = r q_k + q_{k-1} + s statement. |
| Sós 1957/58; Świerczkowski 1959; Slater 1967; van Ravenstein 1988 | | META (reference list in M-S only; not opened) | Primary-source credit only. |
| Berthé & Reutenauer, "On the three-distance theorem", Math. Intelligencer (2023), irif.fr/~berthe/Articles/Intelligencer.pdf | surfaced in search | META | Expository; not read. |

**Leong Theorem 3 (verbatim from the retrieved text).** Let alpha be irrational, convergents p_k/q_k, D_k = q_k alpha - p_k. For every N there is a unique k >= 0 with q_k + q_{k-1} <= N < q_{k+1} + q_k, and unique integers r, s with
N = r q_k + q_{k-1} + s, 1 <= r <= a_{k+1}, 0 <= s <= q_k - 1,
such that the points {alpha}, ..., {N alpha} split [0,1] into **N+1 intervals**, of which
- N_A = N + 1 - q_k have length delta_A = |D_k|,
- N_B = s + 1 have length delta_B = |D_{k+1}| + (a_{k+1} - r)|D_k|,
- N_C = q_k - s - 1 have length delta_C = delta_A + delta_B.
Remark 4 there: delta_C-gaps exist iff s < q_k - 1. Remark 2 there: "Theorem 3 is not new and can be assembled from published results."

**Offset trap for this project.** Leong's N is the number of points {alpha..N alpha}, and the N+1 intervals of [0,1] are the N+1 circular gaps of the N+1 points {0, alpha, ..., N alpha}. The project's N-point orbit {p_j} has N circular gaps, so apply the theorem with N-1 in Leong's role. Also the project rotation step is 2*alpha in angle, i.e. beta' = 2 alpha/(2 pi) = beta mod 1 in turns for the normal directions (2j+1)alpha, so the rotation number is alpha/pi = beta. Re-derive the indexing before citing. Golden case: all a_k = 1, hence r = 1 = a_{k+1}, delta_B = |D_{k+1}|, delta_A = |D_k|, q_k = F_k-type. N = F_m + k bookkeeping then follows from the theorem directly; no new three-gap input is needed.

**Judgment:** the gap lengths and multiplicities in (B) are classical and citable (Leong Thm 3 with proper attribution to Sós/Świerczkowski/Slater/van Ravenstein/Alessandri-Berthé). Not new.

### 1.2 Covering the circle by arcs centred on orbit points

- Dvoretzky (1956), Shepp (1972), Kahane: random arcs. Background only; random centres, not rotation orbits. (META via Encyclopedia of Math / arXiv 0806.0880 snippets.)
- Fan & Schmeling, "Coverings of the circle driven by rotations", in *Dynamical Systems from Number Theory to Probability II* (ed. A. Khrennikov), Växjö Univ. Press 2002, pp. 7-15. **META only** (Lund record 945911; no abstract retrieved). Title matches the setting (arcs centred on rotation orbits); content unread. Must be read before any novelty claim. Its focus is infinite-time covering/Hausdorff dimension, not the finite-N uncovered *measure* at scale c/N.
- Fan-Schmeling-Troubetzkoy, "Dynamical Diophantine approximation", arXiv:0705.4203 (later Proc. LMS 2013 as a multifractal mass transference paper): doubling map; ABS/META.
- Hauke-Shubin-Stefanescu-Zafeiropoulos, "Circle coverings driven by arithmetic sequences...", arXiv:2604.02005 (2026): **ABS**. Random x, centres {q_n x}, radii C/n; lacunary q_n. Not fixed-alpha rotation, no uncovered-measure formula.
- Kim-Constantine-Constantine, arXiv:1201.0941; Fayad, "On the shrinking target property": infinite-time shrinking targets for rotations; META.
- Zhao, "Almost sure convergence of cover times for psi-mixing systems", arXiv:2412.17425 / ETDS: Sec. 5 treats rotations as a non-mixing counterexample; Thm 5.4 (arXiv v2) assumes Diophantine type eta>1 (liminf of log tau/(-log r) = 1, limsup = eta, mu-a.e.). Cover **time** exponents, not uncovered area at the c/N scale. ABS plus search snippet. Not an overlap with (A) or (B).
- Kesten (1960, 1962, 1966): discrepancy of rotation orbits; the quantity m_N(s) is a "local discrepancy"/uncovered-length functional, so Kesten-type and Dolgopyat-Fayad/Kim style discrepancy results are *related machinery*; no paper found treating the uncovered set at width s/N. META.

**Judgment:** I found no paper that states the finite-N uncovered measure m_N(s) of a rotation orbit at scale 1/N or its subsequential limits as a covering result. It is however exactly a function of the three-gap structure (sum of (g - 2s/N)_+), so the formula in itself is a direct computation from 1.1.

### 1.3 Neighbourhoods of linear flows, geodesics, Lorentz gas, Pólya orchard

- Marklof & Strömbergsson, "On the distribution of free-path lengths for the periodic Lorentz gas III", arXiv:math/0301300 (CMP 2004): torus minus a slit partitioned into three strips Y_A, Y_B, Y_C via the Blank-Krikorian 3-length theorem; area of strips drives free-path law. ABS+snippet. Closest in *spirit* to (B) (three-gap/three-strip structure determines an area-valued observable for a fixed irrational direction). Fixed-direction free-path laws: Dahlqvist; Boca-Gologan-Zaharescu; Boca-Zaharescu, CMP 269 (2007) 425-471; Marklof-Strömbergsson, Nonlinearity 21 (2008) 1413-1422, arXiv:0804.0566. META/ABS.
- Biringer & Schmidt, "The three gap theorem and Riemannian geometry", Geom. Dedicata: geodesic segments and eps-neighbourhoods; META.
- "Filling times for linear flow on the torus with truncated Diophantine conditions", arXiv:2112.11786 (recovers Berti-Biasco-Bolle 2003): about the time needed for the flow to become eps-dense; ABS. Time to fill, not area of the uncovered part at a fixed multiple of the spacing.
- Signerska-Rynkowska, "Curlicues generated by circle homeomorphisms", arXiv:1909.09892: considers Area(Gamma^eps)/eps for polygonal curves built from circle-homeomorphism orbits (curve of N steps with rotation-number-dependent geometry). **Closest "tube area of an orbit-built polygonal curve in the plane"** found; ABS+snippet only. Hypotheses and which claim (limit = infinity) applies to which regime not verified. Different curve (displacement curve, not billiard chords) and eps -> 0 at fixed N, not eps = c/N.
- Pólya orchard: Allen (1986), Hening-Kelly, Adiceam arXiv:1509.04188, arXiv:1805.11679: visibility through lattice discs; related to fixed-direction shadow covering but not to this observable. META.
- Kakeya tubes: delta-neighbourhoods of unit line segments in fixed or varying directions; wrong regime (maximal-function/volume lower bounds, not exact asymptotics). META.

**Judgment:** no source found that gives the area of the c/N-neighbourhood of the first N chords of a circular billiard orbit. Not a statement of absence in the literature.

### 1.4 Fixed-frequency hitting/entrance laws

- Coelho & de Faria, "Limit laws of entrance times for homeomorphisms of the circle", Israel J. Math. 93 (1996), 93-112, DOI 10.1007/BF02761095. **META/ABS only** (Springer paywalled; not read). Reported by citing papers: fixed irrational rotation number, targets are descending renormalization intervals, limit laws exist along subsequences (renormalization/Gauss-map data), including piecewise linear laws; non-exponential. Closest to the *gap-law* part of (B).
- Coelho, "The loss of tightness of time distributions for homeomorphisms of the circle", Trans. AMS 356 (2004), 4427-4445, DOI 10.1090/S0002-9947-04-03386-0. ABS (AMS page / York record): in the natural time scale the hitting-time point process never converges in law; subsequential limits characterized. Same status.
- Kim & Seo, "The waiting time for irrational rotations", Nonlinearity 16(5) (2003), 1861-1868. ABS: liminf/limsup of log K_n / n by Diophantine type. Not area.
- Bonanno & Isola, "A renormalization approach to irrational rotations", Ann. Mat. Pura Appl. 188 (2009), arXiv:0708.0048. ABS: renormalization scheme; they defer limit laws to a forthcoming paper of Bonanno. Machinery relevant to (B).
- Dzhalilov & Khomidov, "Limit law of rescaled hitting time functions for quadratic irrational rotations", Uzbek Math. J. 68 (2024), DOI 10.29229/uzmj.2024-2-7: **META only**; abstract not retrieved. Also Dzhalilov-Khomidov, "Hitting functions for mixed partitions", Vestn. Udmurt. Univ. 33:2 (2023), 197-211. These (quadratic irrational, rescaled hitting time functions) are the most likely place for explicit golden/quadratic laws; must be read.
- Dettmann, Marklof, Strömbergsson, "Universal hitting time statistics for integrable flows", J. Stat. Phys. 166 (2017), 714-749, arXiv:1606.04068. **FT of Sec. 2 read.** (2.11): lambda is f-regular if the pushforward of lambda under J -> f(J)/|f(J)| in S^1 is absolutely continuous; (2.12) genericity; **Theorem 1**: lambda absolutely continuous on U, f-regular and (theta,lambda)-generic gives convergence of rescaled entry times as rho -> 0. Examples include ellipse billiards (circle is e=0) with rotation angle alpha(J) from (4.5). Hypotheses are therefore on an absolutely continuous family of tori/frequencies; **a single fixed frequency (alpha fixed) violates f-regularity**, and the observable is a hitting *time* to a hole, not planar tube area. Not a statement of (A) or (B).
- Follow-up "Genericity on submanifolds and application to universal hitting time statistics", arXiv:2105.11068: ABS only; extends the DMS scheme to submanifold parameter families. Does not appear to cover a single point mass, but I did not confirm. Check.

### 1.5 Circular billiard specifics

- Altmann-Friedrich-Motter-Kantz-Richter, Phys. Rev. E 77, 016205 (2008), arXiv:0711.4585: ABS (per this pass; the prior pass read Sec. II). Star-polygon periodic orbits and scatterers; not tube area of an irrational orbit.
- Chernov & Galperin, "Search light in billiard tables", Regul. Chaotic Dyn. 8(2) (2003) 225-241: illumination by cones of directions; not read here (carried from BIBLIOGRAPHY).
- Bunimovich & Dettmann, open circle and zeta function (Experimental Math., 2024 DOI 10.1080/10586458.2024.2423180): not retrieved. Caustic/boundary-hole survival; different observable (boundary escape). Must be read, as it appears in the same journal I list as a venue.
- Elementary: chords of irrational orbit are tangent to the circle of radius cos(alpha) (caustic); orbit dense in the annulus; chords never enter the inner disk (angular-momentum conservation). Textbook (Tabachnikov, Korsch-Zimmer, Knill handouts); not new.

### 1.6 Chord/strip coverage, integral geometry

Search (see queries) returned only generic polygon pages, plus the curlicue paper above. No Crofton-type or Kakeya-type result on the uncovered area of a union of strips with rotation-orbit directions was found. Absence of hits in this web search tool is weak; a MathSciNet/zbMATH search with MSC 52A22/53C65 (integral geometry) and 37E10/11K06 was not possible and is recommended.

## 2. Citation chasing (closest three: Coelho-de Faria 1996, Coelho 2004, DMS 2017)

- Citations of Coelho 2004 (Semantic Scholar API, 9 entries): Ayupov-Zhalilov 2021 (critical circle maps), Zweimüller 2018, Dumbrell 2018 (rescaled hitting/return), Lucarini et al. 2016, Holland-Rabassa-Sterk 2014, Freitas-Freitas-Todd 2008, Haydn et al. 2004/2005. None indicates a spatial-area observable.
- Citations of Coelho-de Faria 1996 (39 rows, 33 distinct): includes Kim-Seo 2003; Bonanno-Isola 2007/09; Dzhalilov (critical maps 2004; break points 2004; waiting time & dynamic partitions 2019, with Khomidov); Kim-Liao "Dirichlet uniformly well-approximated numbers" 2015; Mohr-Mezic, "Searching for targets of nonuniform size using mixing transformations" (2015); Durand-Maass 2001; Kupsa-Lacroix 2005; Pawelec 2014. By title, the only items near a "search/coverage" flavour are Mohr-Mezic (mixing, not rotation) and Kim-Liao (Dirichlet-improvable). Not opened.
- Forward citations of DMS 2017: only arXiv:2105.11068 (genericity on submanifolds) surfaced. A full Google Scholar/Semantic Scholar forward list was not retrieved (Semantic Scholar API queried for Coelho papers only).
- Backward: Coelho-de Faria's reference list not accessible (paywall). Backward chase of DMS limited to what the arXiv text cites (Santaló formula, Elkies-McMullen, Marklof-Strömbergsson).
- Remaining chasing to do: Fan-Schmeling 2002 text; Dzhalilov-Khomidov 2024 and 2023; Bonanno "Limit laws of rotations"; Alessandri-Berthé [1]-reference identification; Google Scholar forward list for Marklof-Strömbergsson Lorentz III in combination with "tube"/"uncovered".

## 3. Overlap matrix

Scale: Y = states or immediately implies; P = partial/ingredient; N = no overlap seen; ? = could not read.

| Source | Gap lengths/counts (B) | Fixed-alpha subsequential gap/hitting laws (B) | Convex-order/liminf at Fibonacci (B) | Threshold c_* (B) | Planar tube area / billiard chords (A,B) | Radial dephasing / square of mean (A) |
|---|---|---|---|---|---|---|
| Leong Thm 3 (FT) | Y | N | N | N | N | N |
| Alessandri-Berthé 1998 | Y (per Leong's remark; text not read) | N | N | N | N | N |
| Marklof-Strömbergsson Monthly 2017 (FT) | at most three; no counts | N | N | N | N | N |
| Coelho-de Faria 1996 | P | **Y (probably the core framework; unread)** | ? | N | N | N |
| Coelho 2004 | P | Y | ? | N | N | N |
| Dzhalilov-Khomidov 2023/24 | P | likely Y for quadratic irrationals (unread) | ? | N | N | N |
| Bonanno-Isola 2009 | P | P | N | N | N | N |
| DMS 2017 (FT of Sec. 2) | N | N (needs a.c. family, excludes fixed alpha) | N | N | P (billiard flows, hitting times) | N |
| MS Lorentz III / Boca-Zaharescu | P (three strips) | P | N | N | P (strip areas for free path) | N |
| Fan-Schmeling 2002 | ? | ? | ? | ? | N | ? |
| Zhao 2024/25 | N | N | N | N | N | N |
| Signerska-Rynkowska 2019 | N | N | N | N | P (eps-nbhd area of orbit polygon) | N |
| Kesten / discrepancy literature | P (local discrepancy) | P | N | N | N | N |

## 4. Verdict

**(A) Radial dephasing.** Literature: no source found that states it. On the mathematics, my own sketch (not a proof, and not checked against the project's proof) suggests it is a short Fourier argument built from standard pieces: (i) the uncovered set U_N is almost invariant under rotation by 2 alpha, because the orbit changes by one point, so its symmetric difference with its shift has measure O(1/N); thus for each fixed mode k >= 1, |U-hat_N(k)| (1 - e^{2ik alpha}) = O(1/N) and the mode vanishes exactly when alpha/pi is irrational (this is where irrationality enters); (ii) Fubini gives an *exact* identity for the lag-averaged autocorrelation: integral of |U cap (U - t)| dt = |U|^2; (iii) the radial change of variables turns the lag distribution into an L^1 density w, whose Fourier coefficients tend to 0 (Riemann-Lebesgue); Parseval, with sum |U-hat(k)|^2 <= |U| uniformly in N, controls the tail. So the dephasing lemma reduces to "almost-invariance + Fubini + Riemann-Lebesgue", not to a deep hitting-time theorem, and it is routine for a specialist. The genuinely delicate parts are elsewhere: the uniform comparison of the Euclidean tube with the angular-arc model near the caustic r -> a (where the angular width (c/N)/sqrt(r^2 - a^2) blows up) and near the boundary, i.e. the o(1) error control. The identity V_N(c) = a^2 + 2 int q m_N(c/q)^2 dq + o(1) is also not a corollary of any retrieved statement. Net: the *idea* is routine; the *theorem for billiard chord tubes* was not found in the literature. This is not a certification of novelty.

**(B) Golden angle.**
- Gap lengths/counts: classical (Leong Thm 3 and the cited primary sources). Not new.
- Existence of subsequential limit laws along the continued-fraction scale for a quadratic irrational (here a one-parameter family indexed by phase x in [0, lambda]): this is the territory of Coelho-de Faria, Coelho, Bonanno-Isola and Dzhalilov-Khomidov. The phase-x family is very probably already contained there for hitting-time distributions. I could not read them, so I cannot say the explicit gap law is not already tabulated.
- Convex-order domination (every phase-x gap law dominating the Fibonacci law) giving liminf at Fibonacci N: not found in any source retrieved. It is plausible as an elementary Jensen-type fact for convex functionals (g -> (g - 2s)_+ is convex and all laws have the same mean). Possibly new as a statement, but short; absence of a hit is not novelty.
- c_* = pi sin(alpha)/(sqrt5 lambda^3) ~ 5.547: I checked only arithmetic consistency (lambda^3 sqrt5 = 0.5279; with alpha = pi (3 - sqrt5)/2 ~ 1.2000 rad, sin alpha ~ 0.932, the formula gives ~5.55). I did not verify the derivation.

**What is genuinely additional (if the project's proofs hold):** (1) the translation from the spatial tube area to a radial integral of the square of the rotation uncovered measure, with the caustic/boundary error control; (2) the explicit limsup/liminf region and threshold c_* for the golden billiard orbit; (3) the convex-order minimality of Fibonacci N.

**Significance rating: (ii) short note** (Experimental Mathematics, Amer. Math. Monthly or similar), provided (a) Fan-Schmeling 2002, Dzhalilov-Khomidov 2023/24, Bonanno's limit-laws work and Coelho-de Faria are actually read and cited with the new theorem correctly positioned as "area observable for a classical subsequential-gap-law input", and (b) the caustic-end error is proven. Reasons against (iii): the rotation/gap ingredients are classical, the dephasing step is routine Fourier analysis, and the setting is a single specific orbit family; a specialist-paper claim would need a broader theorem (all irrational beta with a bounded-type or general continued-fraction criterion for nonconvergence of V_N(c); other caustic geometries or convex tables; or the joint statistics of two branches at fixed r). Reasons it may fall to (i): if Dzhalilov-Khomidov or Coelho-de Faria already tabulate the golden gap/hitting law and the "area" step is viewed as routine. This is a judgement from titles, abstracts and one partial full-text read, not a ruling.

## 5. Honest limits of this pass

- Full text actually read: Leong 1712.03758 (Thm 3 region), Marklof-Strömbergsson Monthly paper (intro, reference list), DMS 1606.04068 (Sec. 2 hypotheses, Theorem 1 statement, billiard example listing). Everything else is abstract/metadata/snippet.
- Search tool is US-only web search with summarising fetch; PDF fetches returned compressed bytes and were converted locally with pdftotext. Springer/Taylor&Francis/AMS full texts were not accessed.
- Not done: Google Scholar/MathSciNet/zbMATH forward-citation lists; reading Fan-Schmeling 2002, Dzhalilov-Khomidov, Coelho-de Faria, Coelho 2004; identifying reference [1] in Leong (the "closest published version").

## 6. Queries and fetches run (all 2026-11-14)

Web searches:
1. Alessandri Berthé "Three distance theorems and combinatorics on words" L'Enseignement Mathématique 1998
2. three gap theorem lengths multiplicities N = r q_k + q_{k-1} + s statement
3. uncovered set circle covered by arcs centered at n alpha shrinking length irrational rotation Dvoretzky covering
4. Fan Schmeling Troubetzkoy dynamical Dvoretzky covering problem rotation
5. epsilon-neighbourhood of linear flow trajectory segment torus area covered three gap theorem free path length
6. circular billiard orbit chords union neighborhood area uncovered caustic rotation number irrational coverage
7. Coelho de Faria "Limit laws of entrance times for homeomorphisms of the circle" Israel J. Math 93 1996 ...
8. Dzhalilov Khomidov "Limit law of rescaled hitting time functions for quadratic irrational rotations"
9. Zhao "cover times" rotation irrational Diophantine type liminf limsup covering time circle shrinking balls arXiv
10. Kesten "Uniform distribution mod 1" covering circle by arcs centered n alpha random discrepancy coverage time rotation
11. Marklof Strömbergsson Kinetic transport ... free path three gap theorem fixed direction Boca Zaharescu limiting distribution
12. Pólya orchard problem visibility fixed direction tube area ... Kakeya
13. Kim Seo "The waiting time for irrational rotations" Nonlinearity 2003 abstract
14. Bonanno Isola "A renormalization approach to irrational rotations" Poincaré recurrences golden mean limit distribution
15. union of strips around chords tangent to a circle uncovered area irrational rotation inscribed polygon star polygon neighbourhood area asymptotics
16. "shrinking target" rotation "uncovered" measure Lebesgue measure ... Steinhaus
17. Dettmann Marklof Strömbergsson "Universal hitting time statistics for integrable flows" J. Stat. Phys. 166
18. Altmann Friedrich Motter Kantz Richter "Prevalence of marginally unstable periodic orbits in chaotic billiards" Phys. Rev. E 77 016205
19. "Curlicues generated by circle homeomorphisms" Minkowski epsilon neighbourhood area golden ratio rotation Fibonacci

Fetches: arxiv.org/pdf/1712.03758 (FT via pdftotext); arxiv.org/abs/2604.02005; people.maths.bris.ac.uk/~majm/bib/threegap.pdf (FT via pdftotext); lup.lub.lu.se Fan-Schmeling record; arxiv.org/abs/2112.11786; Semantic Scholar citations API for Coelho 2004 and Coelho-de Faria 1996; arxiv.org/abs/1606.04068; arxiv.org/pdf/1606.04068 (FT via pdftotext); arxiv.org/abs/1909.09892; arxiv.org/abs/2105.11068. Note: some summaries were produced by the fetch tool's small model; only items marked FT were checked against raw extracted text.

---

# Round 2 (2026-11-14)

Scope: (1) overlap for Theorem C of `docs/THEOREM.md` and its 1D inputs; (2) retry access to four papers; (3) revised rating for A+B+C. Same caveats: web search plus local pdftotext, no proof verification of A/B/C beyond reading Theorem C's stated argument in THEOREM.md (C.1-C.4), which looked internally consistent.

## R2.1 Theorem C and its 1D facts

Facts to source:
- (F1) Jensen/mean-gap bound m_N(s) >= (1 - s/π)_+. Elementary (sum of (g - t)_+ >= (sum g - N t)_+, convexity). No source needed; do not cite as a result.
- (F2) Scaled gap law of {nα} approaches the uniform (single-atom) law along a subsequence of N iff α has unbounded partial quotients.
- (F3) N·(max gap) bounded iff α badly approximable (iff partial quotients bounded).
- (F4) Planar or "coverage" characterization of bounded type.

Sources found:

| Fact | Source | Retrieved | Status |
|---|---|---|---|
| F2, "if" direction | Follows directly from the three-gap statement at N = q_k: gaps η_{k-1}, η_{k-1}+η_k with ratio 1 + η_k/η_{k-1} < 1 + 1/a_{k+1}. Statement of the counts: Leong Thm 3 (Round 1); also Alessandri-Berthé 1998 (unread). | FT (Leong) | Folklore consequence of the three-gap theorem; THEOREM.md C.2-C.3 re-derives it. No separate primary source needed. |
| F2, 1D hitting-time analogue | **Coelho & de Faria 1996, Thm I(a)**: for a subsequence n_i, the entrance-time distributions F^{(1)}_{n_i} (to renormalization intervals J_n at the q_n scale) converge iff either (a) G^{n_i}(α) -> 0, limit = **uniform on [0,1]**, or (b) Γ^{n_i}(α,·) -> (θ,ω), limit piecewise linear F_σ. Remark A: (a) happens along a subsequence for a.e. α (Gauss ergodicity). | **FT** (author copy, York) | Closest primary statement of "uniform law along a subsequence" in the literature. G^{n_i}(α) -> 0 means a_{n_i} -> infinity, so (a) occurs for some subsequence iff the partial quotients are unbounded (the "only if" direction is my reading of the condition; not stated as such in their text that I saw). It concerns entrance times to J_n, not the gap law of N orbit points for every N, though the two are dual via the three-gap/return-time structure. |
| F2 as an "iff bounded type" statement | **Coelho 2004 (Trans. AMS 356, 4427-4445)** abstract (AMS page and York record): in natural time scale the rescaled hitting-time point process never converges in law ("loss of tightness"); search summary of the abstract: for unbounded type some sequence ε_n -> 0 gives two nontrivial limit processes depending on time scale; tightness iff bounded type. | ABS only; full text not accessed | This is a published 1D "bounded type iff tightness" characterization, spirit-adjacent to Theorem C. It is a statement about hitting-time laws, not about uncovered measure or the area functional. |
| F3 | Ramírez, "Khintchine types of translated coordinate hyperplanes", arXiv:1405.7277, §4: "Formula (2) shows that r_x [gap ratio] is always bounded iff x is badly approximable"; with Lemma 11 (ratio <= R gives 1/(RL) < ℓ_min < 1/L < ℓ_max < R/L). Formula (2) is credited there to "[MK98]" (not resolved by me; likely a continued-fraction gap-ratio reference). | **FT** (arXiv PDF, local pdftotext) | Gives bounded gap ratio iff bounded type, which implies N·max gap = O(1) when type is bounded. The converse (N·max gap bounded for all N forces bounded type) is not stated as such in what I read; see the derivation noted below. |
| F3 as folklore | Definition-level: badly approximable iff bounded partial quotients (many sources, e.g. arXiv:1604.02413, arXiv:2410.02357 snippets). | META | Classical. I found no one-line primary source for "N·max gap bounded for all N iff badly approximable". |

Derivation (mine, supporting the F3 converse; not a citation): by THEOREM.md C.3, along N = r q_k + q_{k-1} with r = ceil(a_{k+1}/2) the sparse gap class has frequency q_k/N -> 0 and total length -> 1/2, so its scaled length -> infinity when a_{k+1} -> infinity. Hence unbounded type makes N·max gap unbounded.

F4: **no source found** stating a planar, area, or "coverage" characterization of badly approximable/bounded type in terms of an uncovered-measure functional at scale c/N, or of billiard-chord tube area. Nearby but different: Zhao (cover times, type eta>1 affects exponents; Thm 5.4 arXiv v2); Kim-Seo (waiting-time exponents via type); Coelho 2004 (tightness iff bounded type); Ramírez (gap ratios iff badly approximable); Fan-Schmeling 2002 (coverings driven by rotations; text not obtained). A characterization "lim inf of an uncovered-measure/area functional strictly exceeds its uniform-gap envelope iff bounded type" would be, as far as this search can say, a new packaging of known 1D dichotomies. Not proof of novelty.

Overlap judgment for Theorem C:
- Part 1 (liminf >= V_δ) is Jensen on top of Theorem A: elementary once A holds.
- Part 2 (unbounded: liminf = V_δ, limsup > V_δ, divergence for all c) is the area transfer of F2 plus the C.3 two-distance-time computation; the 1D inputs are classical/Coelho-de Faria-type.
- Part 3 and the corollary (bounded type iff liminf > V_δ at fixed c in (0, πQ)): the 1D fact "bounded type iff the scaled gap law stays away from a point mass" is classical in spirit (compare Coelho 2004 "tightness iff bounded type"); the explicit non-degeneracy lemma in C.4 with ε = 1/((A₀+1)(A₀+2)) is a quantitative form I did not find in print. Its three-distance counting claims (frequency lower bounds q_{k-1}/(q_{k+1}+q_k) etc.) look right against Leong Thm 3 but I did not recheck every inequality.

## R2.2 Access retry (what was actually retrieved)

| Paper | Result | Golden phase-x family? | Convex-order minimality? |
|---|---|---|---|
| Coelho & de Faria 1996 | **Full text obtained** from the author's York page (www-users.york.ac.uk/~zc3/download/circle, 17 pp, pdftotext). Read abstract, intro, Thms I-V statements, Remarks A-B. Proofs not audited. Thm I: limit F^{(1)} along σ is uniform if G^{n_i}(α) -> 0, else a continuous piecewise linear F_σ depending on the limit (θ, ω) of the double Gauss map Γ^{n_i}(α,·), 0<ω<1, θ>0 (their Fig. 1). Thm II: higher entrance times; Thm III: point process; Thms IV-V: Lebesgue-random start for C¹-conjugate-to-rotation diffeomorphisms. | **Structure yes, explicit golden statement no.** For golden α, Γ^n(α,·) converges along n to a periodic (period-2-like) set of (θ, ω); so a finite family of piecewise linear limits arises, parametrized by (θ, ω) at renormalization times only. Whether the *continuum* phase-x family of the project's (B) (N = F_m + k with k/F_{m-1} -> x) appears is **not stated**: their J_n are renormalization intervals at fixed times n, so intermediate N are not covered by their Theorem I. | No. Not stated; Jensen-type or convex ordering of the limit laws does not appear. |
| Coelho 2004 | **Full text not obtained.** AMS page, York research database, ResearchGate (no full text), Semantic Scholar (landing). Abstract only; no author-hosted copy found at the guessed York download path in the search results. | Cannot say. Its "all subsequential limits" characterization could contain the phase family: **unread, must check**. | Cannot say. |
| Dzhalilov-Khomidov 2023 (Vestnik Udmurt. Univ. 33:2, 197-211) | **Full text obtained** (vst.ics.org.ru PDF, 15 pp). Studies K_n = log N_n / (…) for **dyadic/mixed partitions** (Kim-Seo setting), convergence a.e. to a piecewise constant function with two values; Theorem 5 for quadratic irrationals concerns that log-scaled hitting function. Different observable. | **No.** No gap-law or phase-x family; no golden statement of the kind in (B). | No. |
| Dzhalilov-Khomidov 2024 (Uzbek Math. J. 68, DOI 10.29229/uzmj.2024-2-7) | **Full text not obtained.** Only the issue-2 table of contents page (1-page preview PDF) and metadata. No arXiv version found. Title suggests the same log-scaled rescaled hitting function for quadratic irrationals, not the gap law. | Unknown. By title and by the 2023 sibling paper, probably not. Unread. | Unknown. |
| Fan-Schmeling 2002/2003 (Växjö Univ. Press, Vol. 6, pp. 7-15) | **Full text not obtained** (Lund record 945911 has no file; no open copy found). Troubetzkoy, "Approximation and billiards" (arXiv:math/0611599, survey; read the citing lines) only says Fan-Schmeling analyze "the rotation driven dynamical variant of the classical Dvoretzky covering of the circle" and cites it. | Unknown. | Unknown. |

Bottom line for item 2: of the four, two were read in full-text form (Coelho-de Faria, Dzhalilov-Khomidov 2023), two remain unread (Coelho 2004; Dzhalilov-Khomidov 2024) plus Fan-Schmeling. Within what was read, **neither the continuum golden phase-x gap family nor convex-order minimality of the Fibonacci law appears.** That is partial negative evidence only: Coelho 2004 is the most likely place for general subsequential limits and remains a must-read; Fan-Schmeling is the most likely place for rotation-driven covering and also remains unread.

Additional queries/fetches (2026-11-14): "gaps of n alpha mod 1 maximal gap N times max gap bounded iff badly approximable ..."; "Coelho de Faria ... pdf"; "Dzhalilov Khomidov hitting functions quadratic irrational rotations arXiv limit law golden ratio"; "Coelho loss of tightness ... york.ac.uk zc3 download pdf"; "Khomidov Dzhalilov Limit law ... Uzbek Mathematical Journal 2024 pdf"; "Fan Schmeling Coverings of the circle driven by rotations pdf". Fetches: York copy of Coelho-de Faria (curl, 17 pp); vst.ics.org.ru Vestnik PDF; arXiv:1405.7277 PDF; arXiv:math/0611599 PDF; yangi.cspu.uz issue PDF (1-page preview only); AMS page for Coelho 2004 (no abstract parsed by curl).

Corrections to Round 1: the "research-level" assertion in Round 1 that Coelho-de Faria's Theorem I was "probably the core framework" is now confirmed for the uniform/piecewise-linear dichotomy, but their targets are renormalization intervals at times n, not "all N". Also, in my Round 1 table I wrote that Dzhalilov-Khomidov 2023/24 "likely Y for quadratic irrationals" on the gap-law column; the 2023 paper read here is about a different observable (dyadic-partition hitting functions) so that "likely Y" should be downgraded to "no (2023); unknown (2024)".

## R2.3 Updated significance rating (A + B + C together)

**Rating: (ii), upper end: a solid short paper, not yet (iii).** Revised from "short note" because A, B and C together give a single coherent statement: for a circular-billiard orbit with fixed angle, the c/N-tube vacancy V_N(c) has liminf equal to the uniform-gap envelope V_δ(c) exactly for unbounded type, strictly larger for bounded type, and for the golden angle the whole limit set and the threshold c_* are explicit. As far as this search shows, that planar coverage characterization of bounded type is not in print.

Why not (iii):
- Every 1D ingredient is classical or sits in known territory: three-gap counts (Sós/Świerczkowski/Slater/van Ravenstein/Alessandri-Berthé), uniform vs non-uniform subsequential gap/hitting laws and bounded-type tightness (Coelho-de Faria 1996, Coelho 2004), bounded gap ratio iff badly approximable (e.g. Ramírez §4).
- Theorem A's dephasing step reads as routine Fourier analysis (my Round 1 sketch); Theorem C(1) is Jensen; Theorem C(2) is a two-distance-time computation. The technical weight is in the caustic/boundary error control for A, which I have not seen.
- The golden phase family and convex-order minimality are possibly the best original 1D content, but Coelho 2004 and Dzhalilov-Khomidov 2024 (unread) could already contain the family; convex ordering is a short argument.

What would push it to (iii): extending B's minimality to a general criterion beyond noble angles (the project's own note says block-wise convex-order domination fails for silver and other angles, so the lim inf is only known at convergent times there), proving the "open" question that lim inf V_N is always attained along two-distance times, or generalizing A to other convex tables/caustic families with uniform error bounds.

What would push it to (i): confirmation that Coelho 2004 / Fan-Schmeling / Dzhalilov-Khomidov 2024 already state the phase-x family and uniform-law criterion in a form from which A's transfer is a one-line corollary. I read neither in full text.

Not a novelty certification; venue and acceptance are editorial judgments.
