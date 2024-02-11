#a=int(input("enter the number"))
# a = 22
# if a<5:
#     print("hello")
# else:
#     print("no")
#     c=type(a)
#     print(c)
#---------------------------------------------------------------
# marks = int(input("Enter the number "))
# if marks >= 80:
#     print("you are in A0 batch")
# elif marks >= 70 and marks < 80:
#     print("you are in A1 batch")
# elif marks >= 60 & marks < 70:
#     print("you are in A2 batch")
# else:
#     print("padh bhi liya kar bhai")
#----------------------------------------------------------------
l=[1,2,3,4,5,6,7,8]
# a=l[0] + 1
# print(a)
l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
    print(l1)
#------------------------------------------------------------------
print('\n')
l=["mohit","rohit","rohan","pwskills"]
l1=[]
for i in l:
    print(i)
    l1.append(i.upper())
    print(l1)

#----------------------------------------------------------------
print('\n')
l=[1,2,3,'mohit','rohit',345,45.690]
l1_num=[]
l2_str=[]
for i in l:
    if type(i) == int or type(i) == float :
        l1_num.append(i)
      #  print(l1_num)
    else:
        l2_str.append(i)
        
        print(l1_num)
        print(l2_str)
