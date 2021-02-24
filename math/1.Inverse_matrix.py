import numpy as np

def Have_inverse(arr):
    if len(arr) != len(arr[0]):
        return 0
    elif len(arr) == len(arr[0]) and np.linalg.det(arr) == 0:
        return 0
    else:
        return 1

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix arr: \n", arr)
if Have_inverse(arr) == 0:
    print("Matrix arr don\'t have inverse matrix (sigular or degenerate)!")
else:
    print("Inverse matrix of matrix arr: \n", np.linalg.inv(arr))