'''
module03.py
'''

#utils 패키지(폴더, 디렉토리) 안에 있는 mymath1모듈(파이썬파일)의
# 변수, 함수들을 사용
# 방법1. import 모듈이름 [as 별명이름]
# 방법2. from 모듈이름 import 변수/함수, ... [as 별명이름]
# 방법3. from 패키지이름 import 모듈이름 [as 별명이름]
# import utils.mymath1
#import를 썼을때 utils 파일안에 mymath1이라는 이름의 패키지를 실행하기때문에
#mymath1안에 명령어들이 있으면 위에서부터 한번은 실행을 함

from utils.mymath1 import pi
# import utils.mymath1
print('pi =', pi)
# print(' pi =', utils.mymath1.pi)
