"""
    코루틴 예제: 사용자 정보 조회 프로그램
     - 비동기
"""

import asyncio
import time


async def get_user(name: str) -> None:
    """ 유저 정보 출력 """
    print(f"사용자 '{name}' 정보 조회중...")
    await asyncio.sleep(1)
    print(f"사용자 '{name}' 정보 조회 완료!...")


async def main() -> None:
    """ 메인 함수 """
    start = time.time()
    await asyncio.gather(
        get_user(name="Yun"),
        get_user(name="Kim"),
        get_user(name="Song"),
    )
    end = time.time()
    print(f"총 소요시간 {end - start}")


if __name__ == '__main__':
    asyncio.run(main())



