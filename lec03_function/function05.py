'''
가변 길이 인수 (variable - length argument)
함수를 호출할 때 전달하는 argument의 갯수가 변할 수 있을 때
파라미터 이름 앞에 *를 붙임.
'''

print('a')
print('a','b','c','d', sep=':')

def fn_vararg(*varargs):
    print(varargs)
    # 가변길이 인수들은 tuple 처럼 취급하면 됨
    for arg in varargs:
        print(arg)

fn_vararg(1,2,3,4,5,6,7,8,9)


def summation(*args):
    '''
    임의의 갯수의 숫자들을 전달받아서 그  숫자들의 총합을 리턴하는 함수
    :param args: 합계를 계산할 숫자들( 개수 제한 없음
    :return: 숫자들의 합
    '''
    result = 0
    for n in args:
        result += n
    return result

print(summation())
print(summation(1))


def fn_varargs3():
    fn_vararg(1, b=2)

# 가변길이 파라미터 뒤에 선언된 파라미터에 값을 전달할 때는
# keyword 방식으로만 값(argement)를 전달 할 수 있음

def calculator(*values,operator):
    '''
    operator가 '+'인 경우에는 values들의 합계를 리턴하고,
    operator가 '*'인 경우에는 values들의 곱을 리턴하는 함수

    :param values:
    :param operator:
    :return:
    '''

    if operator == '+':
        result = 0
        for x in values:
            result += x
        return result
    elif operator == '*':
        result = 1
        for x in values:
            result *= x #result = result * x
        return result


result = calculator(1,2,3,4,5,operator='+')
print(result)
print(calculator(1,2,3,4,5,operator='*'))

