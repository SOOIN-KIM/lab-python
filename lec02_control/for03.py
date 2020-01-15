'''
for-in 구문 연습
'''

# 구구단 2단부터 9단까지 출력
for gugudan in range(2,10):
    for gugudan1 in range(1,10):
        print(f'{gugudan}x{gugudan1} = {gugudan*gugudan1}')
    print('---------')

# 구구단 2단은 2*2, 3단은 3*3, 4단은 4*4...

for gugudan in range(2,10):
    for gugudan1 in range(1,gugudan+1):
        print(f'{gugudan}x{gugudan1} = {gugudan*gugudan1}')
    print('---------')

for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan} x {n} = {dan * n}')
        if dan ==n:
            break #break가 포함된 가장 가까운 반복문을 종료
    print('---------')

for i in range(1,10):
    if i == 5:
        continue
    print(i, end=' ')
print()

