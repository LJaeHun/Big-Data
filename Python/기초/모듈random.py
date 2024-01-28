
import random
import math
a = random.random()
0 <= a < 1
0  * 6 + 1 <= a * 6 + 1 < 1 * 6 + 1

math.floor(a * 6 + 1)
math.floor(random.random() * 6 + 1)

random.seed(1234)
random.randint(1, 6)



# 주사위 3번 던져서 나온 3개의 수는?
li = []
random.seed(1234)
for i in range(3):
    num : random.randint(1, 6)
    li.append(num)
print(li)
# ↓
# lambda
# ↓
li = [random.randint(1, 6) for i in range(3)]

random.sample(range(1, 7), 3)

