"""
    간단한 웹 서버: imge_index.html 응답하기
    웹 서버
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus


HOST_IP = "localhost"
PORT = 8080


class HttpHandler(BaseHTTPRequestHandler):
    """ 웹서버 실행 """

    def do_GET(self) -> None:
        """ GET 메소드 """
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        with open("index.html", "r", encoding="utf-8") as f:
            msg = f.read()
            self.wfile.write(msg.encode())



if __name__ == '__main__':
    httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
    print(f"Serving HTTP on {HOST_IP}:{PORT}")
    httpd.serve_forever()