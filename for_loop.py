l=[1,2,3,4,5]
for i in l:
    print(i,type(i))
#----------------------------------------------
print('\n')
l1=['krish','rohit','mohit']
for i in l1:
    print(i)
#---------------------------------------------------
print('\n')
l1=['rohit','rakesh','mukesh','mohit']
for i in l1:
    print(i)
else:
    print('if for loop is able to complete itself then only else will be executed')
#-------------------------------------------------------
print('\n')
l1=['rohit','rakesh','mukesh','mohit']
for i in l1:
    if i == 'mukesh':
        break
    print(i)
print('\n')
#------------------------------------------------------
l1=['rohit','rakesh','mukesh','mohit']
for i in l1:
    if i == 'mukesh':
        break
    print(i)
else:
    print('execute this if for loop is complete')
#---------------------------------------------------------
print('\n')
l1=['rohit','rakesh','mukesh','mohit']
for i in l1:
    if i == 'mukesh':
        #print(i)
        continue
    print(i)
else:
    print('execute this if for loop is complete')
#-------------------------RANGE---------------------------
a=list(range(0,8,2)) # last value give the jumping position
b=list(range(0,8))
c=list(range(0,-10,-1))
print(a)
print(b)
print(c)
print('\n')
#-----------------------------------------------------------
l1=['rohit','rakesh','mukesh','mohit']
d=list(range(len(l1)))
print(d)
for i in range(len(l1)-1,-1,-1): #reversing a string in list
    print(l1[i])
# we can also write it as a
    print('\n')
for i in [3,2,1,0]: #reversing a string in list
    print(l1[i])
#-------------------------------------------------------
l2 = [12,14,16,50,20,17,78,22,65]
f=list(range(0,len(l2),2))
print(f)
for i in range(0,len(l2),2):
    print(l2[i])
print('\n')
#-------------------SUBMESSION OF LIST--------------------
l = [1,2,3,4,5,6,7,8,9]
a=sum(l)
print(a)
result = 0
for i in l:
    result = result + i
    #break
    print(result)
print('\n')
#---------------------------------------------------------
t = (1,2,3,4,5,6)
result = 0
for i in t:
    result = result + i
    #break
    #print(i)
    print(result)
#----------------------------------------------------------
s={1,2,3,4,'mohit','pwskill','sudh'}
for i in s:
    print(i)
s1 = {'pwskills'}
for i in s1:
    print(list(i))
#---------------------DICTIONARY--------------------------
d = {'name':'mohit','class':'data science masters','Topic':['python','stats', 'machine learning','deep learning','cv','NLP','resume','interview']}
# c = d['class']
# print(c)
for i in d.keys():
    print(d[i])
for i in d.values():
    print(i)
for i in d.items():
    print(i)
#-----------------------------------------------------------------------------------