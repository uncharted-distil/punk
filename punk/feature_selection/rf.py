from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.pipeline import Pipeline                                                                
from sklearn.model_selection import GridSearchCV
from ..utils import Bunch 



def rfclassifier_feature_selection(X, y, cv=3, scoring='accuracy'):
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
    rankings : Bunch
        "indices" indicate the feature importances of features order in
        ascending order (most importance feature to least important features).

        "feature_importances" The feature importances (the higher, the more
        important the feature).
    """
    rf = Pipeline([('clf', RandomForestClassifier(random_state=1))])
    param_grid = [
        {
            'clf__n_estimators': [10, 100, 1000, 10000]
        },        
    ]

    gs_rf = GridSearchCV(rf, 
                         param_grid,
                         scoring = scoring,
                         cv      = cv,
                         verbose = 0,
                         n_jobs  = 1)
    gs_rf.fit(X, y)

    rankings = Bunch()
    # Rank from most to least important features (0, d-1) 
    importances = gs_rf.best_estimator_.named_steps["clf"].feature_importances_
    rankings["indices"] = np.argsort(importances)[::-1]
    rankings["feature_importances"] = importances

    return rankings



def rfregressor_feature_selection(X, y, cv=3):
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
                                                                                
                                                                                
    Retuns                                                                      
    ------          
    rankings : Bunch
        "indices" indicate the feature importances of features order in
        ascending order (most importance feature to least important features).

        "feature_importances" The feature importances (the higher, the more
        important the feature). 
    """                                                                         
    rf = Pipeline([('clf', RandomForestRegressor(random_state=1))])            
    param_grid = [                                                              
        {                                                                       
            'clf__n_estimators': [10, 100, 1000, 10000]
        },                                                                      
    ]                                                                           
                                                                                
    gs_rf = GridSearchCV(rf,                                                    
                         param_grid,                                            
                         cv      = cv,                                          
                         verbose = 0,                                           
                         n_jobs  = 1)                                           
    gs_rf.fit(X, y)                                                             
                                                                               
    rankings = Bunch()
    # Rank from most to least important features (0, d-1) 
    importances = gs_rf.best_estimator_.named_steps["clf"].feature_importances_
    rankings["indices"] = np.argsort(importances)[::-1]
    rankings["feature_importances"] = importances   

    return rankings 
