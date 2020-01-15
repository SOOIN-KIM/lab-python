'''
emp.csv 파일을 읽어서 , DataFrame을 생성
 -급여 (sal)가 2000이상인 직원들의 모든 정보를 출력(boolean indexing 사용해서_)
 -부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
 -급여가 전체직원의 평균보다 높은 직원들의 사번, 이름, 급여를 출력
 -30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
 -20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호를 출력
 -수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 "CLERK'인 직원들의 모든 정보를 검색
 -사원 이름에 'E'가 포함된 직원들의 이름만 출력(str.contains() 이용)
 -DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서, 데이터 프레임을 파일로 저장
'''
import pandas as pd
from pandas import DataFrame
from pandas import Series

emp = pd.read_csv('emp.csv')
emp.columns = ['empno','ename','job','mrg','date','sal','comm','deptno']

#1)
print(emp[emp['sal'] >= 2000])
print('--------------------------------------------------------------------------------------------------------------')
#2)
print(emp[emp['deptno'] ==10])
print('--------------------------------------------------------------------------------------------------------------')
#3)
sal_mean = emp['sal'].mean()
emp_no_name_sal = emp[['empno','ename','sal']]
print(emp_no_name_sal[emp['sal'] >= sal_mean])