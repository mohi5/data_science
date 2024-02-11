a = 10
import logging
# f = open('r.txt','r')
# print('this is my print') 
# In exception handling we write code in a try/catch block so if one code crashes all should work properly.
try:
    logging.basicConfig(filename='mohit1.log',level=logging.INFO)
    logging.info('this is a txt  file opening code in reading mode which will give error')
    f = open('r.txt','r')
except Exception as c:
    print('this is my except block',c)
try:
    f = open('r.txt','w')
    f.write('my name is john, john banega don')
    # f.close()
except Exception as e:
    print('this is second exception block',e)

# we have one more exception block that is else. it is executed when try block runs successfully.
else:
    f.close()
    print('this will executed once your try will execute without error')

try:
    logging.info('here the file will be not created or here the code will not be executed so it will not go in else block it will go in a exception handling block')
    f = open('r1.txt','r')
    f.write('my name is john, john banega don')
    # f.close()
except Exception as e:
    print('this is second exception block',e)
else:
    f.close()
    print('this will executed once your try will execute without error')

try:
    f=open('r2.txt','w')
    f.write('write anything')
finally:
    print('finally will execute it self in any situation if there is error in a code then also finally block will executed')