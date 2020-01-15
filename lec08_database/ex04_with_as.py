'''
ex04_with_as.py

with ... as 구문을 사용하면
cursor.close()와 connection.close()가 자동으로 호출됨
'''

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn: #conn이 cx_Oracle.connect이고 자동으로 connection.close가 설정되어있다
    with conn.cursor() as cursor: #coursor.close가 자동으로 설정되어 있다.
        cursor.execute('select empno, ename, deptno from emp')
        for row in cursor:
            print(row)
