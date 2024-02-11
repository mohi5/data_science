class test:
    def test_math(self):
        return 'this is my first class'
    
class child_test(test):
        pass

child_test_obj = child_test()
child_test_obj.test_math()
print(child_test_obj.test_math())
print('--------------------------------------------------------')
# Multi-level inheritance
class class1:
     def test1(self):
          return 'this is result from my first class'
     
class class2(class1):
     def test2(self):
          return 'this is result from my second class'
     
class class3(class2):
     pass

obj_class3 = class3()
print(obj_class3.test1())
print(obj_class3.test2())
print('--------------------------------------------------------------------')
# Multiple inheritance
# In multiple inheritance here child inherit the function of both parent mother and father
class class1:
     def test1(self):
          return 'this is my first function'
     
class class2:
     def test2(self):
          return 'this is my second function'
     
class class3(class1, class2):
     pass

obj_class3 = class3()
print(obj_class3.test1())
print(obj_class3.test2())