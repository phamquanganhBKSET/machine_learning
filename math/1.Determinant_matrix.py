import numpy as np
from numpy import asarray

n = int(input("1. Nhập bậc của ma trận: "))
print("2. Nhập ma trận: ")
A_input = []
print("Cách nhập: Nhập từng hàng của ma trận theo dạng: 1,2,3 (không nhập dấu cách)")
for i in range(0, n):
    list = []
    while len(list) != n:
        list = input("Nhập hàng thứ " + str(i + 1) + ": ").split(",")
        list = [int(s) for s in list]
        if len(list) != n:
            print("Vui lòng nhập hàng " + str(i + 1) + " có " + str(n) + " phần tử!")
            continue 
        A_input.append(list)
A = asarray(A_input)
print("3. Kết quả: \n")
print(np.linalg.det(A))
