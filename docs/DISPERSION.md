# Coverage threshold for every irrational angle (2026-11-14)

Status labels: **audited argument** (own proof, checked against computation) unless stated. LaTeX version with the
same statements: `manuscript/sections/dispersion.tex` (labels `disp:*`). Scratch checks: `docs/dispersion_scratch/disp_check.py`
(output saved in `docs/dispersion_scratch/out.txt`).

## Normalization
Gaps g_{N,j} of θ_j=(2j+1)α mod 2π (= 2π × gaps of {jβ}_{j<N}); G_N=max g; h_N=G_N/2π (largest gap in turns);
**D_N = N G_N/2 = π N h_N** (radians; the largest atom of μ_N=N⁻¹Σδ_{N g_j/2}); κ(β)=limsup N h_N; L(β)=πκ(β)=limsup D_N.
Circle dispersion d^T_N=h_N/2 (geodesic metric), so D_N=2πN d^T_N. m_N(s)=(2π)⁻¹Σ(g_j−2s/N)_+ ; m_N(s)=0 ⇔ s≥D_N.
E_N(c)=Ṽ_N(c)−a²=2∫_0^Q q m_N(c/q)² dq ≥ 0. Ṽ_N(c)=a² exactly when c ≥ Q·D_N.

## Statements and proofs
**Lemma 1 (mass).** (n_N/N)(D_N−s)_+/π ≤ m_N(s) ≤ (D_N−s)_+/π, n_N = multiplicity of the largest gap. (Each term of the sum lies in [0,(2/N)(D_N−s)_+], n_N terms attain the top.)

**Lemma 2 (reduction).** E_N(c)→0 ⇔ m_N(c/Q+δ)→0 ∀δ>0; limsup E_N>0 ⇔ limsup m_N(c/Q+δ)>0 for some δ>0. (m_N monotone, ≤1: lower bound E_N ≥ ε²(Q²−q_δ²), q_δ=c/(c/Q+δ); upper bound splits at q_δ.)

**Theorem 1 (iff, every irrational β∈(0,1/2)).** With c_cov(β)=Q·L(β)=πQκ(β):
(i) c ≥ c_cov ⇒ V_N(c)→a². (ii) c < c_cov ⇒ limsup V_N(c) > a². So V_N(c)→a² ⇔ c ≥ c_cov (never if κ=∞).
Proof. Theorem A: V_N−Ṽ_N→0. (i): D_N ≤ L+δ/2 < c/Q+δ eventually ⇒ m_N(c/Q+δ)=0, Lemma 2. (ii): let Λ=inf{σ: m_N(σ)→0}; if c/Q<Λ pick δ with c/Q+δ<Λ, then m_N(c/Q+δ)↛0, Lemma 2. Λ≥L is Prop. 3. ∎

**Lemma (three-gap blocks, classical: Sós; Alessandri–Berthé; Leong).** β=[0;a_1,…], q_k, η_k=‖q_kβ‖. For k≥1, 1≤r≤a_{k+1}, 0≤t<q_k, N=rq_k+q_{k−1}+t: gaps η_k ×(N−q_k), η_{k−1}−(r−1)η_k ×(q_k−t), η_{k−1}−rη_k ×t. Largest gap ℓ_{k,r}=η_{k−1}−(r−1)η_k, multiplicity q_k−t≥1. Verified exactly by `disp_check.py` §1: 0 mismatches over all N≤2500 for 7 angles (golden, two other noble, silver, [0;3,3,..], [0;2,1,2,1,..], 1/e).
With s_k=q_{k−1}/q_k, t_k=η_k/η_{k−1}=[0;a_{k+1},…]<1/a_{k+1}: q_kη_{k−1}=1/(1+s_kt_k).
**Corollary (limsup formula).** N h_N is maximal in block (k,r) at N_{k,r}=(r+1)q_k+q_{k−1}−1, and
κ(β)=limsup_k max_{1≤r≤a_{k+1}} (r+1+s_k)(1−(r−1)t_k)/(1+s_kt_k).

