import json # json is also a file type help to keeo data in key & value pairs

data = {
    'name':'mohit',
    'university':'ICFAI',
    'course':'cyber security',
    'batch': 2023-2024,
    'subjects':['digital skill','c programming']
}

with open('data.json','w') as f:
    json.dump(data, f) #dump is used to fill the data in a file

with open('data.json','r') as f:
    v = json.load(f) # Load is used to read the data file or show the file

c=v['subjects']
print(v,c) # we can also print it directly by writing print(json.load(f))

# Here we will see how we can read the comma seperated value file
import csv # (comma seperated value file)

data = [['name','mail_id','mobile_num'],
        ['mohit','mohit@gmail.com',947154],
        ['rohit','rohit@gmail.com',846466],
        ['shubham','shubham@gmail.com',77879],
        ['manoj','manoj@gmail.com',9754844],
]
with open('data.csv','w') as f: # Here we are writing data in a file
    writer = csv.writer(f)

    for i in data:
        writer.writerow(i)

with open('data.csv','r') as f1:
    read_data = csv.reader(f1)

    for i in read_data:
        print(i)

# Writing and reading data in binary format, Wb is write binary
with open('data.bin','wb') as f2:
    f2.write(b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64')# Hello world
# Reading binary data
with open('data.bin','rb') as f2:
    print(f2.read())