from sklearn.decomposition import PCA


def pca_feature_exatraction(X):
    """ Do PCA and return the components, explained variance ratio.


    Params
    -------
    X : array-like, [n_samples, n_features]
        Training data.


    Returns
    -------
    pca.components_ : array-like, [n_components, n_features]
        Principal axes in feature space, representing the directions of
        maximum variance in the data. The components are sorted by
        ``explained_variance_``.

    pca.explained_variance_ratio_ : array-like, [n_components]
        The amount of variance explained by each of the selected components.
    """
    pca = PCA()
    pca.fit_transform(X)
    return pca.components_, pca.explained_variance_ratio_
