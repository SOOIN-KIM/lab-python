'''
tuple(튜플): 원소(값)들을 변경할 수 없는 리스트
'''

numbers = (1,2,3)
print(numbers)
print(numbers[0]) # 인덱스
print(numbers[0:2]) #slicing
one, two, three = numbers #decomposition
print(one, two, three)

# numbers[0] = 100
# TypeError - Tuple 타입은 값은 변경할 수 없다.
