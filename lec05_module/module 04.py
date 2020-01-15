'''
module04.py
'''

# utils 패키지 안에 있는 mymath1,mymath2 모듈을 사용
# from 패키지 import 모듈을 사용하면 각각의 모듈과 함수를 사용 할 수 있음
from utils import mymath1
from utils import mymath2

print(mymath1.pi)
print(mymath2.divide(10,20))