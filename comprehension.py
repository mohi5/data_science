#---------------------List Comprehension--------------------
l = [1,2,3,4,5,6,26,27]
l1 = [] 
for i in l:
    l1.append(i**2)
    print(l1) 
#-------------Multiplication of value inside list------------
a=[i**2 for i in l] # writing code in a one line is called comprehension function
print(a)

#---------------WAP for finding even no.-------------------
b=[i for i in l if i % 2 == 0]
print(b)
#---------------convert string to uppercase-----------------
l2 = ['mohit','rohit','rohan','rakesh']
c=[i.upper() for i in l2]
d=[i.title() for i in l2]
print(c)
print(d)
#-------------------Tuple comprehension----------------------
#e=(i**2 for i in l) # we can not directly access data through tuple first we have to convert it in list
e=list((i**2 for i in l))
print(e)
#-----------------Dictionary Comprehension--------------------
f={'key1':1, 'key2':2, 'key3':3, 'key4':4}
g={k:v**2 for k, v in f.items()}
#this works in a following step
# f.items() prints all the key and value pairs in the list
# ex:-dict_items([('key1':1, 'key2':2, 'key3':3, 'key4':4)])
print(g)

f={'key1':1, 'key2':2, 'key3':3, 'key4':4}
h={k : v for k, v in f.items() if v>1}
print(h)
#-------------------------------------------------------------