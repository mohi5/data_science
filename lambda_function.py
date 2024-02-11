# WAP for multiplication of two values
n=4
p=5
def test(n,p):
    return n**p
a=test(2,4)
print(a)

# Now in lambda function way of writing the code changes
# lambda is inbuilt function in python it is also calld one line function or anonymous function because it has no name
a=lambda n,p:n**p
b=a(3,4)
print(b)

add = lambda x,y : x + y
c=add(2,3)
print(c)

#---------------------------Celsius to farenheit----------------------------#
c_to_f = lambda c : (9/5)*c + 32
b = c_to_f(45 )
print(b)

#---------------------------Finding Max Function----------------------------#
finding_max = lambda x,y : x if x>y else y
c = finding_max(4,5)
print(c)

#-----------------------------Finding Length--------------------------------#
s='mohit kumar'
find_length = lambda s : len(s)
c=find_length(s)
print(c)