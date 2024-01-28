###############   재귀함수   ###############
def hello():
    print('Hello')
hello()

# 무한반복
def hello():
    print('Hello')
    hello()
hello()



import time

count = 1

def hello():
    global count
    print(count)
    print('Hello')
    time.sleep(1)
    print('Good')
    count += 1
    hello()
hello()



# 5번 출력하고 멈춤
def hello(count):
    if count == 0:
        return 
    print(count)
    print('Hello')
    time.sleep(1)
    print('Good')
    count -= 1
    hello(count)
hello(0)





# factorial 구하기
def factorial(n):
    if n == 1:
        return 1
    # n * (n - 1) * (n -2)...
    return n * factorial(n - 1)

factorial(3)
  


# 피보나치 수열 구하기
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

fib(4)

