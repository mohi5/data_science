# here we know about how can we modify add or delete the private function
# @property decorator helps in get , set and delete the values
# All getter, setter and deleter function are present inside the @property decorator

class pwskills:
    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name

    @property
    def course_price_access(self):# We are making function for giving access to the outsider that he cannot access directly but from this function
        return self.__course_price
    
    @course_price_access.setter # Here setter is a function which helps in set or modify the value of private class 
    def course_price_set(self, price):
        if price <= 3500:
            pass
        else:
            self.__course_price = price

    @course_price_access.deleter # By deleter function we can delete the value inside the function
    def delete_course_price(self):
        del self.__course_price

pw = pwskills(3500, 'data science')
# del pw.delete_course_price # By this we can delete the course price which is private by creating another function
a=pw.course_name
b=pw.course_price_access # By this we can access the private function or data
# b= pw._pwskills__course_price
c=pw.course_price_set = 4500
print(a,b,c)