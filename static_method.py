# static method are methods within a class that have no access to anything else in the class(no self keword or cls keyword).they cannot change or look at any object attributes or call the other methods in the class.

class pwskills:
    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)
pw=pwskills()
pw.student_details('mohit','mohit@gmail.com',9471505480)

class pwskills1:
    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)

    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)

    def mentor(self, mentor_list):
        print(mentor_list)

pwskills1.mentor_class(['mohit','rohit'])

# Calling static method inside a class method
class pwskills2:
    def student_details(self, name, mail_id, number):
        print(name, mail_id, number)

    @staticmethod # This is static method
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)
    
# here we can see how we can call static medhod inside the static method
    @staticmethod
    def mentor_class(list_mentor):
        pwskills2.mentor_mail_id(['mohit@gmail.com', 'rook@gmail.com'])
        print(list_mentor)
    
    @classmethod # This is class method
    def class_name(cls):
        cls.mentor_class(['mohit','rohit'])

    def mentor(self, mentor_list): # This is instance method
        print(mentor_list)
        self.mentor_class(['sudh','krish'])

pwskills2.class_name()
pwskills2.mentor_class(['mohit','rohit'])
# Calling mentor class
pw = pwskills2()
pw.mentor(['sudh','krish'])

# Here we have seen the static methods, class methods & instance methods and how can we access static methods inside class methods and instance methods and on its own static method.