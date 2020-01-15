def say_myself(name, old, man= True):
    print('나의 이름은 %s 입니다.' %name)
    print('나이는 %d살 입니다.' %old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('박응용',27)
say_myself('박응용',27, True)

# vartest.py
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

def vartest(hello):
    hello = hello + 1

# vartest_error.py
def vartest(a):
    a = a +1

vartest(3)
print(a)

a = 1
def vartest(a):
    a = a+1
    return a

b = vartest(3)
print(b)

add = lambda a, b : a+b
result = add(3,4)
print(result)

def add(a,b):
    return a + b

result = add(3,4)
print(result)

