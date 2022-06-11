"""
    Thread 클래스의 파생 클래스 생성

    threading 모듈의 Thread 클래스의 파생 클래스 정의

    run() 메소드 오버라이드
"""
import threading
import datetime


class MyThread(threading.Thread):
    """ 스레드 클래스 """

    def __init__(self, name: str, counter: int) -> None:
        """ 생성자 """
        super().__init__()  # threading.Thread 생성자 상속
        self._name = name
        self._counter = counter

    def run(self):
        """ 스레드 실행 메소드 """
        print(f"\nString {self._name}[{self._counter}]")
        print_date(self._name, self._counter)
        print(f"\nString {self._name}[{self._counter}]")


def print_date(thread_name: str, counter: int) -> None:
    """ 날짜 출력 함수 """
    today = datetime.date.today()
    print(f"\n{thread_name}[{counter}]: {today}")


if __name__ == '__main__':
    """ 실행 """
    thread1 = MyThread("Th", 1)
    thread2 = MyThread("Th", 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("\nExiting the program")