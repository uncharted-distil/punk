from sklearn.decomposition import FastICA


def fastica_feature_exatraction(X):                                                 
    """ Do FastICA and return the components.             
                                                                                
                                                                                
    Params                                                                      
    -------                                                                     
    X : array-like, [n_samples, n_features]                                     
        Training data.                                                          
                                                                                
                                                                                
    Returns                                                                     
    -------                                                                     
    fastica.components_ : array-like, [n_components, n_features]                    
        Unmixing matrix.
    """                                                                         
    fastica = FastICA()                                                                 
    fastica.fit_transform(X)                                                
    return fastica.components_
