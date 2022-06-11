"""
    I/O-bound 프로세스 성능 향상 방안: 멀티프로세싱
"""
import requests
import time
import multiprocessing

session = None


def set_global_session() -> None:
    """ 전역 변수 세션 생성하기 """
    global session
    if not session:
        session = requests.Session()


def download_site(url: str) -> None:
    """ 다운르드 하기 """
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites: list[str]) -> None:
    """ 모든 싸이트 다운로드 하기"""
    with multiprocessing.Pool(processes=5, initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    COUNT = 30
    sites = [
                "https://homepage.sch.ac.kr",
                "https://www.google.com"
            ] * COUNT

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")