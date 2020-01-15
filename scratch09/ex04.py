'''
pandas 패키지를 사용한 csv 파일 읽기
'''

import pandas as pd
import os
import matplotlib.pyplot as plt


file_path = os.path.join('../venv2', 'scratch08', 'mpg.csv')
df = pd.read_csv(file_path)
print(df.head()) # 데이터 프레임의 앞의 일부분 데이터 출력 default = 5
print('shape:', df.shape) # 관측값 234, 변수 11개
print('types:', df.dtypes)
# DataFrame.dtypes : 각 컬럼(변수)의 데이터 타입
# pandas의 데이터 타입: object(문자열), float(실수), int(정수)
print(df.describe())

#df['cloumn_name'] :DataFrame에서 특정 컬럼의 모든 데이터를 선택
displ = df['displ']
print(displ)
cty = df['cty']

plt.scatter(displ, cty)
plt.show()

#DataFrame에서 행(row)를 선택할 때,
# df.iloc[행 번호(인덱스)], df,loc[행 레이블]
print(df.iloc[0])
print(df.iloc[0:3])

# 데이터 프레임에서 여러개의 컬럼(변수)들을 선택
cols = ['displ','cty','hwy'] # []: 리스트
print(df[cols]) # []: 인덱스 연산자

# 데이터 프레임에서 여러개의 행(관측값)과 컬럼(변수)들을 선택
# df.loc[row_label, col_labels]
# df.iloc[row_indices, col_indices]
print(df.loc[0:3 , cols]) # 행 레이블 0부터 3까지 0,1,2,3 을 출력
print(df.iloc[0:3, 0:3]) # iloc는 인덱스를 받으니까 마지막 숫자 -1 까지만 출력 0,1,2