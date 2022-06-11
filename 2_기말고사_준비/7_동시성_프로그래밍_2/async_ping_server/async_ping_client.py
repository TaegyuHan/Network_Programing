"""
    ping 클라이언트
"""
import asyncio


async def ping_client():
    """ 핑 클라이언트 """
    reader, writer = await asyncio.open_connection(host="localhost", port=8000)

    for _ in range(10):
        writer.write(b"ping")
        print("send: ping")

        data = await reader.read(8)  # byte
        print('recv:', data.decode())
        await asyncio.sleep(1)

    writer.write(b"done")
    print("send: ping")
    writer.close()
    await writer.wait_closed()
    print("connection was closed")

if __name__ == '__main__':
    asyncio.run(ping_client())