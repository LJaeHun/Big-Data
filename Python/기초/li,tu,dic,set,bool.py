'''
자료형
list : 60%
tuple : 4%
dictionary : 35%
set : 1%
'''
###############   list 리스트   ###############
# [ ] : 하나로 묶음
# li = [], li = list()
a = [1, 2, 3]
print(a)

b = ['Hello', 'John', '홍길동']
print(b)

c = [1, 2, 3, '전우치']
len(c) # 4
c[0] # 1
c[-1] # '전우치'
c[3][0] # '전'
c[3][1:] # '우치'



# nested list : 중첩 리스트
a = [1, 2, 3, '전우치', ['Hello', 'John', '홍길동']]
print(a)
len(a) # 5
a[4]
a[4][0] # 'Hello'
a[4][2][1:] # '길동'

a[0] = 10 # [10, 2, 3, '전우치', ['Hello', 'John', '홍길동']]
a[4][2] = '전우치' # [10, 2, 3, '전우치', ['Hello', 'John', '전우치']]



a = [1, 2, 3, 4, 'a', 'b', 'c']
a.append('d') # a리스트에 'd' 추가
a = a + ['e'] # a리스트에 'e' 추가

a = [1, 3, 4, 2]
a.sort() # 정렬 [1, 2, 3, 4]

a = [1, 3, 4, 2]
a.reverse() # 순서 거꾸로 [2, 4, 3, 1]





###############   tuple 튜플   ###############
# ()로 만든다. 읽기전용
# tu = (), tu = tuple()

a = (1, 2, 3)
a[0] # indexing
a[1:] # slicing
a[0] = 10 # 튜플 변경 불가능
del a[0] # 튜플 삭제 불가능

a = 1, 2 # 튜플이 default값임
a





###############   dictionary 딕셔너리   ###############
# dic = {}, dic = dict()
#         {key : value}
# 키로 값 접근O / 값으로 키 접근X

d = {'apple':'사과', 'banana':'바나나'}
d['apple']
d['banana']
d['사과'] # 값으로 키 접근불가능

d = {'apple':['사과', '능금', '백설공주와 관련'], 'banana':'바나나'}
d['apple'] # = d.get('apple')
d['apple'][1]
d[0] # index로 접근불가능
d['cherry'] = '체리' # 딕셔너리에 키:값 추가
d['banana'] = '빠나나' # 딕셔너리 키의 값 수정, 키는 수정 불가능
d['domado'] = '토마토'
d['tomato'] = '토마토'

del d['domado'] # 키 삭제
d.clear() # 딕셔너리 키:값 전부 삭제



d = {'apple':['사과', '능금', '백설공주와 관련'], 'banana':'바나나'}
d.keys()
d.values()
d.items()

d['cherry'] = '체리'

keys = d.keys()
for key in keys:
    print(key)

values = d.values()
for value in d.values():
    print(value)

for i, j in d.items():
    print(i)
    print(j)
    print()

for i, _ in d.items():
    print(i)
    #print(j)
    print()





###############   set 집합   ###############
# set = {}, set = set()

A = set([1, 1, 2, 2, 3]) # 순서 없음, 중복 허용안함, 중복 제거 필터로 사용되기도함
for i in A:
    print(i)
A[0] # set은 indexing 불가능, 리스트나 튜플로 변환 후 가능





###############   bool 참거짓   ###############
# bool()
# '', [], (), {}, 0, None
# 빈값, 0 거짓

