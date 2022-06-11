"""
    I/O-bound 프로세스 성능 향상 방안: 스레딩
"""

import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()


def get_session() -> requests.Session:
    """ 세션 얻기 """
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url: str) -> None:
    """ 사이트 다운로드 하기 """
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: list[str]) -> None:
    """ 모든 사이트 다운로드 하기 """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == '__main__':
    COUNT = 30
    sites = [
                "https://homepage.sch.ac.kr",
                "https://www.gogole.co.kr",
            ] * COUNT

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")
