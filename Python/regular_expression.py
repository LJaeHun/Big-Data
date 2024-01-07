# ASCII > Unicode > UTF-8
# 유니코드 도입전 윈도우용 : MS949 Euc-KR CP949

# regular expression = 정규표현식
# 파이썬에서 정규표현식을 지원하는 re모듈
import re

re.findall('[abcde]', 'Attention is all need')
re.findall('[a-zA-Z]', 'Attention is all need')
re.findall('[0-6]', 'Attention is all need 007')
re.findall('[^0-6]', 'Attention is all need 007')
re.findall('\d', 'Attention is all need 0123789')
[0-9] = \d # 숫자만
[^0-9] = \D # 숫자 아닌것만



re.findall('\w', 'Attention is all need 0123789,_!@#$')
/w = alphanumeric + _
re.findall('\W', 'Attention is all need 0123789,_!@#$')
/W = alphanumeric + _ 제외



re.findall("a.l", 'test.py Attention is all need 0123789,_!@#$')
re.findall("t[.]p", 'test.py Attention is all need 0123789,_!@#$')
. = 문자 사이에 어떤 문자가 들어가도 매치됨
[.] = []안 문자로 인식



^ = caret(시작 문자) 
$ = (끝 문자)

+ = 1번 이상
? = 1번 이하
* : 0번 이상


