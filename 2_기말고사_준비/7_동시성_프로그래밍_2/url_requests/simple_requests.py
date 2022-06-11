"""
    기본 프로그램 ( 동시성 없음 )

    - 2개의 사이트를 번갈아 가면서 총 160번의웹 페이지 요청/응답 수신
    - 1개의 요청/응답 수신 후, 다음 요청/응답 수신을 수행함
"""

import requests
import time


def download_site(url: str, session: requests.Session) -> None:
    """ url 다운로드 페이지 출력 """
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: list[str]) -> None:
    """  """
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    COUNT = 30  # < 개수 정하기

    sites = [
                "https://homepage.sch.ac.kr",
                "https://www.google.co.kr"
            ] * COUNT

    start_time = time.time()  # 시작 시간
    download_all_sites(sites)
    duration = time.time() - start_time  # 끝 시간
    print(f"Download {len(sites)} in {duration} seconds")
