# 함수 정의
def test(x,y):
    print(f'x = {x} , y = {y}')
    return x + y, x - y


# 함수 호출
# test() # 실행중에 Type Error 발생
# 파이썬은 함수의 파라미터 타입은 검사하지 않지만,
# 파라미터 갯수는 검사함.
# positional argument : 함수를 호출할 때 전달하는 값(argument)들이
# 함수 정의에 선언된 파라미터 순서대로 전달되는 방식
plus, minus = test(1,2)
plus, minus = test(2,1)

# keyword argument: 함수를 호출할 때 , argument를
# 파라미터 = 값 형식으로 전달하는 방식
# keyowrd argument를 사용하면 함수에 정의된 파라미터 순서와
# 상관없이 argument를 사용 할 수 있따.
plus, minus = test(x = 10, y = 20)
print(minus)
plus,minus = test(x = 10, y = 20)
print(minus)

# default arhument : 함수를 정의할 때
# 파라미터의 기본값을 설정하는 것
def show_msg(msg: str, times: int = 1) -> None:
    print(msg * times)

show_msg('졸리세요?',5)
show_msg('개졸려요 ',3)

# default argument를 갖는 파라미터는 non-default argument 파라미터가 선언된 뒤에 선언해야함
# def test2(x = 1, y):
#     return x + y
