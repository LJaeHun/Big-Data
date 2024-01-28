###############   while반복문   ###############
'''
while 조건:
    실행할 문장
'''
i = 0
while i < 5:
    i += 1
    print(i)



count = 0
sum = 0
while count < 100:
    count += 1
    sum += count
print(sum)



i = 0
sum = 0
while sum < 1000:
    i += 1
    sum += i
    if sum > 500:
        break
print(sum)



while 1 < 2:
    print('Hello')
    print('Good Morning')
    print('Good Evening')

while True: # 무한루프





for i in range(1, 11):
    if i % 3 != 0:
        print(i)



for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)



i = 0
while i < 10:
    i += 1
    if i % 3 != 0:
        print(i)



i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)



i = 1
while True:
    if i % 3 != 0:
        print(i)
    i += 1
    if i > 10:
        break




