###############   class함수   ###############
# class = 변수(변수) + 함수(메소드)
class Calculator:
    def __init__(self, a, b):
        self.first = a
        self.second = b
        
        
    def add(self):
        self.result = self.first + self.second
        return self.result
    
    def subtract(self):
        self.result = self.first - self.second
        return self.result

    def multiply(self):
        self.result = self.first * self.second
        return self.result
    
    def divide(self):
        self.result = self.first / self.second
        return self.result
# ↙인스턴스?
cal = Calculator(2, 3)
cal.first # 인스턴스 변수?
cal.second # 인스턴스 변수?
cal.add()
call.subtract()
# ↓
# ↓
# ↓상속

class Inherit(Calculator):
    def power(self):
        self.result = self.first ** self.second
        return self.result
    
    def divide(self):
        if self.second == 0:
            return 1
        else:
            self.result = self.first / self.second
            return self.result
cal4 = Inherit(3, 0)
cal4.power()
cal4.add()
cal4.substract()
cal4.multiply()
cal4.divide()
#     ↑ 자식 클래스에 부모 클래스에 있던 것을 만들면
#       overriding덮어쓰기 함





class Family:
    lastname = '김' # field 클래스 변수
    
#    def __init__(self): 생성자(constructor)
#        pass
    
    def greet(self):
        self.name = '길동' # method 인스턴스 변수
        return 'Hello'



