"""
    Lock 클래스 사용

    임계구역 보호를 위한 스레드 동기화
    특정 시간에 1개의 스레드만 임계구역에 접근할 수 있도록 함

    - acquire(): 임계구역 진입을 위한 ‘lock’을 획득
        다른 스레드가 ‘lock’을 가지고 있지 않을 경우, ‘lock’을 획득하여 임계구역 진입
        다른 스레드가 ‘lock’을 가지고 있을 경우, ‘lock’을 반납할 때까지 대기
        − ‘lock’이 반납되면 임계구역 진입

    - release(): 임계구역 종료 후 ‘lock’을 반납
        ‘lock’을 반납하여, 대기 중이던 스레드 중 1개의 스레드가 ‘lock’을 획득하도록

    1개의 스레드가 ‘lock’을 획득하면, 다른 스레드들은 ‘lock’이 반납될
    때까지 공유 자원에 접근할 수 없음
"""
import threading

x = 0  # 공유 자원


def increment() -> None:
    """ 공유 자원 값 증가 """
    global x
    x += 1


def thread_task(lock: threading.Lock) -> None:
    """ 스레드 공유자원 증가 """
    for _ in range(300_000):
        lock.acquire()
        increment()
        lock.release()


def main_task() -> None:
    """ 메인 함수 """
    global x
    x = 0  # 공유 자원 초기화

    lock = threading.Lock()  # Lock 인스턴스 생성

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    for i in range(10):
        main_task()
        print(f"Iteration {i}: x = {x}")
