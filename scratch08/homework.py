import pandas as pd
from scratch08.ex04 import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from scratch08.ex01 import *

data = pd.read_csv('C:\dev\lab-python\mpg.csv',usecols=['cty','displ'])

subset = data[['displ','cty']]
tuples = [tuple(x) for x in subset.values]
dispel_cty = tuples
print(tuples)

print('1) 확률적 경사 하강법')
theta = [1,1]
step = 0.001
for epoch in range(200):
    random.shuffle(tuples)

    for x, y in tuples:
        gradient = linear_gradient(x,y, theta)
        theta = gradient_step(theta, gradient, -step)
    if (epoch +1) % 10 == 0:
        print(f'{epoch}:{theta}')
print('2) 배치 경사 하강법')
step = 0.01
theta = [1,1]
for epoch in range(5000):
    gradients = [linear_gradient(x, y, theta)
                 for x, y in tuples]
    gradient = vector_mean(gradients)
    theta = gradient_step(theta, gradient,-step)
    if (epoch +1) % 100 == 0:
        print(f'{epoch}:{theta}')

print('3) 미니 배치 경사 하강법')
theta = [1,1]
step = 0.01
for epoch in range(1000):
    mini_batches = minibatches(tuples, 20 ,True)
    for batch in mini_batches:
        gradients = [linear_gradient(x,y,theta)
                     for x,y in batch]
        gradient = vector_mean(gradients)
        theta = gradient_step(theta, gradient, -step)
    if (epoch +1) % 100 == 0:
        print(f'{epoch}: {theta}')

print(dispel_cty)

dispel = []
cty = []
for x, y in dispel_cty:
    dispel.append(x)
    cty.append(y)
print(dispel)
print(cty)

xs = dispel
ys = cty
init_x = 2
#cty = slope * displ + intersect
#y = -2.5909179919448815 * x + 25.992993758809188
'''
for _ in range(5):
    gradient + difference_quotient(f,init_x,h=0.01)
    tangent_estimates = [tangent(x,gradient, init_x, f(init_x))
                         for x in xs]
    plt.plot(xs,tangent_estimates, label=f'x={init_x}')
    init_x = move(init_x, gradient, step=-0.9)

plt.plot(xs,ys,color ='black')
plt.legend()
plt,ylim(bottom = -1)
plt.show()

'''