'''
클래스(class):
프로그램에서 만들려고 하는 대상(객체)이 가져야 할
속성(데이터)과 기능(함수)을 묶은 "데이터 타입"

메소드(method): 클래스가 가지고 있는 함수
필드(field): 클래스가 가지고 있는 데이터(변수)
'''

# TV 소프트웨어 작성
# TV 속성(데이터) : 채널, 음량, 전원
# TV 기능(함수) : 채널 변경, 음량 변경, 전원 on/off

## 과제 2-1
## TV가 꺼졌을때는 채널버튼과 음량버튼이 작동하면 안됨.
## 과제 2-2
## 채널버튼은 순환되도록 , 음량버튼은 최대값에 도달하면 작동 X

class BasicTv:
    '''

    BasicTv 클래스
    '''
    # 생성자가 호출됐을 때 실행되는 메소드
    def __init__(self,power,channel,volume):
        print('BasicTv 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume

     #  클래스 내부에서 정의하는 함수 : 메소드
    def poweronoff(self):
        if self.power: # power가 True이면(TV가 켜져 있으면)
            self.power = False
            print('TR Off')
        else : #TV가 꺼져 있으면
            self.power = True # TV를 켬
            print('TV On')

    def channelup(self):
        if self.power:
            self.channel += 1
            if self.channel > 5:
                self.channel = 0
            print('Channel:', self.channel)

    def channeldown(self):
        if self.power:
            self.channel -= 1
            if self.channel < 0:
                self.channel =5
        print('Channel:', self.channel)

    def volumeup(self):
        if self.power:
            self.volume += 1
            if self.volume > 5:
                self.volume = 5
            print('Volume:', self.volume)

    def volumedown(self):
        if self.power:
            self.volume -= 1
            if self.volume < 1:
                self.volume = 0
            print('Volume:', self.volume)

#클래스 설계(정의)

# 클래스의 객체(인스턴스)를 생성해서 변수에 저장
# 생성자(constructor) 호출 -> 하게 되면 객체(object) 생성
tv1 = BasicTv(power = False, channel =0, volume=0)
print(tv1)
print(tv1.power)
tv1.poweronoff()
tv1.channelup()







print(tv1.channel)


tv2 = BasicTv(True, 100,5)

## 과제 2-1
## TV가 꺼졌을때는 채널버튼과 음량버튼이 작동하면 안됨.
## 과제 2-2
## 채널버튼은 순환되도록 , 음량버튼은 최대값에 도달하면 작동 X
