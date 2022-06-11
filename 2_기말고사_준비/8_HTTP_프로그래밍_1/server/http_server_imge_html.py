"""
    간단한 웹 서버: imge html 응답하기
    웹 서버
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

HOST_IP = "localhost"
PORT = 8080


class HttpHandler(BaseHTTPRequestHandler):
    """ 서버 생성하기 """

    def do_GET(self) -> None:
        """ GET 메소드 실행하기 """
        self.route()

    def route(self) -> None:
        """ html 라우터 """
        if self.path == "/":  # index 전송
            self.send_html()
        elif self.path == "/static/iot.png":  # image 전송
            self.send_imge()
        else:  # 존재하지 않는 파일
            self.response(HTTPStatus.NOT_FOUND, "Not Found")

    def send_html(self) -> None:
        """ html 전송 """
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        with open("imge_index.html", "r", encoding="utf-8") as f:
            msg = f.read()
            self.wfile.write(msg.encode("euc-kr"))

    def send_imge(self) -> None:
        """ 이미지 전송 """
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "image/png")
        self.end_headers()
        with open("./static/iot.png", "rb") as f:
            msg = f.read()
            self.wfile.write(msg)

    def response(self, status_code: int, body) -> None:
        """ 응답 """
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == '__main__':
    httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
    print(f"Server HTTP on {HOST_IP}:{PORT}")
    httpd.serve_forever()