**Proposition 3 (Λ=L).** Bounded type a_k≤A: take σ<L, ε with (1−ε)(L−ε)>σ, infinitely many blocks with D_{N_{k,r}} ≥ L−ε; N'=N_{k,r}−⌈εq_k⌉ stays in the block, same largest gap, multiplicity ≥εq_k, D_{N'}≥(1−ε)D_{N_{k,r}} (as N_{k,r}≥2q_k−1), frequency ≥ε/(A+2) (N≤(A+2)q_k). Lemma 1 ⇒ m_{N'}(σ) ≥ ε((1−ε)(L−ε)−σ)/(π(A+2)) >0 uniformly in k. Unbounded type: Theorem C(2) gives limsup V_N>a² for all c, hence Λ=∞; and L=∞ (r=⌈a_{k+1}/2⌉ gives bracket ≥a_{k+1}/8). ∎

**Converse: it HOLDS (exact iff); no counterexample.** The worry (largest-gap frequency →0) is real at single N: at N_{k,r} the largest gap has multiplicity 1 (golden: weight f_0=(λ−x)/(1+x)→0 at x=λ). But stepping back by εq_k keeps the same largest gap with frequency ≳ε and loses a factor (1−ε), so the threshold is unaffected. Needs bounded N/q_k, i.e. bounded type; unbounded type is covered by Theorem C(2).

**Proposition 4 (smallest normalized threshold; own proof, circular constant).** κ(β)≥1+2/√5=1.89443… for all irrational β, equality iff β noble. If a_{k+1}≥2 infinitely often then κ≥2 (r=1: (2+s)/(1+st)>(2+s)/(1+s/2)=2 as t<1/2). If a_k=1 eventually: t_k=λ, s_k→λ, only r=1, limit (2+λ)/(1+λ²)=(2+λ)/(2−λ)=1+2/√5. Hence c_cov/(πQ)=κ ≥ 1+2/√5 and c_cov(β) ≥ c_*(β)=πsin(πβ)/(√5λ³), equality iff noble. Normalization caveat: Q=sin πβ depends on β, so "smallest" only after dividing by πQ. Example: silver β=√2−1: κ=1+3√2/4=2.0607.

## Literature: what was actually retrieved (access level: secondary only)
- Niederreiter, "On a measure of denseness for sequences", in *Topics in Classical Number Theory* Vol. II, Colloq. Math. Soc. János Bolyai 34, North-Holland 1984, pp. 1163–1208. **Original NOT read.** Citation confirmed via Tripathi, "A comparison of dispersion and Markoff constants", Acta Arith. 63 (1993) 193–203 (PDF read, text extracted) and Rivoal / arXiv 2404.16352 (snippets).
- Definition retrieved (Tripathi): for x_n∈[0,1], d_N=sup_{0≤x≤1} min_{n≤N}|x−x_n|, D({x_n})=limsup N d_N; D(α)=D({nα mod 1}). **Interval, Euclidean metric — not circular.** Drobot's formula (Tripathi p.1): D(α)=limsup ψ_i(n_i). Niederreiter's Thm 6 (p.1197 per Tripathi) reduces to purely periodic expansions. Rivoal (snippet): Niederreiter and Jager–De Jong dispersion constants are minimal at the golden number (interval version). Arxiv 2404.16352: Kronecker sequence is low-dispersion iff α badly approximable ([Niederreiter 1984], Drobot 1986).
- NOT found: any statement that the circular constant is 1+2/√5 or that noble numbers are exactly the minimizers. Fable's claim "c_*=πQ × Niederreiter's constant" is **wrong as stated**: numerically the interval constant at golden is (1+3/√5)/2≈1.1708 (sup N d_N over N∈[75025,121393): 1.17081), while circular N·maxgap → 1+2/√5=1.8944 (1.89441 observed). Circular minimality is therefore established here by Prop. 4 (own proof), not by citation; possible overlap with Niederreiter/Drobot unverified.

## Numerical verification (`disp_check.py`, output `out.txt`)
1. Block structure: 0 mismatches / ≈12 000 cases.
2. κ from block formula (high-precision η_k, last blocks q_k>200, converging): golden→1.8941 (limit 1.8944), noble [0;3,1,..]→1.8942, [0;2,2,1,..]→1.8941, silver→2.0606 (exact 2.0607), [0;3,3,..]→2.1094, [0;2,1,2,1,..]→ alternating 1.866/2.1546 (limsup 2.155), 1/e→ blocks 1.6–3.4 (unbounded, κ=∞ eventually). Brute-force sampled sup of N h_N agrees within sampling error (e.g. silver 2.0604, golden 1.8879 sampled).
3. Ṽ_N(c)−a² at N = block-end − 1% q_k, last 3 blocks (q_k≤3·10⁴): for c=1.03c_cov exactly 0 at every sampled N, all 5 bounded angles; for c=0.97c_cov ≈1–2·10⁻⁹ and c=0.8c_cov ≈2–4·10⁻⁵, constant across blocks (positive, not decaying; small because the sampled largest-class frequency is ~0.01q_k/N). Caveat: this probes only the extremal phase, not the full limsup; the threshold itself rests on the proof.
4. Unbounded 1/e at N=⌈a_{k+1}/2⌉q_k+q_{k−1}: excess(c=2)=0.081,0.104,0.120 and excess(c=4)=0.004,0.018,0.033 for k=6,9,12 (a_{k+1}=4,6,8): positive and growing, consistent with Theorem C(2) (no threshold).
Not done: direct Monte-Carlo V_N (Theorem A covers V_N−Ṽ_N→0); proof of the 3-gap lemma (cited, computer-checked).
