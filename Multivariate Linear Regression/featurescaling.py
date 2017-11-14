
import numpy as np

def feature_scaling(features):

    m, n = np.shape(features)
    X_norm = np.zeros(np.shape(features))
    mu = np.zeros((1,n))
    sigma = np.zeros((1,n))

    for index in range(0,n):

       mu = np.mean(features,axis=0)
       sigma = np.std(features, axis=0,ddof=1)

       X_norm[:,index] = (features[:,index] - mu[index]) / sigma[index]

    return X_norm, mu, sigma



