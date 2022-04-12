import threading

"""

 멀티 쓰레드를 사용할 때 이렇게 
 코드를 작성해서는 인돼!!!
 
 멀티 프로세스를 만들어서 코딩을 하는 것을 추천한다.
 
"""

x = 0


def increment():
    global x
    x += 1


def thread_task():
    for _ in range(300_000):
        increment()


def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main_task()
    print(f"Iteration {i}: x = {x}")