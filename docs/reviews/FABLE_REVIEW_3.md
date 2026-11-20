# Third-round referee report and submission advice: "Shrinking tubes around a circular billiard orbit" (revision of 15 Nov 2026)

Reviewer: Claude Fable 5.1, 2026-11-20. Sources: `manuscript/main.tex` (496 lines), `manuscript/sections/{related,dephasing,gaplemmas,dispersion}.tex`, the compiled `manuscript/main.pdf` (18 pages, built 2026-11-15 00:09 KST, same minute as the last source edit; read via `pdftotext`), `docs/reviews/FABLE_REVIEW_2.md`, `docs/reviews/READABILITY_CHANGES.md`, `docs/reviews/LIT_ROUND3.md`, and the live GitHub remote (`gh repo view`, `gh api .../contents`, `.../readme`, `.../releases`). Web checks on journals, AI policies and arXiv endorsement were done today; where I could not verify a figure on the journal's own page I say so.

Labels: **classical**, **audited argument**, **gap**, **hypothesis**, as before. No proof was rerun numerically; Sections 5–7 and the statements of Theorems A–C were re-read against my round-2 derivations.

---

## 1. Status of round-2 items

### Must (round 2)

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | Rename κ in proof of Theorem B(3) | **resolved** | `main.tex` l.264 now uses γ |
| 2 | Delete "whose completeness we prove in the repository"; prove or cite the four-candidate reduction | **resolved** | Lemma A.1 with proof, `main.tex` ll.445–461; Section 8 cites it |
| 3 | Make repository public with a `main` branch, or Zenodo DOI | **partially** | `visibility: PUBLIC` confirmed. But the only branch is `codex/research-continuity` (also the default branch); no `main`, no tag/release (`releases` → 0), no `LICENSE` (`license: null`). Fix: see Must 3 below. |
| 4 | Remove `docs/...` scratch paths and "checked by computer" sentences | **resolved** | `dispersion.tex` §7.1 is now a plain numerical check; Remark 5.4 is the Leong comparison only |
| 5 | Lemma 7.4 → reference to Theorem 5.3; delete "indexing shifted" clause | **resolved** | `dispersion.tex` ll.68–70 is a two-line reference |
| 6 | Remove "We did not read"/"bounded search"; fix "recomputed numerically" | **resolved** | `related.tex` ll.29–30, 45–48; `dispersion.tex` l.139 now "We do not claim that [Nie84] states … we know of no source for the circular statement" (acceptable, plain) |
| 7 | Figure 3 caption: `c<Qu` | **resolved** | `main.tex` l.340 |
| 8 | Remove "Draft of" | **resolved** | `\date{14 November 2026}` |

### Should (round 2)

| # | Item | Status |
|---|---|---|
| 9 | Define Λ before Theorem 7.3; monotonicity sentence in Prop. 7.5 unbounded case; restate Lemma 7.4 (now 7.4 "Exact limsup") as a statement | **not resolved** on all three counts (`dispersion.tex` l.63 defines Λ inside a proof; l.91 still skips the one-sentence step; l.76 still begins "Since … is attained at …, and") |
| 10 | Delete Lemma 6.1 (= Cor. 5.8), duplicate μ_N definition, Remark 7.6 last sentence; move proof of Theorem 5.3 to appendix | **partially**: duplicate μ_N definition replaced by "Recall" (good). Lemma 6.1 still present (`main.tex` ll.269–276, with a redundant "we also verified it … for every 2≤N≤3000"). Remark 7.6 still ends "No counterexample to the equivalence exists" (`dispersion.tex` l.111). Three-distance proof still in the body (pp. 9–11). |
| 11 | Tripathi bibitem; DOIs; Ramírez journal version; e-mail | **partially**: e-mail added. Tripathi still cited inline without a bibitem (`dispersion.tex` l.136). No DOIs. Ram14 and Leong17 still arXiv-only. DK24 lacks volume/pages although LIT_ROUND3 has them (vol. 68, no. 2, 61–68). BI09 lacks pages. |
| 12 | Number/caption Section 8 tables; points per seed | **not resolved** (`main.tex` ll.376–385, 399–410 are bare `center`) |
| 13 | Update Section 9; motivation paragraph | Section 9 **resolved** (now consistent with Theorem 7.3). Motivation paragraph **not done**; the paper still opens with definitions. |

