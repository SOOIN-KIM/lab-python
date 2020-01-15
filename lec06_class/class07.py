class Account:
    '''은행 계좌 클래스
    field(데이터) : 계좌번호(accountno),잔액(balance)
    metohod(기능) : 입금(deposit), 출금(withdraw), 이체(transfer)
    '''
    def __init__(self,accountno,balance):
        self.accoutno = accountno
        self.balance = balance
        try:
            temp = balance + 1
        except Exception:
            raise TypeError

    def __repr__(self): #string 을 return 하는 함수
         return f'Account(account no.: {self.accoutno},balance: {self.balance})'

    def deposit(self,money):
        self.balance += money
        print(f'{money} 입금 후 잔액:{self.balance}')

    def withdraw(self,money):
        self.balance -= money
        print(f'{money} 출금 후 잔액:{self.balance}')

    def transfer(self,to,money):
        '''
        계좌 이체 기능. 내 계좌에서 money를 출금해서 상대방(to)계좌에 입금

        :param to: 이체할 상대방 계좌(Account 클래스 객체)
        :param money: 이체할 금액(숫자)
        :return: None
        '''
        self.withdraw(money) #내 계좌에서 출금
        to.deposit(money) # 상대방 계좌에 입금

if __name__=='__main__':
    account1 = Account(123456,1000)
    print(account1)
    account1.deposit(500)
    account1.withdraw(100)

    account2 = Account(45678900,100)
    account1.transfer(account2,500)

    print(account1)
    print(account2)
