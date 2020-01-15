'''
클래스 작성, 테스트
'''
class Point:
    '''
    2차원(x ,y) 평면 상의 점 1개를 저장할 수 있는 클래스
    '''

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_point(self):
        '''
        Point 객체가 가지고 있는 점의 좌표를(x,y) 형식으로 출력하는 메소드

        :return: None
        '''
        print(self.x,self.y)


    def distance(self, other):
        '''
        두 점 사이의 거리를 계산해서 리턴하는 함수

        :param other: Point 객체
        :return: self와 other 사이의 거리
        '''

        return sqrt((self.x - other.x) **2 + (self.y - other.y)**2)

