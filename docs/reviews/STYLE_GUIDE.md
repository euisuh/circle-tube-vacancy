# Style guide for rewriting the manuscript (evidence-based, 2026-11-20)

Purpose: fix the author's complaint that corollaries and Sections 5–7 are hard to read because
chains of formulas are crammed inline. Rules below are derived from recent published papers in
the paper's field (three-distance theorem, Kronecker gaps/dispersion, shrinking targets, uniform
distribution theory), read in full or in the sections indicated. Target venues: Uniform
Distribution Theory, then Monatshefte, Experimental Mathematics.

Scope of this document: style only. No mathematical content is changed; the paper itself was not
edited.

---

## (a) Sources

Files were downloaded to the session scratchpad and read with `pdftotext`. "Read" lists the pages
actually examined.

| # | Citation | Venue / status | URL | Read |
|---|----------|----------------|-----|------|
| S1 | A. Haynes, J. Marklof, *A five distance theorem for Kronecker sequences* | IMRN 2022(24), 19747–19789 (arXiv v3, 34 pp.) | https://arxiv.org/abs/2009.08444 | pp. 1–5 (intro, Thms 1–3, Figs 1–3), 12–16 (Props 8–11, proofs) |
| S2 | D. Badziahin, J. Shallit, *Badly approximable numbers, Kronecker's theorem, and diversity of Sturmian characteristic sequences* | J. Théor. Nombres Bordeaux 35 (2023) 1–15 | https://arxiv.org/abs/2006.15842 ; https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.1236/ | pp. 1–8 (intro, three-gap Thm 3, main Thm 4, Lemma 5, Cor 6–7, Thm 8) |
| S3 | S. Chow, N. Technau, *Dispersion and Littlewood's conjecture* | Adv. Math. 447 (2024) 109697 | https://arxiv.org/abs/2307.14871 | pp. 1–4 (intro, Thms 1.1–1.14), 7–10 (Lemma 2.2 proof, §3 Dispersion, Thm 3.1) |
| S4 | C. Weiß, *Approximation of discrete measures by finite point sets* | **Unif. Distrib. Theory 18 (2023) no. 1, 31–38** | http://pcwww.liv.ac.uk/~karpenk/JournalUDT/vol18/no1/03_Weiss_pdf.pdf | all 8 pp. |
| S5 | M. Paštéka, *On uniform distribution modulo 1 and functional convergence* | **Unif. Distrib. Theory 19 (2024) no. 1–2, 33–42** | https://reference-global.com/2/v2/download/pdf/10.2478/udt-2024-0004 | pp. 1–4 (intro, §1 criteria, Thms 1–3, Cor 1 + proof) |
| S6 | C. Weiß, *Deviation from equidistance for one-dimensional sequences* (gap ratio function) | Aequationes Math. 97 (2023) 683–705 (OA) | https://doi.org/10.1007/s00010-023-00958-x | pp. 1–4 (intro, Lemma 1.1, Props 1.2/1.4, Thm 1.3), 12–14 (§2 Kronecker/LS gap lists, Thm 2.7) |
| S7 | C. P. Dettmann, *Kronecker sequences with many distances* | **Experimental Mathematics 34 (2025) no. 2, 225–236** | https://doi.org/10.1080/10586458.2024.2340742 ; https://people.maths.bris.ac.uk/~macpd/alone/Kronecker_sequences_with_many_distances.pdf | pp. 1–3 (intro, Thms 1–5, Fig 1), 6–8 (Figs 3–4, Table 1, §3.3–3.7 numerics) |
| S8 | N. Moshchevitin, *On an example by Poincaré and sums with Kronecker sequence* | **Monatsh. Math. 206 (2025) 195–216** (arXiv v2) | https://arxiv.org/abs/2310.05003 | pp. 1–3 (intro, §1–2), 9–11 (Thm 1 + proof, Thms 2–3) |
| S9 | V. Beresnevich, S. Datta, A. Ghosh, B. Ward, *Rectangular shrinking targets for Z^m actions on tori* | arXiv 2023 (shrinking targets for rotations; venue not confirmed) | https://arxiv.org/abs/2307.10122 | pp. 1–3 (intro, Thm 1.1, Def 1.2, Thm 1.3, §2 setup), 9–10 (§5 proof) |
| S10 | S. Kim, *Bounds on the gaps in the fractional parts of a linear form* | arXiv v2 Feb 2025 (Marklof–Strömbergsson lattice method) | https://arxiv.org/abs/2312.02414 | pp. 1–3 (intro, Thm 1.1(a)–(c), Corollary, organisation) |
| S11 | T. Hamada, *A concise geometric proof of the three distance theorem* | arXiv v6 Jul 2024 (not published; included as a 3-distance exposition with figures) | https://arxiv.org/abs/2308.11999 | all 6 pp. |

Published 2022–2026: S1–S8 (8 papers), of which two are UDT (S4, S5), one Monatshefte (S8), one
Experimental Mathematics (S7). Marklof-style expository-rigorous: S1, S10.

Measured inline-relation density (sentences in proof pages; relation symbols =,<,>,≤,≥,→,∈
counted; heuristic, PDF text for sources vs TeX source for ours, so compare orders of magnitude,
not single points):

| Text | sentences | with ≥3 inline relations | with ≥4 | mean relations/sentence |
|------|-----------|--------------------------|---------|-------------------------|
| S1 Haynes–Marklof pp. 12–16 | 77 | 42% | 25% | 2.5 |
| S2 Badziahin–Shallit pp. 4–7 | 65 | 23% | 9% | 1.5 |
| S3 Chow–Technau pp. 7–10 | 47 | 21% | 11% | 1.3 |
| S4 Weiß UDT pp. 6–7 | 26 | 12% | 8% | 1.0 |
| S8 Moshchevitin pp. 9–11 | 44 | 25% | 16% | 2.0 |
| S9 Beresnevich et al. pp. 9–10 | 25 | 24% | 20% | 2.0 |
| S11 Hamada pp. 4–5 | 41 | 32% | 22% | 2.6 |
| **ours: main.tex** | 125 | 32% | 24% | 2.1 |
| **ours: sections/dephasing.tex** | 68 | 53% | 34% | 2.7 |
| **ours: sections/dispersion.tex** | 54 | 54% | 43% | 3.3 |
| **ours: sections/gaplemmas.tex** | 100 | **64%** | **50%** | **4.0** |
| ours: sections/related.tex | 20 | 0% | 0% | 0.05 |

Reading: the published papers keep roughly 60–90% of proof sentences at ≤2 inline relations and
move the rest into displays (S3 and S9 have about one display line per prose sentence in their
proof pages). Our Sections 5 and 7 invert that ratio.

---

## (b) Conventions observed, with examples

### B1. Theorem/corollary statements

1. **Hypotheses in prose, conclusion displayed.** Every main statement in S1–S3, S8, S9, S10 puts
   the quantitative conclusion on its own numbered display, even when short.
   - S3 Thm 1.5: "Let ε > 0, α ∈ K and γ ∈ R. Then there exists G ⊆ Bad with dim_H(G) = 1 such
     that if β ∈ G and δ ∈ R then [display (1.1)] has infinitely many solutions n ∈ N."
   - S8 Thm 1: two displayed, numbered conclusions (19), (20), each one line.
   - S1 Thm 1: a one-line hypothesis sentence, then a displayed `cases` (1.3).
