import numpy as np
from matplotlib import pyplot as plt

#Lagrange interpolation
def Denominator(x):
    MS = np.ones_like(x)
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if (j != i):
                MS[i] *= (x[i] - x[j])
    return MS

def Lagrange_function(xi, x, y):
    MS = Denominator(x)
    TS = np.ones_like(x)
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if (j != i):
                TS[i] *= (xi - x[j])
    result = 0
    for i in range(0, len(x)):
        result += y[i] * (TS[i] / MS[i])
    return result

#Newton interpolation
#Divided differences(f[x[i+1],...,x[i+n]] - f[x[i],...,x[i+n-1]]) / (x[i+n] - x[i])
def Div_diff(x, y):
    i = len(x)
    if i == 2:
        return (y[i - 1] - y[i - 2]) / (x[i - 1] - x[i - 2])
    else: #use recurse algorithm 
        return (Div_diff(x[1:len(x)], y[1:len(x)]) - Div_diff(x[:len(x) - 1], y[:len(x) - 1])) / (x[len(x) - 1] - x[0])

def Newton_function(xi, x, y):
    result = y[0]
    poly = xi - x[0]
    for i in range(1, len(x)):
        result += Div_diff(x[:(i + 1)], y[:(i + 1)]) * poly
        poly *= xi - x[i]
    return result

#Numbers of data points
#Shoudn't take more than 20 points because recurse algorithm of Div_diff function will run very low)
n = np.random.randint(2, 10)

#Point tho calculate value of the function (unknown point)
xi = 9.5

#Input data with random function
x = np.linspace(0.0, 10.0, n)
y = np.random.rand(1, n)[0]

#Printing input data 
print("1. Input data: \nx = ", x)
print("y = ", y)
print("2. Lagrange interpolation's result: \nP(" + str(xi) + ") = ", Lagrange_function(xi, x, y))
print("3. Newton interpolation's result: \nP" + str(n) + "(" + str(xi) + ") = ", Newton_function(xi, x, y))

random = np.arange(0.0, 10.1, 0.1)
Lagrange_func = []
Newton_func = []

for i in random:
    Lagrange_func.append(Lagrange_function(i, x, y))

for i in random:
    Newton_func.append(Newton_function(i, x, y))

plt.figure()
#Lagrange interpolation plot
plt.subplot(121)
plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(random, Lagrange_func, 'b-')
plt.plot(x, y, 'ro')
#Unknown point - green
plt.plot(xi, Lagrange_function(xi, x, y), 'go')

#Newton interpolation plot
plt.subplot(122)
plt.title("Newton Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(random, Newton_func, 'b-')
plt.plot(x, y, 'ro')
#Unknown point - green 
plt.plot(xi, Newton_function(xi, x, y), 'go')
plt.show()