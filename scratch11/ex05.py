import matplotlib.pyplot as plt
import pandas as pd

col_names = ['sepal-length', 'sepal-width',
             'petal-length', 'petal-width',
             'Class']
iris = pd.read_csv('iris.csv',header=None,names=col_names)
iris_by_class = iris.groupby(by='Class')

xy= [] # x축 /y축에 사용할 변수 이름
for i in range(4):
    for j in range(i+1,4):
        xy.append((col_names[i],col_names[j]))
print(xy)

fig, ax= plt.subplots(2,3)
xy_idx=0
for row in range(2):
    for col in range(3):
        axis = ax[row, col]
        x = xy[xy_idx][0]
        y = xy[xy_idx][1]
        xy_idx += 1 # 다음 x-y축 데이터 이름으로 이동
        axis.set_title(f'{x} vs {y}')
        axis.set_xlabel(x)
        axis.set_ylabel(y)
        for name,group in iris_by_class:
            axis.scatter(group[x], group[y], label =name)
plt.show()