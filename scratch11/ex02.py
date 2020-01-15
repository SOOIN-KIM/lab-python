'''
R을 활용한 머신러닝 - 암데이터 파일(csv)
scikit - learn 패키지 활용, kNN 결과

'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #1) 데이터준비
    dataset = pd.read_csv('wisc_bc_data.csv')
    print(dataset.shape)
    print(dataset.info)
    print(dataset.describe())
    print(dataset.iloc[:5])

    #2) 데이터 전처리
    # 필요없는 열 삭제
    print('------')
    x = dataset.iloc[ : , 2:32].to_numpy()
    # print(x)
    y = dataset.iloc[ : , 1:2].to_numpy()
    # print(y)

    x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.2)
    print(len(x_train),len(x_test),len(y_train),len(y_test))
    # print(x_train[:3])

    # 3)  변수 표준화

    scaler = StandardScaler() # 스케일러 객체생성
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    for col in range(30):
        print(x_train[ :, col].mean() , x_train[:,col].std())
        print(x_test[ :, col].mean() , x_test[:,col].std())

    # 4) 학습 예측

    classifier = KNeighborsClassifier(n_neighbors = 25)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    print('-------------')
    print(y_pred)

    # 5) 모델 평가
    conf_matrix = confusion_matrix(y_test,y_pred)
    print(conf_matrix)
    report = classification_report(y_test,y_pred)
    print(report)


    # k 값 변경에 따른 보델 성능

    errors = []
    for i in range(1,41):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train,y_train)
        pred_i = knn.predict(x_test)
        errors.append(np.mean(pred_i!= y_test))

    plt.plot(range(1,41), errors)
    plt.show()