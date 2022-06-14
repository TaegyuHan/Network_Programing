"""
    asyncio 온도 습도 서버
"""

import asyncio
import random
from socket import *


PORT = 7777
BUF_SIZE = 1024


async def handler(conn: socket, addr: tuple[str, int]) -> None:
    """
        echo 서버 receive 코루틴
        사용자로부터 ‘Request’ 메시지를 수신하면 온도, 습도, 조도를 전송

        - 온도: 1~50 사이의 임의의 정수를 반환
        - 습도: 1~100 사이의 임의의 정수를 반환
        - 조도: 1~150 사이의 임의의 정수를 반환
    """
    while True:
        data = await asyncio.to_thread(conn.recv, BUF_SIZE)

        if data.decode() == "quit" or not data:
            break

        zero = 0
        make_data = {
            "temperature": random.randint(1, 50), # 온도
            "humidity": random.randint(1, 100), # 습도
            "illumination": random.randint(1, 150) # 조도
        }

        # 바이트 코드 반환
        data_decode = data.decode()
        if data_decode == "1":
            send_data = make_data["temperature"].to_bytes(4, "big") \
                   + (zero.to_bytes(4, "big") * 2)
        elif data_decode == "2":
            send_data = zero.to_bytes(4, "big") \
                   + make_data["humidity"].to_bytes(4, "big") \
                   + zero.to_bytes(4, "big")
        elif data_decode == "3":
            send_data = (zero.to_bytes(4, "big") * 2) \
                   + make_data["illumination"].to_bytes(4, "big")

        print(f"{addr} Received message: ", send_data)
        conn.send(send_data)


async def main() -> None:
    """ 메인 함수 """
    sock = socket()
    sock.bind(("", PORT))
    sock.listen(5)
    print("Run Server")

    while True:
        client, addr = await asyncio.to_thread(sock.accept)
        print(addr, "accepted")
        asyncio.create_task(handler(client, addr))


if __name__ == '__main__':
    asyncio.run(main())
