import numpy as np
from numpy import random as rd

x = rd.random(9)
A = x.reshape(3, 3)

print("1. x = ", x)
print("2. A = ", A)

#l1 norm
l1_x = np.linalg.norm(x, ord = 1)
l1_A = np.linalg.norm(A, ord = 1)

#l2 norm
l2_x = np.linalg.norm(x)
l2_A = np.linalg.norm(A)

#l inf 
linf_x = np.linalg.norm(x, np.inf)
linf_A = np.linalg.norm(A, np.inf)

#Result
print("3. Vector x co: ")
print("l1 norm = ", l1_x)
print("l2 norm = ", l2_x)
print("l inf norm = ", linf_x)

print("4. Ma tran A co: ")
print("l1 norm = ", l1_A)
print("l2 norm = ", l2_A)
print("l inf norm = ", linf_A)