### Regressions introduced by the readability pass (new, must fix)

The pass renamed `s→t` and `w→ν` by search-and-replace and missed or over-hit a few places:

- `gaplemmas.tex` l.105: "Cramer't rule" (visible in the PDF, p. 10); l.123: "previous level't range" (PDF p. 11). Over-hit `'s→'t`.
- `gaplemmas.tex` ll.100, 105–107: Step 2 still uses `w` for `η_{k-1}−ρη_k` (`q_kw+d_ρη_k=1`, `m=dw+…`, `mη_k−nw`) although l.99 defines it as `ν` and the Notation table fixes `w=c/N`. Replace the four `w` by `ν`.
- `gaplemmas.tex` l.104: the lattice is called `Λ`; Section 7 uses `Λ=inf{σ: m_N(σ)→0}`. Rename the lattice (`\mathcal L`).
- `dispersion.tex` ll.96, 98: `D_{N_{k,r}}`, `D_{N'}` (plain `D`) vs `\mathcal D_N` everywhere else.
- `main.tex` l.69 "outer annulus `a<|x|<1`" and `dephasing.tex` l.95 "from `x`": the point was renamed `z`.
- `dispersion.tex` l.91: "Case 1: unbounded partial quotients.} by Theorem…" — lowercase after the heading.
- `gaplemmas.tex` l.106: `nd_\rho` missing `\mathrm`.

---

## 2. Correctness (update)

Audited argument, holds. Nothing in Sections 5–7 changed mathematically since round 2 (the diff is renaming and "Idea of the proof" paragraphs); I re-read every renamed display and found no sign or index change. The one remaining logical gap is unchanged and trivial: Prop. 7.5 Case 1 needs "given σ, take c=Qσ; Lemma 7.2 gives δ with limsup m_N(σ+δ)>0, and m_N is nonincreasing, so limsup m_N(σ)>0." Theorem C(1) ("limit set is an interval") is justified: V_N−V(x_N,c)→0, x↦V(x,c) continuous on the compact interval [0,λ], grids dense. Abstract, Theorems A–C and Theorem 7.3 are mutually consistent (c_* = πQ(1+2/√5) checked again).

---

## 3. Remaining improvements, ranked

### MUST (before submission; no new mathematics; about two hours)

