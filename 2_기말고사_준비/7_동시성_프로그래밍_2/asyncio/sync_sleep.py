"""
    # 동기 처리 # / 비동기 처리 예제
"""

import time


def say_after(delay: int, what: str) -> None:
    """ 기다리고 출력 하는 함수 """
    time.sleep(delay)
    print(what)


def main() -> None:
    print(f"started at {time.strftime('%xx')}")

    say_after(1, "hello")
    say_after(2, "world")


if __name__ == '__main__':
    main()
