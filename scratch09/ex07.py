'''
pandas 데이터 타입
Series : 1차원 리스트 . 인덱스는 한개만 갖음.
DataFrame: 2차원 리스트. 인덱스가 행과 열 두개를 갖음
'''

import pandas as pd
import numpy as np

a = pd.Series([1,3,5,np.nan,6,8])
print(type(a)) # Series
print(a)
# Series 에서 특정 인덱스의 아이템 선택할 때에는 Series[index]
print(a[0]) # 숫자하나만 뽑아내서 데이터 타입이 float
# 인덱스 연산자의([]) 안에서 범위 연산자(:)를 사용 할 수도 있음
print(a[0:3]) # 데이터 타입: Series
# 인덱스 연산자([]) 안에서 리스트 연산자([])를 사용할 수도 있음
print(a[[0,2,4]])
## Series는 인덱스를 무조건 하나 가질수 있다!!
#  print(a[0,2,4]) <-- 이것은 쓸수 없음 인덱스 3개를 갖는 거라서!

# dict 타입({key: value, ...})의 데이터에서 DataFrame 생성
df = pd.DataFrame({
    'no':[3,13,23],
    'name':['김영광','이은지','조유경'],
    'gender':['M','F','F']
})

print(df)

# 2차원 리스트([...],[...],[...]]) 타입의 데이터에서 DataFrame을 생성
students = pd.DataFrame([
    [4,'김재성','M'],
    [14,'이재경','M'],
    [24,'조지원','F']
],columns = ['번호','이름','성별'])
# students.columns = ['번호','이름','성별']
print(students)

# DataFrame.iloc[orw_index, column_index]
print(students.iloc[0,0]) # 0번 row, 0번 column의 아이템
print(students.iloc[0,0:3]) # 0번 row, 0,1,2 column에 있는 아이템
print(type(students.iloc[0, 0:3])) # Series
print(students.iloc[0:2, 0:2])
print(type(students.iloc[0:2, 0:2])) # DataFrame
print(type(students.iloc[:, 1:3])) # 범위 연산자만 사용하면 모든 행 또는 열
print(type(students.iloc[1:3, :])) #
print(type(students.iloc[1:3])) # 모든 컬럼을 선택할 때는 컬럼 인덱스를 생략 가능


# boolean indexing
# DataFrame[[boolean들의 리스트]]: 리스트에서 True인 값의 인덱스를 행 인덱스로 선택
print(students[[False, True, False]])
condition = (students['성별'] == 'M')
print(condition)  # [True, True, False]
print(students[condition])
print(students[students['성별'] == 'F'])


# 데이터 프레임 이어 붙이기 : concat
students.columns = ['no','name','gender']
stu_df = pd.concat([df,students])
print(stu_df)
print(stu_df.iloc[0])
print(stu_df.loc[0])

stu_df2 = pd.concat([df,students], ignore_index=True)
print(stu_df2)


# DataFrame.sort_values(정렬 기준 칼럼 이름)
print(stu_df2.sort_values('no'))
print(stu_df2.sort_values('gender'))

# 두 개 이상의 조건으로 boolean indexing
cond1 = stu_df2['no'] % 2 == 1 # no컬럼의 값이 홀수이면
cond2 = stu_df2['gender']  == 'F'# gender컬럼의 값이 'F'이면
subset = stu_df2[cond1 & cond2]
 # boolean 인덱싱에서는 and, or 연산자는 사용할 수 없고,
 # 각 성분별로 연산을 하는 (bitwise 연산자) &,| 를 사용해야 함!
 print(subset)
