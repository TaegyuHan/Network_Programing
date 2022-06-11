import asyncio

async def add(a: int, b: int) -> int:
    """ 더하기 함수 """
    print(f"add {a} + {b}")
    await asyncio.sleep(1)  # 1초 대기. asyncio.sleep도 코루틴
    return a + b  # 두 수를 더한 결과 반환


async def print_add(a: int, b: int) -> None:
    """ 더한 결과를 출력 """
    result = await add(a, b)  # await로 다른 네이티브 코루틴 실행하고 반환 값을 변수에 저장
    print(f"print_add: {a} + {b} = {result}")

if __name__ == '__main__':
    asyncio.run(print_add(1, 2))  # print_add 실행