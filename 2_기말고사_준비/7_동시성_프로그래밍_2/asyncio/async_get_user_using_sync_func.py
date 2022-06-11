"""
    코루틴 내 블로킹 함수 사용하기

    아직 파이썬 내에 asyncio를 이용한 모듈들이 많지 않아, 불가피하게
    블로킹 함수를 사용하는 경우가 발생함

    그때 > asyncio.to_thread() 함수 사용
"""

import asyncio
import time


async def get_user(name: str) -> None:
    """ 사용자 정보 출력 """
    print(f"사용자 {name} 정보 조회중...")
    await asyncio.to_thread(time.sleep, 1)
    print(f"사용자 {name} 정보 조회 완료!")


async def main():
    """ 메인 함수 """
    start = time.time()
    await asyncio.gather(
        get_user(name="Jeon"),
        get_user(name="Yun"),
        get_user(name="Kim"),
        get_user(name="Song"),
    )
    end = time.time()
    print(f"총 소요시간: {end - start}")


if __name__ == '__main__':
    asyncio.run(main())
