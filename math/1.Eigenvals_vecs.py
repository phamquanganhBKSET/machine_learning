import numpy as np 

A = np.array([[1, 2, 3], 
			[2, 3, 4], 
			[4, 5, 6]]) 

print("Printing the Original square array:\n", A) 

w, v = np.linalg.eig(A) 

print("Printing the Eigen values of the given square array:\n", w) 

print("Printing Right eigenvectors of the given square array:\n", v) 
