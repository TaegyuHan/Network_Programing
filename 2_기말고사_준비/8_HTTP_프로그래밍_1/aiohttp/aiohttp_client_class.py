"""
    비동기 클라이언트 모듈
"""

import aiohttp
import asyncio

async def main() -> None:
    """ 메인 함수 """
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as rsp:
            print(rsp.status)
            print(rsp.headers)
            print(await rsp.text())


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())