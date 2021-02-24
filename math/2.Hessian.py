import numpy as np

#Chú ý: Bài này nên tránh những hàm có first-order gradient là một ma trận n chiều vì sẽ khó tìm ra đạo hàm bậc 2 chính xác để so sánh kết quả (vì không có công thức) 
def Product_matrix(arr, n):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            arr[i][j] *= n
    return arr 

def Hessian_approximate(fn, arr, eps):
    arr_flat = arr.reshape(-1)
    arr_shape = arr.shape
    hessian_flat = np.zeros_like(arr_flat)
    result = np.zeros_like(arr_flat)
    numelements = arr_flat.shape[0]

    for i in range(0, numelements):
        Xp_flat = arr_flat.copy()
        Xn_flat = arr_flat.copy()
        Xp_flat[i] += eps
        Xn_flat[i] -= eps
        Xp = Xp_flat.reshape(arr_shape)
        Xn = Xn_flat.reshape(arr_shape)
        hessian_flat[i] = ((fn(Xp) - Product_matrix(fn(arr), 2) + fn(Xn))/(eps**2))
    
    result = hessian_flat.reshape(arr_shape)
    return result

m, n = 10, 20
epsilon = 1e-6

#Vector x
x = np.random.rand(m, 1)

#Function: x^T*x
def fn(x):
    return (x.T).dot(x)

#Exactly hessian of function:
def hes(x):
    return Product_matrix(np.ones_like(x), 2)

print("1. Vector x: \n", x)
print("2. Approximately hessian: \n", Hessian_approximate(fn, x, epsilon))
print("3. Exactly hessian: ", hes(x))