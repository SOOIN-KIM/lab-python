import pandas as pd

if __name__ == '__main__':
    # csv 파일에서 데이터 프레임을 생성
    emp_df = pd.read_csv('emp_df.csv')
    print(emp_df.iloc[0:5])

    # 부서별 ,직책별 직원 수를 출력
    grouped = emp_df.groupby(['DEPTNO','JOB'])
    emp_by_dept = grouped['EMPNO']
    result_df = emp_by_dept.count()
    print(result_df)

    unstacked = result_df.unstack()
    print(unstacked)

    # grouping 기준이 되는 컬럼의 값들이 index(행의 이름) 으로 사용되지 않고,
    # 컬럼으로 사용하려면,
    grouped = emp_df.groupby('DEPTNO', as_index= False)
    print(grouped['EMPNO'].count())

    grouped = emp_df.groupby(['DEPTNO','JOB'], as_index=False)
    print(grouped['EMPNO'].count())