'''
반복문 연습
'''

# shift+F6(shift+Fn+F6): refactor / rename

# 1+2+3+...+100 = ?

total=0
for i in range(1,101):
    total = total +i
print(total)


# 1+ 2+ 3+ ... + x <= 100

total = 0
x = 1
while True:
    total+= x
    print(f'x= {x}, sum = {total}')
    if total > 100:
        break
    x +=1

total, x = 0, 1
while total <= 100:
    total += x
    print(f'x={x}, sum = {total}')
    x +=1