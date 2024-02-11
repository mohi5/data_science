f = open('test.txt','w') # here open creates the new file in a directory
f.write("i have to complete this course and become data science engineers") # write helps to write in the created file.
f.close()

f = open('test.txt','w')
f.write("my name is mohit") # when we write two times in a same file it erases the previous data in the file and write the new data
f.close()

# If we want to to write data in the file without erasing previous data we will use 'a' which will allow to write and append

f = open('test.txt','a')
f.write('\nRemote Language Learning and Cultural Exchange Platform: A SaaS tool that connects language learners with native speakers for virtual language exchange sessions, offering opportunities to practice speaking and immerse oneself in different culturesVirtual Reality-based Employee Training and Development Platform: A SaaS solution that leverages virtual reality technology to create immersive training simulations and scenarios for employee onboarding, skills development, and compliance /training.Personalized Wedding Planning App: A SaaS platform that guides couples through the wedding planning process, offering tools for budgeting, vendor selection, guest list management, and day-of coordination.These ideas span various industries and address diverse needs and pain points, offering opportunities for innovation and differentiation in the market.')

f = open('test.txt','r') # This is use to show the 
print(f.read())
f.seek(0) # It is used to reset the pointer to starting point
print(f.readline())

f1 = open('test.txt','r')
# we can also write the above line as
with open('test.txt','r') as f1: 
    for i in f1:
        print(i.capitalize)

# Finding the size of the file
import os
print(os.path.getsize('test.txt'))

# we can also delete the file
# os.remove('test.txt')

# Renaming the file 
# os.rename('lab.txt','robo.txt')

# copying the file
# import shutil
# shutil.copy('robo.txt','rank.txt')