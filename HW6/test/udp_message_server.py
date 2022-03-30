import unittest
from collections import deque

from HW6.udp_message_server import Server


class TestServer(unittest.TestCase):

    def test_data_parsing(self):
        """ 메시지 데이터 파싱 테스트 """
        BAD_REQUEST = 400
        S = Server()

        # 성공
        result, data, test = S._data_parsing("send 1 Hello, IoT")
        self.assertEqual((result, data, test), ("send", "1", "Hello, IoT"))

        result, data, test = S._data_parsing("send 1 This is UDP")
        self.assertEqual((result, data, test), ("send", "1", "This is UDP"))

        result, data, test = S._data_parsing("send 1 See you later!")
        self.assertEqual((result, data, test), ("send", "1", "See you later!"))

        result, data, test = S._data_parsing("receive 1")
        self.assertEqual((result, data, test), ("receive", "1", ""))

        result, data, test = S._data_parsing("receive 2")
        self.assertEqual((result, data, test), ("receive", "2", ""))

        # 싪패
        result, data, test = S._data_parsing("send1See you later!")
        self.assertEqual(BAD_REQUEST, result)

        result, data, test = S._data_parsing("send1 Hello, IoT")
        self.assertEqual(BAD_REQUEST, result)

        result, data, test = S._data_parsing("send 1This is UDP")
        self.assertEqual(BAD_REQUEST, result)

        result, data, test = S._data_parsing("send1See you later!")
        self.assertEqual(BAD_REQUEST, result)

        result, data, test = S._data_parsing("rceive 1")
        self.assertEqual(BAD_REQUEST, result)

        result, data, test = S._data_parsing("receive2")
        self.assertEqual(BAD_REQUEST, result)

        result, data, test = S._data_parsing("quit")
        self.assertEqual(BAD_REQUEST, result)

    def test_insert_data(self):
        """ 데이터 넣기 확인 """

        S = Server()
        S._insert_data("1", "This is UDP")
        S._insert_data("1", "This is UDP2")
        print(S.data)

    def test_select_data(self):
        """ 데이터 주기 확인 """
        d = deque(["hello"])
        print(d.popleft())
        print(d.popleft())

