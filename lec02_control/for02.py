# 빈 리스트(scores)를 선언

# 난수(0 <= x <=  100) 10개를 리스트에 저장

# append 써서 비어있는 리스트에 10개의 점수 저장

# list에 저장된 시험점수 10개의 평균을 계산, 출력

# 리스트에 저장된 시험 점수 10개 중에서 최대값, 최소값을 찾아서 출력


scores = []

import numpy as np

for i in range(10):
    scores.append(np.random.randint(0,101))
print('scores',scores)


for i in range(9):
    total =sum(scores)
print(total)

print(total/10)
print()

from math import sqrt
print(sqrt(total))
print(max(scores))
print(min(scores))

#리스트에 저장된 시험 점수 10개의 평균을 계산, 출력
avg = total / len(scores)
print(f'평균 = {avg}')
print(f'평균2 =', np.mean(scores))

#표준편차 계산 from math import sqrt
sum_of_squares = 0
for score in scores:
    sum_of_squares += (score - avg)**2
standard_deviation = sqrt(sum_of_squares / len(scores))
print(f'표준편차 = {standard_deviation}')
print('표준편차2 =', np.std(scores))

# 최대값

max_score = scores[0]
min_score = scores[0]
for score in scores:
    if score > max_score:
        # 리스트에서 현재 최대값보다 더 큰 수를 찾은 경우
        max_score = score
    if score < min_score:
        # 리스트에서 현재 최소값보다 더 작은 수를 찾은 경우
        min_score = score
print(max_score, min_score)

sorted_scores = sorted(scores)
print(sorted_scores)
print(scores)