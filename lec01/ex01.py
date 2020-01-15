'''
Block commnt(블록 주석)
'''

print('Hello, Python')
#Ctrl+Shift+F10: 파이썬 코드 실행

# 변수 사용 - 프로그램에 필요한 데이터를 저장하는 공간
# 변수 이름 = 값
age = 16
print(age)

# 파이썬의 문자열: 따옴표('') 또는 큰따옴표("") 사용
name = '김수인'
print(name)

company = '아이티월'
print(company)

str1 =  ' He said "yes!"'
print(str1)

str2 =  "I'm a boy."
print(str2)

str3 = 'I\'m a girl.'
print(str3)

'''
여러가지 print() 방법
'''
print('Hello, Phtyon')

age = 16
name = '오쌤'
print('나이:',age, ',이름 :', name)
print(f'나이: {age}, 이름: {name}') #formatted string
print('나이: {}, 이름: {}'.format(age,name))
print('나이: %d, 이름: %s' %(age,name))
# $d : 정수, %f: 실수 $s: 문자열
# digit, floating point number, string

'''
사용자입력(키보드 입력) 처리
'''

print('>>> 이름 입력:')
name = input()
print(f'name: {name}')

age = input('>>> 나이 입력:')
print(f'age: {age}')
# print(age +1) #실행 중 오류(TypeError) 발생
# Ctrl+/ : 주석 토글
