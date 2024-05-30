import threading
import random
import time


class BankAccount(threading.Thread):
    account_balance = 100
    def __init__(self,name, money_request):
        threading.Thread.__init__(self)
        self.name = name
        self.money_request = money_request

    def run(self):
        threadLock.acquire()
        BankAccount.get_money(self)
        thread_lock.release()

    @staticmethod
    def get_money(customer):
        print()


thread_lock = threading.Lock()
        