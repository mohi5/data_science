import threading
import urllib.request

# def file_download(url, filename):
#     urllib.request.urlretrieve(url, filename)

# file_download('https://edu.google.com/coursebuilder/courses/pswg/1.2/assets/notes/Lesson1.6/Lesson1.6Findingtextonawebpage_Text_.html','m.txt')

# url_list = ['https://github.com/CMiksche/network.txt','https://www.data.gov/','https://archive.ics.uci.edu/ml/index.php']

# file_name_list = ['mark.txt','mark2.txt','mark3.txt']

# ther=[threading.Thread(target=file_download , args=(url_list[i], file_name_list[i])) for i in range(len(url_list))]
# for t in ther:
#     t.start()

# for t in ther:
#     t.join()

import time
def test1(id):
    for i in range(10):
        print('test1 %d printing %d %s' %(id,i,time.ctime()))
        time.sleep(1)
# test1(1)
# thread1 = [threading.Thread(target=test1, args=(i,))for i in range(3)]
# # for t in thread1:
# #     t.start()

shared_var = 0
lock_var = threading.Lock()
def test2(id):
    global shared_var
    with lock_var:
        shared_var = shared_var + 1
        print("test2 id is %d has increased the shared variable by %d" % (id,shared_var))
        time.sleep(1)
thread2 = [threading.Thread(target = test2, args=(i,))for i in range(3)]
# print(thread2)
test2(0)
for t in thread2:
    t.start()