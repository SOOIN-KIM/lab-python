# try :
#     age = int(input('나이를 입력>>'))
#     if age < 0:
#         raise ValueError('나이는 0 또는 양의 정수여야 합니다!')
#     print('입력한 나이:' ,age)
# except ValueError:
#     print(e.args)
#
def user_input():
    while True:
        n = int(input('숫자를 입력 하세요>>'))
        if n > 3:
            raise ValueError('1,2,3 중에 숫자하나를 입력하세요')
        elif n < 0:
            raise ValueError('1,2,3 중에 숫자하나를 입력하세요')
        print('입력한 숫자 :', n)
        break
    except ValueError as v:
        print(v.args)
    return n


# 학생 5명의 성적을 국어 영어 수학 과학 0~100 사이의 점수를 랜덤하게 입력

