"""
    간단한 HTTPS 웹서버
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import ssl


HOST_IP = "localhost"
PORT = 8080


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self) -> None:
        """ GET 메소드 호출 """
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b"<h1>Hello, IoT!</H1>")


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.pem", keyfile="server.key")

httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
print(f"Serving HTTP on {HOST_IP}:{PORT}")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()