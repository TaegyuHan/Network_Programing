"""
    I/O-bound 프로세스 성능 향상 방안: 비동기 I/O
"""
import asyncio
import time
import aiohttp


async def download_site(session, url: str) -> None:
    """ 사이트 다운로드 하기 """
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")


async def download_all_sites(sites: list[str]) -> None:
    """ 모든 싸이트 다운로드하기 """
    async with aiohttp.ClientSession() as session:  # 비동기 http 세션 생성
        tasks = []  # 동시에 처리할 일을 저장할 리스트

        for url in sites:
            task = asyncio.create_task(download_site(session, url))  # 일 생성
            tasks.append(task)

        # 동시에 일 처리
        # 모두 마무리가 될때 까지 기다림
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    COUNT = 30
    sites = [
                "https://homepage.sch.ac.kr",
                "https://www.google.com"
            ] * COUNT

    start_time = time.time()

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(download_all_sites(sites))

    duration = time.time() - start_time

    print(f"Download {len(sites)} sites in {duration} seconds")