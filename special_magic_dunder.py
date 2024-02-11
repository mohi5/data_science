# dunder function basically means that double underscore in start and end__add__
# dunder function show what the work is going inside a function or input we give

print(dir())
a = 100
b = a+5
print(b)
# we can write above function as 
c = a.__add__(5)
print(c)

# In python while compiling code before init function __new__ function is called
# we do not use magic/dunder functions much in a python
class pwskills:
    def __new__(cls):
        print('this is my new function')

    def __init__(self):
        print('this is my init function')

        self.mobile_number = 948265165

pw = pwskills()
