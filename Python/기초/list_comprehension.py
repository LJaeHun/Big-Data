###############   list comprehension   ###############
li = []
for i in range(1, 11):
    li.append(i)
li = [i for i in range(1, 11)]



li = []
for i in range(1, 11):
    li.append(i * 10)
li = [i * 10 for i in range(1, 11)]



li = []
for i in range(1, 11):
    if i % 2 == 0:
        li.append(i)
li = [i for i in range(1, 11) if i % 2 == 0]



# 10부터 20까지 숫자를 list comprehension으로 만들기
li = []
for i in range(10, 21):
    if i % 2 == 0:
        li.append(i)
li = [i for i in range(10, 21) if i % 2 == 0]
li = [i for i in range(4, 101, 4) if i % 4 == 0]




