# 1 부터 n 까지의 숫자들의 합을 리턴하는 함수
# 1 + 2 + 3 + ...+ n
def sum_total(*values):
    result = 0
    for n in values:
        result += n
    return result

print(sum_total(1,2,3,4,5))

#1. 선생님코드
def sum_to_n(n:int) -> int:
    return n * (n+1) /2

result = sum_to_n(50)
print(result)
#2. 선생님 코드
def sum_to_n3(n:int) -> int:
    numbers = [x for x in range(1, n +1)]
    print(numbers)
    return sum(numbers)

result = sum_to_n3(9)


# 1부터 n 까지 숫자들의 제곱의 합을 리턴하는 함수
# 1**2 + 2**2 + 3**2+...+n**2

def square_sum(*values):
    result = 0
    for n in values:
        result = result+(n**2)
    return result

print(square_sum(1,2,3,4,5,6,7,8))

#1. 선생님 코드
def sum_to_squares(n:int) -> float:
    return n * (n +1) * (2*n + 1) / 6

#2. 선생님 코드2
def sum_to_squres2(n:int) -> int:
    _sum = 0
    for x in range(1, n +1):
        _sum += x ** 2
    return _sum
print(sum_to_squres2(8))

# 숫자들의 리스트를 전달 받아서 최댓값을 찾아서 리턴하는 함수

def find_maximum(numbers:list) -> float:
    maxValue = my_list[0]
    for i in range(1,len(my_list)):
        if maxValue < my_list[i]:
            maxValue = my_list[i]
    return maxValue

my_list=[1,23,56,6,213,123,12,321,321,321,5,52]
print(find_maximum(my_list))

# 1. 선생님 코드
def find_max(values:list) -> float:
    # return max(values)
    _max = values[0]
    for x in values:
        if x > _max:
            _max = x
    return _max

numbers = [1,23,56,6,213,123,12,321,321,321,5,52]
print(find_max(numbers))

# 2. 선생님 코드 2번
def find_max2(values: list) -> float:
    # sorted(list) : list를 정렬한 새로운 리스트 리턴
    # 원본 리스트(list)는 순서가 그대로 유지됨
    # list.sort(): 원본 리스트를 정렬해서 순서를 바꿈.
    # None을 리턴함(값을 리턴하지 않음)
    sorted_values = sorted(values,reverse = True)
    print('values :', values)
    print('sorted_values:', sorted_values)
    values.sort()
    print('values:', values)

print(find_max2(numbers))




# 숫자들의 리스트를 전달받아서 최댓값의 인덱스를 리턴하는 함수

def find_maxindex(numbers):
    maxindex = 0
    for n in numbers:
        if find_maximum(numbers) == n:
            return maxindex
        maxindex = maxindex + 1

my_list=[1,23,56,6,213,123,12,321,321,321,5,52]
print(find_maxindex(my_list))

# 1. 선생님코드
def find_max_index(values: list) -> float:
    max_id, max_val = 0, values[0]
    for i, v in enumerate(values):
        print(f'i = {i}, v= {v}')
        if v > max_val:
            max_id, max_val = i, v
    return max_id

numbers = [1,23,56,6,213,123,12,321,321,321,5,52]
print(find_max_index(numbers))
# 2. 선생님 코드
def find_max_index2(values):
    _max = values[0]
    max_id = 0
    for i in range(1, len(values)):
        if values[i] > _max:
            _max = values[i]
            max_id = i
    return max_id
numbers = [1,23,56,6,213,123,12,321,321,321,5,52]
print(find_max_index2(numbers))

# 3. 선생님 코드

def find_max_index3(values):
    max_id, _max = 0, values[0]
    idx = 0
    for x in values:
        if x > _max:
            max_id, _max = idx, x
        idx += 1
    return max_id






# 숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수
# 오름차순 정렬 알고리즘 함수 만들기
def sort_algo(numbers):
    index_num = my_list[0]
    print(index_num)
    for n in numbers:
        if index_num < n:
            return index_num
    index_num = index_num + 1

my_list = [4,5,1,3,2]
print(sort_algo(my_list))

#1. 선생님 코드

def median:
    #리스트를 정렬(내림차순)
    sorted_values = sorted(values)
    length = len(sorted_values) # 리스트의 크기
    mid = length // 2 # 리스트의 중간 위치
    if length % 2: # 리스트의 원소 개수가 홀수인 경우
        median = sorted_values[mid]
    else: # 리스트의 원소의 개수가 짝수인 경우
        left = mid - 1
        median_value = (sorted_values[left]+sorted_values[mid]) / 2
    return median_value
