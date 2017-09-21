import numpy as np
from sklearn.decomposition import PCA
from typing import NamedTuple, List
# from ..base import DataCleaningPrimitiveBase
from primitive_interfaces.base import PrimitiveBase

Input = np.ndarray
Output = List[int]
Params = NamedTuple('Params', ())
CallMetadata = NamedTuple('CallMetadata', ())

class PCAFeatures(PrimitiveBase[Input, Output, Params]):

    def __init__(self) -> None:
        pass

    def fit(self) -> None:
        pass

    def set_training_data(self, inputs: Input) -> None:
        pass

    def get_params(self) -> Params:
        return self.Params()

    def set_params(self, params: Params) -> None:
        pass

    def get_call_metadata(self) -> CallMetadata:
        return self.CallMetadata()

    def produce(self, inputs: Input) -> Output:
        """ Perform PCA and return a list of the indices of the most important
        features, ordered by contribution to first PCA component
                                                                                
        The matrix M will correspond to the absolute value of the components of 
        the decomposiiton thus giving a matrix where each column corresponds to 
        a principal component and rows are the components that rescale each 
        feature.  
                                                                                
        For example, pca.components_.T could look like this:                        
                                                                                
        array([[ 0.52237162,  0.37231836, -0.72101681, -0.26199559],                
            [-0.26335492,  0.92555649,  0.24203288,  0.12413481],                 
            [ 0.58125401,  0.02109478,  0.14089226,  0.80115427],                 
            [ 0.56561105,  0.06541577,  0.6338014 , -0.52354627]])                
                                                                                
        So the most important feature with respect to the first principal 
        component would be the 3rd feature as this has an absolute value of 
        0.58125401 which is greater than all the entries in that column.                             
                                                                                
                                                                                
        "importance_on1stpc" corresponds to the indices of most important       
        features for the first principal. Component are in ascending order      
        (most important feature 0, least important feature n_features-1).       
                                                                                
        
        Params 
        ------- 
        data : np.ndarray, [n_samples, n_features]
            Training data.
        """

        pca = PCA()

        try:
            pca.fit_transform(inputs)

            M = np.absolute(pca.components_.T)

            # Rank features based on contribtuions to 1st PC
            self.importance_on1stpc = np.argsort(M[:,0], axis=0)[::-1]
        except:
            # If any error occurs, just return indices in original order
            # In the future we should consider a better error handling strategy
            self.importance_on1stpc = [i for i in range(inputs.shape[0])]

        return self.importance_on1stpc