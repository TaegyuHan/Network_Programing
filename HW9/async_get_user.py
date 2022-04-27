import asyncio
import time

async def get_user(name):
    print(f"사용자 {name} 정보 조회중...")
    await asyncio.sleep(1)
    print(f"사용자 {name} 정보 조회 완료!")

async def main():
    start = time.time()
    await asyncio.gather(
        get_user("Jeon"),
        get_user("Yun"),
        get_user("Kim"),
        get_user("Song")
    )
    end = time.time()
    print(f"총 소요시간: {end - start}")

asyncio.run(main())