

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report


if __name__ == '__main__':
    #1) 데이터 준비
    dataset = pd.read_csv('knndata.csv')
    print(dataset.shape)
    print(dataset.info())
    print(dataset.describe())

    #2) 데이터 전처리

    X = dataset.iloc[ : , :-1].to_numpy()
    y = dataset.iloc[ : , 2].to_numpy()
    # print(y)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
    print(len(X_train),len(X_test),len(y_train),len(y_test))

    #3) 변수 표준화

    scaler = StandardScaler() # 변수표준화 다음에 스케일러 객체생성
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    for col in range(2):
        print(X_train[ : , col].mean(), X_train[ :,col].std())
        print(X_test[ : , col].mean(), X_test[ :, col].std())

    #4) 학습 예측 - 여기선 classifier가 바로 나와야함 KN

    classifier = KNeighborsClassifier(n_neighbors=17)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    conf_matrix = confusion_matrix(y_test,y_pred)
    print(conf_matrix)
    report = classification_report(y_test,y_pred)
    print(report)