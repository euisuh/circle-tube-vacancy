"""Finite chord tubes in the unit disk. NumPy only; no proof certification."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np

TAU = 2 * math.pi
LAMBDA = (math.sqrt(5) - 1) / 2
ALPHA = math.pi * LAMBDA**2


def geometry(alpha, n):
    if not math.isfinite(alpha) or not 0 < alpha <= math.pi / 2:
        raise ValueError('alpha must lie in (0, pi/2]')
    if not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError('n must be a positive integer')
    angles = np.remainder(2 * alpha * np.arange(n + 1), TAU)
    vertices = np.column_stack((np.cos(angles), np.sin(angles)))
    normals = np.remainder((2 * np.arange(n) + 1) * alpha, TAU)
    return vertices, normals


def checked_points(points):
    points = np.asarray(points, dtype=float)
    if points.ndim != 2 or points.shape[1] != 2 or not np.isfinite(points).all():
        raise ValueError('points must be a finite (m,2) array')
    if np.any(np.linalg.norm(points, axis=1) > 1 + 1e-12):
        raise ValueError('points must lie in the unit disk')
    return points


def segment_distances(points, starts, ends):
    delta = ends - starts
    t = np.sum((points - starts) * delta, axis=-1) / np.sum(delta * delta, axis=-1)
    closest = starts + np.clip(t, 0, 1)[..., None] * delta
    return np.linalg.norm(points - closest, axis=-1)


def brute_distances(points, alpha, n):
    points = checked_points(points)
    vertices, _ = geometry(alpha, n)
    answer = np.full(len(points), np.inf)
    for j in range(n):
        answer = np.minimum(answer, segment_distances(points, vertices[j], vertices[j + 1]))
    return answer


def fast_distances(points, alpha, n):
    """Exact candidate reduction for points inside D (floating arithmetic).

    At fixed radius r, segment distance versus absolute normal-angle delta
    decreases up to acos(a/r) then increases; for r<=a it increases from 0.
    Interior-projection distance is |r cos(delta)-a|. Endpoint distance on
    remaining pieces is sqrt(r²+1-2r cos(delta-alpha)); both have these same
    monotonicities inside D. Thus a discrete minimum is adjacent to one of
    the two continuous minimizers. Four angular neighbors suffice, including
    endpoint cases. This does not assert interval-certified arithmetic.
    """
    points = checked_points(points)
    vertices, normals = geometry(alpha, n)
    order = np.argsort(normals)
    sorted_normals = normals[order]
    radius = np.linalg.norm(points, axis=1)
    theta = np.arctan2(points[:, 1], points[:, 0])
    ratio = np.divide(math.cos(alpha), radius, out=np.full_like(radius, np.inf), where=radius > 0)
    root = np.arccos(np.clip(ratio, 0, 1))
    answer = np.full(len(points), np.inf)
    for sign in (-1, 1):
        target = np.remainder(theta + sign * root, TAU)
        insertion = np.searchsorted(sorted_normals, target)
        for offset in (-1, 0):
            index = order[(insertion + offset) % n]
            answer = np.minimum(answer, segment_distances(points, vertices[index], vertices[index + 1]))
    return answer


def golden_gaps(x):
    if not math.isfinite(x) or not 0 <= x <= LAMBDA:
        raise ValueError('x must lie in [0, lambda]')
    lengths = TAU / (LAMBDA**2 * math.sqrt(5)) * (1 + x) * LAMBDA ** np.arange(3)
    frequencies = np.array([LAMBDA - x, LAMBDA**2 + x, x]) / (1 + x)
    return lengths, frequencies


def predictor(c, x):
    if not math.isfinite(c) or c < 0:
        raise ValueError('c must be finite and nonnegative')
    lengths, frequencies = golden_gaps(x)
    a, upper = math.cos(ALPHA), math.sin(ALPHA)
    cuts = sorted(set([0.0, upper] + [min(upper, 2*c/length) for length in lengths]))
    total = a*a
    for low, high in zip(cuts[:-1], cuts[1:]):
        active = lengths * ((low + high) / 2) > 2*c
        A = float(np.sum(frequencies[active] * lengths[active]) / TAU)
        B = float(2*c*np.sum(frequencies[active]) / TAU)
        if A == 0:
            continue
        def primitive(q):
            return A*A*q*q - 4*A*B*q + (2*B*B*math.log(q) if B else 0)
        total += primitive(high) - primitive(low)
    return total


def predictor_quadrature(c, x, order=128):
    """Independent Gauss-Legendre integration, split at target activation."""
    if not math.isfinite(c) or c < 0:
        raise ValueError('c must be finite and nonnegative')
    lengths, frequencies = golden_gaps(x)
    upper = math.sin(ALPHA)
    cuts = sorted(set([0.0, upper] + [min(upper, 2*c/length) for length in lengths]))
    nodes, weights = np.polynomial.legendre.leggauss(order)
    total = math.cos(ALPHA)**2
    for low, high in zip(cuts[:-1], cuts[1:]):
        q = low + (nodes + 1)*(high-low)/2
        vacancy = np.maximum(lengths[:, None] - 2*c/q, 0)
        u = frequencies @ vacancy / TAU
        total += float(np.sum(weights * 2*q*u*u)*(high-low)/2)
    return total


def gap_report(n, x):
    _, normals = geometry(ALPHA, n)
    gaps = np.diff(np.r_[np.sort(normals), np.min(normals)+TAU]) * n
    lengths, frequencies = golden_gaps(x)
    assignment = np.argmin(abs(gaps[:, None] - lengths), axis=1)
    return {'n': n, 'x': x, 'predicted_lengths': lengths.tolist(),
            'predicted_frequencies': frequencies.tolist(),
            'observed_frequencies': (np.bincount(assignment, minlength=3)/n).tolist(),
            'max_scaled_length_error': float(np.max(abs(gaps-lengths[assignment]))),
            'scaled_mean': float(np.mean(gaps))}


def experiment(samples, batch, seed, ns, cs):
    if samples < 2 or batch < 1 or len(ns) != 2 or any(n < 1 for n in ns):
        raise ValueError('samples>=2, batch>=1, exactly two positive n values required')
    if not cs or any(not math.isfinite(c) or c < 0 for c in cs):
        raise ValueError('c values must be finite and nonnegative')
    rng = np.random.default_rng(seed)
    sums = np.zeros((2, len(cs)), dtype=np.int64)
    diff_sums = np.zeros(len(cs), dtype=np.int64)
    diff_squares = np.zeros(len(cs), dtype=np.int64)
    started = time.perf_counter()
    for start in range(0, samples, batch):
        size = min(batch, samples-start)
        # Interleaved draws make sample sequence invariant under batching.
        uniform = rng.random((size, 2))
        radius = np.sqrt(uniform[:, 0])
        theta = TAU*uniform[:, 1]
        points = radius[:, None]*np.column_stack((np.cos(theta), np.sin(theta)))
        masks = []
        for i, n in enumerate(ns):
            distance = fast_distances(points, ALPHA, n)
            mask = distance[:, None] > np.asarray(cs)[None, :]/n
            sums[i] += mask.sum(axis=0)
            masks.append(mask)
        diff = masks[1].astype(np.int64)-masks[0]
        diff_sums += diff.sum(axis=0)
        diff_squares += (diff*diff).sum(axis=0)
    rows = []
    for j, c in enumerate(cs):
        means = sums[:, j]/samples
        difference = diff_sums[j]/samples
        se = math.sqrt(max(0, (diff_squares[j]-samples*difference*difference)/(samples-1)/samples))
        rows.append({'c': c, 'n0': ns[0], 'n1': ns[1],
                     'uncovered_count0': int(sums[0, j]), 'uncovered_count1': int(sums[1, j]),
                     'paired_sum': int(diff_sums[j]), 'paired_sum_squares': int(diff_squares[j]),
                     'uncovered0': float(means[0]),
                     'uncovered1': float(means[1]),
                     'se0': math.sqrt(means[0]*(1-means[0])/(samples-1)),
                     'se1': math.sqrt(means[1]*(1-means[1])/(samples-1)),
                     'paired_difference': difference, 'paired_se': se,
                     'predicted0': predictor(c, 0), 'predicted1': predictor(c, 1/3),
                     'predicted_difference': predictor(c, 1/3)-predictor(c, 0)})
    return {'samples': samples, 'batch': batch, 'seed': seed, 'alpha': ALPHA,
            'completed_at_utc': datetime.now(timezone.utc).isoformat(),
            'platform': platform.platform(), 'machine': platform.machine(),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'halfwidth': 'c/N', 'rng': 'numpy.default_rng / PCG64; interleaved radius-angle',
            'python': platform.python_version(), 'numpy': np.__version__,
            'elapsed_seconds': time.perf_counter()-started, 'rows': rows,
            'gap_checks': [gap_report(ns[0], 0), gap_report(ns[1], 1/3)],
            'prediction_scope': 'limits x=0 and x=1/3; arbitrary CLI n need not approximate these subsequences'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true', help='4 million paired points, N=4181,5574')
    parser.add_argument('--samples', type=int)
    parser.add_argument('--batch', type=int, default=100000)
    parser.add_argument('--seed', type=int, default=20261115)
    parser.add_argument('--ns', nargs=2, type=int, default=[4181, 5574])
    parser.add_argument('--cs', nargs='+', type=float, default=[1.0, 2.0])
    parser.add_argument('--output', type=Path, default=Path('results/smoke'))
    args = parser.parse_args()
    result = experiment(args.samples if args.samples is not None else (4000000 if args.full else 20000),
                        args.batch, args.seed, args.ns, args.cs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    with args.output.with_suffix('.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=result['rows'][0].keys())
        writer.writeheader()
        writer.writerows(result['rows'])
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
