import matplotlib.pyplot as plt
import numpy as np

#np.random.seed(1234)
#print(np.random.randn(4))

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).transpose()
y = np.array([[5, 6, 7, 8, 9, 10]])
one = np.ones((X.shape[0], 1))
test = np.concatenate((one, X), axis = 1)
print(X)
print(test)