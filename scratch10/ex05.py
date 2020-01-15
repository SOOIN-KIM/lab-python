import pandas as pd
import numpy as np


def squares(x):
    return x **2


def doubles(x):
    return x *2



if __name__ == '__main__':
    result1, result2, = squares(3), doubles(3)
    print(result1,result2)

    array = np.array([1,2,3])
    print('array =', array)
    result1 = squares(array)
    result2 = doubles(array)
    print('squares = ', result1)
    print('doubles =', result2)

    df = pd.DataFrame({
        'a' : [1,2,3],
        'b' : [4,5,6]
    })
    print(df)
    print(squares(df))

    result = df.apply(squares)
    print(result)

    print(np.sum([1,2,3]))
    result = df.apply(np.sum, axis =0)
    print(result)
    result = df.apply(np.sum, axis =1)
    print(result)
    # DataFrame.apply(function, axis)
    # axis = 0(default)일 때는, 데이터프레임의 각 컬럼을 함수의 파라미터로 전달.
    # axis = 1 일 때는, 데이터프레임의 각 행(row)을 함수의 파라미터로 전달.
    # 함수의 리턴 값을 돌려받음
