import binascii
import socket
import struct
from iphdr_1 import Iphdr


def unpack_Iphdr(buffer):
    unpacked = struct.unpack("!BBHHHBBH4s4s", buffer[:20])
    return unpacked


def get_packet_size(unpacked_ipheader):
    return unpacked_ipheader[2]


def get_protocol_id(unpacked_ipheader):
    return unpacked_ipheader[6]


def get_ip(unpacked_ipheader):
    src_ip = socket.inet_ntoa(unpacked_ipheader[8])
    dst_ip = socket.inet_ntoa(unpacked_ipheader[9])
    return (src_ip, dst_ip)


if __name__ == '__main__':
    ip = Iphdr(1000, 6, "10.0.0.1", "11.0.0.1")
    packed_iphdr = ip.pack_Iphdr()
    print(binascii.b2a_hex(packed_iphdr))

    unpacked_iphdr = unpack_Iphdr(packed_iphdr)
    print(unpacked_iphdr)
    print(f"Packet size:{get_packet_size(unpacked_iphdr)} Protocol: {get_protocol_id(unpacked_iphdr)} IP:{get_ip(unpacked_iphdr)}")