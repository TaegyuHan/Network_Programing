"""
    코루틴을 이용한 프로그램 작성하기
    
    비동기 팩토리얼
"""

import asyncio


async def factorial(name: str, number: int) -> int:
    """ 팩토리얼 사용하기 """
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i

    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main() -> None:
    """ 메인 함수 """
    L = await asyncio.gather(
        factorial(name="A", number=2),
        factorial(name="B", number=3),
        factorial(name="C", number=4),
    )
    print(L)


if __name__ == '__main__':
    asyncio.run(main())