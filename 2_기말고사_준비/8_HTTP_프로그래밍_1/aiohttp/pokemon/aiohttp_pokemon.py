"""
    aiohttp 모듈: 클라이언트 (비동기)
"""

import aiohttp
import asyncio
import time

async def get_pokemon(session: aiohttp.ClientSession, url: str) -> str:
    """ URL GET 포켓몬 아이디 얻기 """
    async with session.get(url) as rsp:
        pokemon = await rsp.json()
        return pokemon["name"]


async def main() -> None:
    """ 메인 함수 """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 11):
            url = f"https://pokeapi.co/v2/pokemon/{number}"
            tasks.append(asyncio.create_task(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end_time = time.time()
    print(f"--- {end_time - start_time} seconds ---")

