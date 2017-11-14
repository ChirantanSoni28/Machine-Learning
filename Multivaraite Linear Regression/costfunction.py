import numpy as np

def computecost(X,y,theta):
    m = len(y)
    J = 0
    prediction = np.dot(X,theta)
    sqrerror = np.power((prediction - y),2)
    J = 1/(2*m) * np.sum(sqrerror)

    return J