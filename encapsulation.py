class test :

    def __init__(self, a, b):
        self.a = a
        self.b = b

t = test(3,4)
# b=t.a=554
# print(b)
# we can also write it as
t.a=554
print(t.a)


class car:
    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0

    def set_speed(self, speed):
        self.__speed = 0 if speed < 0 else speed

    def get_speed(self):
        return self.__speed
c = car(2021,'toyota','inova',12)
b=c._car__year
print(b)

d = c.set_speed(45)
e=c.get_speed() # here i have wasted much time in simple error i have used e=get_speed() instead of e=c.get_speed(). i missed c
print(e)
# print(c.get_speed())

class bank_account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True    
        else:
            return False
        
    def get_balance(self):
        return self.__balance
    
mohit = bank_account(5000)
# mohit.get_balance()
print(mohit.get_balance())

mohit.deposit(50000)
print(mohit.get_balance())

mohit.withdraw(100)
# print(mohit.withdraw(1000)) // here we can check true or false 
print(mohit.get_balance())