1. Fix the readability-pass regressions listed above (`gaplemmas.tex` ll.100–107, 123; `dispersion.tex` ll.91, 96, 98; `main.tex` l.69; `dephasing.tex` l.95). A referee who hits "Cramer't rule" on p. 10 will assume nobody proofread the paper.
2. `dispersion.tex`: define Λ before Theorem 7.3 (move l.63's definition to the preamble after l.20); add the monotonicity sentence in Case 1 (l.91); turn l.76 into a statement ("Within each block (k,r), Nγ_N is increasing in N, so its supremum is attained at N_{k,r}=…, and κ(β)=…"); delete the last sentence of Remark 7.6 (l.111).
3. Repository: create `main` from the current head and make it the default branch; add a `LICENSE` (MIT for code; CC BY 4.0 for text/data, or a single MIT if simpler); tag `v1.0-submitted` and mint a Zenodo DOI from the tag; cite the DOI in "Code and data availability" next to the URL. Without a license the public code is legally all-rights-reserved and a reader may not run it.
4. Bibliography: add `A. Tripathi, A comparison of dispersion and Markov constants, Acta Arith. 63 (1993), 193–203` and cite it as `\cite{Tri93}` in Remark 7.9; complete DK24 (`68 (2024), no. 2, 61–68`); add pages for BI09; replace Ram14 by its journal version if it exists (round 2 said Acta Arith. 170 (2015); verify on MathSciNet/zbMATH before changing).
5. `main.tex` ll.376–385, 399–410: wrap both numerics tables in `table` with captions and labels; state the number of points per seed for the 20-seed run (l.387).
6. Add `\hypersetup{pdftitle={…},pdfauthor={Euisuh Jeong}}`; the PDF currently has empty Title/Author metadata (`pdfinfo`). Replace `\date{14 November 2026}` by `\date{\today}` or the submission date.

### SHOULD (improves odds; half a day)

7. Delete Lemma 6.1 and its "verified for N≤3000" sentence (`main.tex` ll.269–276); cite Corollary 5.8 directly in Step 1 of the proof of Theorem C. The exact-arithmetic check belongs in Appendix A only.
8. Move the proof of Theorem 5.3 (`gaplemmas.tex` ll.54–118) to an appendix, keeping the statement, the "Idea of the proof" and Remark 5.4 in the body. Saves two body pages; the paper reads as 13–14 pages of new material plus appendices, which is what it is.
9. One motivation paragraph at the top of Section 1 (three to five sentences): why a tube of width 1/N (the natural scale at which the covered fraction is nontrivial), why the planar observable differs from circle covering, what the headline is (the exact threshold πQκ(β), minimal at noble angles). Editors decide desk-reject on page 1.
10. `related.tex` l.21: "The planar vacancy area of Theorem~\ref{thm:C}" renders as Theorem B; Theorem A is what reduces the observable. Check intent.
11. Section 8: the Monte Carlo paragraph should say in one sentence that the MC and the deterministic integrator are independent checks of the same finite-N quantity, and that agreement with the *limits* is a separate statement (currently the table header says "limit difference" without saying what is being compared with what).
12. README: "reviewed … by AI referees" → "internally reviewed with AI assistance (reports in `docs/reviews/`)". A human referee who follows the link will read `FABLE_REVIEW.md` ("major revision") and `FABLE_REVIEW_2.md`; that is fine and honest, but the word "referees" invites misreading. Also move `AGENTS.md`, `HANDOFF-codex-1.md`, `CLAUDE_GOAL.md` (currently untracked, keep it that way) out of the root or into `docs/process/`.

### NICE

13. Extend to α∈(π/2,π) in one sentence: replacing α by π−α reflects the orbit (2j(π−α)≡−2jα), so Γ_N and V_N are unchanged; the standing assumption β<1/2 is a normalization, not a restriction. Put it after the definition of V_N.
14. Mark Qu on Figure 3; add the silver angle to the Section 8 numerics (κ=1+3√2/4 from Remark 7.8) as one row, so Section 7 has a non-noble numerical instance in the paper itself.
15. Replace `\paragraph` heads by `\subsection*` (amsart renders them as unemphasized run-in text).

### Mathematical strengthening: worth doing vs not

**Worth a remark, not a theorem, before submission.** A rate in Theorem A for badly approximable β. Step 1 gives |F̂_{N,s}(k)| ≤ 2s/(πN|e^{2πikβ}−1|) ≤ C_β s|k|/N; with the Parseval tail bound B_ε/K and K≈N^{1/2} the frozen-s error is O(N^{−1/2}) at fixed ε, and ε can then be sent to zero at a polynomial rate because Ω_ε grows polynomially in 1/ε (arccos derivatives near the caustic). The result is V_N−Ṽ_N=O(N^{−θ}) for some explicit θ>0 under bounded type. The numerics show the true error is O(1/N) and geometric (the caustic deficit −2ac/N), so a sharp rate is out of reach here; a two-sentence remark after Remark 4.1 saying that a polynomial rate holds for badly approximable β, with the sketch above, pre-empts the standard "no rate" referee complaint. Only include it if the author can verify the sketch; otherwise leave "No rate is claimed" as is. **Hypothesis** until written out.

**Worth stating as a question, not attempting.** Divergence of V_N(c) for every bounded-type non-noble β and every c<c_cov(β) (Section 9 already poses this). The silver angle β=√2−1 is the natural test case: blocks (k,r), r∈{1,2}, give a two-parameter family of three-atom laws, so the limit set is a union of two intervals and the liminf need not sit at a convergent denominator. This is a follow-up paper, not a revision.

**Not worth it.** A rate for unbounded type (depends on the approximation exponent; no clean statement). An optical/beam model. Replacing the self-contained three-distance proof by a citation chain (the N-point convention with t=0 allowed is genuinely awkward to extract from [Leong17]; Remark 5.4 already explains this; appendix placement is the right compromise). Trying to obtain Coelho (2004): it is cited only as context for "tightness characterizes bounded type", which matches the abstract; nothing in the paper depends on it.

---

## 4. Recommendation: submit?

**Yes.** The mathematics has survived three rounds and an independent dispersion review; every proof in Sections 3–7 has been re-derived at least twice; the numerics are reproducible from a public repository. The contribution is modest in depth but clean, correct and, as far as three literature passes could establish, new in its circular form (Theorem 7.3 and Proposition 7.7). It is a solid paper for a specialist journal in uniform distribution / Diophantine approximation, not for a general top-tier journal.

**When.** After Must 1–6 (two hours) and the author's own line-by-line reading of the PDF, which he has committed to. Should 7–9 are worth the extra half day because they lower the desk-reject risk at the first-choice venue; do them if the author has the time, but do not let them delay submission by weeks. Do not wait for Coelho access or for any further mathematical extension.

---

## 5. Venue plan

Ranked by fit × realistic odds for a single non-academic AI-assisted author. Odds are my estimate, **hypothesis**, conditional on the Must items being done.

| Rank | Venue | Fit | Odds | AI policy | APC | Review time | Notes |
|---|---|---|---|---|---|---|---|
| 1 | **Uniform Distribution Theory** (Math. Inst. Slovak Acad. Sci.; Sciendo/De Gruyter platform) | Best. Scope is 11K/11J (distribution of {nα}, dispersion, continued fractions); Theorem 7.3/Prop. 7.7 are squarely in it. | 40–55% | No journal-specific generative-AI statement found; Sciendo/De Gruyter general policy: no AI authorship, disclose use. The existing Acknowledgements paragraph suffices. | Journal homepage states OA with no author charge; CC BY-NC-ND. Confirm on the current Sciendo/reference-global page at submission (I could not fetch it: redirect). | Semiannual; small editorial board; expect 4–9 months to decision (unverified). | Check the "Instructions for authors" on the journal page for the submission channel (likely e-mail to the editor). |
| 2 | **Monatshefte für Mathematik** (Springer / ÖMG) | Good; Ji–Lu's dispersion paper appeared there. Broad scope, dynamics + number theory. | 25–35% | Springer Nature: no AI authorship; declare generative-AI use in the Acknowledgements (tool, extent). Current paragraph fits; add the model versions used. | Hybrid; subscription route free. | Springer reports median 12 days to first decision (includes desk rejects); crowd-sourced 1–3 months to decision for refereed papers. | Fast; good second choice. |
| 3 | **Experimental Mathematics** (Taylor & Francis) | Good for the paper's shape: theorems inspired by, and checked against, certified computation; the Fibonacci-phase family was found numerically first. | 25–35% | T&F requires a standalone "Declaration of generative AI use" (tool name, version, how used, why) in Methods or Acknowledgements. T&F forbids generative AI for creating figures or original research data; here figures are produced by deterministic Python scripts and the AI role was coding/review assistance, which T&F lists as permitted. State this explicitly. | Hybrid; no APC required. | Aggregators report ~16% acceptance; decision typically 3–6 months (unverified). | Single-anonymized review. |
| 4 | **Journal de Théorie des Nombres de Bordeaux** (Centre Mersenne) | Moderate; number theory with a Diophantine-approximation section. | 20–30% | Follows EMS/COPE code; no specific AI statement found; keep the disclosure. | Diamond OA; no fees; CC BY-ND. | Slow: ~18 months submission to publication. | Author chooses a section editor at submission. |
| 5 | **Journal of Number Theory** (Elsevier) | Moderate (Don 2012 precedent). | 15–25% | Elsevier requires a titled section "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process" with the sentence "During the preparation of this work the author used [tool] to [reason]." | Hybrid; subscription route free. | Often 6–12 months. | |
| 6 | **Acta Arithmetica** (IMPAN) | Borderline; dispersion precedent (Tripathi 1993) but depth is below their median. | 10–15% | Explicit: substantial AI use must be disclosed in the manuscript and in the EditFlow form; papers that appear substantially AI-generated without adequate human contribution may be rejected on editorial grounds. | None. | 6–12 months. | Long shot; only after 1–3 fail. |

Lower fallbacks if all of the above reject: *Integers* (free electronic, number theory), *Moscow J. Combinatorics and Number Theory*, *Indagationes Mathematicae*. Not recommended: Nonlinearity, J. Stat. Phys. (observable is not physical enough), Ergodic Theory Dynam. Systems (too high).

**Fallback chain:** UDT → Monatshefte → Experimental Mathematics → JTNB → JNT → Acta Arith. → Integers. Resubmit within a week of each rejection; incorporate any referee report; do not submit to two journals at once.

### arXiv

**Post before journal submission**, as `math.DS` primary with `math.NT` cross-list (`math.MG` not needed). Reasons: editors and referees will look for it; it timestamps priority for Theorem 7.3; UDT and JTNB explicitly allow preprints.

**Endorsement is required and is the real obstacle.** Since December 2025 (math) and January 2026 (arXiv-wide), a new submitter is auto-endorsed only with *both* an institutional academic e-mail *and* prior authorship on an arXiv paper in the domain. The author has neither (personal domain e-mail, no arXiv record), so he must obtain a personal endorsement from an established arXiv author in math.DS or math.NT; arXiv staff cannot waive this. Practical route for the author himself (the project constraint "no contacting authors" binds the agents, not the human): start the submission to get the endorsement code; then e-mail one or two active arXiv authors whose work the paper engages with (the "Which of these authors are endorsers?" link on their arXiv abstract pages shows who qualifies), attaching the PDF and the repository link, with a two-paragraph message. Expect some non-replies; allow two weeks. math.DS and math.NT are separate endorsement domains; one endorsement in the primary category is enough to submit with a cross-list request, but the cross-list may be moderated. If no endorsement arrives in a month, submit to the journal anyway and post to Zenodo (the DOI from Must 3 already serves as the public preprint); revisit arXiv after acceptance, when the journal reference itself helps.

arXiv's AI policy: significant use of text-to-text generative AI must be reported in the paper (the existing Acknowledgements paragraph does this); AI cannot be an author; authors are fully responsible. A May 2026 one-year-ban policy targets unchecked AI content (hallucinated references, nonsense); the paper's bibliography is verified (LIT_ROUND3), which is exactly the check that policy is about. Reports of that ban are secondary sources; confirm on info.arxiv.org before posting.

---

## 6. Risks for this author and how to handle them

1. **AI-assisted single-author paper from outside academia.** Both flags are now screened for by editors. Mitigation is already mostly in place: the disclosure paragraph, the public repository with tests and certified computations, self-contained proofs. Add in the cover letter (not in the paper): one sentence that the author personally verified every proof line by line, and that the AI role was drafting, literature search and independent re-derivation, with all statements the author's responsibility. Name the tools and versions once, in the paper's Acknowledgements, as Springer/T&F/Elsevier formats require.
2. **Affiliation "Republic of Korea Air Force".** Two issues. (a) Editorial: an employer rather than a research institution; an editor may query it. Use the cover letter to say the work is independent and unfunded. (b) Employer rules: many armed forces require clearance for external publication, even of unrelated mathematics. **Check the applicable service regulation before submitting or posting**; this is a user-side blocker I cannot assess. If clearance is slow, "Seoul, Republic of Korea" plus e-mail is an acceptable affiliation line in mathematics (independent researchers publish this way) and avoids the question entirely.
3. **Public AI referee reports.** `docs/reviews/FABLE_REVIEW*.md` are visible to anyone following the repository link. This is a transparency asset but also exposes the "major revision" history. Keep them; fix the README wording (Should 12); do not scrub.
4. **Length vs depth.** Eighteen pages with a 2.5-page classical proof reads heavier than the content. Should 7–8 fix this; if not done, a referee's first comment will be "shorten".
5. **"Folklore" objection to Prop. 7.7.** A specialist may say the circular minimality at noble angles is known. Remark 7.9 handles this honestly. In the cover letter, state the three concrete new things in one sentence each: (i) exact planar-to-circle reduction with the square appearing only after radial integration (Theorem A); (ii) iff coverage threshold πQκ(β) for every irrational angle (Theorem 7.3); (iii) golden/noble limit set as an interval with the liminf at Fibonacci times by convex order (Theorem C). Do not claim more.
6. **Referee suggestions.** Most systems ask for suggested referees. Reasonable, non-conflicted names are the authors of the cited three-distance/dispersion/hitting-time papers; suggest 3–4 and exclude none. Do not contact them in advance.

### Cover letter skeleton (≤ 250 words)

- Title; main results in three sentences (as in Risk 5).
- Fit to the journal in one sentence (for UDT: distribution of {nα}, circular dispersion, three-distance theorem).
- Independence: single author, no institutional affiliation for this work, unfunded.
- AI disclosure: tools and roles, one sentence; author checked every proof and takes responsibility.
- Reproducibility: public repository and Zenodo DOI; all numerics reproducible with NumPy/mpmath.
- Not under consideration elsewhere; arXiv number if available.
- Suggested referees (3–4).

---

## 7. Verdict

**Accept for submission after the Must list.** No mathematical change is required. The blocking items are the search-and-replace regressions ("Cramer't rule", stray `w`/`Λ`/`D`/`x`), the Section 7 presentation fixes already requested in round 2, the Tripathi/DK24 bibliography entries, numbered tables, PDF metadata, and the repository hygiene (`main` branch, LICENSE, tag + Zenodo DOI). First venue: Uniform Distribution Theory; post to arXiv (math.DS, cross-list math.NT) first if an endorsement can be obtained within a month, otherwise rely on the Zenodo DOI and submit.

### Sources consulted (web)
- [UDT homepage (no author charge statement)](http://pcwww.liv.ac.uk/~karpenk/JournalUDT/welcome-Dateien/welcome.htm); [Sciendo UDT page](https://sciendo.com/journal/UDT) (redirects to reference-global.com); [Jisc Open Policy Finder, UDT](https://openpolicyfinder.jisc.ac.uk/id/publication/43518?template=romeo)
- [arXiv math endorsement policy, Dec 2025](https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/); [arXiv-wide update, Jan 2026](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/); [arXiv endorsement help](https://info.arxiv.org/help/endorsement-math.html); [arXiv content moderation / AI policy](https://info.arxiv.org/help/moderation/index.html); [CASRAI on the 2026 one-year ban (secondary)](https://casrai.org/news/arxiv-one-year-ban-unchecked-ai-content)
- [Springer Nature AI guidance](https://group.springernature.com/gp/group/ai/ai-guidance-for-our-researchers-and-communities); [Monatshefte journal page (first-decision metric)](https://link.springer.com/journal/605); [LetPub Monatshefte reviews](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=5995)
- [Taylor & Francis AI policy](https://taylorandfrancis.com/our-policies/ai-policy/); [T&F authorship / AI declaration](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/); [Experimental Mathematics aims](https://www.tandfonline.com/journals/uexm20/about-this-journal)
- [JNT guide for authors](https://www.sciencedirect.com/journal/journal-of-number-theory/publish/guide-for-authors)
- [JTNB submissions](https://jtnb.math.u-bordeaux.fr/jtnbsubmit_english.html); [JTNB about](https://jtnb.math.u-bordeaux.fr/aboutjtnb_english.html)
- [Acta Arithmetica information for authors](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/information-for-authors); [Acta Arith. EditFlow submission](https://ef.msp.org/submit_new.php?j=impan_ActaArith)
