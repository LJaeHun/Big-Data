###############   input()   ###############
name = input('이름을 입력해주세요:    ')
age = input('나이를 입력해주세요:    ')
print(f'나의 이름은 {name}이고, 나이는 {age}세 입니다.')



age1 = int(input('내 나이를 입력해 주세요:   '))
age2 = int(input('어머니 나이를 입력해 주세요:   '))
print(f'내 나이는 {age1}이고, 어머니 나이는 {age2}이고 나이의 합은 {age1 + age2}입니다.')



# --------------------
# for반복문을 사용해서 1부터 입력받은 값까지 출력
a = int(input('값을 입력해주세요:    '))
for i in range(1, a + 1):
    print(i)

