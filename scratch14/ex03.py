from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import math

def logistic(x):
    '''Logistic Sigmoid 함수'''
    return 1 / (1 + math.exp(-x))


def predict(row, betas):
    '''row의 x1, x2값과 betos의  b0, b1, b2를 사용해서
    회귀식 y = b0 _ b1 * x2 + b2* x2를 만들고,
    회귀식을 로지스틱 함수의 파라미터에 전달해서 예측값을 알아냄'''
    y_hat = betas[0]
    for i in range(len(betas) - 1):
        y_hat += betas[i+1] * row[i]
    return logistic(y_hat)

def coefficioent_sgd(dataset, learning_rate, epochs):
    '''회귀식 y =b0 +b1* x1 + b2 * x2의 계수들(b0, b1, b2)을
    stochastic gradient descent 방법으로 추정(estimate)'''
    # 회귀식에서 가장 처음에 사용할 betas 초깃값을 0으로 시작
    betas = [0 for _ in range(len(dataset[0]))]
    for epoch in range(epochs): # epochs 회수만큼 반복
        sse = 0
        for sample in dataset: # 데이터 세트에서 row 개수만큼 반복
            prediction = predict(sample,betas)
            error = sample[-1] - prediction
            sse += error ** 2
            # 계수들(b0, b1, b2)를 아래와 같은 방법으로 업데이트
            # b_new = b + learning_rate * error * prediction * (1-prediction)
            betas[0] = betas[0] + learning_rate * error * prediction * (1 - prediction)
            for i in range(len(sample) - 1):
                betas[i + 1] = betas[i + 1] + learning_rate * error * prediction * (1 - prediction) * sample[i]





if __name__ == '__main__':
    iris = load_iris()
    print(iris.DESCR)
    X = iris.data # iris['data']
    y = iris.target # iris['target]
    features = iris.feature_names

    for i in range(len(features)):
        plt.scatter(X[:,i],y, label=features[i])
    plt.legend()
    plt.show()

    # petal -length, petal-width가 calss(품종)을 분류할 떄 상관관계가 높아 보임.
    X = X[: ,2:4] # pl, pw만 선택
    print(X[:5])

    # setosa 5개, setosa가 아닌 품종 5개를 샘플링
    indices = [x for x in range(0,100,10)]
    sample_data = np.c_[X[indices, :], y[indices]]
    print(sample_data)

    np.random.seed(1218)
    betas = np.random.random(3)
    for sample in sample_data:
        prediction = predict(sample, betas)
        # 오류 = 실제값 - 예측값
        error = sample[-1] - prediction
        print(f'실제값={sample[-1]}, 예측값={prediction}, 오차={error}')
