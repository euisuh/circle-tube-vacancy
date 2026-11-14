"""Numerical checks against independent geometry and integration references."""
import math
import unittest

import numpy as np

import circle_research as cr


class Distances(unittest.TestCase):
    def test_fast_against_brute_random_and_adversarial(self):
        rng = np.random.default_rng(8675309)
        for alpha in [math.pi/2, math.pi/3, 3*math.pi/8, cr.ALPHA, 0.003, 1.4]:
            for n in [1, 2, 7, 31, 127]:
                vertices, normals = cr.geometry(alpha, n)
                random = rng.normal(size=(500, 2))
                random /= np.linalg.norm(random, axis=1)[:, None]
                random *= np.sqrt(rng.random((500, 1)))
                angles = np.r_[normals, normals+alpha, normals-alpha, 0, math.pi]
                radii = [0, math.cos(alpha), max(0, math.cos(alpha)-1e-10),
                         min(1, math.cos(alpha)+1e-10), 1-1e-12, 1]
                special = np.concatenate([r*np.column_stack((np.cos(angles), np.sin(angles))) for r in radii])
                midpoints = (vertices[:-1]+vertices[1:])/2
                points = np.vstack([random, special, vertices, midpoints])
                with self.subTest(alpha=alpha, n=n):
                    np.testing.assert_allclose(cr.fast_distances(points, alpha, n),
                                               cr.brute_distances(points, alpha, n), atol=2e-12, rtol=1e-10)

    def test_diameter_analytic(self):
        points = np.array([[0, 0], [0.4, 0.2], [-0.7, 0.3], [0, 1]])
        np.testing.assert_allclose(cr.fast_distances(points, math.pi/2, 1), abs(points[:, 1]), atol=1e-15)

    def test_center_and_chord(self):
        for n in [1, 23, 4181]:
            self.assertAlmostEqual(cr.fast_distances([[0, 0]], cr.ALPHA, n)[0], math.cos(cr.ALPHA), places=12)
        v, _ = cr.geometry(cr.ALPHA, 5)
        np.testing.assert_allclose(cr.fast_distances((v[:-1]+v[1:])/2, cr.ALPHA, 5), 0, atol=1e-15)

    def test_validation(self):
        for alpha, n in [(0, 1), (2, 1), (float('nan'), 1), (1, 0), (1, 1.2)]:
            with self.assertRaises(ValueError):
                cr.geometry(alpha, n)
        for points in [[[2, 0]], [[float('nan'), 0]], [0, 1]]:
            with self.assertRaises(ValueError):
                cr.fast_distances(points, 1, 1)


class Predictions(unittest.TestCase):
    def test_primitive_against_independent_quadrature(self):
        for x in [0, 0.1, 1/3, cr.LAMBDA]:
            for c in [0, 0.01, 0.4, 1, 2, 10]:
                with self.subTest(x=x, c=c):
                    self.assertAlmostEqual(cr.predictor(c, x), cr.predictor_quadrature(c, x), places=11)
        self.assertAlmostEqual(cr.predictor(0, 1/3), 1, places=13)
        self.assertAlmostEqual(cr.predictor(10, 0), math.cos(cr.ALPHA)**2, places=13)

    def test_gap_constants_against_real_rotations(self):
        for n, x in [(4181, 0), (5574, 1/3), (75025, 0), (100033, 1/3)]:
            report = cr.gap_report(n, x)
            self.assertLess(report['max_scaled_length_error'], 0.002)
            np.testing.assert_allclose(report['observed_frequencies'], report['predicted_frequencies'], atol=0.0003)
            self.assertAlmostEqual(report['scaled_mean'], cr.TAU, places=11)

    def test_exact_finite_fibonacci_gap_counts(self):
        fibonacci = [0, 1]
        for _ in range(22):
            fibonacci.append(sum(fibonacci[-2:]))
        for m in [4, 5, 8, 13, 18, 22]:
            for k in [0, fibonacci[m-1]//3, fibonacci[m-1]]:
                n = fibonacci[m]+k
                _, normals = cr.geometry(cr.ALPHA, n)
                angles = np.sort(normals)
                actual = np.sort(np.diff(np.r_[angles, angles[0]+cr.TAU]))
                counts = [fibonacci[m-1]-k, fibonacci[m-2]+k, k]
                lengths = cr.TAU*cr.LAMBDA**(m-2+np.arange(3))
                expected = np.sort(np.repeat(lengths, counts))
                with self.subTest(m=m, k=k, n=n):
                    self.assertEqual(sum(counts), n)
                    np.testing.assert_allclose(actual, expected, atol=2e-10, rtol=0)

    def test_batching_reproducibility_and_uncertainty(self):
        first = cr.experiment(1000, 137, 42, [13, 17], [1, 2])
        second = cr.experiment(1000, 1000, 42, [13, 17], [1, 2])
        self.assertEqual(first['rows'], second['rows'])
        for row in first['rows']:
            self.assertGreaterEqual(row['paired_se'], 0)
            self.assertAlmostEqual(row['paired_difference'], row['uncovered1']-row['uncovered0'])

    def test_monte_carlo_statistics_against_brute_samples(self):
        count, seed, ns, cs = 231, 123, [7, 11], [0.4, 1.2]
        uniform = np.random.default_rng(seed).random((count, 2))
        theta = cr.TAU*uniform[:, 1]
        points = np.sqrt(uniform[:, 0])[:, None]*np.column_stack((np.cos(theta), np.sin(theta)))
        masks = [cr.brute_distances(points, cr.ALPHA, n)[:, None] > np.array(cs)/n for n in ns]
        rows = cr.experiment(count, 17, seed, ns, cs)['rows']
        for j, row in enumerate(rows):
            difference = masks[1][:, j].astype(float)-masks[0][:, j]
            self.assertEqual(row['uncovered0'], float(masks[0][:, j].mean()))
            self.assertEqual(row['uncovered1'], float(masks[1][:, j].mean()))
            self.assertAlmostEqual(row['paired_se'], float(difference.std(ddof=1)/math.sqrt(count)), places=15)
            self.assertEqual(row['paired_sum'], int(difference.sum()))
            self.assertEqual(row['paired_sum_squares'], int((difference*difference).sum()))
            self.assertEqual(row['uncovered_count0'], int(masks[0][:, j].sum()))
            self.assertEqual(row['uncovered_count1'], int(masks[1][:, j].sum()))

    def test_prediction_validation(self):
        for c, x in [(-1, 0), (1, -0.1), (float('inf'), 0), (1, 1)]:
            with self.assertRaises(ValueError):
                cr.predictor(c, x)
        with self.assertRaises(ValueError):
            cr.experiment(1, 1, 1, [1, 2], [1])
        with self.assertRaises(ValueError):
            cr.experiment(100, 10, 1, [1, 2], [])


if __name__ == '__main__':
    unittest.main()
