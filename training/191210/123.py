from sklearn.metrics import r2_score



y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
r2=r2_score(y_true, y_pred)
print(r2)

y_true = [5,6,7,8]
y_pred = [-100,524,-1,3]
r2=r2_score(y_true, y_pred)
print(r2)
r2_