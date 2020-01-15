'''
Lec06_class\class 07.py 파일에서 정의한 Account 클래스를 사용해서
은행 어플리케이션을 생성
1) 계좌 개설
2) 입금
3) 출금
4) 이체

'''

from lec06_class.class07 import Account #lec06_class라는 파이썬 패키지에서 class07 파이썬 파일의 Account클래스를 가져온다

print('Banking Application')
# 여러 계좌들을 관리하기 위한 dict를 선언
# key: 계좌번호, value:Account 객체
accounts = {} #empty dict


while True: # 무한 루프
    print('[0] 종료')
    print('[1] 계좌 개설')
    print('[2] 입금')
    print('[3] 출금')
    print('[4] 이체')
    print('[5] 계좌 정보 출력')
    print('--------------')
    print('선택>>')
    menu = input()
    if menu == '0':
        break
    elif menu == '1': # 계좌 개설
        print('---신규 계좌 개설 화면---')
        print('계좌번호 입력>>')
        account_no = int(input())
        print('잔액 입력>>')
        money = int(input())
        accounts[account_no] = Account(account_no,money)
        print(accounts)
    elif menu == '2' : #계좌 입금
        print('---입금 화면---')
        account_no = int(input('입금 계좌 번호>>'))
        money = int(input('입금 금액>>'))
        accounts[account_no].deposit(money)
    elif menu == '3':
        print('---출금 화면---')
        account_no = int(input('출금 계좌 번호>>'))
        money = int(input('출금 금액>>'))
        accounts[account_no].withdraw(money)
    elif menu =='4':
        print('---이체 화면---')
        from_acc = int(input('내 계좌 번호 입력>>'))
        to_acc = int(input('상대방 계좌 번호 입력>>'))
        money = int(input('이체할 금액>>'))
        accounts[from_acc].transfer(accounts[to_acc],money)
    elif menu == '5':
        print('계좌 조회 화면')
        account_no = int(input('조회할 계좌 번호 >>'))
        print(accounts[account_no])
print('Banking App 종료')
