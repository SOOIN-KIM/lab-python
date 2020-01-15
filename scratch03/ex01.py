'''
matplotlib.pyplot 모듈을 사용한 데이터 시각화
'''

# plotting을 위한 패키지 import
import matplotlib.pyplot as plt

years = [1950, 1960, 1970,1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6 ,10289.7, 14958.3]

plt.plot(years,gdp,c = 'green',marker='o') # plot: 선 그래프 생성
plt.title('연도별 GDP', fontname = 'D2Coding')
plt.xlabel('Year')
plt.ylabel('GDP(Billions of $')

# savefig : 그래프를 이미지 파일로 저장
plt.savefig('../image_output/year_gdp.png')

plt.show() # 화면에 직접 띄우기 위해서는 show 함수를 써줘야함


# 막대 그래프(bar chart) 이산형 데이터
# 영화 제목
movies = ['Annie Hall', 'Ben-Hur','casablanca', 'Gandhi','West Side Story']
# 아카데미 시상식에서 받은 상의 갯수
num_oscars = [5, 11, 3, 8, 10]

plt.bar(movies,num_oscars)
font_name = {'fontname': 'D2Coding'}
plt.title('아카데미 수상작',font_name)
plt.ylabel('수상 갯수',font_name)
plt.show()


# 히스토그램(histogram) #연속형 데이터
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

from collections import Counter # 파이썬 기본 패키지
histogram = Counter(min(grade // 10 *10, 90) for grade in grades)
print(histogram) # 각 점수대별 시험 성적 객수
plt.bar(histogram.keys(), histogram.values())
plt.yticks([0,1,2,3,4,5])
plt.show()

plt.hist(grades, edgecolor='black')
plt.yticks([0,1,2,3,4,5])
plt.show()

mentions = [500, 505]
years = [2013, 2014]
plt.bar(years,mentions, 0.5)
plt.xticks(years) # X 축에 표시할 눈금
plt.show()