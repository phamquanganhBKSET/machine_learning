import numpy as np
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt 

#LINEAR REGRESSION: weight = w1*height + w0

#Height(cm), input data, each row is data point 
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).transpose()

#Weight(kg)
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

#Building Xbar
one = np.ones((X.shape[0], 1)) #X.shape[0] is number of rows of matrix X
Xbar = np.concatenate((one, X), axis = 1).transpose() #Join a sequence of arrays along an existing axis

#Calculating
A = np.dot(Xbar, Xbar.transpose())
b = np.dot(Xbar, y)
w = np.dot(np.linalg.pinv(A), b)

#weight vector
w0 = w[0]
w1 = w[1]

#Test set: 155 cm and 160 cm
y1 = w1*155 + w0
y2 = w1*160 + w0

#Linear Regression point 
y_pred = w1*X + w0

#Scikit-learn:
#Fit the model by Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, y) #In scikit-learn, each sample is one row

poly = PolynomialFeatures(degree = 4)
X_poly = poly.fit_transform(X)
regr2 = linear_model.LinearRegression()
poly.fit(X_poly, y)
regr2.fit(X_poly, y)

#Compare two results
print("scikit-learn’s solution: w1 = ", regr.coef_[0], ", w0 = ", regr.intercept_)
print("our solution           : w1 = ", w[1], ", w0 = ", w[0])

plt.figure()
#Our solution
plt.subplot(121)
plt.title("Linear Regression")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.plot(X, y, 'ro')
plt.plot(X, y_pred, 'g-')
plt.plot(155, y1, 'bo')
plt.plot(160, y2, 'bo')

#Scikit-learn's solution
plt.subplot(122)
plt.title("Polynomial Regression")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.plot(X, y, 'ro')
plt.plot(155, regr.coef_[0]*155 + regr.intercept_, 'bo')
plt.plot(160, regr.coef_[0]*160 + regr.intercept_, 'bo')
plt.plot(X, regr2.predict(poly.fit_transform(X)), 'g-') 
plt.show()