2. **Multiple conclusions → enumerated items, one relation per item.**
   - S10 Thm 1.1: items (a), (b), (c), each a single displayed inequality.
   - S4 Thm 1.2 (UDT): items (i)–(iii), each ending in a displayed inequality
     `D*_N(μ,ν_N) ≥ 1/(6N)`; S4 Thm 1.1 likewise.
   - S11 Thm 1 and Thm 2: bullets "• n+1−b of them have length bα−a, • n+1−d of them have length
     c−dα, • b+d−(n+1) of them have length (b−d)α+c−a."
   - S2 Thm 3 (van Ravenstein's three-gap theorem): the gap set is a displayed `cases` by range of
     N, not a prose list.
3. **Case/multiplicity data in `cases` or aligned lists, never comma-separated inline.**
   - S6 §2: gap lengths of an LS-sequence as five aligned lines `L_1 = β^{n+1}, L_2 = …, L_5 = …`
     followed by five aligned multiplicity lines `N_1 = …, …, N_5 = …` (pp. 694–695).
   - S2 Thm 4: `f(B) = cases{1+(a+1)^2/(2√(a²+2a)) if B=2a; 1+(a²+3a+2)/√(4a²+12a+5) if B=2a+1}`.
4. **Named constants are defined in a display before the theorem, then used by name.**
   - S3: `K := {α : Λ(α) < ∞}` displayed before Thm 1.3; S9: weighted quasi-norms displayed
     before "Weighted Dirichlet's theorem".
5. **Corollaries are short (≤3 lines), one displayed relation, and name their parent.**
   - S2 Cor 6: "We have B/4 ≤ f(B) ≤ (1+√(4/5))B." (one display-ready relation);
     Cor 7: one sentence of setup, one displayed formula for N and g.
   - S3 Cor 1.6/1.10/1.12/1.14: each ≤3 lines, reuses the displayed equation label (1.1)/(1.3)
     rather than restating the formula.
6. **Theorem statements rarely exceed 2 inline relations per sentence.** Counted on S1–S3, S8:
   at most 2–3 inline relations in the hypothesis sentence, 0 in the conclusion sentence (the
   conclusion is the display).

### B2. Proof structure

1. **"Proof of Theorem X" as a header; subdivision by cases or by prose signposts.** S9 §5.1/5.2
   use subsections per case; S2 uses "Case 1 / Case 2 / Case 2.1 / Case 2.2" run-in headers; S11
   uses "Case 1:/Case 2:". Numbered "Step k" is acceptable (ours already does this) but the step
   should be a paragraph, not a sentence followed by a formula wall.
2. **Every chain of ≥2 relations is a display**, usually one relation per line (`align`) or a
   single-line chain if it fits.
   - S8 p.10: `F(tα) ≥ Σ 2^{-j} F_{ν_j}(tα) = Σ 2^{-j} |sin(πtζ_{ν_j})|/ζ_{ν_j} ≥ 2t Σ 2^{-j} ≥ 2tσ_{r_k} ≥ 2tσ_t`
     — five relations, one display, then one prose sentence "The last inequality together with
     (26) gives us (20)."
   - S2 Cor 6 proof: two displayed chains (one per parity of B), each 4–5 relations, zero inline
     relations in the surrounding prose.
   - S4 §2: `N μ({x}) = lim |…| = lim |… − … + …| ≤ 2N D*_N(μ,ν_N)` as a three-line aligned display.
   - S9 p.10: system (36) as four aligned inequalities with one equation number.
3. **Key estimates are numbered and cited by number afterwards** ("by (32)", "using (25) and
   (28)", "This has at most … solutions, by Lemma 2.1"). S9 numbers (1)–(45) in 13 pages; S3
   numbers every estimate it reuses.
4. **Intermediate parameters are introduced by a displayed definition, one per line**, not by a
   run-on "Let a=…, b=…, c=…" sentence. S3 §3: `D = (log T)^{3+2ε}` on its own line; S9 defines
   `Γ_α(ε,H) := {…}` and `K_H := {…}` as separate displays.
5. **Prose carries the logic; symbols carry the quantities.** Typical S3 proof sentence: "By the
   triangle inequality, we have |B_1| ≥ 2 and [display]. This has at most 8^{j_2−1} Y^{j_2−2}
   solutions, by Lemma 2.1." One inline formula, one display, one citation.
6. **Contradiction arguments spell out the contradicted object once**: S1 Prop 8: "This is a
   contradiction, so we conclude that v − v_j ∉ R_{>0}D." Not a colon followed by "contradiction".
7. **"Idea of proof"/outline paragraphs** appear as (i) an Organisation paragraph at the end of
   the introduction (S7 p.3, S10 §1.3, S8 p.1) and (ii) a one-paragraph plan at the start of a
   long proof section (S3 §3: "The plan is to show that, generically, intervals of length
   roughly D/T have the expected number of points. To this end, we use a concentration argument
   and the union bound."). Unnumbered, italic lead-in or plain prose, 2–4 sentences, few symbols.

### B3. Definitions and notation

1. **Standing notation is a short displayed block, not a dense prose paragraph.** S9 §2 and S10
   §1.2 each spend ~1 page of short paragraphs, each introducing one object with its own display.
   S3 puts conventions in a `Remark 1.7` ("Here f ≪ g means …").
2. **Continued-fraction facts are displayed and numbered individually.** S2 p.2–3: (1) φ_k =
   q_{k−1}/q_k ; (2) q_k‖q_{k−1}θ‖ + q_{k−1}‖q_kθ‖ = 1 ; (3), (4) — four one-line numbered
   displays, each later cited by number.
3. **Definitions of named objects use a `Definition` environment or a displayed `:=`** (S6 Def
   2.5; S9 Def 1.2; S3 `disp(A) = max(a_{t+1} − a_t)` displayed with a one-line gloss).
4. A notation **table** (as ours has) is not seen in any of S1–S11; the convention is a notation
   paragraph/section with displays. Keeping the table is fine for UDT but should not replace
   in-place definitions in Sections 5–7.

### B4. Numerical evidence, tables, figures

1. **Methods paragraph before results**, in prose with named methods (S7 p.2: "Random search …
   Rational search … Lattice search …", then "Mathematica was used to verify solutions; see the
   Appendix").
2. **Tables have short captions stating what the rows are and which bound they illustrate**
   (S7 Table 1: "Examples where the bound Eq. 15 is tight for the Euclidean norm."). Columns are
   few (3–4); numbers are given to the precision that matters (S7: fractions or 4 decimals; S1
   p.4: `δ_{1,N} = √74/125 ≈ 0.0688`, exact plus 4 decimals).
3. **Long digit strings are avoided in running text**; S1 gives exact radicals with a 4-digit
   decimal, S7 gives rational α and 3-significant-figure volumes.
4. **Figures**: S1 Fig 2–3 and S7 Fig 3–4 are geometric configurations with captions that name
   every drawn object ("The vertex representing nα + Z² is labeled by n and colored in pink. The
   blue directed edges point …"). S11 Fig 2 is a one-sentence caption with the defining formula.
   S7 Fig 1: plot of bounds vs dimension, caption names the two curves and colours.
5. **"Rigorous conditional on software" is stated explicitly** (S7 p.2).

### B5. Introduction and related work

1. Introduction length: S1 ≈ 5 pp. of 34 (15%), S3 ≈ 4 of 14 (30%, but it *is* the statement of
   14 results), S7 ≈ 3 of 14, S4/S5 ≈ 1–1.5 of 8–10, S2 ≈ 1.5 of 13. Related work is woven into
   the introduction as citation clusters ("see [38–41] for the original proofs and [24, 27, 31,
   …] for alternative approaches", S1 p.1); none of S1–S10 has a separate "Related work" section.
   S11 has a one-paragraph survey inside §1.
2. Main theorems appear **in the introduction**, after one paragraph of context each (S1, S3, S7,
   S9, S10). Numbered consecutively with the section (Thm 1.1, 1.3, …) or globally (S1, S7).
3. Open questions/conjectures are stated as "Remarks" right after the theorem (S7 "Remarks: 1. …
   2. …") or in a final short section.

---

## (c) Rewrite rules (mechanical checklist for the editor agent)

Apply to every `\begin{theorem|lemma|proposition|corollary}` body and every proof paragraph.
Rules R1–R6 are hard; R7–R12 are strong defaults.

- **R1. ≤2 nontrivial inline formulas per sentence** (a "nontrivial" formula contains a relation
  symbol or more than one operator; bare symbols like `$N$`, `$\beta$` do not count). A sentence
  exceeding this is split, or its formulas go to a display.
- **R2. Any chain with ≥2 relation symbols (`= … ≤ …`, `a<b<c`) is displayed**, on one line if it
  fits, otherwise `align` with one relation per line, right-aligned at the relation.
- **R3. A statement with ≥2 conclusions, cases, or conditions is an `enumerate`** (`(i)`, `(ii)`,
  … or `(1)`, `(2)`), one conclusion per item, each item's relation displayed if it has ≥2
  relation symbols or a fraction/`\lceil`/sub-subscript.
- **R4. Multiplicity/case data (gap lengths with counts, atoms with weights, "A = … (k times)")
  is an `align*` or a `cases` or a small table**, never a comma-separated inline run.
- **R5. Every estimate that is cited later gets an equation number** (`\begin{equation}\label`),
  and later citations use `\eqref`, not a prose re-derivation.
- **R6. "Let" sentences define ≤2 symbols.** Three or more new symbols → a displayed definition
  list (`\[ a:=…,\qquad b:=…,\qquad c:=… \]` or one per line).
- **R7. Conclusion of a theorem/corollary is a display**, even if it is one short relation; the
  hypothesis sentence stays in prose with ≤2 inline formulas.
- **R8. Parenthetical derivations `(indeed …=…)` of ≥2 relations inside a statement or definition
  move to the proof or to a footnote-free display.**
- **R9. Proof of a lemma that is pure calculation is a display followed by one prose sentence**
  ("The identity follows from y_+ = y + (−y)_+ .").
- **R10. One "Idea of the proof" paragraph per theorem with a proof ≥ 1 page**, ≤4 sentences,
  ≤2 symbols per sentence, placed immediately before `\begin{proof}`; never inside the proof
  environment and never duplicated with a Roadmap sentence.
- **R11. Remarks that compare with the literature (Leong, Niederreiter) are ≤6 lines and contain
  ≤1 display**; detailed index bookkeeping goes to a displayed two-line comparison.
- **R12. Numbers in prose: ≤4 significant digits; full-precision digits only in tables, and
  table cells ≤12 digits with "…" (or state digits certified in the caption).**
- **R13. Step labels (`\emph{Step k: …}`) introduce a paragraph of ≥2 sentences; a step that is a
  single formula wall is merged with a neighbour or turned into a displayed estimate with a
  one-sentence gloss.**
- **R14. Colons introducing a chain (`so: a=b=c`) are replaced by a display; "contradiction" after a
  colon becomes a full sentence ("…, a contradiction." or "This contradicts the choice of d±.").**
- **R15. Section 2 (Related work) keeps its current prose density (it passes); do not add
  formulas there.**

Quick acceptance test for an edited file: rerun the density scan (script in session log); target
≤30% of proof sentences with ≥3 inline relations and mean ≤2.2 per file, matching S1/S8/S9.

---

## (d) Per-file audit

Line numbers refer to the current files. Severity: **H** = violates R1–R6 (hard rules), M =
violates R7–R14. The corollaries and Sections 5–7 (gaplemmas.tex, main.tex §6 golden angle,
dispersion.tex) are listed exhaustively; §1–4 and §8–9 list the main offenders only.

### main.tex

| Lines | Item | Violation | Fix |
|-------|------|-----------|-----|
| 29–48 | Abstract | one sentence with 13 inline formulas, 7 relations (items (i)–(iii) crammed into one sentence); `c_*=\pi\sin\alpha/(\sqrt5\lambda^3)` and `\kappa(\beta)\ge1+2/\sqrt5` inline | **H** R1. Split into three sentences, one per item; drop the formula for `c_*` and `\kappa` from the abstract (state "an explicit constant"). |
| 86 | after Thm A | "Equivalently, with $q=\sqrt{r^2-a^2}$, $V_N(c)=a^2+2\int_a^1 r\,m_N(…)^2dr+o(1)$" inline integral | M R7. Display it. |
| 107–117 | Theorem C | item (2) has two relations plus "In particular" in one item; `W(c)>\Vd(c)` chain inline | M R3. Split (2) into (2a) liminf = V_δ, (2b) limsup ≥ W > V_δ as a display, sentence "In particular …" after. |
| 119–122 | Corollary (unnumbered label) | fine length, but conclusion `\liminf V_N(c)>\Vd(c)` inline | M R7. Display; also give the corollary a label and `\ref` it from §5. |
| 124–131 | setup of Thm B | one sentence defines λ, β, u (3 symbols), next defines μ_x, ℓ_i, f_i, (f_0,f_1,f_2) inline | **H** R6. Display `λ=…, u=…` and `ℓ_i = u(1+x)λ^i, (f_0,f_1,f_2) = (λ−x, λ²+x, x)/(1+x)` as an aligned block. |
| 133–146 | Theorem B(3) | "with strict inequality exactly when $0<x<\lambda$ and $c<Qu(1+x)$. Consequently limsup>liminf iff [display]" — two conditions + a consequence in one item | M R3. Split into (3) inequality + strictness condition (display the condition), (4) the threshold statement. |
| 148–154 | κ paragraph | "Let γ_N be the largest circular gap, in turns, of {nβ}_{n<N} and [display]" then "The coverage threshold is πQκ(β)" | M R7. Display the threshold `c_cov(β) = πQκ(β)` and number it; it is cited in §7. |
| 156–160 | certified values in prose | four 10-digit numbers inline | M R12. Refer to Table 1 instead; keep ≤4 digits in prose. |
| 213–216 | Lemma 4.1 (Jensen) | two statements + an identity, all inline: `m_N(s)\ge(1-s/\pi)_+`; `\widetilde V_N(c)\ge\Vd(c)`; `2\pi(m_N(s)-(1-s/\pi))=\sum_j(2s/N-g_{N,j})_+` | **H** R3/R7. Enumerate (i) inequality (display), (ii) consequence, (iii) identity (display). |
| 218–221 | proof of Lemma 4.1 | chain `\sum(…)_+\ge\max(0,\sum(…))=(2\pi-2s)_+` inline | **H** R2. Display. |
| 229 | Idea of proof (Thm C) | placed *before* `\begin{proof}` (good), but 5 sentences, inline `W`, `V_δ`; fine | OK (R10). |
| 234–244 | Thm C proof Step 2 | sentence at 234–236: 7 formulas, 6 relations (`N\eta_{k-1}`, `N(\eta_{k-1}+\eta_k)` in `(1-1/a_{k+1},1+1/a_{k+1})`, `m_N\to`, `V_N\to`); sentence 236–238: frequency/length/total length three quantities with `\to` each, inline | **H** R1/R4. Display the two scaled-gap bounds; display the three limits of the second class as an aligned list (frequency → 0, scaled length → ∞, total length → 1/2). Lines 242–244 chain `(\tfrac12-\tfrac s\pi)_++\tfrac12\ge(1-\tfrac s\pi)_+` → display. |
| 246–252 | Step 3 | sentence 246–247: 12 formulas, 9 relations ("Every N has a unique form … with … and then by Theorem … the gaps are"); line 251–252: two frequency bounds + "one of them, call it E" inline | **H** R1/R4. Keep the display at 248–250 but convert to `align*` with one class per line (as gaplemmas.tex l.46–50 already does — cite that theorem instead of restating). Display the two frequency bounds. |
| 254–258 | Step 4 | 9 relations in 2 sentences: `1/(A_0+2)\le\eta_{k+1}/\eta_k\le(1+1/(A_0+1))^{-1}`; `C/A=1+B/A\ge1+\eta_{k+1}/\eta_k\ge1+\varepsilon`; `B/A\ge…\ge…`; `A/B=…\ge…\ge…` | **H** R2/R4. One displayed `cases` with three lines (E=C; E=B, r<a_{k+1}; E=B, r=a_{k+1}), each a chain. This duplicates Cor 5.5(iii); better: cite Cor 5.5(iii) and display only the conclusion "ratio ≥ 1+ε". |
| 260–266 | Step 5 | "puts mass at least ε²/4 on [0,π(1−ε²/4)]: otherwise the larger atom exceeds π(1+ε/2), forcing ∫(π−ℓ)_+ ≥ πε²/2, while this integral is at most πμ([0,π(1−τ)])+πτ with τ=ε²/4" — 5 relations, colon-chain; then `m_N(s)-(1-s/\pi)\ge\varepsilon^4/32` inline | **H** R2/R14. Display the two-sided bound on `∫(π−ℓ)_+` as an `align`, then one prose sentence. Display the final lower bound and number it (it is the conclusion of part (3)). |
| 270–274 | Lemma 6.1 (golden gaps) | hypotheses 4 inline relations; conclusion "are λ^{m−2}, λ^{m−1}, λ^m with multiplicities F_{m−1}−t, F_{m−2}+t, t" inline | **H** R4. Display as a three-line aligned list (gap & multiplicity), or a 3×2 table; identical to Cor 5.7 — consider stating once (in §5) and only citing here. |
| 280 | Idea of proof (Thm B) | inside `\begin{proof}` | M R10. Move before `\begin{proof}`. |
| 282–288 | Thm B Step 1 | sentence 283–284: atoms `πF_mλ^{m−2}(1+x_N)λ^i` with frequencies `(F_{m−1}−t, F_{m−2}+t, t)/N` inline; sentence 284–286: three limits `F_mλ^{m−2}\to…`, `F_{m−1}/F_m\to\lambda`, `F_{m−2}/F_m\to\lambda^2` inline; parenthetical 287 is a 13-formula sentence | **H** R1/R4/R8. Display atoms+weights (2-line align); display the three limits on one line; move the parenthetical (x_N may exceed λ) to a separate short paragraph or a numbered remark. |
| 290–293 | Step 2 lead-in | "atoms are ordered `uλ²(1+x)≤uλ≤uλ(1+x)≤u≤u(1+x)`" (4 relations inline); next sentence "Using πM=∫(ℓ−s)_+dμ, ∫ℓdμ=π, 1−λ=λ², 1/(1+λ)=λ" (4 identities inline) | **H** R2/R6. Display the ordering chain; display the four identities as one line `\[ …,\quad …,\quad …,\quad … \]`. The table at 294–307 is good (R4) — keep. |
| 308–310 | Step 2 conclusion | "Φ>0 on (uλ²(1+x), u(1+x)) except at s=uλ(1+x); for x∈{0,λ}, μ_x=μ_0" — 7 relations | **H** R3. Enumerate: (a) Φ ≥ 0 (convex order); (b) strict positivity set (display); (c) degenerate phases. |
| 312–316 | Step 3 | opens with a displayed-length formula inline `V(x,c)-V(0,c)=2\int…\ge0`; "exactly when (c/Q,∞) meets (uλ²(1+x),u(1+x)) … i.e. when c<Qu(1+x)"; final sentence 6 relations | **H** R2/R7. Display the difference formula and number it; display `c<Qu(1+x)` ⇔ condition; display `c\ge c_*\Rightarrow M_x(c/q)=0`. |
| 318–323 | Step 4 (noble) | "gaps η_{k−1}, η_k, η_{k−2} with counts N−q_{k−1}, t, q_{k−1}−t" inline; "From q_{k−1}/q_k→λ, η_k/η_{k−1}→λ and q_kη_{k−1}+q_{k−1}η_k=1 one gets q_kη_{k−2}→1/(√5λ²)" (4 relations) | **H** R4/R2. Cite Cor 5.8 for the gap list (do not restate), display the single limit `q_kη_{k−2} → 1/(√5λ²)`. |
| 341 | Fig. 2 caption | 5 relations in the caption ("positive exactly for c<Qu; Theorem C(3) guarantees positivity for c<πQ, and on [πQ,Qu) it follows from V(0,c)>a²=V_δ(c)") | M R1. Caption names the curves only; move the justification to the text after Step 3. |
| 345–350 | Certified constants paragraph | primitive `A^2q^2-4ABq+2B^2\log q` of `2q(A-B/q)^2`, with `A=…`, `B=…` all inline in one sentence | **H** R6. Display the integrand, its primitive, and the definitions of A, B on separate lines. |
| 352–366 | Table 1 | 20-digit cells; caption carries two more 20-digit constants | M R12. Truncate to 12 digits + "…", state "digits certified" in caption; move a² and c_* into table rows. |
| 377–388 | Table 2 (MC) | OK (4 columns, SE in parentheses). Caption fine. | OK |
| 395–401 | Deterministic integration paragraph | one sentence lists breakpoints `a\pm w`, `a`, endpoint radii, and the error `2.4\times10^{-6}` at `N\approx4000` | M R1. Split into method sentence / accuracy sentence. |
| 416–425 | numerics discussion | sentence 421–425: 10 formulas (`2ac/N`, `a^2`, `m=20`, `5.99\times10^{-5}`, `c=4`, `x=0.55`, `5.93\times10^{-5}`, `c\ge5.4`, `10^{-9}`, `N\approx10^4`) | **H** R1. Make a 3-row mini-table (c, x, measured excess, limit) or three sentences. |
| 450–454 | Lemma A.1 | `\varphi\pm\arccos(\min(1,a/r))` inline in hypothesis, "nearest orbit point on one side of θ^+ or of θ^-" | M R7. Display θ^± definition. |
| 456–466 | proof of Lemma A.1 | sentence 458–459: two distance formulas inline; 459–462: `d=\arccos(a/r)\le\alpha`, `\delta\ge\arcsin(Q/r)\ge\alpha`, derivative `2r\sin(\delta-\alpha)\ge0` inline | **H** R2/R4. Display the piecewise distance as a `cases`; display the two monotonicity facts. |

### sections/related.tex (Section 2)

Passes R1–R14 (0% dense sentences). Only note: l.23–30 dispersion paragraph has the only display
and a 4-line sentence at l.29–30 ("The threshold c_* … equal to 1+2/√5 for noble angles); …");
split at the semicolon (M, prose only). Per B5, a UDT/Monatshefte reader expects this material
in the introduction; merging §2 into §1 as citation clusters is optional, not a violation.

### sections/dephasing.tex (Sections 3–4)

| Lines | Item | Violation | Fix |
|-------|------|-----------|-----|
| 3–14 | Conventions paragraph | one paragraph defines `\mathbb T`, `\hat F(k)`, `z`, `q(r)`, `ε`, `I_ε`, `w`, `τ_ε`, `N_0` (9 symbols) with one display | **H** R6. Split into 3 short paragraphs or a displayed definition list; keep (deph:N0) numbered. |
| 28–31 | Lemma 3.1 (branches) | fine: hypothesis + one inline relation; conclusion `\varphi-\theta_j\in\pm[d_-(r),d_+(r)]\pmod{2\pi}` inline | M R7. Display the conclusion. |
| 33–41 | proof | sentence 35–36: `|r\cos\delta-a|`, `\le w` iff `\cos\delta\in[…]`, iff `|\delta|\in[d_-,d_+]` (3 relations, 2 "iff"); sentence 37–38: `r|\sin\delta|\le r\sin d_+=\sqrt{r^2-(a-w)^2}<Q` (3-relation chain inline) | **H** R2. Display the iff-chain as a 3-line `align` (`\iff`); display the sine chain. |
| 43–47 | F_{N,s} paragraph | sentence 43–44: `\int F=m_N(s)`, "nonincreasing in s", `\hat F(0)=m_N(s)` — three facts in one sentence; l.45–47 defines ζ, d_∓, d̄_N, h_N, s_N, ψ_N (6 symbols) in one sentence + one display | **H** R6. Display the three facts as an itemised list; the display at 47 is fine but put ζ on its own display line. |
| 49–55 | autocorrelation derivation | "Lemma says: z is uncovered iff F(…)F(…)=1" inline product | M R7. Display the iff. |
| 57–64 | Lemma 3.2 (reg) | items (1)–(3) displayed/inline mix; item (2) has a `\dfrac` sum inline; item (3) two relations | M R3/R7. Each item: one displayed inequality. Good use of `enumerate` otherwise. |
| 66–70 | proof lead-in | sentence 67–69: K, interval `[a/2,(a+\varepsilon/2)/(a+\varepsilon)]\subset(0,1)`, list of bounded derivatives `|\partial_r^2\zeta|, |\partial_t^2\zeta|, |\partial_r^j\partial_t^2\zeta|` (10 inline formulas) | **H** R1/R6. Display the interval inclusion; display the list of derivatives Ω_ε bounds. l.70 explicit partials → display (they are used in (1) and (2)). |
| 72–73 | proof (1) | `s_N=\frac N2(\zeta(r,-w)-\zeta(r,w))=\frac c{2w}\int…` inline 2-relation chain with an integral; then `|s_N-c/q|\le c\Omega_\varepsilon w=c^2\Omega_\varepsilon/N` inline | **H** R2. Display both chains. |
| 75–79 | proof (2),(3) | `\psi_N-\psi=\zeta(r,w)+\zeta(r,-w)-2\zeta(r,0)=w^2\int_0^1…du` inline (contains an integral and a bracket) | **H** R2. Display. |
| 86–88 | §4 opening | `\widetilde V_N=a^2+2\int_a^1…=a^2+2\int_0^Q…` inline double-integral chain; `V_N=2\int_0^1 rU_N(r)dr` inline | **H** R2/R7. Display both, number the first (it is "recalled" again at main.tex l.210 — one numbered display, cited twice). |
| 90 | Idea of the proof | inside the section but before Step 0, 5 sentences, ≤2 symbols each | OK (R10). |
| 92–104 | Step 0 layers | itemised (good, R3); but each bullet packs 2–3 relations inline (`\in[0,a^2-(a-w)^2]`, `a^2-(a-w)^2\le2aw\le2w`) | M R2. Within bullets, display or shorten: "contributes at most a²−(a−w)² ≤ 2w". |
| 106–114 | Step 1 | sentence 106–109: 9 inline formulas; `\|F(\cdot-2\alpha)-F\|_{L^1}\le2s/(\pi N)` inline before the display | **H** R1. Display the L¹ bound (it is the key estimate; number it). |
| 116–118 | Step 2 | `F^2=F`, Parseval `\sum|\hat F|^2=m_N(s)\le1`, `\mathcal C(t)=\sum|\hat F(k)|^2e^{ikt}` — 3 displayed-length identities inline in one sentence | **H** R2/R6. Display the two identities on one `align`. |
| 122 | after ibp display | `|2r/\psi_N'|\le2/a`, `|(2r/\psi_N')'|=|…|\le2/a+4\Omega/a^2` inline 2-chains | **H** R2. Display as two lines. |
| 133–134 | Step 3 | `\|F_{N,s}-F_{N,t}\|_{L^1}\le(t-s)/\pi` inline | M R5/R7. Display and number (used immediately). |
| 138–140 | partition sentence | 8 inline formulas: `I_ε=J_1∪…∪J_L`, `s_i=c/q(r_i)`, `r_i∈J_i`, `\sup|s_N-c/q|<\eta`, `N\ge N_1(\eta,\varepsilon)`, `|s_N(r)-s_i|<2\eta`, `|c/q(r)-s_i|<\eta` | **H** R1/R6. Three sentences: partition (display), approximation (display), consequence (the existing display at 141–143). |
| 150–155 | Step 4 | `\limsup_N|\mathcal E_N|\le6\eta/\pi+L\mathcal B_\varepsilon/K` inline; `\limsup_N|V_N-\widetilde V_N|\le4\varepsilon` inline | M R2/R7. Display both (they are the conclusion). |
| 157–161 | Remark (order of limits) | one sentence lists 6 parameters in order with parentheses | M R1. Write the order as a displayed arrow chain `N\to\infty,\ K\to\infty,\ \eta\to0,\ \varepsilon\to0` and one prose sentence on rates. |

### sections/gaplemmas.tex (Section 5, "Gap laws"): exhaustive

| Lines | Item | Violation | Fix |
|-------|------|-----------|-----|
| 12–17 | Lemma 5.1 | `\int\ell\,d\mu_N(\ell)=\pi` inline before the display; fine otherwise | M R7. Put both identities in one two-part display. |
| 18–21 | proof | `\int\ell d\mu_N=\frac1N\sum_j\frac N2g_{N,j}=\pi` inline chain; second chain `\pi m_N(s)=\frac12\sum…=\frac1N\sum…` inline with `\tfrac` | **H** R2/R9. Two displayed chains, one prose line. |
| 25–27 | §5.2 opening | one sentence defines `q_{-1}, q_0, q_{k+1}, p_{-1}, p_0, \delta_k, \eta_k, \eta_{-1}, \eta_0` (9 symbols, 9 relations) | **H** R6. Display recursions for q and p on one `align`, define δ_k, η_k on a second display. |
| 29–34 | facts (F1),(F2) | (F1) packs three identities in one item; (F2) has a parenthetical derivation with a 2-relation chain | **H** R3/R8. (F1a) determinant, (F1b) sign, (F1c) recursion — three numbered displays à la S2 (1)–(4); move the "Indeed …" proof of (F2) below the list as one display + one sentence. |
| 35–37 | consequences | `q_{k-1}<q_k` for `k\ge1`, `\eta_k\le\eta_0<\tfrac12` inline; convention sentence fine | M R2. Display the two inequalities on one line. |
| 39–52 | Theorem 5.2 (three distances) | decomposition display and `align*` for gaps are good (R4); but `(N-t)A+q_kB=1` as "Moreover …" inline | M R7. Add as a fourth displayed line or number it (it is cited at l.60 and used in §7). |
| 54 | Idea of the proof | before the proof (good), 3 sentences; `\mathrm d_\pm\le N-1`, `\rho q_k+q_{k-1}` inline — fine | OK |
| 57–62 | Preliminaries: uniqueness | `I_k=[q_k+q_{k-1},q_{k+1}+q_k)` inline; `N-q_{k-1}\in[q_k,(a_{k+1}+1)q_k)` inline; count identity `(N-q_k)+t+(q_k-t)=N` inline; the (F2) identity `(N-t)\eta_k+q_k(\eta_{k-1}-r\eta_k)=q_{k-1}\eta_k+q_k\eta_{k-1}=1` inline 2-chain | **H** R2. Four one-line displays. |
| 64–65 | case k=0 | `(N-1)\beta<a_1\beta<1`, `0<\beta<\dots<(N-1)\beta<1`, gaps `\beta=\eta_0` (N−1 times) and `1-(N-1)\beta=C` (once): 8 relations in one sentence | **H** R2/R4. Display the ordering; display gaps-with-counts as two aligned lines. |
| 67–69 | Step 1 setup | `\Delta_+=\{\mathrm d_+\beta\}`, `\Delta_-=1-\{\mathrm d_-\beta\}` inline | M R6. Display the two definitions. |
| 71–73 | (a) | contradiction split across `\{d\beta\}=\Delta_+-\Delta_-\in(0,\Delta_+)` and `\{d\beta\}=1-\Delta_-+\Delta_+>\{\mathrm d_-\beta\}` inline | **H** R2/R14. Display the two-case computation as a `cases`; end with "Both contradict the choice of d±." |
| 74–78 | (b) statement | "gaps are Δ_+ (N−d_+ times), Δ_- (N−d_- times), Δ_++Δ_- (d_++d_-−N times)" inline | **H** R4. Three aligned lines (mirrors Thm 5.2's `align*`). |
| 79–93 | (b) bullets | each bullet is a 3–5-relation chain inline: l.80–81 `\{(e+\mathrm d_+)\beta\}=\{e\beta\}+\Delta_+-1\in(0,\Delta_+)`; l.83–84 `\{(d+\mathrm d_-)\beta\}=\{d\beta\}+1-\Delta_-\in(\{\mathrm d_-\beta\},1)`; l.85–86 index bounds `\ge N-\mathrm d_-\ge1` and `<\mathrm d_+\le N-1`; l.86–87, 88–89 two more chains; l.90–92 a 5-line parenthetical with 3 chains | **H** R2/R8/R14. Per bullet: one prose sentence naming the case, one displayed chain, one sentence "a contradiction". Move the parenthetical (90–92) to its own short paragraph "The candidate index" with one display. This is the single densest block in the paper (13 inline chains in 15 lines). |
| 94–95 | sizes | fine (one sentence, 3 symbols). | OK |
| 98–100 | Step 2 setup | `k\ge1`, `0\le\rho\le a_{k+1}`, `\mathrm d_\rho=\rho q_k+q_{k-1}\ge1`, `\nu=\eta_{k-1}-\rho\eta_k>0` (+ parenthetical `\nu\ge\eta_{k+1}`), `\sigma=(-1)^k`, `q_k\beta\equiv\sigma\eta_k`, `\mathrm d_\rho\beta\equiv-\sigma\nu`, `q_k\nu+\mathrm d_\rho\eta_k=1` — 8 relations in 2 sentences | **H** R6/R2. Display definitions (d_ρ, ν, σ) on one line; display the three congruence/identity facts on an `align`. |
| 101–102 | Claim | `e=\sigma(d\beta-p)\in(-\nu,\eta_k)\setminus\{0\}` inline inside an italic "Claim:" | M R7. Display the claim's condition. |
| 103–107 | lattice argument | `b_1=(q_k,\sigma\eta_k)`, `b_2=(\mathrm d_\rho,-\sigma\nu)`, `\mathcal L=\{(d,d\beta-p)\}` inline; Cramer `m=d\nu+\mathrm d_\rho e`, `n=\eta_kd-q_ke` inline; two contradiction chains `d=mq_k+n\mathrm d_\rho\le N-1<q_k+\mathrm d_\rho` and `e=m\eta_k-n\nu\ge\eta_k` inline | **H** R2/R6. Display b_1, b_2; display the Cramer formulas; `cases` for the two sign cases ending in displayed contradictions. |
| 108–112 | consequence | `\{d\beta\}\notin(0,\eta_k)` and `\notin(1-\nu,1)` if σ=1 (and … if σ=−1) in one sentence; extremal sets `\{\{q_k\beta\},\{\mathrm d_\rho\beta\}\}=\{\eta_k,1-\nu\}` or `\{1-\eta_k,\nu\}`; then `\{\mathrm d_+,\mathrm d_-\}=\{q_k,\mathrm d_\rho\}`, `\{\Delta_+,\Delta_-\}=\{\eta_k,\nu\}` and a 3-gap list inline | **H** R3/R4. `cases` by σ for the excluded intervals; display the two set identities; the gap list as 3 aligned lines (or "by Step 1(b)" and cite). |
| 114–118 | Step 3 | two sentences with 11 and 12 inline formulas, 11 and 9 relations respectively (the densest sentences in the file): `\mathrm d_r=N-t\le N-1`, `N-\mathrm d_r=t`, `q_k\le N-1`, `N=\mathrm d_r+t\le\mathrm d_r+q_k`, `\nu=B`, counts; then the t=0 analogue | **H** R1/R2/R4. Two displayed verification blocks (one per case), each an `align*` listing the four hypotheses of Step 2 and the resulting counts; prose: "If t ≥ 1 take ρ = r. Then [display], so Step 2 applies and gives the counts N−q_k, t, q_k−t. If t = 0 take ρ = r−1. Then [display]." |
| 120–126 | Remark (Leong) | 7 lines, one sentence with 8 formulas and 11 relations (`q_k+q_{k-1}\le N'<q_{k+1}+q_k` becomes `q_k+q_{k-1}<N\le q_{k+1}+q_k`, `N=q_k+q_{k-1}`, `r=1,t=0`, `k\to k-1`, `r'=a_k`, `r=1`, `N=q_k`) | **H** R11. Display the two ranges as a two-line comparison; one sentence on the level drop. |
| 130–131 | ξ_k paragraph | `\xi_k=\eta_k/\eta_{k-1}`, `\xi_k=1/(a_{k+1}+\xi_{k+1})`, `\xi_k\in(0,1)` because `\eta_{k-1}\ge a_{k+1}\eta_k+\eta_{k+1}>\eta_k` — 4 relations + a 2-chain | **H** R2/R6. Display definition and recursion on one line; display the chain. |
| 133–136 | Corollary 5.3 (standard inequalities) | two statements in one sentence, second is a 2-chain `\dfrac1{a_{k+1}+2}<q_k\eta_k<\dfrac1{a_{k+1}}` with `\dfrac` inline | **H** R3/R2. Enumerate (i) identity, (ii) two-sided bound, each displayed. |
| 137–141 | proof | `1/(q_k\eta_k)=q_{k+1}/q_k+\eta_{k+1}/\eta_k` inline; chain `a_{k+1}\le q_{k+1}/q_k=a_{k+1}+q_{k-1}/q_k<a_{k+1}+1` inline (3 relations); `0<\eta_{k+1}/\eta_k<1` | **H** R2. Display the identity and the chain. |
| 143–147 | Corollary 5.4 (two-distance times) | (i) and (ii) run inline in the statement body with "(i) If …: the gaps are η_k (N−q_k times) and … (q_k times). (ii) If …: the gaps are …" — conditions and multiplicities all inline, 8 formulas | **H** R3/R4. `enumerate`; each item: hypothesis sentence, then a 2-line aligned gap/count display. |
| 148–153 | proof | `N=q_k=a_kq_{k-1}+q_{k-2}` has decomposition `(k-1,r=a_k,t=0)`; `\eta_{k-2}-(a_k-1)\eta_{k-1}=\eta_k+\eta_{k-1}` using (F1) `\eta_k=\eta_{k-2}-a_k\eta_{k-1}` — all inline | **H** R2. Display the decomposition and the identity. |
| 154–155 | post-corollary paragraph | `q_k\eta_{k-1}=1-q_{k-1}\eta_k\in(1-1/a_{k+1},1)` and `q_k(\eta_{k-1}+\eta_k)=1+(q_k-q_{k-1})\eta_k\in(1,1+1/a_{k+1})` — two 2-chains inline | **H** R2. Display as a two-line `align`, number it (used in main.tex l.235). |
| 157–163 | Corollary 5.5 (bounded type) | (i)–(iii) typed inline inside one paragraph; (i) a 2-chain with fractions; (ii) two bounds; (iii) three conditional bounds separated by semicolons — 10 formulas, 11 relations in the statement | **H** R3/R2/R4. `enumerate`; (i) displayed chain; (ii) two displayed bounds on one line; (iii) displayed `cases` (always / r<a_{k+1} / r=a_{k+1}). |
| 164–169 | proof | (i) `\xi_{k+1}=1/(a_{k+2}+\xi_{k+2})>1/(A_0+1)`, `\xi_{k+1}<1/(1+\xi_{k+2})<1/(1+1/(A_0+1))` inline; (ii) `N-q_k=(r-1)q_k+q_{k-1}+t\ge q_{k-1}\ge q_k/(A_0+1)` and `N<q_{k+1}+q_k\le(A_0+2)q_k`, then `(N-q_k)/N\ge q_{k-1}/((A_0+2)q_k)\ge\varepsilon`; (iii) four chains | **H** R2. Each sub-proof: one display with its chains, one prose sentence. |
| 170–171 | post-corollary note | fine prose; "for k=0 the frequency of class A may be 0 … finitely many N≤a_1" | OK |
| 173–176 | Corollary 5.6 (golden law) | statement: `\lambda=(\sqrt5-1)/2`, `F_1=F_2=1`, `\beta=\lambda^2=[0;2,1,1,\dots]`, then gap list "λ^{m−2}, λ^{m−1}, λ^m with multiplicities F_{m−1}−t, F_{m−2}+t, t" inline | **H** R6/R4. Display the three definitions on one line; display gaps/multiplicities as a 3-line `align*` (or 3×2 table). |
| 177–182 | proof | sentence 178–179: 11 formulas, 13 relations (`a_1=2`, `a_j=1`, `q_j=F_{j+2}`, `\eta_j=\lambda^{j+2}`, `q_0=1,q_1=2`, `\eta_0=\lambda^2`, `\eta_1=1-2\lambda^2=\lambda^3`, `\eta_{j+1}=\eta_{j-1}-\eta_j` as `\lambda^{j+3}=\lambda^{j+1}-\lambda^{j+2}`); 179–181: `q_K+q_{K-1}=F_{m-1}+F_{m-2}=F_m\le N<F_{m+1}=q_{K+1}+q_K` (5-relation chain inline), then `A=\eta_K=\lambda^{m-1}` (count), `B=…`, `C=…` inline | **H** R1/R2/R4 — worst sentence in the file by count. Display: (a) the identification `q_j=F_{j+2}, \eta_j=\lambda^{j+2}` with its 2-line verification; (b) the 5-relation chain; (c) A, B, C with counts as 3 aligned lines. |
| 183–184 | parenthetical paragraph | 2 lines of prose with `\lambda=[0;1,1,\dots]`, `x\mapsto-x`, `\{j\lambda\}\to\{j\beta\}`, `\beta\equiv-\lambda` | M R8. Make it a one-sentence Remark or drop. |
| 186–189 | Corollary 5.7 (noble law) | statement: gap list inline with counts (6 formulas); second sentence: four limits `\eta_k/\eta_{k-1}=\lambda`, `q_{k-1}/q_k\to\lambda`, `q_k\eta_{k-1}\to1/(1+\lambda^2)=1/(\sqrt5\lambda)`, `q_k\eta_{k-2}\to1/(\sqrt5\lambda^2)` inline | **H** R3/R4/R2. (i) gap/count display (3 aligned lines); (ii) the four limits as a displayed list, one per line or two per line. |
| 190–194 | proof | l.191: `K=k-1\ge k_0\ge1`, `q_k=q_K+q_{K-1}`, `N=q_K+q_{K-1}+t` with `r=1=a_{K+1}`, `0\le t<q_K`, then A,B,C with counts (12 relations in 2 sentences); l.192: `\xi_j=1/(1+\xi_{j+1})`, `f(x)=1/(1+x)`, `|f(x)-\lambda|\le\lambda|x-\lambda|`, `|\xi_j-\lambda|\le\lambda^n`; l.193: `q_k\eta_{k-1}=(1+(q_{k-1}/q_k)\xi_k)^{-1}\to1/(1+\lambda^2)`, `\eta_{k-2}=\eta_{k-1}/\lambda`, `(1+\lambda^2=\sqrt5\lambda.)` | **H** R1/R2/R6. Three displays: the decomposition; the contraction estimate; the limit computation. Drop the trailing parenthetical identity into the display. |
| 195 | closing paragraph | one 4-line sentence: `x_N=t/q_k\in[0,q_{k-1}/q_k)`, atoms `\pi N\eta_{k-2}\cdot\{1,\lambda,\lambda^2\}`, weights `(q_{k-1}-t,N-q_{k-1},t)/N`, parenthetical `\eta_{k-1}=\lambda\eta_{k-2}, \eta_k=\lambda^2\eta_{k-2}`, limit `N\eta_{k-2}=(1+x_N)q_k\eta_{k-2}\to(1+x)/(\sqrt5\lambda^2)` — 9 formulas, 7 relations | **H** R1/R4. Display atoms and weights as a 2-line align; display the limit; two prose sentences. |

### main.tex §6 (The golden angle, l.268–366) — covered above (rows 270–366).

### sections/dispersion.tex (Section 7): exhaustive

| Lines | Item | Violation | Fix |
|-------|------|-----------|-----|
| 6–8 | opening | one sentence: `\beta=\alpha/\pi\in(0,\tfrac12)`, `a=\cos\alpha`, `Q=\sin\alpha`, gaps, `\theta_j=(2j+1)\alpha` (7 relations) — repeats main.tex l.54–63 | **H** R6. Replace with "We keep the notation of Section 1" plus the one new fact (gaps are 2π times those of {jβ}). |
| 10–15 | notation displays | good (R6 satisfied) | OK |
| 16–20 | gloss paragraph | `d^{\mathbb T}_N=\gamma_N/2`, `\mathcal D_N=2\pi Nd^{\mathbb T}_N` inline; l.20 repeats Lemma 5.1 inline (`\int\ell\,d\mu_N=\pi`, `\pi m_N(s)=\int(\ell-s)_+d\mu_N`) and adds "D_N is the largest atom" | **H** R2/R5. Display `\mathcal D_N=2\pi N d^{\mathbb T}_N`; cite Lemma 5.1 by number instead of restating; display "D_N = max supp μ_N". |
| 22–28 | Lemma 7.1 | statement good (displayed two-sided bound); "In particular m_N(s)=0 iff s≥D_N" inline — fine | OK |
| 29–32 | proof | `(G_N-2s/N)_+=\tfrac2N(\mathcal D_N-s)_+` inline | M R2. Display. |
| 34 | E_N definition | `E_N(c)=2\int_0^Qq\,m_N(c/q)^2dq=\widetilde V_N(c)-a^2\ge0` inline 2-chain with integral | **H** R2/R6. Display and number (E_N is used throughout §7). |
| 36–39 | Lemma 7.2 | two "if and only if" statements each with `\limsup`, `m_N(c/Q+\delta)` inline; 7 relations | **H** R3. Enumerate (i) `E_N(c)\to0 \iff …` displayed; (ii) `\limsup E_N>0 \iff …` displayed. |
| 40–46 | proof | l.41–42: `m_N(c/q)\ge\varepsilon` for `q\in[c/(c/Q+\delta),Q]`, so `E_N(c)\ge\varepsilon^2(Q^2-(cQ/(c+\delta Q))^2)` inline; l.43–45: 11 formulas, 8 relations (`q_\delta=c/(c/Q+\delta)`, `Q^2-q_\delta^2`, `Q^2m_N(…)^2\to0`) | **H** R1/R2. Display the lower bound (number it); display `q_\delta` and the two-part bound as an `align`. |
| 48–51 | Λ definition | fine (display) | OK |
| 53–60 | Theorem 7.3 (coverage threshold) | hypothesis sentence: `\beta\in(0,\frac12)`, `c>0`, `L=L(\beta)=\pi\limsup N\gamma_N\in[\pi,\infty]` (3-relation chain inline); items (i),(ii) good; "Hence … iff c≥c_cov(β):=QL(β)=πQκ(β) (never, if κ=∞)" — 3-relation definition chain inline in the conclusion | **H** R2/R7. Display the definition of L before the theorem (it already is at l.14 — cite, don't redefine); display `c_{\rm cov}(\beta):=QL(\beta)=\pi Q\kappa(\beta)` as a numbered equation (it is the paper's headline constant and is used in main.tex l.153 and §7.5). |
| 62–63 | proof opening | `V_N(c)-a^2-E_N(c)\to0`, `E_N\ge0`, `\widetilde V_N\ge a^2`, "(ii) means limsup E_N>0" | M R1. Split into two sentences; display the first limit. |
| 65–66 | (i) | `\mathcal D_N\le L+\delta/2<c/Q+\delta` inline 2-chain + `m_N(c/Q+\delta)=0` | **H** R2. Display the chain. |
| 68–71 | (ii) | `c/Q<\Lambda`, `c/Q+\delta<\Lambda`, `m_N(c/Q+\delta)\not\to0`, `\limsup E_N>0`, `\Lambda\ge L`, `(\Lambda\le L)` — 5 relations | M R1. Two sentences; display `\Lambda\le L\le…` relation once. |
| 73–75 | blocks paragraph | "By Theorem 5.2 (with t in place of s), the blocks (k,r), 1≤r≤a_{k+1}, tile N≥q_1+q_0, and in block (k,r), N=rq_k+q_{k-1}+t, the largest gap is ℓ_{k,r}=η_{k−1}−(r−1)η_k with multiplicity q_k−t≥1" — 9 formulas, 6 relations, one sentence | **H** R1/R6. Display `\ell_{k,r}:=\eta_{k-1}-(r-1)\eta_k` (numbered; it is used in Lemma 7.4, Prop 7.5, 7.7); one prose sentence for the tiling. |
| 77–78 | ω_k, ξ_k | `\omega_k=q_{k-1}/q_k=[0;a_k,\dots,a_1]`, `\xi_k=\eta_k/\eta_{k-1}=[0;a_{k+1},\dots]`, `q_k\eta_{k-1}=1/(1+\omega_k\xi_k)`, `\xi_k<1/a_{k+1}` — 4 definitions/relations inline, and ξ_k was already defined in gaplemmas l.130 | **H** R6. One display with ω_k, ξ_k; one display for the identity; cite §5 for ξ_k. |
| 80–86 | Lemma 7.4 | statement: "N γ_N is increasing in N, so its supremum … is attained at N_{k,r}=(r+1)q_k+q_{k−1}−1" inline; formula displayed (good) | M R6. Display `N_{k,r}:=(r+1)q_k+q_{k-1}-1` (it is reused in Prop 7.5 and Remark 7.6). |
| 87–89 | proof | one line: `N_{k,r}\ell_{k,r}=((r+1)+\omega_k)q_k\ell_{k,r}-\ell_{k,r}`, `q_k\ell_{k,r}=(1-(r-1)\xi_k)q_k\eta_{k-1}`, `\ell_{k,r}\le\eta_{k-1}\to0` — three identities inline | **H** R2/R9. One 3-line `align*`, no prose needed beyond "Indeed,". |
| 91–93 | Proposition 7.5 | `\Lambda=L(\beta)` …; "that is, limsup m_N(σ)>0 for every σ<L(β)" inline | M R7. Display the equivalent form. |
| 94 | Idea of the proof | before `\begin{proof}`, 1 sentence | OK |
| 96–100 | Case 1 | one sentence with 11 formulas, 10 relations (the densest sentence in §7): `\limsup V_N(c)>a^2`, `c=Q\sigma`, `\limsup m_N(\sigma+\delta)>0`, `\limsup m_N(\sigma)>0`, `L=\infty`, `r=\lceil a_{k+1}/2\rceil`, bracket `\ge a_{k+1}/8` | **H** R1/R2. Three sentences: (1) Thm C(2)+Lemma 7.2 ⇒ display `\limsup m_N(\sigma+\delta)>0`; (2) monotonicity ⇒ claim; (3) `L=\infty`: display the bracket bound with r = ⌈a_{k+1}/2⌉. |
| 102–111 | Case 2 | l.102: `\sigma<L`, `\varepsilon\in(0,\tfrac12)`, `(1-\varepsilon)(L-\varepsilon)>\sigma`; l.103: `\mathcal \mathcal D_{N_{k,r}}=\pi N_{k,r}\ell_{k,r}\ge L-\varepsilon` (note stray double `\mathcal`); l.104–106: `j=\lceil\varepsilon q_k\rceil`, `N'=N_{k,r}-j`, `t'=q_k-1-j\ge0`, multiplicity `j+1\ge\varepsilon q_k`, `N_{k,r}\ge2q_k-1`, `j/N_{k,r}\le\varepsilon`, `\mathcal D_{N'}\ge(1-\varepsilon)\mathcal D_{N_{k,r}}`, `N'\le N_{k,r}\le(A+2)q_k`, `n_{N'}/N'\ge\varepsilon/(A+2)` — 12 relations in 3 sentences | **H** R1/R2/R6. Display `j:=…, N':=…`; display the three facts about N' as a 3-line aligned list (same largest gap; multiplicity ≥ εq_k; D_{N'} ≥ (1−ε)D_{N_{k,r}}); display the frequency bound. Fix the typo `\mathcal \mathcal`. |
| 113–118 | Remark 7.6 | 6 lines; l.114 `m_N(s)\ge(\mathcal D_N-s)_+/(\pi N)` inline; l.115 `f_0=(\lambda-x)/(1+x)` inline | M R11. Acceptable length; display the one inequality. |
| 120–127 | Proposition 7.7 (smallest threshold) | sentence 1: `\kappa(\beta)\ge1+2/\sqrt5=1.8944\ldots` with the iff; sentence 2: `\kappa(\beta)\ge2`; display good; "with equality iff β noble; for noble β this is the threshold c_* of Theorem B" | M R3. Enumerate: (i) lower bound + equality case (display), (ii) `a_{k+1}\ge2` i.o. ⇒ κ≥2 (display), (iii) consequence for c_cov (existing display). |
| 128–132 | proof | l.129–130: `r=1`, `\xi_k<\tfrac12`, `\omega_k\in(0,1)`, `(2+\omega_k)/(1+\omega_k\xi_k)>(2+\omega_k)/(1+\omega_k/2)=2`, `\kappa\ge2>1+2/\sqrt5` (8 relations); l.130–131: `a_k=1` for `k\ge k_0`, `r=1`, `\xi_k=\lambda`, `\omega_k\to\lambda`, bracket `\to(2+\lambda)/(1+\lambda^2)=(2+\lambda)/(2-\lambda)=1+2/\sqrt5` using `\lambda^2=1-\lambda` (9 relations) | **H** R2. Two displayed chains (one per case), each followed by one prose sentence. |
| 134–137 | Remark 7.8 | `\kappa=1+3\sqrt2/4\approx2.061` for `\beta=\sqrt2-1` inline — fine; "(or for fixed β as in the last display)" — fine | OK |
| 139–146 | Remark 7.9 (Niederreiter) | l.140–141: definitions `d_N=\sup\min|x-x_n|`, `\mathrm{Disp}=\limsup Nd_N` inline (already displayed in related.tex l.24 — duplicate); l.142: `(1+3/\sqrt5)/2\approx1.1708`, `\kappa/2=0.9472` inline; 8 lines total | M R11/R5. Cite the display in §2 instead of redefining; keep the two numbers; cut to ≤6 lines. |
| 148–153 | §7.5 Numerical check | prose only, "of order 10^{-5} and 10^{-9}", `0.8c_{\rm cov}`, `0.97c_{\rm cov}`, `1.03c_{\rm cov}` — no table | M B4. Per S7, give a 4–5-row table (angle, c/c_cov, N, excess) with a one-line caption, and name the angles tested ("golden, noble, silver and mixed" → list β). |

### Cross-file duplication (fix once, cite elsewhere)

- Three-gap data for golden/noble angles appear three times: gaplemmas Cor 5.6/5.7 (l.173–195),
  main.tex Lemma 6.1 (l.270–277) and Step 4 (l.318–323). Keep the displayed version in §5; the
  others become "By Corollary 5.6, …" with no restated list.
- `\widetilde V_N` formula appears at main.tex l.183 (table), l.210 and dephasing l.86; number it
  once (dephasing l.86) and `\eqref` it.
- `\xi_k` defined at gaplemmas l.130 and dispersion l.77.
- Niederreiter dispersion defined at related l.24 and dispersion l.140.
- Lemma 5.1 restated at dispersion l.20.

### Worst ten spots (by inline-relation count and reader impact)

1. gaplemmas.tex l.177–182, Cor 5.6 proof: 11 formulas/13 relations in one sentence, plus a
   5-relation chain and A/B/C-with-counts inline.
2. gaplemmas.tex l.114–118, Thm 5.2 Step 3: two sentences with 11 and 9 inline relations
   verifying four hypotheses each.
3. gaplemmas.tex l.79–93, Thm 5.2 Step 1(b) bullets: 13 inline contradiction chains, 5-line
   parenthetical.
4. gaplemmas.tex l.157–169, Cor 5.5 statement+proof: (i)–(iii) with 11 relations typed inline in
   the statement, then four more chains in the proof.
5. dispersion.tex l.96–100, Prop 7.5 Case 1: one sentence, 11 formulas, 10 relations.
6. dispersion.tex l.102–111, Prop 7.5 Case 2: 12 relations in three sentences, stray
   `\mathcal \mathcal`.
7. main.tex l.246–258, Thm C Steps 3–4: 18 relations across 4 sentences, duplicating Cor 5.5(iii).
8. main.tex l.282–288, Thm B Step 1: atoms/weights/limits inline plus a 13-formula parenthetical.
9. gaplemmas.tex l.186–195, Cor 5.7 + proof + closing paragraph: four limits inline in the
   statement, 12 relations in two proof sentences, 7 in the closing paragraph.
10. main.tex l.29–48, Abstract: 13 inline formulas and three results in one sentence; formulas
    for `c_*` and `\kappa` do not belong in a UDT/Monatshefte abstract (S1–S8 abstracts contain
    at most one displayed-style formula, S3, and otherwise prose).
