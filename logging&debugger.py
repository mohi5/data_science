print('this is a print statement')
import logging
logging.basicConfig(filename='test.log',level = logging.INFO)
logging.info('log this line of execution')
logging.info('this is a print statement')
# There are 6 basic level of a logging
# 1. NOTSET
# 2. DEBUG
# 3. INFO # if we have given level as a info we can print below under this level but not the upper like notset & debug.
# 4. WARNING
# 5. ERROR
# 6. Critical
logging.debug("this is my msg") # this will not be logged in a file when level is INFO we have to change level to DEBUG
# But we can print warnings & error EX:-
logging.warning('this is warning')
logging.error('this is error')
logging.critical('this is critical')
logging.shutdown() # we use shutdown() to close the file

logging.basicConfig(filename='mohit.log', level=logging.INFO)
logging.info('this is information')
logging.warning('this is warning')