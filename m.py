import logging
logging.basicConfig(filename='mohit.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('this is information')
logging.warning('this is warning')

l=[1,2,33,43,45,[8,9,10], 'mohit', 'sudh']
l1=[]
l2=[]
# we can also log str
for i in l:
    logging.info('here we are iterating value over the local variable'+str(l))
    if type(i) == list:
        logging.info('here we are inside the if statement and trying to check the type of list')
        for j in i:
            logging.info('here we are inside the for loop inside for loop')
            if type(j) == int:
                logging.info('here we are adding the value inside l1 list')
                l1.append(j)
    elif type(i) == int:
        l1.append(i)

    else:
        if type(i) == str:
         l2.append(i)

print(l1, l2)
logging.info("the final result of int is {l}, and str is {l}".format(l=l1,l3=l))