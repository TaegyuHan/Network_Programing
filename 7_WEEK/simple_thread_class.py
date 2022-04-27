import threading
import datetime


class MyThread(threading.Thread):

    def __init__(self, name, counter):
        super().__init__()
        self.name = name
        self.counter = counter

    def run(self) -> None:
        print(f"\nStarting {self.name}[{self.counter}]")
        print_date(self.name, self.counter)
        print(f"\nExiting {self.name}[{self.counter}]")

def print_date(thread_name, counter):
    today = datetime.date.today()
    print(f"\n{thread_name}[{counter}]: {today}")

thread1 = MyThread("Th", 1)
thread2 = MyThread("Th", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
