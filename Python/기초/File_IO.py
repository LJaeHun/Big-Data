###############   File I/O 파일 입출력   ###############
# 파일 만들기
#     ↓열때, 만들때 둘다 씀
f = open('newfile.txt', 'w')
data = 'Good'
f.write(data)
f.close()



# ↓ f.close 생략
with open('newfile.txt', 'w') as f:
    data = 'Good'
    f.write(data)



f = open('newfile.txt', 'w')
for i in range(1, 11):
    data = f'{i}번째 줄입니다. \n'
    f.write(data)
f.close()



with open('new.txt', 'w') as f:
    for i in range(1, 11):
        data = f'{i}번째 줄입니다. \n'
        f.write(data)



# 파일 이름은 'test.txt'
# 내용은 '안녕하세요'인 파일 만들기
with open('test.txt', 'w') as f:
    data = '안녕하세요'
    f.write(data)



# 파일 이름은 'test.txt'
# 내용은 '좋은 아침입니다'인 파일 만들기
with open('test.txt', 'a') as f:
    data = f'\n좋은 아침입니다'
    f.write(data)



data = '''1번째 줄입니다.  
2번째 줄입니다.  
3번째 줄입니다.  
4번째 줄입니다.  
5번째 줄입니다.  
6번째 줄입니다.  
7번째 줄입니다.  
8번째 줄입니다.  
9번째 줄입니다.  
10번째 줄입니다.
''' 
with open('test.txt', 'w') as f:
    f.write(data)



# readline 읽기 # 한줄만 읽어옴
f = open('test.txt', 'r')
line = f.readline()
print(line)
f.close()



# readlines 읽기 # 모든 줄 (리스트로 묶어서)읽어옴
f = open('test.txt', 'r')
lines = f.readlines()
print(lines)
f.close()



# --------------------
#readlines 읽기 # 모든 줄 읽어옴
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end = '')
f.close()


#read()로 읽기
f = open('test.txt', 'r')
data = f.read()
print(data)
f.close()
#    ↓↓↓↓↓↓↓↓↓↓
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end = '')

with open('test.txt', 'r') as f:
    data = f.read()
    print(data)

