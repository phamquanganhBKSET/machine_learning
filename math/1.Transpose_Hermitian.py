import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1 + 2J, 3 - 4J], [0 + 1J, 2]])

#1. Transpose matrix of arr1
arr_trans = arr1.transpose()

#2. Hermitian matrix of arr2 
arr_her = arr2.transpose().conjugate()

print("1. Original Matrix 1: \n", arr1)
print("2. Original Matrix 2: \n", arr2)
print("3. Transpose Matrix of Matrix 1: \n", arr_trans)
print("4. Hermitian Matrix of Matrix 2: \n", arr_her)