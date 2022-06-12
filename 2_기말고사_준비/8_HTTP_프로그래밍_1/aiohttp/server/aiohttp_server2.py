"""
    aiohttp 모듈: 서버
"""

from aiohttp import web, web_request
import aiofiles


async def send_html(request: web_request.Request) -> web.Response:
    """ HTML 응답하기 """
    # file_name = "index_button.html"
    # file_name = "index_get.html"
    file_name = "index_post.html"

    async with aiofiles.open(file_name, "r") as f:
        msg = await f.read()
        return web.Response(text=msg, content_type="text/html")


async def proc_query(request: web_request.Request) -> web.Response:
    """ HTML GET 응답하기 """
    parsed_query = request.query_string.split("=")
    print(request)

    status = parsed_query[1]
    if status == "on":
        message = "<h2>LED in IoT Device is now turned on</h2>"
        # GP.output(18, 1)  # 라즈베리 파이 제어 코드
    elif status == "off":
        message = "<h2>LED in IoT Device is now turned off</h2>"
        # GP.output(18, 0)  # 라즈베리 파이 제어 코드
    else:
        message = "<h2>Wrong status</h2>"

    return web.Response(text=message, content_type="text/html")


async def proc_form_post(request: web_request.Request) -> web.Response:
    """ HTML Post 응답 """
    data = await request.post()
    print(type(request))

    status = data["status"]
    if status == "on":
        message = "<h2>LED in IoT Device is now turned on</h2>"
        # GP.output(18, 1)  # 라즈베리 파이 제어 코드
    elif status == "off":
        message = "<h2>LED in IoT Device is now turned off</h2>"
        # GP.output(18, 0)  # 라즈베리 파이 제어 코드
    else:
        message = "<h2>Wrong status</h2>"

    return web.Response(text=message, content_type="text/html")


if __name__ == '__main__':
    app = web.Application()

    app.add_routes([web.get('/', send_html),
                    web.get('/button', proc_query),
                    web.get('/form_get', proc_query),
                    web.post('/form_post', proc_form_post)])

    web.run_app(app, port=8000)