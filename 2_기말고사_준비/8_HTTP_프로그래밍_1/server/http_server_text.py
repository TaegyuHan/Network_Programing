"""
    간단한 웹 서버: 텍스트 응답하기
    웹 서버
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

HOST_IP = "localhost"
PORT = 8080


class HttpHandler(BaseHTTPRequestHandler):
    """ 서버 실행 클래스 """

    def do_GET(self) -> None:
        """ GET 메소드 """
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b"Hello IoT!")


if __name__ == '__main__':
    httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
    print(f"serving HTTP on {HOST_IP}:{PORT}")
    httpd.serve_forever()
