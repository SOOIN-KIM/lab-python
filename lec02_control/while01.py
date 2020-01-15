'''
while 반복문:
[초기식]
while 조건식:
    조건식이 참인 동안에 실행할 문장
    [변경 식]
'''

# 1,2,3,...,10

n = 1
while n <= 10:
    print(n, end=' ')
    n += 1 # n= n+1
print()

n = 1
while n <= 9:
    print(f'2 x {n} = {2*n} ')
    n += 1

# 2단부터 9단까지 출력

a = 2
while a <= 9:
    b = 1
    while b <= 9:
        print(f'{a} x {b} = {a * b}')
        b += 1
    a += 1
    print('--------')


a = 2
while a <= 9:
    b = 1
    while b <= 9:
        print(f'{a} x {b} = {a * b}')
        if a == b:
            break
        b += 1
    a += 1
    print('--------')