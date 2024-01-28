###############   formatting   ###############
print('I ate 3 apples. So I sicked two days.')
number = 3
days = 'two'

print('I ate %d apples. So I sicked %s days.' %(number, days))

# %s = 문자열(string)
# %c = 문자1개(character)
# %d = 정수(integer)
# %o = 8진수
# %x = 16진수
#. %% = %문자


###############   f-string   ###############
print(f'I ate {number} apples. So I sicked {days} days.')

pi = 3.1415926
print(f'{pi:.2f}')
print(f'{pi:10.2f}') # 8칸띄고 소수점 두번째 자리까지
print(f'원주율 값은 {pi:.2f}이다.')

#f'{pi:10.2f}' : 공백 수.소수점 자릿수f
