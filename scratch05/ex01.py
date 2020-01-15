'''
통계

중심 경향성 : 평균 , 중앙값, 분위수(4분위,100분위=퍼센트), 최빈값
산포도 : 분산(variance), 표준편차(standard deviation), 범위(range)
상관관계 : 공분산(covariance), 상관 계수(correlation)
'''

from scratch04.ex01 import dot
import math

def mean(x):
    '''
    리스트 x의 모든 아이템들의 평균을 계산해서 리턴

    :param x: 원소 n개인 1차원 리스트
    :return: 평균
    '''
    result = 0
    for i in x:
        result += i
    return result/len(x)

def mean(x):
    """
    리스트 x의 모든 아이템들의 평균을 계산해서 리턴
    x = [x1, x2, ..., xn]
    mean = (x1 + x2 + ... + xn) / n

    :param x: 원소 n개인 (1차원) 리스트
    :return: 평균
    """
    return sum(x) / len(x)

def median(x):
    '''
    리스트 x를 정렬했을 때 중앙에 있는 값을 찾아서 리턴
    n이 홀수이면, 중앙값을 찾아서 리턴
    n이 짝수이면, 중앙에 있는 두 개 값의 평균을 리턴

    :param x: 원소 n개인 1차원 리스트
    :return: 중앙값
    '''
    # result = 0
    # sorted(x)
    # if len(x)%2 == 1:
    #     result = len(x)
    # else :
    #     result = ((len(x)//2) - 1) + (len(x)//2)
    # return result

    #선생님 코드
    # n = len(x) #리스트의 아이템 개수
    # sorted_x = sorted(x) # 데이터 크기 순으로 정렬(오름차순)
    # mid_point = n // 2 # 리스트의 가운데 위치(인덱스)
    # if n % 2: # n이 홀수인 경우
    #     median_value = sorted_x(mid_point)
    # else: # n이 짝수인 경우
    #     median_value = (sorted_x[mid_point-1]+sorted_x[mid_point])/2
    # return median_value



def quantile(x,p):
    '''
    리스트 x의 p분위에 속하는 값을 찾아서 리턴
    :param x: 원소 n개인 1차원 리스트
    :param p: 0 ~ 1.0 사이의 값(퍼센트)
    :return:
    '''

    n = len(x) # 리스트 아이템의 개수
    p_index = int(n * p) # 해당 퍼센트의 인덱스 - 소수점 버림
    sorted_x = sorted(x) #오름차순 정렬된 리스트트
    return sorted_x[p_index]

def mode(x):
    '''
    리스트에서 가장 자주 나타나는 값을 리턴.
    최빈값이 여러개인 경우, 최빈값들의 리스트를 리턴.
    from collections import Counter

    :param x: 원소가 n개인(1차원) 리스트
    :return: 최빈값들의 리스트
    '''

    from collections import Counter

    # list = []
    # counts = Counter(x)
    # max_count = max(counts.values())
    # for _ in list:
    #     count

    # 선생님코드
    counts = Counter(x) #Counter 객체(인스턴스) 생성
    # print(counts) #(값,빈도수) 튜플들의 리스트
    # print(counts.keys(), counts.values())
    # # Counter.keys(): 데이터(아이템), Counter.values():빈도수
    # print(counts.items())
    max_count = max(counts.values()) # 빈도수의 최대값
    return [val for val,cnt in counts.items() if cnt == max_count]

    # freq = [] # 최빈값들을 저장할 리스트
    # for val,cnt in counts.items(): #Counter 객체에 대해서 반복
    #     if cnt == max_count: # 빈도수가 최대 빈도수와 같으면
    #         freq.append(val) # 리스트에 저장
    # return freq


def data_range(x):
    '''


    :param x: 원소 n개인 (1차원) 리스트
    :return: 리스트의 최댓값 - 리스트의 최솟값
    '''

    return max(x) - min(x)

def de_mean(x):
    '''
    편차(데이터 -평균) 들의 리스트

    :param x: 원소 n개인 1차원 리스트
    :return: 편차(deviation)들의 리스트

    '''
    mu = mean(x)
    return [x_i - mu for x_i in x]

def variance(x):
    '''
    (x1 - mean)**2 + (x2 - mean)**2 +...+(xn - mean)**2)/(n-1)

    :param x: 원소가 n개인 (1차원) 리스트
    :return: 분산
    '''
    n = len(x)
    total=0
    for x_i in x:
        total += (x_i - mean(x))**2
    return total /(n-1)

def variance2(x):
    n = len(x)
    deviations = de_mean(x)
    return dot(deviations,deviations) / (n - 1)

def standard_deviation(x):
    '''
    from math import sqrt
    sqrt(variance)

    :param x: 원소가 n개인 (1차원) 리스트
    :return: 표준편차
    '''

    return math.sqrt(variance2(x))


def covariance(x,y):
    '''
    공분산(covariance)
    cov = sum((xi - x_bar)(yi - y_bar)) / (n - 1)

    :param x: 원소가 n개인 (1차원) 리스트
    :param y: 원소가 n개인 (1차원) 리스트
    :return: 공분산
    '''
    n = len(x)
    x_bar = mean(x)
    y_bar = mean(y)
    x_deviations = [x_i - x_bar for x_i in x]
    y_deviations = [y_i - y_bar for y_i in y]
    # x_total = 0
    # y_total = 0
    # for x_i in x:
    #     x_total += (x_i - mean(x))
    # for y_i in y:
    #     y_total += (y_i - mean(y))
    #
    # return ((x_total) * (y_total))/(n-1)
    xy_total = 0
    for x_i,y_i in zip(x,y):
        xy_total += (x_i - mean(x)) * (y_i - mean(y))
    return xy_total / (n-1)

    sum_of_deviations = dot(x,y)


def correlation(x,y):
    '''
    상관계수 (correlation)
    Corr= Cov(x,y)/(sd(x) * sd(y))

    :param x: 원소가 n개인 (1차원) 리스트
    :param y: 원소가 n개인 (1차원) 리스트
    :return: 상관계수 ( -1 ~ 1)
    '''
    sd_x = standard_deviation(x)
    sd_y = standard_deviation(y)
    if sd_x!= 0 and sd_y !=0:
        corr = covariance(x,y)/ (sd_x * sd_y)
    else:
        corr = 0
    return corr




if __name__ == '__main__':
    data = [2,2,3,3,4,4,4,6,6,6,100]
    print('mean =', mean(data))

    median_data = median(data)
    print('median =', median_data)

    quantile_1 = quantile(data, 0.1)
    print(quantile_1)
    quantile_3 = quantile(data, 0.75)
    print(quantile_3)

    most_frequent = mode(data)
    print(most_frequent)

    x = [2,2,3,3,4,4,4,6,6,6,100]
    y = [10,2,5,3,4,1,4,0,6,1,7]
    print('data_range =',data_range(x))
    print('varaiance =', variance(x))
    print('varaiance2 =', variance2(x))
    print('standard deviation =', standard_deviation(x))

    print('covariance =',covariance(x,y))
    print('correlation =', correlation(x,y))

    x = [-3,-2,-1,0,1,2,3]
    y = [3,2,1,0,1,2,3]