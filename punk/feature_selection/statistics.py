import numpy as np
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.model_selection import cross_val_score
from ..utils import Bunch


def compute_scores(X):
    """ Compare PCA against FactorAnalysis.

        Code taken from 'http://scikit-learn.org/stable/auto_examples/'
        'decomposition/plot_pca_vs_fa_model_selection.html'.

    Params 
    ------  
    X : array-like
        Training data.

    Returns
    -------
    pca_scores, fa_scores : tuple of arrays
    """
    pca = PCA(svd_solver='full')
    fa = FactorAnalysis(max_iter=1000000, tol=1e-8)

    pca_scores, fa_scores = [], []
    n_components = X.shape[1]
    for n in n_components:
        pca.n_components = n
        fa.n_components = n
        pca_scores.append( np.mean(cross_val_score(pca, X)) )
        fa_scores.append( np.mean(cross_val_score(fa, X)) )

    return pca_scores, fa_scores


def test_heteroscedasticity(X):
    """ Test heteroscedaticity of your data.

    The consequence is that the likelihood of new data can be used for model
    selection and covariance estimation.

    Params
    ------
    X : array-like
        Training data.

    Returns
    -------
    results : Bunch
        "pca" returns a two tuple of number of componenets and likelihood for
        best principal componenets estimator.
        "fa" returns a two tuple of number of componenets and likelihood for
        best factor analysis estimator.

    """
    n_components = np.arange(0, n_features, 5)  # options for n_components

    pca_scores, fa_scores = compute_scores(X)                                       
    best_score_pca = np.amax(pca_scores)
    n_components_pca = np.argmax(pca_scores)  
    best_score_fa = np.amax(fa_scores)
    n_components_fa = np.argmax(fa_scores)

    results = Bunch()
    results["pca"] = (best_score_pca, n_components_pca)
    results["fa"] = (best_score_fa, n_components_fa)
    
    return results
