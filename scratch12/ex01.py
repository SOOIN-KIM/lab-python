'''
Naive Bayes 알고리즘
Naive Bayes 분류기(Classifier)를 사용한 iris 품중 분류
'''

from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
print(type(iris))
# Bunch 클래스: {'data' :[], 'target':[]}으로 이루어진 dict와 비슷한 클래스
# data: 특성(변수)들. n 차원 공간의 점(point)
# target: 레이블(분류 클래스)
# print(iris)

print('data shape:', iris.data.shape)
print('iris target:', iris.target_names)
print('iris features:', iris.feature_names)

X = iris.data
print(type(X))

X,y = datasets.load_iris(return_X_y= True)

# 데이터 세트를 학습/ 검증 세트로 난눔
X_train,X_test, y_train, y_test = train_test_split(X,y, test_size=0.2
                                                   )

# 데이터들을 변환(스케일링)
scaler = StandardScaler()
scaler.fit(X_train)
X_train_trainformed = scaler.transform(X_train) # 학습 데이터 세트 변환
X_test_trainsformed = scaler.transform(X_test)

# 머신 러닝 모델 선택 -Naive Bayes
gnb = GaussianNB() # Gaussian Naive Bayes 모델 선택 - 연속형 자료
gnb.fit(X_train_trainformed, y_train) # 모델 학습
y_pred = gnb.predict(X_test_trainsformed) # 예측
print(y_pred)
# 성능 측정
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
