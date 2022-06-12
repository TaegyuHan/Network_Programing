"""
    aiohttp 모듈: 서버
"""

from aiohttp import web, web_request


async def handler(request: web_request.Request) -> web.Response:
    """ 웹 응답 함수 """

    name = request.match_info.get("name", "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/', handler),
        web.get('/{name}', handler)
    ])

    web.run_app(app, port=8080)