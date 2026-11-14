"""Independent exact-angular-measure integrator for the golden chord-tube model.
Written from the spec only (no reference to circle_research.py)."""
import numpy as np
from math import pi, sqrt, cos, sin, acos, asin

TWO_PI = 2 * pi
FAST = True
BETA = (3 - sqrt(5)) / 2
ALPHA = pi * BETA
LAM = (sqrt(5) - 1) / 2


def base_arcs(r, alpha, w):
    """Arcs (start, length) in delta (angle from segment normal) at radius r
    with dist(point, segment) <= w, for the segment with normal along delta=0.
    Segment: u=cos(alpha), |t|<=sin(alpha). Returns list of (start,len)."""
    a, Q = cos(alpha), sin(alpha)
    arcs = []
    lo, hi = (a - w) / r, (a + w) / r
    if lo <= 1 and hi >= -1:
        A1 = acos(min(hi, 1.0))
        A2 = acos(max(lo, -1.0))
        s0 = asin(min(1.0, Q / r))
        for (x, y) in ((max(A1, 0.0), min(A2, s0)), (max(A1, pi - s0), min(A2, pi))):
            if y > x:
                arcs.append((x, y - x))
                arcs.append((-y, y - x))
    kap = (r * r + 1 - w * w) / (2 * r)
    if kap <= -1:
        arcs.append((0.0, TWO_PI))
    elif kap <= 1:
        h = acos(kap)
        arcs.append((alpha - h, 2 * h))
        arcs.append((-alpha - h, 2 * h))
    return arcs


def uncovered_fraction(r, N, alpha, w, theta=None):
    if theta is None:
        theta = ((2 * np.arange(N) + 1) * alpha) % TWO_PI
    B = base_arcs(r, alpha, w)
    if not B:
        return 1.0
    if any(L >= TWO_PI for _, L in B):
        return 0.0
    if FAST and len(B) == 2 and B[0][1] == B[1][1]:
        # all arcs identical length L: union length = sum(min(L, circular gap of sorted starts))
        st = np.sort(np.concatenate([(theta + B[0][0]) % TWO_PI, (theta + B[1][0]) % TWO_PI]))
        g = np.diff(st, append=st[0] + TWO_PI)
        return max(0.0, 1.0 - np.minimum(g, B[0][1]).sum() / TWO_PI)
    st = np.concatenate([(theta + b) % TWO_PI for b, _ in B])
    ln = np.concatenate([np.full(N, L) for _, L in B])
    en = st + ln
    wr = en > TWO_PI
    st = np.concatenate([st, np.zeros(wr.sum())])
    en2 = np.concatenate([np.minimum(en, TWO_PI), en[wr] - TWO_PI])
    o = np.argsort(st, kind="stable")
    s, e = st[o], en2[o]
    M = np.maximum.accumulate(e)
    prev = np.concatenate([[0.0], M[:-1]])
    cov = np.maximum(0.0, e - np.maximum(s, prev)).sum()
    return max(0.0, 1.0 - cov / TWO_PI)


_gl = {}
def gl(n):
    if n not in _gl:
        _gl[n] = np.polynomial.legendre.leggauss(n)
    return _gl[n]


def breakpoints(alpha, w):
    a, Q = cos(alpha), sin(alpha)
    c = [a - w, a, a + w, Q, sqrt((a - w) ** 2 + Q * Q), sqrt((a + w) ** 2 + Q * Q), 1 - w, 1.0]
    lo = max(a - w, 0.0)
    pts = sorted(set([lo] + [x for x in c if lo < x <= 1.0]))
    return pts


def V_N(N, c, alpha=ALPHA, h=1.0, nodes=6, theta=None):
    """V_N = 2 * int_0^1 r U(r) dr; panel width ~ h/N (U oscillates on scale ~1/N)."""
    w = c / N
    if theta is None:
        theta = ((2 * np.arange(N) + 1) * alpha) % TWO_PI
    pts = breakpoints(alpha, w)
    x, wt = gl(nodes)
    total = pts[0] ** 2  # U=1 for r < a-w  -> 2*int_0^{a-w} r dr
    for p0, p1 in zip(pts[:-1], pts[1:]):
        L = p1 - p0
        small = L * N < 10
        k = max(int(np.ceil(L * N / h)), 8 if small else 1)
        for i in range(k):
            t0, t1 = i / k, (i + 1) / k
            t = 0.5 * (t1 - t0) * (x + 1) + t0
            if small:
                sm, dsm = t * t * (3 - 2 * t), 6 * t * (1 - t)
            else:
                sm, dsm = t, 1.0
            r = p0 + L * sm
            jac = L * dsm * 0.5 * (t1 - t0) * wt
            for ri, ji in zip(r, jac):
                total += 2 * ji * ri * uncovered_fraction(ri, N, alpha, w, theta)
    return total


