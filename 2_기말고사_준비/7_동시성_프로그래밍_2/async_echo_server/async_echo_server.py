"""
    코루틴: 에코 서버 만들기
"""

import asyncio
from socket import *


PORT = 2500
BUF_SIZE = 1024


async def handler(conn: socket, addr: tuple[str, int]) -> None:
    """ echo 서버 receive 코루틴 """
    while True:
        data = await asyncio.to_thread(conn.recv, BUF_SIZE)
        if not data:
            break

        print(f"{addr} Received message: ", data.decode())
        conn.send(data)


async def main() -> None:
    """ 메인 함수 """
    sock = socket()
    sock.bind(("", PORT))
    sock.listen(5)

    while True:
        client, addr = await asyncio.to_thread(sock.accept)
        print(addr, "accepted")
        asyncio.create_task(handler(client, addr))


if __name__ == '__main__':
    asyncio.run(main())
