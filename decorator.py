# decorator function is used to call or print the same thing at diffrent times
# like if we have to print (start and end point of code) in every program we can directly call the decoretor function there with @ decorator.

def test():
    print ('this is start of my code')
    print(2+2)
    print('this is end of my code')
# instead of writing start and end position in every function we can make a function and call it.
    
def deco(func):
    def inner_dec():
        print('this is start of my code')
        func()
        print('this is end of my code')
    return inner_dec

@deco
def test1():
    print(2+2)

test1()

@deco
def mohit():
    print(8+8)
mohit()

# Program for calucating the time taken by program to run using decorator and time function
import time

def timer_test(func):
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return timer_test_inner

@timer_test
@deco
def test2():
    print(2000000054844894800000000**9)
test2()

@timer_test
def test3():
    for i in range (100000000):
        pass
test3()