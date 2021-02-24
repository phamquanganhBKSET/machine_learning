import numpy as np

def Numerical_gradient(fn, arr, eps):
    arr_flat = arr.reshape(-1)
    arr_shape = arr.shape
    grad_flat = np.zeros_like(arr_flat)
    result = np.zeros_like(arr_flat)
    numelements = arr_flat.shape[0]

    for i in range(0, numelements):
        Xp_flat = arr_flat.copy()
        Xn_flat = arr_flat.copy()
        Xp_flat[i] += eps
        Xn_flat[i] -= eps
        Xp = Xp_flat.reshape(arr_shape)
        Xn = Xn_flat.reshape(arr_shape)
        grad_flat[i] = ((fn(Xp) - fn(Xn))/(2*eps))
    
    result = grad_flat.reshape(arr_shape)
    return result

m, n = 10, 20
eps = 1e-6

#Matrix 1-D 
A = np.random.rand(m, m)

#Matrix n-D
B = np.random.rand(m, m)

#Matrix input x
x = np.random.rand(m, 1)

#Matrix input X
X = np.random.rand(m, n)

print("1. Matrix A (1-D): \nA = ", A)
print("2. Matrix B (" + str(m) + "-D): \nB = ", B)

#Function 1: trace(X^T*A*X)
def fn1(X):
    return np.trace(X.transpose().dot(A).dot(X))

#Function 2: x^T*B*x
def fn2(x):
    return x.transpose().dot(B).dot(x)

#Exactly gradient of function 1
def grad1(X):
    return (A + A.transpose()).dot(X)

#Exactly gradient of function 2
def grad2(x):
    return (B + B.transpose()).dot(x)

print("3.1. Numerical gradient of fn1(x): \n", Numerical_gradient(fn1, X, eps))
print("3.2. Exactly gradient of fn1(x): \n", grad1(X))
print("4.1. Numerical gradient of fn2(x): \n", Numerical_gradient(fn2, x, eps))
print("4.2. Exactly gradient of fn2(x): \n", grad2(x))
