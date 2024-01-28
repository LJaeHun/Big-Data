# a, b 거듭제곱 함수
def asd(a, b):
    return a ** b
asd(2, 10)



# a의 b 거듭제곱 람다함수
(lambda a, b : a ** b)(2, 10)


# num = int(input('숫자를 입력하세요:    '))

# 1부터 입력받은 수까지 출력
for i in range(1, 11):
    print(i)

# 1부터 10까지 짝수만 화면에 출력
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in range(2, 11, 2):
        print(i)

li = [i for i in range(1, 11) if i % 2 == 0]

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        print(i)

# 1부터 10까지 합 화면에 출력
i = 1
sum = 0
while True:
    if i < 10:
        sum += i
        i += 1
    else:
        break
print(sum)



# 1부터 1000까지 n의 배수들의 합을 구하는 함수 출력
# ............................
def my_sum(n):
    sum = 0
    for i in range(1, 1001):
        if i % n == 0:
            sum += i
        return sum
my_sum(5)
print(sum)



# 1부터 10까지 3의 배수만 출력
li = [i for i in range(1, 10) if i % 3 == 0]

li = []
for i in range(1, 10):
    if i % 3 == 0:
        li.append(i)



# 1부터 30까지 7의 배수를 갖는 리스트 만들기
li = []
for i in range(1, 31):
    if i % 7 == 0:
        li.append(i)

[i for i in range(1, 31) if i % 7 == 0]



# 여러개를 입력받아 입력받은 모든 수의 합을 구하는 함수 만들기
def my_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
        
my_sum(1, 2, 3, 4, 5)

# 여러개를 입력받아 입력받은 모든 수의 평균을 구하는 함수 만들기
def my_avg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)
my_avg(1, 2, 3)



# 다음 리스트에서 문자열의 길이 숫자 출력
Fruit = ['apple', 'banana', 'cherry', 'strawberry']
for i in Fruit:
    print(len(i))

li = [len(i) for i in Fruit]