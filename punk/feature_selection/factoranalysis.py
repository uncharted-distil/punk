from sklearn.decomposition import FactorAnalysis
from ..utils import Bunch


                                                                                
def fa_feature_selection(X, max_iter=1000000, tol=1e-8):                                             
    """ Do FactorAnalysis and return the components.             
                                                                                
                                                                                
    Params                                                                      
    -------                                                                     
    X : array-like, [n_samples, n_features]                                     
        Training data.                                                          
                                                                                
                                                                                
    Returns                                                                     
    -------                                                                     
    fastica.components_ : array-like, [n_components, n_features]                    
        Components with maximum variance.                             
    """                                                                         
    fa = FactorAnalysis(max_iter=max_iter, tol=tol)                                                         
    fa.fit_transform(X)   

    rankings = Bunch()
    rankings["components"] = fa.pca.components_
    rankings["noise_variance"] = fa.noise_variance_
    return rankings
