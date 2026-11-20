"""Verify the three-gap formulas of manuscript/sections/gaplemmas.tex.
High precision: beta to 400 digits (CF), points as integers mod M=10^110 (exact rotation by
ib/M, within 3000/M of the true beta). Gap predictions rounded to integer units of M; tolerance 10^6 units.
Run: python3 verify_gaps.py [Nmax_special] [Nmax_random]
"""
import sys, random, bisect
from collections import Counter
from mpmath import mp, mpf, sqrt, floor, e, pi

mp.dps = 400
M = 10**110
TOL = 10**6

def cf(beta, nterms=60):
    a, x = [], beta
    for _ in range(nterms):
        a0 = int(floor(x)); a.append(a0)
        fr = x - a0
        if fr < mpf(10)**(-300): break
        x = 1/fr
    return a  # a[0]=0, a[1]=a_1,...

def data(beta, Nmax):
    a = cf(beta)
    q = {-1: 0, 0: 1}; p = {-1: 1, 0: 0}
    k = 0
    while True:
        k += 1
        q[k] = a[k]*q[k-1] + q[k-2]; p[k] = a[k]*p[k-1] + p[k-2]
        if q[k] > 4*Nmax + 10: break
    K = k
    eta = {-1: mpf(1)}
    for j in range(0, K+1):
        eta[j] = abs(q[j]*beta - p[j])
    return a, q, eta, K

def toi(x): return int(x*M)

def decompose(N, q, a, K):
    """unique (k,r,s), N = r q_k + q_{k-1} + s, 1<=r<=a_{k+1}, 0<=s<q_k"""
    found = []
    for k in range(0, K):
        for r in range(1, a[k+1]+1):
            s = N - r*q[k] - q[k-1]
            if 0 <= s < q[k]:
                found.append((k, r, s))
    assert len(found) == 1, (N, found)
    return found[0]

def predict(N, k, r, s, q, a, eta):
    A = eta[k]
    B = eta[k-1] - r*eta[k]
    C = A + B
    assert abs(B - (eta[k+1] + (a[k+1]-r)*eta[k])) < mpf(10)**(-300)
    return Counter({toi(A): N-q[k], toi(B): s, toi(C): q[k]-s}) , (A,B,C)

def check_beta(name, beta, Nmax, log):
    a, q, eta, K = data(beta, Nmax)
    ib = toi(beta)
    pts = [0]
    # identities
    for k in range(0, K):
        assert abs(q[k]*eta[k-1] + q[k-1]*eta[k] - 1) < mpf(10)**(-300)
        assert mpf(1)/(a[k+1]+2) < q[k]*eta[k] < mpf(1)/a[k+1], (name, k)
        th = eta[k]/eta[k-1] if k >= 0 else None
        if k >= 1: assert 0 < eta[k+1]/eta[k] < 1
    A0 = max(a[1:K+1])
    nbad = 0
    for N in range(2, Nmax+1):
        j = N-1
        bisect.insort(pts, (j*ib) % M)
        gaps = [pts[i+1]-pts[i] for i in range(N-1)] + [pts[0]+M-pts[-1]]
        assert sum(gaps) == M
        k, r, s = decompose(N, q, a, K)
        pred, (A, B, C) = predict(N, k, r, s, q, a, eta)
        pv = [(toi(x)) for x in (A, B, C)]
        cnt = Counter()
        for g in gaps:
            best = min(pv, key=lambda v: abs(v-g))
            assert abs(best-g) < TOL, (name, N, g, pv)
            cnt[best] += 1
        for v, c in pred.items():
            if cnt.get(v, 0) != c:
                nbad += 1; log.write(f"MISMATCH {name} N={N} (k,r,s)={(k,r,s)} class {v} got {cnt.get(v,0)} want {c}\n")
        # cross-checks of corollaries
        if s == 0:      # two-distance time N = r q_k + q_{k-1}
            assert set(cnt) <= {toi(A), toi(C)}
        # bounded-type frequency bound  (N-q_k)/N >= q_{k-1}/(q_{k+1}+q_k)
        assert q[k]+q[k-1] <= N < q[k+1]+q[k]
    # N=q_k two-distance
    for kk in range(1, K):
        N = q[kk]
        if N < 2 or N > Nmax: continue
        pts2 = sorted((j*ib) % M for j in range(N))
        gaps = [pts2[i+1]-pts2[i] for i in range(N-1)] + [pts2[0]+M-pts2[-1]]
        want = Counter({toi(eta[kk-1]): q[kk]-q[kk-1], toi(eta[kk-1]+eta[kk]): q[kk-1]})
        cnt = Counter()
        for g in gaps:
            best = min(want, key=lambda v: abs(v-g)); assert abs(best-g) < TOL; cnt[best] += 1
        if cnt != want: nbad += 1; log.write(f"N=q_k MISMATCH {name} k={kk}\n")
    # bounded-type ratio bounds
    if A0 <= 60:
        for k in range(1, K-2):
            t = eta[k+1]/eta[k]
            assert mpf(1)/(A0+1) < t < mpf(A0+1)/(A0+2), (name, k)
    log.write(f"{name}: N<= {Nmax}, partial quotients {a[1:min(K,14)+1]}..., levels used K={K}, mismatches={nbad}\n")
    return nbad

