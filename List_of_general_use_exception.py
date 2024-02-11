try:
    a=10/0
except ZeroDivisionError as e:
    print(e)

try:
    int('sudh')
except (ValueError, TypeError) as e:
    print(e)

try:
    int('sudh')
except:
    print('This will catch an error')

try:
    import mohit
except ImportError as e:
    print(e)

try:
    d = {'key': 'mohit', 1:[2,3,4,5]}
    print(d['key2'])
except KeyError as e:
    print(e)

try:
    'mohit'.test()
except AttributeError as e:
    print(e)

try:
    l=[1,2,3,4,5]
    print(l[6])
except IndexError as e:
    print(e)

try:
    123+'sudh'
except TypeError as e:
    print(e)

try:
    with open('file.txt','r') as f:
        f.read()
except FileNotFoundError as e:
    print(e)
print(dir(Exception))

try:
    with open('file.txt','r') as f:
        f.read()
except Exception as e:
    print(e)
except FileNotFoundError as e:
    print('i will not be executed when my superclass is available because it handles all kind of exceptions so we should also write super class exception in last')