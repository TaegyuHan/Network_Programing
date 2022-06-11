"""
    IoT 디바이스를 제어하는 HTTP 서버
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from urllib import parse

HOST_IP = "localhost"
PORT = 8080


class HttpHandler(BaseHTTPRequestHandler):
    """ 서버 """

    def do_GET(self) -> None:
        """ GET 메소드 """
        self.route()

    def do_POST(self) -> None:
        """ POST 메소드 """
        self.route()

    def route(self) -> None:
        """ url 라우터 """
        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path

        if real_path == "/":
            self.send_html()
        elif real_path == "/button":
            self.proc_query()
        elif real_path == "/form_get":
            self.proc_query()
        elif real_path == "/form_post":
            self.proc_form_post()
        else:
            self.response(HTTPStatus.NOT_FOUND, "<h1>Not Found</h1>")

    def send_html(self) -> None:
        """ html 보내기 """
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html_type = "index_button.html"
        # html_type = "index_get.html"
        # html_type = "index_post.html"

        with open(html_type, 'r', encoding="utf-8") as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def proc_query(self) -> None:
        """ GET 쿼리로 데이터 받기 """
        parsed_path = parse.urlparse(self.path)
        query = parsed_path.query

        parsed_query = parse.parse_qs(query)

        # 쿼리 status=on을 {'status': ['on']} 으로 파싱
        status = parsed_query['status'][0]

        if status == "on":
            message = "<h2>LED in IoT Device is now turned on <h2>"
            # GP.output(18, 1) # 라즈베이 파이 LED 제어 코드
        elif status == "off":
            message = "<h2>LED in IoT Device is now turned off <h2>"
            # GP.output(18, 0) # 라즈베이 파이 LED 제어 코드
        else:
            message = "<h2>Wrong status</h2>"
        self.response(HTTPStatus.OK, message)

    def proc_form_post(self) -> None:
        """ POST로 데이터 받기 """
        content_length = int(self.headers["content-Length"])
        # HTTP Request의 body 읽기
        body = self.rfile.read(content_length).decode()
        parsed_body = body.split("=")
        status = parsed_body[1]

        if status == "on":
            message = "<h2>LED in IoT Device is now turned on <h2>"
            # GP.output(18, 1) # 라즈베이 파이 LED 제어 코드
        elif status == "off":
            message = "<h2>LED in IoT Device is now turned off <h2>"
            # GP.output(18, 0) # 라즈베이 파이 LED 제어 코드
        else:
            message = "<h2>Wrong status</h2>"
        self.response(HTTPStatus.OK, message)

    def response(self, status_code: int, body) -> None:
        """ 응답 메시지 전송 """
        self.send_response(status_code)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == '__main__':
    httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
    print(f"Serving HTTP on {HOST_IP}:{PORT}")
    httpd.serve_forever()

