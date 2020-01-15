'''
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 *hint seperater='  '
DataFrame으로 변환.
DataFrame의 행과 열의 갯수 확인 *shape
DataFrame의 앞쪽 데이터 5개를 출력 head
DataFrame의 뒷쪽 데이터 5개를 출력 tail
DataFrame의 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터 타입들을 출력
DataFrame에서 'country','lifeExp',' gdpPercap'컬럼들만 출력
DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력 *iloc
DataFrame에서 행 레이블이 840 ~ 851 행들의 나라이름 ,기대수명 ,1인당gdp를 출력 *loc
DataFrame에서 연도(year)별 기대 수명의 평균을 출력 *groupby, mean
DataFrame에서 연도(year)별, 대륙(continent)별 기대 수명의 평균을 출력
'''

import pandas as pd
import os
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

# sep 파라미터: 데이터 구분자(separator)
file_path =('gapminder.tsv')
df = pd.read_csv(file_path, sep= '\t',encoding='UTF-8')

# DataFrame.shape:(row 개수, column 개수)
print('Shape =',df.shape)
nrows,ncols = df.shape
print(f'nrows = {nrows}, ncols={ncols}')


print(df.head(5))
print(df.tail(5))
# 행 인덱스를 이용한 출력
# DataFrame.iloc[row index, column index]
print(df.iloc[0:5])

# DataFrame.columns:: pandas.Index 클래스 객체, 컬럼 이름들의 리스트를 가지고 있음.
print(df.columns)

# DataFrame.dtypes : 각 칼럼의 이름과 데이터 타입을 저장하고 있는 프로퍼티
# pandas.read_csv() 함수는 파일의 문자열들을 타입에 맞게끔 변환하는 기능을 가지고 있음
# pandas 데이터 타입: object(문자열), int64(64비트 정수), float64(비트 실수)
print(df.dtypes)


cols = ['country','lifeExp','gdpPercap']
print(df[cols])

#데이터 프레임에서 특정 행(row)들을 인덱스로 선택
print(df.iloc[[0,99,999]])

#loc에서 범위 연산자(:)이 사용되던 이름(label)로 취금하기 때문에 양쪽 숫자 모두 포함
#iloc에서 범위 연산자(:)가 사용되면 인덱스로 취급하기 때문에 뒤쪽 숫자는 미포함

print(df.loc[840:851, cols])
print(df.iloc[840:852,[0,3,5]]) #iloc는 행인덱스 번호이기때문에 마지막 숫자를 포함하지않음 출력하고싶은 행번호+1

print('===========')
group1 = df['lifeExp'].groupby(df['year'])
print(group1.mean())
group2 = df['lifeExp'].groupby([df['year'],df['continent']])
print(group2.mean())

# 연도별 기대수명(lifeExp)의 평균
df_by_year = df.groupby('year')
print(df_by_year['lifeExp'])
print(df_by_year['lifeExp'].mean())


# 연도별 기대수명 그래프

year_lifeExp = df.groupby('year')['lifeExp'].mean()
plt.plot(year_lifeExp)
plt.title('lifeExp by year')
plt.show()

# 연도별 전세계 인구수를(pop) 그래프

year_pop = df.groupby('year')['pop'].sum()
print(year_pop)
plt.plot(year_pop)
plt.title('pop by year')
plt.show()