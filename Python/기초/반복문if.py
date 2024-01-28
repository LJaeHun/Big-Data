###############   if문   ###############
'''
if 조건:
    실행할 문장



if 조건:
    실행할 문장
else:
    실행할 문장



if 조건:
    실행할 문장
elif:
    실행할 문장
else:
    실행할 문장

조건
A in B
A not in B
'''

'''
for member in members:
    print(member)

for '홍길동' in members:
    print('네 그렇습니다')
'''
members = ['홍길동', '전우치', '이순신']
name = '홍길동'
if name in members:
    print('네 그렇습니다')
else:
    print('아니오')

bool('홍길동' in members)



# 이름을 입력받아서, 있으면 '합격입니다', 그외 '불합격입니다'
합격자명단 = ['박', '김', '최', '이', '정']
put = input('이름을 입력하세요:    ')
if put in 합격자명단:
    print('합격입니다')
else:
    print('불합격입니다')



money = 2000
card = True
if money > 3000 or card: # | = or
    print('택시 타')
else:
    print('걸어가')

if money > 3000 and card: # & = and
    print('택시 타')
else:
    print('걸어가')



score = 50
if score >= 60:
    message = 'sucess'
else:
    message = 'failure'
print(message)

score = 70
message = 'sucess' if score >= 60 else 'failure'



pocket = ['card', 'bill', 'coin']
if 'card' in pocket:
    print('택시 타')
elif 'bill' in pocket:
    print('버스 타')
elif 'coin' in pocket:
    print('버스 타')
else:
    print('걸어가')
