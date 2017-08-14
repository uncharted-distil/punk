import unittest

import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 

from punk.feature_selection.pca import pca_feature_selection
from punk.feature_selection.pca import rf_feature_selection


class TestPCA(unittest.TestCase):                                                
                                                                                
    def setUp(self):    
        iris = datasets.load_iris() 
        sc = StandardScaler()
        self.X = sc.fit_transform(iris.data)
                                                                                
    def test_pca(self):
        r1, r2 = pca_feature_selection(self.X)      

        self.assertTrue( np.array_equal(r1, np.array([2, 3, 0, 1])) )
        self.assertTrue( np.array_equal(r2, np.array([2, 1, 0, 2])) )


class TestRF(unittest.TestCase):

    def setUp(self):
        df_wine = pd.read_csv('https://archive.ics.uci.edu/'
                              'ml/machine-learning-databases/wine/wine.data',
                              header=None)
        X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
        self.X, _, self.y, _ = train_test_split(X, y, test_size=0.3, random_state=0)

    def test_pca(self):
        r = rf_feature_selection(self.X, self.y)

        wine_importances = array([9, 12, 6, 11, 0, 10, 5, 3, 1, 4, 8, 2, 7])
        self.assertTrue( np.array_equal(r, wine_importances) )


