# 데이터 타입 = int, float, str, bool
#              정수, 실수, 문자, 참거짓



a = 'Good Morning'
type(a)
a.capitalize() # 맨첫글자만 대문자
a.title() # 단어의 첫글자 대문자
a.count('o') # o의 갯수
a.find('o') # 첫 o의 위치(index값), 존재하지 않으면 -1 출력
a.index('o') # 첫 o의 index
a.lower() # 전부 소문자
a.upper() # 전부 대문자



a = '   Hello   '
print(a)
a.rstrip() # 오른쪽 공백삭제
a.lstrip() # 왼쪽 공백삭제
a.strip() # 공백 삭제

# 바꾸기
a.replace("Hello", 'Good morning')

# 분리
a = 'a:b:c:d'
a.split(':')

# 삽입
a = ', '
a.join('abcd')

