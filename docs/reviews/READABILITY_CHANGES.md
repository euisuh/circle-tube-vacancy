# Readability revision (no mathematical content changed)

Files edited: manuscript/main.tex, manuscript/sections/{related,dephasing,gaplemmas,dispersion}.tex.

## Added
- Notation table and Roadmap at the end of the introduction.
- "Idea of the proof" paragraphs before the proofs of Theorems A (spatial dephasing), B (uniform-gap envelope), C (golden), the three-distance theorem, and Proposition 7.x (bounded-type case).
- Proofs of the envelope theorem and the golden-angle theorem are split into numbered steps; the three-distance proof keeps Steps 1-3 plus labelled preliminaries; the Proposition on Lambda has Case 1/Case 2.
- Displays for V_delta (eq:Vd), W (eq:W), M_x and V(x,c) (eq:Vx), kappa(beta); explicit V_delta formula as a cases display.

## Symbol clashes removed
- point of the disk x -> z (x is the golden-angle phase); chord normals u_j -> n_j (u is the golden constant).
- remainder s in N = r q_k + q_{k-1} + s, and N = F_m + k -> t (s is the scaled half-width).
- gap ratio theta_k -> xi_k (theta_j is the orbit angle); q_{k-1}/q_k and eta_k/eta_{k-1} in Section 7: s_k -> omega_k, t_k -> xi_k.
- Section 7: h_N (largest gap in turns) -> gamma_N (h_N is the arc half-width in Section 3); D_N -> mathcal D_N; Niederreiter's D -> Disp.
- Section 3: g(r,t) -> zeta(r,t) (g_{N,j} are gaps); M_eps -> Omega_eps (M_x is the golden transform); C_{N,s} -> mathcal C_{N,s}; B_eps -> mathcal B_eps.
- Three-distance proof: d_pm -> roman d_pm (d_mp is the angular offset in Section 3), w -> nu in Steps 2-3 (w = c/N), successor map sigma(j) -> nxt(j).
- Golden proof: D(x,s) -> Phi(x,s).
- Remaining intentional reuse: unsubscripted q is the radial variable, q_k are denominators; a is the caustic radius, a_k partial quotients (stated in Notation).

## Style
- American spelling (centered, neighborhood, behavior, nonincreasing); limsup/liminf written with N -> infinity throughout; duplicate definitions of mu_N and kappa in Section 7 replaced by references/"Recall".
- Run-in step headings use "Step n: ..."; no bold added.

## Compile
pdflatex twice: 0 errors, 0 undefined references, 0 overfull boxes. 18 pages (was 17).
