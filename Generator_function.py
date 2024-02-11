a=range(1,10,3)
print(list(a))

# def generator():
#     yield "mohit"
#     yield 'kumar'
#     for i in generator():
#         print(i)
# my_generator = generator()
# print(my_generator)

def test_fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b
for i in test_fib(10):
    print(i)
# test_fib(10)
c = list(test_fib(10))
print(c)
#-------------------------------------------------------------------------#
def test_fib1():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
fib = test_fib1()
for i in range(10):
    print(next(fib))
#-------------------------------------------------------------------------#
# s = 'mohit'
# a=next(s)
# TypeError: 'str' object is not an iterator
# print(a) to make string iterator we use iter() function
# iterator means moving to next element using next() function

s1='mohit'
a=iter(s1)
b=next(a)
c=next(a)
d=next(a)
e=next(a)
f=next(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#-------------------------------------------------------------------------#
def count_test(n):
    count = 1
    while count <= n:
        yield count
        count =  count+1
c = count_test(5)
for i in c:
    print(i)
#-------------------------------------------------------------------------#