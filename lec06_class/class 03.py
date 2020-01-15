'''
클래스 작성, 객체 생성, 메소드 사용 연습
'''

class Employee:
    '''
    field: empno, ename, salary, deptno
    method : raise salary(self, pct)
    '''
    def __init__(self,empno, ename, salary, deptno):
        self.empno = empno
        self.ename = ename
        self.salary = salary
        self.deptno = deptno

    def raise_salry(self,pct):
        self.salary = (1 + pct) * self.salary
        return self.salary

    def __repr__(self):
        return f'(사번: {self.empno}, 이름 : {self.ename}, 급여: {self.salary}, 부서번호{self.deptno})'


gil_dong = Employee(1010,'홍길동',1000,10)
print(gil_dong.__repr__())
gil_dong.raise_salry(0.1)
print(gil_dong.__repr__())

scott = Employee(1011, 'Scott',10000,20)
print(scott.__repr__())
scott.raise_salry(-0.1)
print(scott.__repr__())

ohssam = Employee(1012,'오쌤',500,30)

employees = [ohssam,gil_dong, scott]
print(employees)
print(sorted(employees,key=lambda x: x.empno))
print(sorted(employees,key=lambda x: x.salary))
print(sorted(employees,key=lambda x: x.ename))
print(sorted(employees,key=lambda x: x.deptno))


