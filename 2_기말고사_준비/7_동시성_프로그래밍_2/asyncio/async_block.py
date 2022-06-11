"""
    코루틴 내에서 일반(동기) 함수 사용

    - asyncio.to_thread() 함수는 스레드를 이용하여 병렬로 실행함
"""

import asyncio
import time


def blocking_io() -> None:
    """ 블록킹 함수 """
    print(f"start_time blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main() -> None:
    """ 메인 함수 """
    await asyncio.gather(
        asyncio.to_thread(blocking_io),  # thread 로 실행
        asyncio.sleep(1)  # asyncio로 실행
    )

if __name__ == '__main__':
    blocking_io()