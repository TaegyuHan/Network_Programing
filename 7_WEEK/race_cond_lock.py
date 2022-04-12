import threading

"""
    
    쓰레딩 프로그램을 할 때
    락 을걸어서 데이터를 메모리를 보호한다.

    락을 최대한 줄여야한다.

"""

x = 0


def increment():
    global x
    x += 1


def thread_task(lock):
    for _ in range(300_000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main_task()
    print(f"Iteration {i}: x = {x}")