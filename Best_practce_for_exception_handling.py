import logging
logging.basicConfig(filename='m1.log', level=logging.INFO)

#use always a specific exception
try:
    15/0
except ZeroDivisionError as e:
    print(e)

#Print always a proper message
try:
    15/0
except ZeroDivisionError as e:
    print('i am trying to handle ZeroDivisionError',e)

# always try to log your error
try:
    20/0
except ZeroDivisionError as e:
    print(e)
    logging.error('An error occurred: {}'.format(e))
    # logging.error('i am trying to handle ZeroDivisionError{}'format(e),exc_info=True)

# always try to avoid multiple exception handling
try:
    10/0
except TypeError as e:
    logging.error('i am handling type errot {}'.format(e))
except FileNotFoundError as e:
    logging.error('i am handling file not found {}'.format(e))
except AttributeError as e:
    logging.error('i am handling attributeError {}'.format(e))
except ZeroDivisionError as e:
    logging.error('i am handling zeroDivisionError {}'.format(e))

# Always try to write document of the code with proper meaning
# Cleanup the resources so it can not get under or over utilized
try:
    with open('rk.txt','w') as f:
        f.write('write anything')
except FileNotFoundError as e:
    logging.error('i am handling file not found {}'.format(e))
finally:
    f.close()# always cleanup the resources
