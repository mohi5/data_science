class pwskills:
    def __init__(self, name, email):

        self.name = name
        self.email = email

    def student_details(self):
        print(self.name, self.email)

pw = pwskills('mohit','mohit@gmail.com')
print(pw.name)
print(pw.email)
print(pw.student_details())

#class-method is a method by which we can overload a function or how can we call above function in diffrent ways
class pwskills1:
    def __init__(self, name, email):

        self.name = name
        self.email = email

    @classmethod # we can also directly pass data using decorator function
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email)

b=pwskills1.details('rohit','rohit@gmail.com')
print(b.name)
print(b.student_details())

# Now we will make a clas variable and we can directly call it by class name

class pwskills2:

    mobile_num = 9471505999

    def __init__(self, name, email):

        self.name = name
        self.email = email

    @classmethod
    def change_num(cls, mobile):
        pwskills2.mobile_num = mobile

    @classmethod # we can also directly pass data using decorator function
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, pwskills2.mobile_num)

pw = pwskills2.details('mohit', 'mohit@gmail.com')
c = pw.student_details()
print(c) # here we are able to access mobile no. through a function

pwskills2.change_num(8978789456)
b = pwskills2.mobile_num
# print(a)
print(b)

# Adding outside function inside a class method 
# We can add external or out outside function 
class pwskills3:

    mobile_num = 9471505999

    def __init__(self, name, email):

        self.name = name
        self.email = email

    @classmethod
    def change_num(cls, mobile):
        pwskills3.mobile_num = mobile

    @classmethod # we can also directly pass data using decorator function
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, pwskills2.mobile_num)

def course_details(cls, course_name):
    print('your course name is', course_name)

pwskills3.course_details = classmethod(course_details)
f = pwskills3.course_details('data science masters')
print(f)

def mentor(cls, list_of_mentor):
    print(list_of_mentor)
pwskills3.mentor = classmethod(mentor)
pwskills3.mentor(['rohit', 'mohit'])

# we can also delete a function using del function

class pwskills4:

    mobile_num = 9471505999

    def __init__(self, name, email):

        self.name = name
        self.email = email

    @classmethod
    def change_num(cls, mobile):
        pwskills2.mobile_num = mobile

    @classmethod # we can also directly pass data using decorator function
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, pwskills2.mobile_num)

del pwskills4.change_num
# We can also delete by using delattr()
# We can delete anything or any function in class methods
delattr(pwskills4,'details')