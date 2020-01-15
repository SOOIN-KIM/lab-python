'''
클래스 = 데이터(필드,field) + 기능(method) => 데이터 타입
'''

class Score:
    # 생성자가 호출되었을때 field들을 초기화 하는 함수를 만듦(__init__)
    def __init__(self,korean,english,math):
        self.korean = korean #내가가지고있는(self).korean으로받음 점수를 저장함
        self.english = english
        self.math = math

    def calc_total(self):
        return self.korean + self.english + self.math

    def calc_average(self):
        return self.calc_total() / 3

# Scroe 클래스의 객체를 생성
score1 = Score(99,88,77) # 생성자 호출
score1.math = 79
print(score1.calc_total())
print(score1.calc_average())

score2 = Score(90,85,70)
print(score2.calc_total())
print(score2.calc_average())