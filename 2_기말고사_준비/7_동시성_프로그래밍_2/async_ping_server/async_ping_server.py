"""
    asyncio를 이용한 ping 서버 프로그램
"""

import asyncio
from asyncio import StreamReader, StreamWriter


async def handle_asyncclient(reader: StreamReader, writer: StreamWriter) -> None:
    """ 클라이언트 호출 함수 """
    print("client :", writer.get_extra_info("peername"))

    while True:
        data = await reader.read(8)  # byte

        if data == b"ping":
            writer.write(b"pong")
            await writer.drain()
            print("recv: ping -> send: pong")

        elif data == b"done":
            print("recv: done")
            break

        elif len(data) == 0:
            break

    writer.close()
    await writer.wait_closed()
    print("connection was close")


async def server_asyncmain() -> None:
    """ 서버 실행 """
    server = await asyncio.start_server(handle_asyncclient, 'localhost', 8000)
    print("server started")
    await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(server_asyncmain())