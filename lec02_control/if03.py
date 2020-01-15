'''
가위(1)/바위(2)/보(3)
'''

print('가위 바위 보 게임')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('---------------')
print('선택>>')

user = int(input())

import numpy as np

computer = np.random.randint(1,4) # 1 <= com < 4 난수
print(computer)


if user == computer:
    print('Draw')
elif user == 1 and computer ==2:
    print('Computer win')
elif user == 2 and computer ==3:
    print('Computer win')
elif user == 3 and computer ==2:
    print('User win')
elif user == 3 and computer ==1:
    print('Computer win')
elif user == 1 and computer ==3:
    print('User win')
else:
    print('User win')

result = user - computer
if result ==0: # 비김
    pass
elif result == 1 or result == -2: # user
    pass
else:
    pass

