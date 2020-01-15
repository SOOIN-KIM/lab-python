import numpy as np
import pandas as pd

def squred_mean(data):
    '''데이터의 제곱의 평균을 리턴'''

    squred_sum = 0
    for x in data:
        squred_sum += x**2
    return squred_sum / len(data)

def my_func(x):
    '''tuple을 리턴하는 함수'''
    return x.min(),x.max()

if __name__ == '__main__':
    df = pd.DataFrame({
        'pop' : np.random.randint(1,10,4),
        'income' : np.random.randint(1,10,4)
    }, index = ['a','b','c','d'])
    print(df)

    # agg(aggregate) : DataFrame의 축을 기준으로 통계량을
    # 집계(aggregate) 하기 위한 함수
    #   통계량(statistic): 합계(sum), 평균(mean), 분산
    #   agg 함수는 집계가 목적이기 때문에 데이터 타입이 숫자 타입인 행/열에만
    # 함수가 적용이 된다.
    # agg 함수는 pandas나 numpy외에 사용자 정의 함수를 사용할 수 있다.
    # 단, 함수는ㄴ Seires를 파라미터로 전달하면 스칼라(숫자)하나를 리턴하는 함수여야 한다.

    print('=== agg by column(axis=0)')
    print(df.agg('mean', axis = 0)) # 파라미터 axis의 기본값은 0(컬럼 방향)

    print('=== agg by ros(axis=1)')
    print(df.agg('mean', axis=1))


    print(df.agg(squred_mean, axis =1))

    # apply : DataFrame에 축을 기준으로 함수를 적용(apply) 하기 위한 함수
    # 적용하는 함수는  pandas 객체를 리턴하면 됨.
    # apply 함수는 agg 함수보다 더 일반적으로 유연하게 사용 할 수 있지만,
    # 집계와 같은 특수한 목적인 경우에는 agg 함수보다 성능이 느림.
    print('=== apply by column(axis =0)')
    print(df.apply('mean'))

    print('=== apply by row(axis= 1)')
    print(df.apply('mean', axis =1))