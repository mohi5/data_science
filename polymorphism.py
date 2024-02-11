# polymorphism means doing multiple work or having diffrent behaviours in diffrent circumstances of single entity
def test(a, b):
    return a+b

a=test(3,4)
print(a)

b=test('mohit',' kumar')
print(b)

c=test([1,2,3,4],[5,6,7,8])
print(c)

class data_science:
    
    def syllabus(self):
        print('this is my syllabus for data science')

class web_dev:
    
    def syllabus(self):
        print('this is my syllabus for web_dev')

def class_parcer(class_object):
    for i in class_object:
        i.syllabus()

data_science = data_science()
web_dev = web_dev()

class_object = [data_science, web_dev]
class_parcer(class_object)