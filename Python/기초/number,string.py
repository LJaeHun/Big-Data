###############   숫자형   ###############
# 정수 : integer = int
# 실수(소수) : floating = float

# 8진수 octal
0o11 # = 9

# 16진수 hexadecimal
0x11 # = 17
0xa # = 10
0xf # = 15
0x1f # = 31
0x2f # = 47
0xff # = 255
0xfff # 15*16*16 + 15*16 + 15 = 4095

# #000000 색상코드(검정)

# ** = 제곱
2 ** 3 # 8

# % = 나머지
15 % 3 # 0
15 % 2 # 1

# // = 몫
15 // 2 # 7





###############   문자열   ###############
# 문자 : string = str
print('Hello')
print('He says, "I love you."')
print('Life is too short.\nYou need python') # \n = 줄바꿈
print('Life is too short.\t \tYou need python') # \t = tab(탭)
print('''Life is too short.
      You need python
                 -Guido''')
print('Hello' + 'Good Morning') # HelloGood Morning



# 문자열 덧셈
# str은 str과 합칠 수 있음
a = 'Hello'
b = '\tGood Morning'
print(a + b) # Hello   Good Morning

# 문자열 곱셈
# str의 곱셈은 횟수 반복
print('adc' * 3) # adcadcadc
