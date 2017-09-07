import unittest

import numpy as np
from scipy import linalg

from punk.novelty_detection import HeteroscedasticityTest


class TestHetero(unittest.TestCase):                                                
    def setUp(self):    
        n_samples, n_features, rank = 1000, 50, 10
        sigma = 1.0
        rng = np.random.RandomState(42)
        U, _, _ = linalg.svd(rng.randn(n_features, n_features))
        X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

        sigmas = sigma * rng.rand(n_features) + sigma / 2.
        self.X_hetero = X + rng.randn(n_samples, n_features) * sigmas
                                                                               
    def test_hetero(self):
        hetero = HeteroscedasticityTest(max_iter=1000, tol=0.01)
        hetero = hetero.fit("matrix", self.X_hetero)

        self.assertTrue( hetero.fa[0] > -80 and hetero.fa[0] < -70 )
        self.assertTrue( hetero.fa[1] == 10 )
        self.assertTrue( hetero.pca[0] > -80 and hetero.pca[0] < -70)
        self.assertTrue( hetero.pca[1] >= 40 )
        self.assertTrue( np.all(np.isfinite(hetero.pca_scores)) )
        self.assertTrue( np.all(np.isfinite(hetero.fa_scores)) )
