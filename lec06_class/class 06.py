from math import pi

class Circle:
    # field: 반지름(radius)
    # method:
    # __init__: 초기화(객체 생성 함수)
    # area(): 원의 넓이를 리턴
    # perimeter(): 원의 둘레 길이를 리턴
    # __str__(): 출력형태를 Circle(r=123) 형식으로 출력
    # __eq__(): 반지름이 같으면 equal(True)

    #__init__(): 초기화(객체 생성) 함수
    def __init__(self,radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError('반지름은 0또는 양수')

    # area(): 원의 럽이를 리턴
    def area(self):
        return (self.radius)**2 *pi

    def perimeter(self):
        return 2*(self.radius)* pi

    def __str__(self):
        return f'Circle(r={self.radius})'

    def __repr__(self):
        return f'원({self.radius})'

    def __eq__(self, other):
        print('__eq__ 호출')
        return self.radius == other.radius

    def __ne__(self,other): # not equal
        # != 연산자를 사용하면 자동으로 호출되는 메소드
        return  self.radius!= other.radius

    def __gt__(self,other):
        # greater than: > 연산자를 사용 하면 자동으로 호출되는 메소드
        print('__gt__ 호출')
        return self.radius > other.radius

    def __ge__(self,other):
        # greater than or equal to
        # >= 연산자를 사용하면 자동으로 호출되는 메소드
        return self.__gt__(other) or self.__eq__(other)

if __name__ == '__main__':
    c1 = Circle(1)
    print(c1)
    print('c1 area:', c1.area())
    print('c2 perimeter:', c1.perimeter())
    print('c1 id:', id(c1))

    c2 = Circle(1)
    print('c2 id:', id(c2))

    print(c1 == c2)
    print(c1!=c2)
    print(c1 > c2)
    print(c1 >= c2)
    print(c1 < c2)

Circles = [
    Circle(10),
    Circle(5),
    Circle(40),
    Circle(1),
    Circle(0)
]

print(Circles)
print(sorted(Circles, reverse =True))