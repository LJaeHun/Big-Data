###############   계산기   ###############
# 객체.메소드
# 메소드 = 함수
# 객체지향 프로그래밍(Object Oriented Programming)OOP
# 클래스, object객체, instance인스턴스, method메소드
# attribute속성
'''
object = method, attribute
새 = fly(), sing(), sleep() <동사
     color, speed, size     <형용사

car = go(), run(), turn()
      owner, price, color, speen, size
'''

# 생산자 constructor

#      ↓class는 대문자로
class Pos:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result = self.result + num
        return self.result
    
    def subtract(self, num):
        self.result = self.result - num
        return self.result
        
    def multiply(self, num):
        self.result = self.result * num
        return self.result
    
    def divide(self, num):
        self.result = self.result / num
        return self.result
    
# ↙object(m1) = instance
m1 = Pos()
m1.add(100)
m1.add(200)
m1.subtract(50)
m1.divide(50)


m2 = Pos()
m2.add(1000)
m2.add(500)
m2.subtract(100)
m2.divide(100)


m3 = Pos()
m3.add(2000)
m3.multiply(3)
m3.divide(100)





result = 0
def add(num):
    global result
    result = result + num
    return result

def subtract(num):
    global result
    result = result - num
    return result
    
def multiply(num):
    global result
    result = result * num
    return result

add(100)
add(200)
subtract(50)



result1 = 0
def add1(num):
    global result1
    result1 = result1 + num
    return result1

def subtract1(num):
    global result1
    result1 = result1 - num
    return result1

def multiply1(num):
    global result1
    result1 = result1 * num
    return result1

add1(1000)
add1(500)
subtract1(100)



result2 = 0
def add2(num):
    global result2
    result2 = result2 + num
    return result2

def subtract2(num):
    global result2
    result2 = result2 - num
    return result2

def multiply2(num):
    global result2
    result2 = result2 * num
    return result2

add2(100)
subtract2(50)





###############   복습   ###############
# 클래스, 객체, 인스턴스, 메서드, 속성, OOP

class Calculator:
    def __init__(self, a, b):
        self.first = a
        self.second = b
        self.name = input('이름을 입력해 주세요:    ')

    def add(self):
        self.result = self.first + self.second
        return self.result
    
    def substract(self):
        self.result = self.first - self.second
        return self.result

cal4 = Calculator(1, 2)
cal4.substract()
cal4.add()
cal4.name
cal4.first
cal4.second



cal5 = Calculator(3, 4)
cal5.add()
cal5.substract()
cal5.first
cal5.second






cal3 = Calculator(10, 20) # __init__으로 시작하면 필수
cal3.add()
cal3.substract()



cal1 = Calculator()
cal1.setdata(10, 20)
ret = cal1.add()



cal2 = Calculator()
cal2.setdata(3, 5)
cal2.substract()





a = 'Hello'
a.__len__()

len(a)

dir(a)

b = 11
# b. int는 __len__() 사용 불가능