# --- predictions ---
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def V_limit(x, c, alpha=ALPHA, n=4000):
    a, Q = cos(alpha), sin(alpha)
    C = LAM ** -2 / sqrt(5)
    l = [pi * C * (1 + x) * LAM ** i for i in range(3)]
    f = [(LAM - x) / (1 + x), (LAM ** 2 + x) / (1 + x), x / (1 + x)]
    def M(s):
        return sum(fi * max(li - s, 0.0) for fi, li in zip(f, l)) / pi
    xs, ws = np.polynomial.legendre.leggauss(64)
    # integrand q*M(c/q)^2 is piecewise smooth; kinks at q=c/l_i
    br = sorted(set([0.0, Q] + [c / li for li in l if 0 < c / li < Q]))
    tot = 0.0
    for q0, q1 in zip(br[:-1], br[1:]):
        q = 0.5 * (q1 - q0) * (xs + 1) + q0
        tot += 0.5 * (q1 - q0) * sum(wi * qi * M(c / qi) ** 2 for wi, qi in zip(ws, q))
    return a * a + 2 * tot


def m_tilde_V(N, c, alpha=ALPHA):
    a, Q = cos(alpha), sin(alpha)
    ang = np.sort(((2 * np.arange(N) + 1) * alpha) % TWO_PI)
    g = np.diff(np.concatenate([ang, [ang[0] + TWO_PI]]))
    def m(s):
        return np.maximum(g - 2 * s / N, 0).sum() / TWO_PI
    # kinks at q = 2c/(N g_j); piecewise quadratic in between -> exact GL with few nodes
    ks = 2 * c / (N * g)
    br = np.unique(np.concatenate([[0.0, Q], ks[ks < Q]]))
    xs, ws = np.polynomial.legendre.leggauss(4)  # integrand q*m^2 piecewise poly in 1/q: use 4 nodes on tiny pieces
    # between kinks m(c/q) = A - B/q ; q*m^2 = A^2 q - 2AB + B^2/q  -> integrate exactly
    tot = 0.0
    for q0, q1 in zip(br[:-1], br[1:]):
        if q1 <= q0:
            continue
        qm = 0.5 * (q0 + q1)
        act = g > 2 * c / (N * qm)
        A = (g[act]).sum() / TWO_PI
        B = (2 * c / N) * act.sum() / TWO_PI
        if q0 == 0:
            q0 = 1e-300
        tot += A * A * (q1 * q1 - q0 * q0) / 2 - 2 * A * B * (q1 - q0) + B * B * np.log(q1 / q0)
    return a * a + 2 * tot


def brute_arcs_covered(r, delta, alpha, w):
    """boolean: dist(r e^{i delta}, segment [normal along 0]) <= w"""
    a, Q = cos(alpha), sin(alpha)
    px, py = r * np.cos(delta), r * np.sin(delta)
    return seg_dist(px, py, a, -Q, a, Q) <= w


def seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    t = np.clip(((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy), 0, 1)
    return np.hypot(px - ax - t * dx, py - ay - t * dy)


def mc_V(N, c, alpha=ALPHA, n=2_000_000, seed=1, chunk=100_000):
    rng = np.random.default_rng(seed)
    w = c / N
    ang = 2 * np.arange(N + 1) * alpha   # N+1 vertices: path is open, not closed
    P0 = np.stack([np.cos(ang), np.sin(ang)], 1)
    P, Pn = P0[:-1], P0[1:]
    unc = 0
    for _ in range(n // chunk):
        r = np.sqrt(rng.random(chunk)); ph = rng.random(chunk) * TWO_PI
        px, py = r * np.cos(ph), r * np.sin(ph)
        m = np.ones(chunk, bool)
        d = np.full(chunk, np.inf)
        for s in range(0, N, 64):
            A, B = P[s:s + 64], Pn[s:s + 64]
            dd = seg_dist(px[:, None], py[:, None], A[:, 0], A[:, 1], B[:, 0], B[:, 1]).min(1)
            d = np.minimum(d, dd)
        unc += (d > w).sum()
    p = unc / n
    return p, sqrt(p * (1 - p) / n)
