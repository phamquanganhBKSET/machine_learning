import numpy as np
from numpy import asarray
from fractions import Fraction as Fr

#Giải hệ phương trình A.x = B

#Hàm nhập
def Input(n, arrA, arrB):
    print("1. Nhập ma trận A: ")
    print("Cách nhập: Nhập từng hàng của ma trận theo dạng: 1,2,3 (không nhập dấu cách)")
    for i in range(1, n + 1):
        string = input("Nhập hàng thứ " + str(i) + " của ma trận: ").split(",")
        row = [int(s) for s in string]
        arrA.append(row)
    B_input = input("Nhập vector B: ").split(",")
    B_int = [int(s) for s in B_input]
    for i in B_int:
        arrB.append(i)

#Kiểm tra điều kiện giải hệ phương trình
def Check(n, arrA, arrB):
    if n != len(arrA) or n != len(arrA[0]):
        return False
    if np.linalg.det(arrA) == 0:
        return False
    return True

#Hàm giải hệ phương trình
def Calculate(n, arrA, arrB, Result):
    for i in range(0, n):
        A_copy = arrA.copy() #Nếu không sử dụng ma trận copy sẽ dẫn đến thay đổi ma trận arrA khiến cho các phép toán sau bị sai
        temp = A_copy.transpose() 
        for j in range(0, n):
            temp[i, j] = arrB[j]
        Ai = temp.transpose()
        Result.append(np.linalg.det(Ai) / np.linalg.det(arrA))
    return Result

# Nhập phương trình 
input_array = []
B = []
Result = []
n = int(input("Nhập số nghiệm: "))
Input(n, input_array, B)

#Ma trận hệ A
A = asarray(input_array)
print("2. Ma trận A: \nA = ", A)

#Ma trận B
print("3. ma trận B: \nB = ", B)

#Kết quả 
if Check(n, A, B) == False:
    print("Hệ phương trình không thể giải bằng phương pháp Cramer")
else:
    print("Nghiệm của hệ phương trình: ", Calculate(n, A, B, Result))