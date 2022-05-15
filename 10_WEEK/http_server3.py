"""
    웹 서버 실행하기
    index.html 읽어서 실행
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

HOST_IP = "localhost"
PORT = 8080

class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """ GET 요청 해결 """
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        with open("index.html", "r", encoding="utf-8") as f:
            msg = f.read()
            self.wfile.write(msg.encode())

httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
print(f"Serving HTTP on {HOST_IP}:{PORT}")
httpd.serve_forever()