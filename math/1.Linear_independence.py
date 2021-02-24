import numpy as np
from numpy import asarray

#Kiểm tra sự độc lập tuyến tính của một hệ vector gầm các vector(ma trận) có rows hàng, columns cột

#Zeros matrix by list 
def Zeros(rows, columns):
    arr = [[0 for col in range(1, columns + 1)] for row in range(1, rows + 1)]
    return asarray(arr)

#Product a matrix with a float number 
def Product(arr, n):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            arr[i][j] *= n
    return arr 

def Check_ratio(arrA, arrB, rows, columns):
    ratio = arrA[0][0] / arrB[0][0]
    temp = arrB.copy()
    if (arrA == Product(temp, ratio)).all() == True:
        return True
    return False

def Check_independence(space, rows, columns):
    for i in range(0, len(space) - 1):
        for j in range(i + 1, len(space)):
            if Check_ratio(space[i], space[j], rows, columns) == True:
                return False 
    return True

n = int(input("1. Nhập số lượng vector có trong hệ: "))
rows = int(input("2. Nhập số  hàng: "))
columns = int(input("3. Nhập số cột: "))

print("4. Nhập hệ vector: ")
print("Cách nhập: Nhập từng hàng của ma trận theo dạng: 1,2,3 (không nhập dấu cách)")
space = []
for i in range(1, n + 1):
    print("4." + str(i) + ". Nhập vector thứ " + str(i))
    arr = []
    for i in range(1, rows + 1):
        list = []
        while len(list) != columns:
            list = input("\tNhập hàng thứ " + str(i) + ": ").split(",")
            list = [int(s) for s in list]
            if (len(list) != columns):
                print("\tVui lòng nhập hàng có " + str(columns) + " phần tử !")
                continue
        arr.append(list)
    space.append(asarray(arr))

print("5. Kết quả: ")
if Check_independence(space, rows, columns) == True:
    print("Hệ độc lập tuyến tính!")
else:
    print("Hệ phụ thuộc tuyến tính!")