import threading
import time
def update():
    print("Updating database.....")
    time.sleep(5)
    print("Database updated")
def num(n):
    for i in range(1,n):
        print(i)
th=threading.Thread(target=update)#this is only intialize part
th.start()#without giving this the thread wont start
num(100)
th.join()#this method  wait the main thread until this thread complete
print("Bye")
