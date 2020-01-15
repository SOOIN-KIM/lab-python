'''
Boston house prices dataset
'''

import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import PolynomialFeatures




boston = load_boston()
data = pd.DataFrame(boston.data,columns=boston.feature_names)
print(data.head())

# 보스턴 집값 데이터 세트 로딩

boston = load_boston()
X, y = load_boston(return_X_y=True)



print(X.shape, y.shape)
features = boston.feature_names
print(features)
print(X[0])
print(y[0])
# 데이터 탐색 - 그래프
X_transpose = [column for column in zip(*X)]
print(len(X_transpose))
fig, ax = plt.subplots(4, 4)
# ax: 3x4 형태의 2차원 배열(ndarray)
ax_flat = ax.flatten()
for i in range(len(features)):
    subplot = ax_flat[i]
    subplot.scatter(X[:, i], y)
    subplot.set_title(features[i])
plt.show()




# 단순 선형 회귀
# y+ b + a * x

rm = X[:, np.newaxis,12] # data에서 rm 컬럼만 선택
print(rm.shape)

# 학습세트/ 검증 세트 나눔
rm_train = rm[:-100]
rm_test = rm[-100:]
y_train = y[:-100]
y_test = y[-100:]

# 학습 세트를 사용해서 선형회귀 - 단순선형회귀, 다중 선형회귀
# RM 컬럼과 y와의 단순 선형회귀

regr = linear_model.LinearRegression()
regr.fit(rm_train,y_train)
print('intercept = ', regr.intercept_ ,'coefficients =', regr.coef_)

# 검증 세트를 사용해서 예측
y_pred = regr.predict(rm_test)
plt.scatter(rm_test, y_test)
plt.plot(rm_test, y_pred,'r-')
plt.show()

# Mean Square Error 계산
mse = mean_squared_error(y_test,y_pred)
print('Mean Square Error =', mse)

# R2-score 계산
R2 = r2_score(y_test,y_pred)
print('R2- Score =', R2)

# 다중선형회귀
# 모든 컬럼과 y와의 다중선형회귀

X_train = X[:400]
X_test = X[400:]
y_train = y[:400]
y_test = y [400:]
lin_reg =linear_model.LinearRegression()
lin_reg.fit(X_train,y_train)
print('intercept = ', lin_reg.intercept_ ,'coefficients =', lin_reg.coef_)
y_pred = lin_reg.predict(X_test)

R2_all = r2_score(y_test,y_pred)

print(y_test)
print(y_pred)
print(R2_all)