def golden(log, Nmax):
    lam = (sqrt(5)-1)/2; beta = lam**2
    F = [0, 1, 1]
    while len(F) < 40: F.append(F[-1]+F[-2])
    ib = toi(beta); pts = [0]; bad = 0
    for N in range(2, Nmax+1):
        bisect.insort(pts, ((N-1)*ib) % M)
        gaps = [pts[i+1]-pts[i] for i in range(N-1)] + [pts[0]+M-pts[-1]]
        m = max(i for i in range(3, 40) if F[i] <= N); k = N - F[m]
        assert 0 <= k < F[m-1]
        want = Counter({toi(lam**(m-2)): F[m-1]-k, toi(lam**(m-1)): F[m-2]+k, toi(lam**m): k})
        want = Counter({v: c for v, c in want.items() if c})
        cnt = Counter()
        for g in gaps:
            best = min(want, key=lambda v: abs(v-g)); assert abs(best-g) < TOL; cnt[best] += 1
        if cnt != want: bad += 1; log.write(f"golden MISMATCH N={N}\n")
    log.write(f"golden law (Lemma gap:golden), 2<=N<={Nmax}: mismatches={bad}\n")
    return bad

def noble(log, Nmax):
    lam = (sqrt(5)-1)/2
    bad = 0
    for name, beta in [("noble [0;3,2,1^inf]", 1/(3+1/(2+lam))), ("noble [0;5,1,4,1^inf]", 1/(5+1/(1+1/(4+lam)))),
                       ("noble [0;2,1^inf]=lam^2", lam**2), ("noble 1/(7+lam)", 1/(7+lam))]:
        a, q, eta, K = data(beta, Nmax); ib = toi(beta)
        # find k0 with a_j=1 for all j>=k0 (within computed range, 60 terms)
        k0 = max(i for i in range(1, len(a)) if a[i] != 1) + 1
        pts = [0]
        for N in range(2, Nmax+1):
            bisect.insort(pts, ((N-1)*ib) % M)
            for k in range(k0+1, K):
                if q[k] <= N < q[k]+q[k-1]:
                    s = N - q[k]
                    gaps = [pts[i+1]-pts[i] for i in range(N-1)] + [pts[0]+M-pts[-1]]
                    want = Counter({toi(eta[k-1]): N-q[k-1], toi(eta[k]): s, toi(eta[k-2]): q[k-1]-s})
                    want = Counter({v: c for v, c in want.items() if c})
                    cnt = Counter()
                    for g in gaps:
                        best = min(want, key=lambda v: abs(v-g)); assert abs(best-g) < TOL; cnt[best] += 1
                    if cnt != want: bad += 1; log.write(f"noble MISMATCH {name} N={N}\n")
        lamm = float(lam)
        k = K-1
        lim1 = float(q[k]*eta[k-2]); lim2 = 1/(5**.5*lamm**2)
        log.write(f"{name}: k0={k0}; eta_k/eta_(k-1) at k=K-1: {float(eta[k]/eta[k-1]):.12f} (lam={lamm:.12f}); "
                  f"q_k eta_(k-2)={lim1:.9f} vs 1/(sqrt5 lam^2)={lim2:.9f}; q_(k-1)/q_k={q[k-1]/q[k]:.9f}\n")
    log.write(f"noble law: mismatches={bad}\n")
    return bad

def mu_identity(log, rng):
    """pi m_N(s) = int (l-s)_+ d mu_N, mean pi, using float gaps for random beta."""
    import math
    worst = 0
    for t in range(20):
        beta = rng.random()*0.5
        for N in (2, 7, 50, 333):
            th = sorted((2*math.pi*(j*beta % 1)) for j in range(N))
            g = [th[i+1]-th[i] for i in range(N-1)] + [th[0]+2*math.pi-th[-1]]
            l = [N*x/2 for x in g]
            assert abs(sum(l)/N - math.pi) < 1e-9
            for s in (0.1, 0.5, 1, 2, 3, 3.14):
                mN = sum(max(x-2*s/N, 0) for x in g)/(2*math.pi)
                rhs = sum(max(x-s, 0) for x in l)/N
                worst = max(worst, abs(math.pi*mN-rhs))
    log.write(f"mu_N identity pi*m_N(s)=int (l-s)_+ dmu_N and mean pi: max abs err {worst:.2e}\n")

if __name__ == "__main__":
    Ns = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    Nr = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    log = sys.stdout
    tot = 0
    lam = (sqrt(5)-1)/2
    special = [("golden lam^2", lam**2), ("silver sqrt2-1", sqrt(2)-1), ("sqrt3-1 over 2? (sqrt3-1)/2... [0;2,1,2,1..]", (sqrt(3)-1)/2),
               ("bronze (sqrt13-3)/2", (sqrt(13)-3)/2), ("e-type 3-e", 3-e), ("pi-3 -> 1/(7.06..)", pi-3),
               ("large a: 1/(1000+pi)", 1/(1000+pi)), ("[0;2,50,3,200,1,1,7]-ish", 1/(2+1/(50+1/(3+1/(200+1/(mpf(1)+lam)))))),
               ("1/2-1e-9 + irrational", mpf(1)/2 - mpf(10)**(-7)*sqrt(2))]
    for name, b in special: tot += check_beta(name, b, Ns, log)
    rng = random.Random(20261114)
    for i in range(30):
        b = mpf(rng.random())*mpf('0.5') + mpf(10)**(-20)*sqrt(mpf(i+2))
        tot += check_beta(f"random#{i} beta={float(b):.6f}", b, Nr, log)
    # random CF with heavy-tailed partial quotients
    for i in range(10):
        aa = [max(1, int(1/rng.random()**0.8)) for _ in range(12)]; aa[0] = max(2, aa[0])
        x = lam
        for t in reversed(aa): x = 1/(t + x)
        tot += check_beta(f"randomCF#{i} {aa[:6]}", x, Nr, log)
    tot += golden(log, Ns); tot += noble(log, Ns)
    mu_identity(log, rng)
    log.write(f"TOTAL MISMATCHES: {tot}\n")
