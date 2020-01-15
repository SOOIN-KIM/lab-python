# gapminder.tsv 파일을 읽어서 데이터 프레임 생성
import pandas as pd

df = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
print(df.iloc[0:5])

# boolean indexing:
# 컬럼의 값을 이용해서 특정 레코드(행,row)들을 선택하는 방법
# DataFrame[(컬럼의 값을 이용한) 조건식]
# SQL : select * from DataFrame where column =='';
df_afg = df[df['country'] =='Afghanistan']
print(df_afg)

df_korea = df[df['country'] == 'Korea, Rep.']
print(df_korea)

# 대한민국(Korea. Rep.)의 인구(pop)와 1인당 GDP(gdpPercap)을 출력


# print(df_korea[['pop','gdpPercap']])
print(df[df['country'] == 'Korea, Rep.'][['pop','gdpPercap']])

# mpg.csv 파일을 읽어서 DataFrame을 생성
# cty 컬럼의 값이 cty 평균보다 큰 자동차들의 model, displ, cty, hwy를 출력

# dataframe 생성
df_mpg = pd.read_csv('../scratch08/mpg.csv', sep =',', encoding='UTF=8')
print(df_mpg.head(5))

# 평균을 계산

df_mpg_cty_mean = df_mpg['cty'].mean()
print('cty의 평균=',df_mpg_cty_mean)

# cty 컬럼의 값이 평균보다 큰 레코드 들을 출력
subset = df_mpg[df_mpg['cty'] > df_mpg_cty_mean]
print(subset)

#cty가 평균 이상인 자동차들의 model, cty,hwy 컬럼을 출력
print(subset[['model','cty','hwy']])