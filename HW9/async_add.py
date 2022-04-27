import asyncio

async def add(a, b):
    print(f"add: {a} + {b}")
    await asyncio.sleep(1)
    return a + b

async def print_add(a, b):
    result = await add(a, b)
    print(f"print_add: {a} + {b} = {result}")

asyncio.run(print_add(1, 2))


