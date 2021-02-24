import numpy as np
from numpy import asarray 

print("1. Nhap vector: ")
n = int(input("1.1. Nhap so an: "))
a_input = []
b_input = []
while len(b_input) != n: 
    b_input = input("1.2. Nhap vector can bieu dien: ").split(",")
    print("Nhap theo dang: 1,2,3 (khong nhap dau cach)")
    if len(b_input) != n:
        print("Vui long nhap vector b co so phan tu bang " + str(n) + "!")
        continue
    b_input = [float(s) for s in b_input]
print("1.3. Nhap he vector: ")
for i in range(0, n):
    list = []
    while len(list) != n:
        list = input("Nhap vector thu " + str(i + 1) + ": ").split(",")
        list = [float(s) for s in list]
        if (len(list) != n):
            print("Vui long nhap cac vector co " + str(n) + " phan tu!")
            continue
        a_input.append(list)
a = asarray(a_input)
b = asarray(b_input)
print("2. Ket qua: ", np.linalg.solve(a, b))