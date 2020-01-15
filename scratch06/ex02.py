'''
사건의 종속성 vs 독립성
사건 A의 발생 여부 사건 B의 발생 여부에 대한 정보를 제공한다면,
사건 A와 사건 B는 종속 사건(dependent event)
사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면,
사건 A와 사건 B는 독립 사건(independent event).

동전 2개를 던지는 경우,
A: 첫번째 동전이 앞면
B: 두번째 동전이 뒷면
C: 두 동전 모두 뒷면
A와 B는 독립 사건.
A와 C는 종속 사건.

P(A): 사건 A가 일어날 확률
P(B): 사건 B가 일어날 확률
P(A,B): 사건A와 사건 B의 교집합이 일어날 확률

P(A,B) = P(A) * P(B)이 성립하면, 두 사건은 독립 사건.

'''

# 자녀가 2명인 경우,
# A: 첫째가 딸인 경우
# B: 둘째가 아들인 경우
# C: 둘 다 딸인 경우
# A와 B가 독립사건, A와 C는 종속사건임을 증명
# P(A), P(B), P(C), P(A,B), P(A,C)

import random
from collections import Counter
def experiment(type,n, t):
    '''

    :param type: 실험 타입(동전 던지기 or 주사위 던지기,...)
    :param n: 동전 or 주사위의 갯수
    :param t: 실험 횟수
    :return: 리스트
    '''
    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(t):  # 실험 횟수만큼 반복
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):  # 동전 갯수만큼 반복
            rand = random.choice(type)  # 'H' or 'T'
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 tuple로 변환 후 저장
        # Counter 클래스는 tuple의 갯수는 셀 수 있지만,
        # list의 갯수는 셀 수 없음!
        cases.append(tuple(case))
    return cases

def first_daughter(x):
    counter = Counter(x)
    return Counter['D']

children =['D','S']
house_count =10_000
daughter,son = 0,0
# for _ in range(house_count):
#     random_childeren = random.choice(children)
#     if random_childeren =='D':
#         daughter +=1
#     else:
#         son +=1
# p_a = daughter/house_count
# p_b = son/house_count

children_exp = experiment(children,2,10_000)
print(children_exp[0:10])
child_event_counts = Counter(children_exp)
num_of_cases = 0
for ev,cnt in child_event_counts.items():
    if first_daughter(ev) =='D':
        num_of_cases +=cnt
p_a =num_of_cases / house_count
print(' 첫째가 딸일 확률) =',p_a)
