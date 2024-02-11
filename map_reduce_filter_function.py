#======================================MAP========================================#
l=[2,3,4,5,6]
def test(l):
    l1=[]
    for i in l:
        l1.append(i**2)
    return l1
a=test(l)
print(a)
# we can do above process in short format using map map takes two arguments as input 1st is function & 2nd is iterables object.
def sq(x):
    return x**2
b=list(map(sq,l))
print(b)

# we can take external functions or also the lambda function

c = list(map(lambda x:x**3,l))
print(c)

l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10,11,12]
d = list(map(lambda x,y : x+y,l1,l2))
print(d)
# we can write above lambda function as external function
def add(x,y):
    return x+y
e = list(map(add,l1,l2))
print(e)

s = 'mohit'
f = list(map(lambda s: s.upper(),s))
print(f)

#======================================REDUCE=======================================#
from functools import reduce
l = [1,2,3,4,5]
g=reduce(lambda x,y : x+y,l)
print(g)
# reduce function work as like [1,2,3,4,5] in this list 1 become x and 2 become y and after adding 3 become x and next 3 become y after adding this 6 become x and 4 become y and after adding 10 become x and 5 becomes y this is how the reduce function work in python.
# we can only give two variable of argument no more than that
# multiplication using reduce
h = reduce(lambda x, y: x*y,l)
print(h)
# WAP for finding large numbers in list
i = reduce(lambda x,y : x  if x>y else y,l)
print(i)

#======================================FILTER=======================================#
# filter, filters the function and return the output
# This is a program for finding even no. in a list
j=list(filter(lambda x : x % 2 == 0,l))
print(j)

# This is a program for finding odd numbers in a list
k=list(filter(lambda x : x % 2 != 0,l))
print(k) 

# This is a program for finding negative numbers in a list
l1 = [-4,-3,-2,1,2,3,-8]
m = list(filter(lambda x : x<0,l1))
print(m)

# This is a program for printing the string whose length is less then 6 in a list
l2 = ['sudh','mohit','pwskills','computer']
n = list((filter(lambda x: len(x)<6,l2)))
print(n)

