import threading
import time
import random

print(time.strftime("%y-%m-%d %H:%M:%S" , time.gmtime()))


def execute_thread(i):
    print("Thread {} is about to sleep at {}".format(i, time.strftime("%y-%m-%d %H:%M:%S" , time.gmtime())))
    print("Name of the thread", threading.current_thread())
    time.sleep(random.randint(1,4))
    print("Thread {} is woke up at {}".format(i, time.strftime("%y-%m-%d %H:%M:%S" , time.gmtime())))

for i in range(10):
    thread = threading.Thread(
        target=execute_thread,args=(i,))
    thread.start()

    print("Active threads : ", threading.active_count())

