import threading
import random
import time


def get_time(name):
    print("Thread {} is about to sleep at {}".format(name, time.strftime("%y-%m-%d %H:%M:%S", time.gmtime())))
    time.sleep(random.randint(1, 4))
    print("Thread {} is woke up at {}".format(name, time.strftime("%y-%m-%d %H:%M:%S", time.gmtime())))


class Custom_Thread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        get_time(self.name)
        print("Thread", self.name, "Execution ends -----")

thread1 = Custom_Thread("1")
thread2 = Custom_Thread("2")

thread1.start()
thread2.start()
