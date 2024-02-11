#OOPS mainly refer to a real world entity in for of a class we describe all things about 
class test:
    pass
a = test()
print(type(a))

class pwskills:

    def welcome_msg(self):
        print('welcome to pw skills')

rohan = pwskills()
rohan.welcome_msg()

mohit = pwskills()
mohit.welcome_msg()

# Here __init__ is called initialisation its work is to pass the data through class & self is usedto connect function/method to class
# self also binds the value to the class
class pwskill1:

        def __init__(self,student_id, email_id, phone_number):
             self.student_id = student_id
             self.email_id = email_id
             self.phone_number = phone_number

        def return_student_detail(self):
             return self.student_id, self.email_id, self.phone_number
        
mohit = pwskill1(458,'mohit@gmail.com',9110015118)
a=mohit.return_student_detail()
print(a)
b=mohit.student_id
print(b)
# init do the work of taking data when object is created
# self is not a reserved keyword

class pwskill2:

        def __init__(soap,student_id, email_id, phone_number):
             soap.student_id = student_id
             soap.email_id = email_id
             soap.phone_number = phone_number

        def return_student_detail(soap):
             return soap.student_id, soap.email_id, soap.phone_number
        
rohit = pwskill1(458,'mohit@gmail.com',9110015118)
c=rohit.return_student_detail()
print(c)
        
        