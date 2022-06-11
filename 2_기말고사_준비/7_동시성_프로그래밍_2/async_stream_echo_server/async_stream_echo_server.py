"""
    스트림 streams

    asyncio에서 제공하는 비동기 소켓통신을 위한 고수준의 TCP용 통신 모듈

    콜백이나 저수준의 프로토콜과 트랜스포트를 사용하지 않고, 데이터를
    송수신할 수 있게 해 줌

    연결을 통한 스트림 생성은 매우 간단하며, 통신에 필요한 '스트림 리더stream
    reader'와 '스트림 라이터stream writer'를 어떻게 사용 하느냐만 고려하면 됨


    스트림 생성
    서버:
        asyncio.start_server(client_connected_cb, host, port, ...)

        client_connected_cb: 클라이언트의 요청을 처리하는 핸들러 함수

            해당 함수는 일반 함수이거나 코루틴 함수 일 수 있음

            코루틴 함수면, 자동으로 Task로 예약됨

        소켓 서버를 시작하고, 새 클라이언트와의 연결이 이루어질 때 client_connected_cb
        콜백 함수가 호출되고, (스트림 리더, 스트림 라이터) 쌍을 인자로 넘겨줌


    클라이언트:
        asyncio.open_connection(host, port, ...)

            TCP 서버와 네트워크 연결을 수행하고, (스트림 리더, 스트림 라이터) 쌍을 반환
"""

import asyncio
from asyncio import StreamReader, StreamWriter


PORT = 2500
BUF_SIZE = 1024


async def handler_echo(reader: StreamReader, writer: StreamWriter) -> None:
    """ 소켓 핸들러 함수 """

    while True:
        data = await reader.read(BUF_SIZE)
        addr = writer.get_extra_info("peername")
        print(f"Received '{data.decode()}' from '{addr}'")

        writer.write(data)
        await writer.drain()
        print(f"Send: '{data.decode()}'")


async def main() -> None:
    """ 메인 함수 """
    server = await asyncio.start_server(handler_echo, host="", port=PORT)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())































