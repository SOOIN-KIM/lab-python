'''
ex09.py
1) emp 테이블에서 부서번호를 일력받아서, 해당부서의
직원들의 사번,이름 부서번호를 출력

2) emp 테이블에서, 사원 이름을 입력받아서,
해당 글자가 이름에 포함된 직원들의 사번, 이름, 급여를 출력
'''

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect (cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호를 입력>> '))

        sql_select = 'select empno,ename,deptno from emp where deptno = :deptno'
        cursor.execute(sql_select, deptno = deptno)
        for row in cursor:
            print(row)

        print('================')
        sql2 = '''select empno, ename, sal
        from emp 
        where lower(ename) like :keyword #데이터가 들어올자리다 명시 keyword
        '''
        name = input('검색할 이름을 입력 >> ')
        name = name.lower() # 입력한 문자열을 소문자로 변환
        name = '%' + name + '%' #like 검색

        cursor.execute(sql2, keyword = name)
        for empno, ename, sal in cursor:
            print(empno, ename, sal)