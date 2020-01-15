'''
Python에서 True/False 판별
1) 숫자 타입인 경우 0은 False, 0 이외의 숫자는 True취 급
2) 숫자 이외의 타입인 경우,
비어있는 값 ('','',[],{}, ...)은 False 취급
그 이외의 다른 값들은 True 취급
'''


n = 3
if n % 2:
    print('홀수')
else:
    print('짝수')
# n을 2로 나누었을 때 값이 0이니까 0은 False이다,
# Flase이면 if문에서 else를 실행하기때문에 '짝수'

my_list = ['r'] # 비어 있는 리스트(empty list)
if my_list:
    print(my_list)
else:
    my_list.append('Python')
    print(my_list)

# in 연산자
# 변수 in list / tuple/ dictionary/...

languages = ['PL/SQL','R']
if 'Python' in languages:
    pass # 아무 일도 하지 않고 지나감
else:
    languages.append('Python')
print(languages)

lang = ['python','pl/sql','r']
if 'Python' not in lang:
    lang.append('Python')
print(lang)
