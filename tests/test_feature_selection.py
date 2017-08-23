import unittest

import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 

from punk.feature_selection.pca import pca_feature_selection
from punk.feature_selection.rf import (rfclassifier_feature_selection,
                                       rfregressor_feature_selection)


class TestPCA(unittest.TestCase):                                                
    def setUp(self):    
        iris = datasets.load_iris() 
        sc = StandardScaler()
        self.X = sc.fit_transform(iris.data)
                                                                                
    def test_pca(self):
        rankings = pca_feature_selection(self.X)      

        self.assertTrue( np.all(np.isfinite( rankings.components )) )
        self.assertTrue( np.all(np.isfinite( rankings.explained_variance_ratio )) )
        self.assertTrue( np.array_equal(rankings.importance_on1stpc, np.array([2, 3, 0, 1])) )
        self.assertTrue( np.array_equal(rankings.importance_onallpcs, np.array([2, 1, 0, 2])) )


class TestRFC(unittest.TestCase):
    def setUp(self):
        df_wine = pd.read_csv('https://raw.githubusercontent.com/rasbt/'
                              'python-machine-learning-book/master/code/datasets/wine/wine.data', 
                              header=None)    
        X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
        self.X, _, self.y, _ = train_test_split(X, y, test_size=0.3, random_state=0)


    def test_rfc(self):
        rfc = rfclassifier_feature_selection(self.X, self.y)
                           
        self.assertTrue( np.all(np.isfinite( rfc.feature_importances )) )
        importances = np.array([9, 12, 6, 11, 0, 10, 5, 3, 1, 8, 4, 7, 2])
        self.assertTrue( np.array_equal(rfc.indices, importances) )


class TestRFR(unittest.TestCase):
    def setUp(self):
        boston = datasets.load_boston()
        self.X, self.y = boston.data, boston.target

    def test_rfr(self):
        rfr = rfregressor_feature_selection(self.X, self.y)

        self.assertTrue( np.all(np.isfinite( rfr.feature_importances )) )
        importances = np.array([5, 12, 7, 0, 4, 10, 9, 6, 11, 2, 8, 1, 3])
        self.assertTrue( np.array_equal(rfr.indices, importances) )


