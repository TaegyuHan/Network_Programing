"""
    asyncio gather 사용하기
"""

import asyncio
import time


async def add(a: int, b: int) -> None:
    """ 더하기 """
    print("In add() func")
    await asyncio.sleep(1)
    print(a + b)


async def mul(a: int, b: int) -> None:
    """ 곱하기 """
    print("In mul() func")
    await asyncio.sleep(2)
    print(a * b)


async def main() -> None:
    """ 메인 함수 """
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(add(1, 2))
    task2 = asyncio.create_task(mul(1, 2))

    await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())
