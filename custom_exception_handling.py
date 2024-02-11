age = int(input('Enter your age :'))
# we can also say that custom exceptions are the user defined exception are designed as per the requirement of the program.
class validateage(Exception):

    def __init__(self, msg):
        self.msg = msg

def validateage(age):
    if age < 0:
        raise validateage('entered age is negative')
    elif age > 200:
        raise validateage('entered age is very high')
    else:
        print('age is valid')

try:
    age = int(input('Enter your age :'))
    validateage(age)
except validateage as e:
    print(e)