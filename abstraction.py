import abc
# Abstarction is generally a skeleton of a program
class pwskills:
    @abc.abstractmethod
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assignment(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass

class student_details(pwskills):

    def student_details(self):
        return 'this is a method for taking a student details'
    
    def student_assignment(self):
        return 'this is a method for taking a student assignment'
    
class data_science_master(pwskills):

    def student_details(self):
        return 'this will return a student detail for data science'
    
    def student_assignment(self):
        return 'this will return a student assignment for data science'

sd = student_details()
print(sd.student_details())    

dsm = data_science_master()
print(dsm.student_details())

