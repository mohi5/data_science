d6={456,256}
type(d6)
print(type(d6))
d5={'number': [2,4,7,5], 'assignment':(1,4,4,5,),'launch_date':{28,12,14},'Class_time':{'web_dev':8,'Data science masters':8,'java with dsa and system design':7}}
a=d5['number'][2]
print(a)
print(d5)
# we can store list, tupple, string in dictionary
# dictionary always should have unique keys value
# we can alsostore dictionary inside dictionary
b=d5['Class_time']['java with dsa and system design']
print(b)
d5['mentor']=['sudhanshu','krish','anurag','hayder']

del d5['assignment']
c=list(d5.keys())
d=d5.items()
e=d5.pop('mentor')
print(e)
print(d)
print(c)
print(d5)