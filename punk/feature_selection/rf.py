from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline                                                                
from sklearn.model_selection import GridSearchCV



def rf_feature_selection(X, y, cv=3, scoring='accuracy'):
    """ Rank features using Random Forest classifier.

    Use GridSearchCV to optimize the scoring method for a random forest
    classifier and return the importance of the features.

    Params
    ------  
    X : array-like, [n_samples, n_features]
        Training data. 
    y : array, [n_samples]    
        Labels. 
    cv : int, optional
        Cross-validation splitting strategy.
    scoring : string, callable, list/tuple, dict or None, (default: 'accuracy')
        Scorer function.


    Retuns
    ------  
    indices : array, [n_features]
        Features indices related to feature importance order in decreasing order
        (most importance feature to least important features).
    """
    rf = Pipeline([('clf', RandomForestClassifier(random_state=1))])
    params_estimators = [10, 100, 1000, 10000]
    param_grid = [
        {
            'clf__n_estimators' : params_estimators
        },        
    ]

    gs_rf = GridSearchCV(rf, 
                         param_grid,
                         scoring = scoring,
                         cv      = cv,
                         verbose = 0,
                         n_jobs  = 1)
    gs_rf.fit(X, y)
    importances = gs_rf.best_estimator_.named_steps["clf"].feature_importances_

    # Rank from most to least important features (0, d-1)
    indices = np.argsort(importances)[::-1]

    return indices

