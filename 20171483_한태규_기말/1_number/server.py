"""
    aiohttp 서버 생성
"""

from aiohttp import web, web_request
import aiofiles


HOST_IP = "localhost"
PORT = 8080


async def send_html(request: web_request.Request) -> web.Response:
    """ HTML 응답하기 """
    file_name = "./imge_index.html"

    async with aiofiles.open(file_name, "r", encoding="utf-8") as f:
        msg = await f.read()
        return web.Response(text=msg, content_type="text/html")


async def send_image(request: web_request.Request) -> web.Response:
    """ 이미지 응답하기 """
    file_name = "./static/iot.png"
    async with aiofiles.open(file_name, "rb") as f:
        image = await f.read()
        return web.Response(body=image, content_type="image/png")


async def send_not_found(request: web_request.Request) -> web.Response:
    """ 페이지 404 """
    text = "Not Found"
    return web.Response(text=text, content_type="text/html")


if __name__ == '__main__':
    app = web.Application()

    app.add_routes([
        web.get('/', send_html),
        web.get('/static/iot.png', send_image),
        web.get('/*', send_not_found),
    ])
    web.run_app(app, port=8080)