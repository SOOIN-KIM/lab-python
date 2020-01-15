def user_input():
    '''
    사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 안내.
    사용자가 입력한 숫자를 리턴.
    사용자가 숫자로 변환할 수 없는 문자를 입력하면, 안내문 출력 후 다시 입력받음.
    사용자가 1, 2, 3 이외의 숫자를 입력하면, 안내문 출력후 다시 입력

    :return: 1,2,3 중하나
    '''

    while True:
        try:
            num = int(input('숫자를 입력>>'))
            if num > 3 :
                raise ValueError('1, 2, 3 중의 숫자를 입력하세요')
            elif num < 0 :
                raise ValueError('1, 2, 3 중의 숫자를 입력하세요')
            print('입력한 숫자 :', num)
            break
        except ValueError as v:
            print(v.args)
    return num

user = user_input()
print(' 입력 값',user)


