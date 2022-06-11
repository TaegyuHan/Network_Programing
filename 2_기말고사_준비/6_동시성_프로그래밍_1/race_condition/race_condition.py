"""
    경쟁 상태

    공유 자원에 대해 여러 개의 스레드가 동시에 접근을 시도할 때 접근의
    타이밍이나 순서 등이 결과값에 영향을 줄 수 있는 상태

    - Python 3.10 version 부터는 자동적으로 경쟁조건 해결함
    - Pyhton 3.9 이하에서만 경쟁 상태가 발생함
"""
import threading

x = 0  # 공유 변수


def increment() -> None:
    """ 공유 번수 값 증가 """
    global x
    x += 1


def thread_task() -> None:
    """ 스레드 연산 """
    for _ in range(300_000):
        increment()


def main_task() -> None:
    """ 메인 함수 """
    global x
    x = 0  # 공유 변수 0으로 초기화

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    for i in range(10):
        main_task()
        print(f"Iteration {i}: x = {x}")
