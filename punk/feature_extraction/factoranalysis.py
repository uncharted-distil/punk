from sklearn.decomposition import FactorAnalysis
                                   
                                                                                
def fa_feature_exatraction(X):                                             
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
    fa = FactorAnalysis()                                                         
    fa.fit_transform(X)                                                    
    return fa.components_
