import numpy as np

A = np.random.random(9).reshape(3, 3)
print("1. Ma tran A: ")
print("A = ", A)
print("2. Duong cheo cua A: ")
print("diag(A) = ", np.diag(A, k = 0))
print("3. Trace cua A: ")
print("trace(A) = ", np.sum(np.diag(A, k = 0)))
