import threading
import urllib.request
def test(id):
    print('the id is %d'%id)
test(45)

thread = [threading.Thread(target = test, args =(i,))for i in range(10)]
for t in thread:
    t.start()
print(id(thread))

def file_download(url, filename):
    urllib.request.urlretrieve(url, filename)

file_download('https://edu.google.com/coursebuilder/courses/pswg/1.2/assets/notes/Lesson1.6/Lesson1.6Findingtextonawebpage_Text_.html','m.txt')

url_list = ['https://edu.gcfglobal.org/en/basic-html/text-elements-in-html/1/','https://www.codecademy.com/article/local-web-page','https://www.hostinger.in/tutorials/making-website-with-html']

file_name_list = ['mark.txt','mark2.txt','mark3.txt']

ther=[threading.Thread(target=file_download , args=(url_list[i], file_name_list[i])) for i in range(len(url_list))]
