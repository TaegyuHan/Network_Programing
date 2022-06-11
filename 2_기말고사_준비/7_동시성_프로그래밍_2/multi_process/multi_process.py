"""
    멀티 프로세싱 모듈 사용하기
"""
from multiprocessing import Process
import os


def info(title: str) -> None:
    """ 정보 알림 """
    print(title)
    print("parent process id:", os.getppid())
    print("process id:", os.getpid())


def f(name: str) -> None:
    """ 출력 함수 """
    info("function f")
    print("hello", name)


if __name__ == '__main__':
    info("main line")
    p = Process(target=f, args=("bob",))
    p.start()
    p.join()
