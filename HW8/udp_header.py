import binascii
import struct


class Udphdr:

    def __init__(self,
                 source_port: int,
                 destination_port: int,
                 length: int,
                 check_sum: int):

        self.source_port = source_port # 2byte
        self.destination_port = destination_port # 2byte
        self.length = length # 2byte
        self.check_sum = check_sum # 2byte

    def pack_udphdr(self):
        """ byte 패킷 생성 """
        packed = b""
        packed += struct.pack(
            "!4H",
            self.source_port,
            self.destination_port,
            self.length,
            self.check_sum
        )
        return packed


def unpack_udphdr(buffer):
    """ UDP 해더를 unpack하는 함수 """
    unpacked = struct.unpack("!4H", buffer)
    return unpacked


def get_src_port(unpacked_iphdr):
    """ 송신 포트 확인 """
    return unpacked_iphdr[0]


def get_dst_port(unpacked_iphdr):
    """ 수신 포트 확인 """
    return unpacked_iphdr[1]


def get_length(unpacked_iphdr):
    """ 길이 확인 """
    return unpacked_iphdr[2]


def get_check_sum(unpacked_iphdr):
    """ 헤더 정보 손상 정보 확인 """
    return unpacked_iphdr[3]


if __name__ == '__main__':
    # 실행결과
    udp = Udphdr(5555, 80, 1000, 0xFFFF)
    packed_udphdr = udp.pack_udphdr()
    print(binascii.b2a_hex(packed_udphdr))

    unpacked_iphdr = unpack_udphdr(packed_udphdr)
    print(unpacked_iphdr)

    print((
        f"Source Port:{get_src_port(unpacked_iphdr)} "
        f"Destination Port:{get_dst_port(unpacked_iphdr)} "
        f"Length:{get_length(unpacked_iphdr)} "
        f"Checsum:{get_check_sum(unpacked_iphdr)}"
    ))