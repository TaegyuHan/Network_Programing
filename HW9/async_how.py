import asyncio
import time


async def add(a, b):
    print("In add() func")
    await asyncio.sleep(1)
    print(a + b)


async def mul(a, b):
    print("In mul() func")
    await asyncio.sleep(2)
    print(a * b)


async def main():
    print(f"stred at {time.strftime('%X')}")
    task1 = asyncio.create_task(add(1, 2))
    task2 = asyncio.create_task(add(3, 4))

    await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())