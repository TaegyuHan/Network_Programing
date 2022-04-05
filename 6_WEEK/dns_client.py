import socket
import struct
import sys


class DnsClient:

    def __init__(self, domain_name):

        self.domain_name = domain_name

        # DNS Query Header
        self.transation_id = 1
        self.flag = 0x0100
        self.questions = 1
        self.answerRRs = 0
        self.authorityRRs = 0
        self.additionalRRs = 0

    def response(self, packet): # processing dns response
        dns_header = packet[:12]
        dns_data = packet[12:].split(b"\x00", 1)

        ansRR = packet[12+len(dns_data[0])+5:12+len(dns_data[0])+21]
        rr_unpack = struct.unpack("!2sHHIH4s", ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domain_name, ip_addr)

    def query(self): # create dns query
        # DNS header packing
        query = struct.pack("!HH", self.transation_id, self.flag)
        query += struct.pack("!HH", self.questions, self.answerRRs)
        query += struct.pack("!HH", self.authorityRRs, self.additionalRRs)

        part = self.domain_name.split(".")

        for i in range(len(part)):
            query = query + struct.pack("!B", len(part[i]))
            query = query + part[i].encode()

        query = query + b'\x00'

        query_type = 1 # Type: A
        query_class = 1
        query = query + struct.pack("!HH", query_type, query_class)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = ("220.69.193.130", 53) # 순천향대학교 DNS 서버 주소
        sock.sendto(query, addr)
        packet, address = sock.recvfrom(65535)
        self.response(packet)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = DnsClient(sys.argv[1])
        client.query()