"""
    동기 처리 / # 비동기 처리 # 예제

    동기 처리 < 처리와 동일하게 작동
"""

import asyncio
import time


async def say_after(delay: int, what: str) -> None:
    """ 비동기 기다리고 출력 하는 함수  """
    await asyncio.sleep(delay)
    print(what)


async def main() -> None:
    """ 메인 함수 """
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
