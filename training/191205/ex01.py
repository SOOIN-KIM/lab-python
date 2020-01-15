import pandas as pd
import cx_Oracle
from scratch09.ex10 import get_column_names_of
from scratch09.ex10 import select_all_from
import csv


def peak_to_peak(x):
    return x.max() - x.min()


if __name__ == '__main__':
    # with - as 구문을 사용해서 오라클 DB서버에 접속
    # with-as 구문을 사용해서 Cursor 객체를 생성
    # scratch 09 패키지에서 작성한 테이블 전체 검색 함수를 사용해서,
    # emp_df, dept_df 데이터 프레임을 생성
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        with connection.cursor() as cursor:
            emp_columns = get_column_names_of('emp', cursor)
            emp_df = select_all_from('emp', cursor)
            dept_df = select_all_from('DEPT', cursor)
            # emp_df를 csv 파일로 저장
            # emp_df.to_csv('emp_df.csv')

            # emp_df 에서 부서별 평균 급여를 출력( groupby 를 deptno)
            group_by_deptno = emp_df.groupby('DEPTNO')
            group_by_deptno_sal = group_by_deptno['SAL']
            print(group_by_deptno_sal.mean())

            # emp_df 에서 부서별 인원수를 출력
            group_by_deptno_cnt = group_by_deptno['SAL']
            print(group_by_deptno_cnt.count())

            # emp_df에서 부서별 급여 최소값 출력
            print(group_by_deptno_sal.min())

            # emp_df에서 부서별 급여 최대값 출력
            print(group_by_deptno_sal.max())

            # 위에 결과를 하나의 데이터 프레임으로 출력
            df = pd.DataFrame({
                'count' : group_by_deptno_cnt,
                'mean' : group_by_deptno.mean(),
                'min' : group_by_deptno_sal.min(),
                'max' : group_by_deptno_sal.max(),
            })
            print(df)

            # agg(), aggregate() :파라미터에 함수 이름( 또는 리스트)를 전달하면
            # GroupBy 객체에 함수를 적용한다
            # 함수가 집계 함수(pandas.Series 또는 pandas.DataFrame 클래스가
            # 가지고 있는 메소드들 :count, mean, sum,...)인 경우에는 함수이름을 문자열로 전달함.
            # 개발자가 작성한 함수는 함수이름을 파라미터로 전달해야함


            # emp_df에서 직책별 직원 수, 급여 평균 최소,최대 값을 출력

            # agg() 함수가 만드는 DataFrame의 컬럼 이름을 설정할때는
            # keyword-arguement 방식 또는 dict를 파라미터로 전달함.


            # emp_df에서 부서별, 직책별 직원 수 ,급여평균, 최소,최대 값 출력

            # agg(), aggregate() 함수의 파라미터에 dict를 전달하는 방식은
            # pandas 패키지가 업그레이될 떄 없어질수 있는 기능(deprecated)
            # dict 방식보다는 keyword - arguement 방식을 사용하는 것이 안전함.







