"""
    여러 개의 코루틴을 실행하기
"""

import asyncio
import time


async def add(a: int, b: int) -> None:
    """ 더하기 출력 """
    print("In add() func")
    await asyncio.sleep(1)
    print(a + b)


async def mul(a: int, b: int) -> None:
    """ 곱하기 출력 """
    print("In mul() func")
    await asyncio.sleep(2)
    print(a * b)


async def main() -> None:
    """ 메인함수 """
    task1 = asyncio.create_task(add(1, 2))
    task2 = asyncio.create_task(add(3, 4))
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())