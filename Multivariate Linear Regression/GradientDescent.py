import numpy as np
import pandas as pd
from costfunction import computecost


def gradientdescent(X, y , theta, alpha, num_iters):

    m = len(y)
    J_history = np.zeros((num_iters,1))

    for i in range(0,num_iters):



        h = np.dot(X,theta)
        diff = (h - y)
        term = diff * X

        theta = theta.T - alpha * (1/m) * sum(term)
        theta = theta.T

        J_history[i] = computecost(X,y,theta)

    return theta, J_history



