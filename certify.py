"""Exact and interval-certified checks for the golden-angle theorem.

1. three_gap_exact(nmax): for every 2<=N<=nmax, the gaps of {j*beta mod 1},
   beta=lambda^2, j<N, computed in exact Z[lambda] arithmetic, equal the
   three-distance law used in docs/THEOREM.md: N=F_m+k, 0<=k<F_(m-1), gaps
   lambda^(m-2), lambda^(m-1), lambda^m with counts F_(m-1)-k, F_(m-2)+k, k.
2. certified_limit(x, c): mpmath interval enclosure of
   V(x,c)=a^2+2*int_0^Q q*M_x(c/q)^2 dq (exact piecewise primitive).
Needs mpmath (already installed with sympy); no new dependency for the core code.
"""
import functools
import json
import sys
from math import isqrt

from mpmath import iv, mp

# Elements of Z[lambda] are pairs (p, q) meaning p + q*lambda, lambda^2 = 1 - lambda.


def sign(p, q):
    """Exact sign of p + q*lambda = (2p - q + q*sqrt5)/2."""
    A, B = 2 * p - q, q
    if A >= 0 and B >= 0:
        return (A > 0 or B > 0) and 1 or 0
    if A <= 0 and B <= 0:
        return -1
    s = A * A - 5 * B * B          # nonzero: sqrt5 irrational
    return (1 if s > 0 else -1) if A > 0 else (-1 if s > 0 else 1)


def frac_point(j):
    """{j*lambda^2} = {-j*lambda} = ceil(j*lambda) - j*lambda, exactly (j>=1)."""
    floor = (isqrt(5 * j * j) - j) // 2   # floor(j*lambda); j*sqrt5 irrational
    return (floor + 1, -j)


def lambda_power(n):
    p, q = 1, 0
    for _ in range(n):
        p, q = q, p - q
    return (p, q)


def three_gap_exact(nmax):
    fib = [0, 1]
    while fib[-1] <= nmax + 1:
        fib.append(fib[-1] + fib[-2])
    cmp = functools.cmp_to_key(lambda u, v: sign(u[0] - v[0], u[1] - v[1]))
    points = [(0, 0)]
    for n in range(2, nmax + 1):
        points.append(frac_point(n - 1))
        ordered = sorted(points, key=cmp)
        gaps = [(b[0] - a[0], b[1] - a[1]) for a, b in zip(ordered, ordered[1:])]
        gaps.append((ordered[0][0] + 1 - ordered[-1][0], ordered[0][1] - ordered[-1][1]))
        m = max(i for i in range(len(fib)) if fib[i] <= n)
        k = n - fib[m]
        if m >= 3 and k == fib[m - 1]:   # never happens: F_m+F_(m-1)=F_(m+1)
            raise AssertionError
        want = {}
        for power, count in ((m - 2, fib[m - 1] - k), (m - 1, fib[m - 2] + k), (m, k)):
            if count:
                want[lambda_power(power)] = want.get(lambda_power(power), 0) + count
        got = {}
        for g in gaps:
            got[g] = got.get(g, 0) + 1
        if got != want:
            raise AssertionError(f'N={n}: got {got}, want {want}')
    return nmax


def constants():
    lam = (iv.sqrt(5) - 1) / 2
    alpha = iv.pi * lam**2
    C = 1 / (lam**2 * iv.sqrt(5))
    return lam, iv.cos(alpha), iv.sin(alpha), iv.pi * C


def certified_limit(x, c):
    """Interval enclosure of V(x,c); x, c given as exact strings/ints."""
    lam, a, Q, u = constants()
    x, c = iv.mpf(x), iv.mpf(c)
    ell = [u * (1 + x) * lam**i for i in range(3)]
    f = [(lam - x) / (1 + x), (lam**2 + x) / (1 + x), x / (1 + x)]
    # active class i on q in (c/ell_i, Q]; breakpoints must be decidable.
    cuts = []
    for e in ell:
        t = c / e
        if t.b < Q.a:
            cuts.append(t)
        elif t.a <= Q.b:
            raise ValueError('breakpoint too close to Q to decide')
    pts = sorted(cuts, key=lambda t: t.a)
    for lo, hi in zip(pts, pts[1:]):
        if not lo.b < hi.a:
            raise ValueError('breakpoints not separated')
    total = a * a
    bounds = pts + [Q]
    for k in range(len(pts)):
        lo, hi = bounds[k], bounds[k + 1]
        # class i is active on (lo, hi) iff its breakpoint c/ell_i is <= lo
        active = [i for i in range(3) if (c / ell[i]).a <= lo.a]
        A = sum((f[i] * ell[i] for i in active), iv.mpf(0)) / iv.pi
        B = c * sum((f[i] for i in active), iv.mpf(0)) / iv.pi
        def P(q):
            return A * A * q * q - 4 * A * B * q + 2 * B * B * iv.log(q)
        total += P(hi) - P(lo)
    return total


def main():
    mp.dps = iv.dps = 50
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    three_gap_exact(nmax)
    lam, a, Q, u = constants()
    cstar = Q * u / lam
    out = {'three_gap_exact_checked_up_to_N': nmax, 'dps': iv.dps,
           'a2': str(a * a), 'c_star': str(cstar), 'limits': []}
    for c in ('1', '2'):
        v0, v1 = certified_limit('0', c), certified_limit('1/3', c)
        d = v1 - v0
        out['limits'].append({'c': c, 'V(0,c)': str(v0), 'V(1/3,c)': str(v1),
                              'difference': str(d), 'difference_positive': bool(d.a > 0)})
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
