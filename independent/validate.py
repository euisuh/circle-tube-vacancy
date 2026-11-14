import json, time, hashlib, sys
import numpy as np
import geom
from geom import *
out = {"config": {}, "arcs": [], "mc_small": [], "mc_big": [], "fast_vs_general": []}
rng = np.random.default_rng(12345)
# (a) per-segment arcs vs dense brute sampling
worst = 0.0
d = np.linspace(-pi, pi, 400001)
for al in [ALPHA, pi / 2, 2 * pi / 5, 0.7 * pi, 0.3 * pi, 3 * pi / 7, pi / 3, 0.9 * pi]:
    wmax = 0
    for _ in range(60):
        r = rng.uniform(0.02, 1.0); w = rng.uniform(0.001, 0.4)
        brute = brute_arcs_covered(r, d, al, w)
        cov = np.zeros_like(d, bool)
        for s, l in base_arcs(r, al, w):
            cov |= (((d - s) % TWO_PI) <= l)
        wmax = max(wmax, int((cov != brute).sum()))
    out["arcs"].append({"alpha": al, "max_mismatching_grid_points_of_400001": wmax})
# fast path vs general merge
for N, c in [(233, 1.0), (610, 2.0), (987, 5.0)]:
    th = ((2 * np.arange(N) + 1) * ALPHA) % TWO_PI; w = c / N; mx = 0
    for r in rng.uniform(0.3, 1.0, 300):
        geom.FAST = True; f = uncovered_fraction(r, N, ALPHA, w, th)
        geom.FAST = False; g = uncovered_fraction(r, N, ALPHA, w, th)
        mx = max(mx, abs(f - g))
    geom.FAST = True
    out["fast_vs_general"].append({"N": N, "c": c, "max_abs_diff_U": mx})
# (b) small-N V_N vs MC with brute segment distances (several alpha)
t0 = time.time()
for al, N, c in [(ALPHA, 8, 1.0), (ALPHA, 21, 1.0), (ALPHA, 34, 2.0), (pi / 2, 12, 1.0), (2 * pi / 5, 15, 1.5), (0.7 * pi, 17, 1.0)]:
    v = V_N(N, c, alpha=al, h=0.05, nodes=8)
    v2 = V_N(N, c, alpha=al, h=0.025, nodes=8)
    # MC (alpha generic): reuse mc_V with alpha
    p, se = mc_V(N, c, alpha=al, n=2_000_000, seed=7)
    out["mc_small"].append({"alpha": al, "N": N, "c": c, "V_exact": v, "V_refined": v2, "refine_diff": v2 - v, "MC": p, "MC_se": se, "z": (p - v2) / se})
# (c) big N vs saved MC
sv = json.load(open("../results/verified-full.json"))
for row in sv["rows"]:
    for key, N in (("0", row["n0"]), ("1", row["n1"])):
        c = row["c"]
        if c not in (1.0, 2.0): continue
        v1 = V_N(N, c, h=1.0); v2 = V_N(N, c, h=0.5)
        mc = row["uncovered" + key]; se = row["se" + key]
        out["mc_big"].append({"N": N, "c": c, "V_h1": v1, "V_h05": v2, "saved_MC": mc, "saved_se": se, "z": (mc - v2) / se})
        print(out["mc_big"][-1], flush=True)
out["elapsed"] = time.time() - t0
json.dump(out, open("../results/indep-validation.json", "w"), indent=1)
print(json.dumps(out, indent=1))
