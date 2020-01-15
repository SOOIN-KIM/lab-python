from scratch11.ex03 import train_test_split, MyScaler, MyKnnClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,classification_report

if __name__ == '__main__':
    col_names = ['sepal-length', 'sepal-width',
                 'petal-length', 'petal-width',
                 'Class']
    iris = pd.read_csv('iris.csv',
                header=None,
                names=col_names)
    print(iris.iloc[:5])

    # 데이터 프레임을 이용해서 각 특성(변수)들과 Class(레이블)과의 관계 그래프
    iris_by_class =iris.groupby(by='Class')
    for name, group in iris_by_class:
        # print(name,len(group))
        plt.scatter(group['sepal-length'],group['petal-width'],
                    label=name)
    plt.legend()
    plt.xlabel('sepal_length')
    plt.ylabel('petal_width')
    plt.show()

    # 데이터 세트를 points와 Labels로 구분
    X = iris.iloc[:, :-1].to_numpy() # points
    y = iris.iloc[:, 4].to_numpy() # labels

    # 학습/ 검증(train/test) 세트로 변경
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

    # Scaling
    scaler = MyScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train) # 데이터 변환
    X_test = scaler.transform(X_test)

    #k -NN 알고리즘 적용
    knn = MyKnnClassifier(n_neighbors=5) # 분류기 객체 생성
    knn.fit(X_train, y_train) # 학습
    y_pred = knn.predict(X_test) # 예측
    print(np.mean(y_test == y_pred)) # ㅇㅖ측 결과 확인


    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))