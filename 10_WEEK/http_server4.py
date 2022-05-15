from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_IP = "localhost"
PORT = 8080

class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.route()

    def route(self):
        if self.path == "/":
            self.send_html()
        elif self.path == "/iot.png":
            self.send_image()
        else:
            self.responses(404, "Not Found")

    def send_html(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "r", encoding="utf-8") as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def send_image(self):
        self.send_response(200)
        self.send_header("Content-type", "image/jpg")
        self.end_headers()
        with open("iot.jpg", "rb") as f:
            msg = f.read()
            self.wfile.write(msg.encode())

    def response(self, status_code, body):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


httpd = HTTPServer((HOST_IP, PORT), HttpHandler)
print(f"Serving HTTP on {HOST_IP}:{PORT}")
httpd.serve_forever()