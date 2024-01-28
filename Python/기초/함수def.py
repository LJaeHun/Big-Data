###############   def함수   ###############
'''
def 함수이름(, , , .....):
    작동...

    return...
'''
def multiply(x):
    y = 2*x
    return y
multiply(3)



# 입력된 수의 3을 더하고 10거듭제곱을 한 수 5로 나눈 나머지를 구하는 함수
def asd(x):
    y = (x + 3)**10 % 5
    return y
asd(2)



# 입력값 두개를 받아서 더하여 출력하는 이름이 add인 함수
def add(x, y):
    return(x + y)
add(2, 3)



def test():
    print('Hello')
test()



def add(*x, y, z):
    return (x ** y) + z
add(2, 3, 4)



#         ↓변수에 *붙으면 리스트(?)로 받음
def add(*args): # arguments
    for i in args:
        print(i)
add(2, 3, 4)
add(2, 3)
add(2)
[2, 3]



# 입력되는 모든 수의 합을 구하는 함수
def asd(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
asd(2, 3)
asd(2, 3, 4)
asd(2, 3, 4, 5)



#                   ↓keyward arguments
def print_kwargs(**kwargs):
    result = kwargs
    return result
print_kwargs(apple = '사과', banana = '바나나')



def add_multiply(a, b):
    result1 = a + b
    result2 = a * b
    return result1, result2
add_multiply(10, 20)



def add_multiply(a, b):
    if a > b:
        result = a + b
        return result
    else:
        result = a * b
        return result
add_multiply(1, 2)
add_multiply(3, 2)



def test_return(a, b):
    result = a + b
    return(result)
x = test_return(10, 20)
print(x + 10)



result = 10
def test():
    return 20

def test():
    a = result + 20
    return a



a = 10
def test(x):
    a = x
    return a
test(1)



a = 10
def test(x):
    b = a + x
    return b
test(1)



a = 10
def test(x):
    global a
    a = a + x
    return a
test(1)


