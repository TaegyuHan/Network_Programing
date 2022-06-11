"""
    asyncio를 이용한 웹 클라이언트
"""

import asyncio
import urllib.parse


async def print_http_headers(url: str) -> None:
    """ HTTP headers 읽기 """
    url = urllib.parse.urlsplit(url)
    if url.scheme == "https":
        reader, writer = await asyncio.open_connection(url.hostname, port=443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url.hostname, port=80)

    http_req = f"HEAD / HTTP/1.1\r\nHost: {url.hostname}\r\n\r\n"

    writer.write(http_req.encode())
    await writer.drain()
    while True:
        resp = await reader.readline()
        if not resp or resp == "\r\n":
            break

        resp = resp.decode().rstrip()
        print(url.hostname, "HTTP header>", resp)

    writer.close()
    await writer.wait_closed()


async def main() -> None:
    """ 메인 함수 실행 """
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(print_http_headers(url)))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    urls = [
        "https://www.sch.ac.kr",
        "https://www.google.com",
        "https://www.daum.net",
        "https://www.naver.com"
    ]

    asyncio.run(main())
