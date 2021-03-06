'''
list: 여러개의 값들을 하나으 ㅣ변수에 저장하기 위한 데이터 타입
원소(element): 리스트에 저장된 값
인덱스(index): 리스트에 값이 저장된 위치 번호
리스트 원소들을 변경(추가/삭제) 가능함(mutable).
'''

numbers = [1,2,3,4,5]
print(numbers)
print(numbers[0])
# print(numbers[5]) # 리스트의 마지막 인덱스 = 리스트 길이 -1
print(numbers[0:3]) # 범위 연산자를 사용한 slicing

# 배열에 저장된 값(월소)을 변경
numbers[0] = 100
print(numbers)

#배열에 원소 추가
numbers.append(6)
print(numbers)

numbers.extend([7,8,9])
print(numbers)

#append와 extend 비교
numbers.append([7,8,9])
print(numbers)

# append는 원소 하나를 추가하는 것이고 [7,8,9]를 하나의 원소라고 생각한다

# 원소 삭제
numbers.remove(100) # 원소의 값으로 삭제
print(numbers)

del numbers[1] # 인덱스 번호의 원소 값을 삭제
print(numbers)

empty = [] #원소가 없는 빈 리스트
# 파이썬의 리스트는 여러가지 타입의 값들을 함께 저장할 수 있음.
person = ['오쌤',16,170.5,True]
print(person[0], type(person[0]))
print(person[1], type(person[1]))

# list decomposition
name, age, height, marriage = person
print(name, age, height, marriage)

# 2차원 리스트
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[0], type(matrix[0])) # matrix의 0 번째 인덱스 = [1,2,3], 그것의 타입
print(matrix[0][0]) # matrix의 0번재 인덱스의(리스트)의 0번째 인덱스 = 1
print(matrix[0][1]) # matrix의 0번재 인덱스의(리스트)의 1번째 인덱스 = 2
print(matrix[0:2])

