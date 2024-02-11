import io
# we can store data in chunks
with open('data2.txt','wb') as data:
    file = io.BufferedWriter(data)
    file.write(b'this is a first line\n')
    file.write(b'this is my second line')
    file.flush() # file flush is just like a close in a file

#reading a file 
with open('data2.txt','rb') as data:
    file = io.BufferedReader(data)
    f = file.read(100)
    print(f)