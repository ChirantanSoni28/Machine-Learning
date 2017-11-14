import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from featurescaling import feature_scaling
from GradientDescent import gradientdescent


 # Load Data
data = pd.read_csv("/Users/chirantansoni/Downloads/machine-learning-ex1 2/ex1/ex1data2.txt", names=["Area","# of BR","Price($)"])
X = data.as_matrix(columns=["Area","# of BR"])
y = data.as_matrix(columns=["Price($)"])
m,n = np.shape(X)


# scaling the feature to set mean to zero

X_norm, mu, sigma = feature_scaling(X)


# Adding one's column

X_padded = np.column_stack((np.ones((m,1)),X_norm))

#Applying gradient descent

# Select aplha and number of iterations

alpha = 0.1
num_iters = 400

theta = np.zeros((X_padded.shape[1],1))

theta, J_history = gradientdescent(X_padded, y, theta, alpha, num_iters)

# plot J convergence

plt.plot(np.arange(num_iters), J_history)
plt.xlabel('Number of iterations')
plt.ylabel('Cost J')
plt.xlim([0, 50])
plt.show()

#prediction

price = 0

X_pre = np.array([1,1650,3])

scaled = (X_pre - np.insert(mu,0,0)) / np.insert(sigma,0,1)
price = np.dot(scaled,theta)

print("The predicted price for the house is ${}".format(int(price)))







