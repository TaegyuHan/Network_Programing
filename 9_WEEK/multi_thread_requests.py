import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    """ 세션 얻기 """
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_sites(url):
    """ URL에서 get 얻기 """
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)}  from {url}")


def download_all_sites(sites):
    """ 쓰레드풀 로 실행하기 """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_sites, sites)


if __name__ == '__main__':
    sites = [
        "https://home.sch.ac.kr",
        "https://www.google.co.kr"
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")