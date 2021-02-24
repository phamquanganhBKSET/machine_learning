import numpy as np

arrA = np.array([[1, 2], [3, 4]])
arrB = np.array([[5, 6], [7, 8]])

#1. Dot 
arr_dot = arrA.dot(arrB)

#2. Hadamard 
arr_har = arrA * arrB

print("1. Matrix A: \n", arrA)
print("2. Matrix B: \n", arrB)
print("3. Dot matrix: \n", arr_dot)
print("4. Hadamard matrix: \n", arr_har)