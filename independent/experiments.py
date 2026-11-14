import json, csv, time, hashlib, sys, platform
import numpy as np
from multiprocessing import Pool
from geom import *

H = 1.0
def fibs(m): return fib(m)

def task(t):
    kind, m, k, c = t
    F = fib(m); N = F + k; x = k / F
    t0 = time.time()
    v = V_N(N, c, h=H)
    return dict(kind=kind, m=m, F=F, k=k, N=N, x=x, c=c, V_N=v, Vtilde=m_tilde_V(N, c),
                V_lim=V_limit(x, c), a2=cos(ALPHA) ** 2, sec=time.time() - t0)

def main():
    tasks = []
    for m in range(12, 22):
        F = fib(m)
        for x in (0.0, 1 / 3):
            for c in (0.5, 1.0, 2.0, 3.0):
                tasks.append(("conv", m, int(np.floor(x * F)), c))
    for m in (20, 21):
        F = fib(m)
        n = 17 if m == 20 else 15
        for i in range(n):
            k = int(round(i / (n - 1) * LAM * F))
            for c in (1.0, 2.0):
                tasks.append(("sweep", m, k, c))
    F = fib(20)
    for c in (4.0, 5.0, 5.4, 6.0, 7.0):
        for x in (0.0, 0.55, 0.6):
            tasks.append(("thresh", 20, int(round(x * F)), c))
    tasks.sort(key=lambda t: -(fib(t[1]) + t[2]))
    t0 = time.time()
    rows = []
    with Pool(10) as p:
        for i, r in enumerate(p.imap_unordered(task, tasks)):
            rows.append(r)
            print(i + 1, len(tasks), r["kind"], r["N"], r["c"], round(r["sec"], 1), flush=True)
    rows.sort(key=lambda r: (r["kind"], r["m"], r["c"], r["k"]))
    sha = hashlib.sha256(open("geom.py", "rb").read() + open("experiments.py", "rb").read()).hexdigest()
    cfg = dict(h=H, nodes=6, alpha=ALPHA, workers=10, code_sha256_geom_plus_experiments=sha,
               total_seconds=time.time() - t0, python=platform.python_version(), numpy=np.__version__)
    json.dump(dict(config=cfg, rows=rows), open("../results/indep-experiments.json", "w"), indent=1)
    with open("../results/indep-experiments.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("done", cfg["total_seconds"])

if __name__ == "__main__":
    main()
