from socket import *


class FileCode:
    HTML = 1
    PNG = 2
    ICO = 3
    ERROR = -1


class WebServer:

    def __init__(self, port):
        self.port = port
        self.BUFSIZE = 1024
        self.ststic_path = "./static"

    def _min_type_parsing(self, http_request: str) -> str:
        """ http 요청 min_type 파싱 함수 """

        request_method = http_request.split("\r\n")[0]
        return request_method.split()[1].split("/")[-1]

    def _read_file(self, file_name: str) -> (bytes, int):
        """ file read 함수 """

        extension = file_name.split(".")[-1]

        try:
            if extension == "html":
                with open(file=f"{self.ststic_path}/{file_name}",
                          mode="r",
                          encoding="utf-8") as f:
                    file_data = f.read()

                return file_data.encode("euc-kr"), FileCode.HTML

            elif extension in ["png", "ico"]:
                with open(file=f"{self.ststic_path}/{file_name}",
                          mode="rb") as f:
                    file_data = f.read()

                if extension == "png":
                    return file_data, FileCode.PNG

                elif extension == "ico":
                    return file_data, FileCode.ICO

        except FileNotFoundError as e: # 페이지가 없는 경우
            return b"-1", FileCode.ERROR

    def _http_200_header(self, content_type: str) -> str:
        """ 성공 header """
        header = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Type: {content_type}\r\n"
            "\r\n"
        )
        return header

    def _http_404(self) -> str:
        """ 성공 header """
        html = (
            "HTTP/1.1 404 Not Found\r\n"
            "\r\n"
            "<html>"
            "<head><title>Hot Found</title></head>"
            "<body>Not Found</body>"
            "</html>"
        )
        return html

    def run(self) -> None:
        """ 웹 서버 실행 """
        self.sock = create_server(
            address=("", self.port),
            family=AF_INET,
            backlog=1
            )

        while True:
            conn, (remotehost, remoteport) = self.sock.accept()
            print("connected by", remotehost, remoteport)

            data = conn.recv(self.BUFSIZE)
            if not data:
                break

            request = data.decode()

            # 요청 파일
            request_file = self._min_type_parsing(request)
            read_file, file_code = self._read_file(file_name=request_file)

            if file_code == FileCode.ERROR: # 파일 존재 안함
                conn.send(self._http_404().encode())
                conn.close()
                continue

            elif file_code == FileCode.HTML:
                mimetype = "text/html"
                header = self._http_200_header(content_type=mimetype).encode()
                body = read_file

            elif file_code == FileCode.PNG:
                mimetype = "img/png"
                header = self._http_200_header(content_type=mimetype).encode()
                body = read_file

            elif file_code == FileCode.ICO:
                mimetype = "img/x-icon"
                header = self._http_200_header(content_type=mimetype).encode()
                body = read_file

            conn.send(header)
            conn.send(body)
            conn.close()

        self.sock.close()


if __name__ == '__main__':
    server = WebServer(port=80)
    server.run()