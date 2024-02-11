def test():
    pass
def test1():
    print('this is my very very first function')
#print(test1())
test1()

def test2():
    return "my name is :"
#============================================================#
# c=test2()+ 'mohit' # print returns nontype object so we    cannot add nontype with str so we have to use return function. return function gives all types of value
# print(c)
# return is also used to print the multiple values at a time
#============================================================#
a = test2() + 'mohit'
print(a)

#------------------------------------------------------------#
def test3():
    return 'mohit',123,345.6,['mohit',34.2,45]
a,b,c,d = test3()
print(list(a))
result = test3()
print(result)

#-------------------------------------------------------------
def test4():
    a = 10+20/2
    return a
a = test4()
print(a)

def test5(a,b,c):
    d=a+b/c
    return d
b=test5(2,3,4)
print(b)

def test6(a,b):
    print(a+b)
# test6(4,5)  # directly calls(ex:-test6(4,5)) work only with print function not with return function.
c = test6(4,5)
#c = test6('mohit',' kumar')
print(c)
#============================================================================#
l=[1,2,3,4,'mohit',34.3,[4,5,6,7,8]]
l1=[]
for i in l:
    if type(i) == int or type(i) == float:
        l1.append(i)
print(l1)
#now we add above program in a function
def test7(l):
    l1=[]
    for i in l:
        if type(i) == int or type(i) == float:
            l1.append(i)
    return l1
#print(l1)
d=test7(l)
print(d)

def test8(a):
    '''this is function for extracting value from a list'''
    l1=[]
    for i in a:
        if type(i) == list:
            for j in i:       
                l1.append(j)
        else:
            if type(i) == int or type(i) == float:
                l1.append(i)
    return l1
e = test8(l)
print(e)

def test9():
    return a+b

def test10(*args):
    return args
# c=type(test10())
# print(c)
a=test10(4,8,10) 
# * the meaning of staric is to take n no. of arguments
print(a)

def test11(*args,b):
    return args, b
d=test11(33,23,34,b=5)
print(d)

def test12(c,d,a=23,b=22):
    return c, d, a, b
e=test12(3,4)
# e=test12(3,4, a=1)# we can override the decleared values
print(e)

def test13(**kargs): # we use double ** staric for dictionary values
    return kargs

f=test13(a=4,b=6,c=[])
print(f)
