###############   for반복문   ###############
members = [1, 2, 3, 4, 5, 6]
for member in members:
    print(member)
    print(member * 10)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)



# range(start, stop, step)
list(range(10))
list(range(1, 11, 2)) # 1~10 2개씩 
list(range(2, 11, 3)) # 1~10 3개씩 



# --------------------
# append()와 for반복문 사용해서 li 리스트에 [2, 4, 6, 8, 10]이 있도록 만들기.
li = []
for i in range(2, 11, 2):
    li.append(i)
    print(li)



li = list()
for i in [1, 2, 'Hello']:
    li.append(i*2)
print(li)



marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark > 60:
        print(f'{number}번 학생은 합격입니다')
    else:
        print(f'{number}번 학생은 불합격입니다')



# continue
for i in range(1, 11):
    if i % 2 == 0:# 나머지가 0이면 전단계 반복
        continue
    print(i)

# pass
for i in range(1, 11):
    if i % 2 == 0:# 나머지가 0이여도 다음단계
        pass
    print(i)



scores = [90, 25, 67, 45, 80]
sum = 0
avg = 0
for i in scores:
    sum += i
#    print(sum)
avg = sum / len(scores)

print(f'총합은 {sum}입니다')
print(f'평균은 {avg}입니다')



# 구구단 2단
for i in range(2, 3):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')

# 구구단
for i in range(2, 10):
    print(f'{i}단 입니다')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print()



for i in range(3):
    print(i, end = ' ')

