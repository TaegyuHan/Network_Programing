"""
    Python 멀티스레드 구현: threading.Thread 클래스

    threading 모듈

    threading 모듈의 Thread 클래스를 이용해 새로운 스레드 객체 생성

    객체 인자
        − target: 스레드에서 실행할 함수
        − args: 함수에 필요한 인자
"""
import threading


def prt_square(num: int) -> None:
    """ square 출력 함수 """
    print(f"Square: {num ** 2}")


def prt_cube(num: int) -> None:
    """ cube 출력 함수 """
    print(f"Cube: {num ** 3}")


# 객체 생성하기
t1 = threading.Thread(target=prt_square, args=(10,))
t2 = threading.Thread(target=prt_cube, args=(10,))

# 스레드 실행하기
t1.start()  # start thread 1
t2.start()  # start thread 2

t1.join()  # t1 스레드 실행이 완료될 때 까지 기다리기
t2.join()  # t2 스레드 실행이 완료될 때 까지 기다리기

print("Done!")
