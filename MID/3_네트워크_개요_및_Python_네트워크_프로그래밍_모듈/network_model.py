"""
    ipaddress 모듈

    파이썬에서 IP 주소를 표현하고 처리하기 위해 사용하는 모듈
"""

# ------------------------------------------------------------------------------------------- #
"""
    ip_address()
        P IP 주소 객체를 생성하는 함수
        P IPv4 또는 IPv6를 자동 인식
"""
# import ipaddress
# addr4 = ipaddress.ip_address("192.0.2.1")
#
# # IPv4
# print(type(addr4))
# # <class 'ipaddress.IPv4Address'>
#
# print(addr4)
# # 192.0.2.1
#
# print(addr4.version)
# # 4
#
# addr6 = ipaddress.ip_address("2001:A8::1")
#
# # IPv6
# print(type(addr6))
# # <class 'ipaddress.IPv6Address'>
#
# print(addr6)
# # 2001:a8::1
#
# print(addr6.version)
# # 6

# ------------------------------------------------------------------------------------------- #
"""
    ip_address()
        P IP 주소 객체를 생성하는 함수
        P IPv4 또는 IPv6를 자동 인식
"""
# import ipaddress
# net = ipaddress.ip_network("114.71.200.0/24")
#
# print(net)
# # 114.71.200.0/24
#
# print(net.with_netmask)
# # 114.71.200.0/255.255.255.0
#
# print(net.num_addresses)
# # 256
#
# print(net.netmask)
# # 255.255.255.0
#
# print(net.hostmask)
# # 0.0.0.255

# ------------------------------------------------------------------------------------------- #
"""
    네트워크에서 사용 가능한 호스트 주소 알아보기
"""
# net = ipaddress.ip_network("114.71.200.0/24")
# for x in net.hosts():
#     print(x)
#
# """
#     in 연산자를 이용하여 호스트 주소가 네트워크에 속하는지 알아보기
# """
# net = ipaddress.ip_network('114.71.220.0/24')
# addr = ipaddress.ip_address('114.71.220.95')
# print(addr in net)
# # True
#
# addr = ipaddress.ip_address('192.168.0.1')
# print(addr in net)
# # False

# ------------------------------------------------------------------------------------------- #
"""
    호스트 정보 관련 함수
"""
# import socket
# name = socket.gethostname()
# print(name)
# # HanTaeGyu
#
# print(socket.gethostbyname(name))
# # 192.168.56.1
#
# print(socket.gethostbyname('homepage.sch.ac.kr'))
# # 220.69.189.98
#
# print(socket.gethostbyname_ex('homepage.sch.ac.kr'))
# # ('homepage.sch.ac.kr', [], ['220.69.189.98'])
#
# print(socket.gethostbyaddr('220.69.189.98'))
# # ('homepage.sch.ac.kr', [], ['220.69.189.98'])
#
# print(socket.getfqdn('220.69.189.98'))
# # homepage.sch.ac.kr
#
# print(socket.getfqdn('www.daum.net'))
# # www.daum.net
#
# print(socket.getfqdn('www.google.com'))
# # nrt12s22-in-f4.1e100.net

# ------------------------------------------------------------------------------------------- #
"""
    여러 사이트의 IP 주소를 확인하는 프로그램 
"""
import socket
# HOSTS = [
#     'www.sch.ac.kr',
#     'homepage.sch.ac.kr',
#     'www.daum.net',
#     'www.google.com',
#     'iot'
# ]
# for host in HOSTS:
#     try:
#         print('{} : {}'.format(host, socket.gethostbyname(host)))
#     except socket.error as msg:
#         print('{} : {}'.format(host, msg))
#
# print(socket.getservbyname('http'))
# # 80
#
# print(socket.getservbyname('ftp'))
# # 21
#
# print(socket.getservbyname('ssh'))
# # 22
#
# print(socket.getservbyname('https'))
# # 443
#
# print(socket.getservbyport(80))
#
# print(socket.getservbyport(25))

# import socket
# for port in [80, 443, 21, 25, 143, 993, 110, 995]:
#     url ='{}://example.co.kr/'.format(socket.getservbyport(port))
#     print('{:4d}'.format(port), url)


# ------------------------------------------------------------------------------------------- #
"""
    IPv4 주소 표현 
"""
import binascii
import socket
import sys
for string_address in ['114.71.220.95']:
    packed = socket.inet_aton(string_address)
    # inet_aton(): 문자열 주소를 4바이트 bytes 객체로 변환
    # inet_ntoa(): 4바이트 bytes 객체를 문자열 주소로 변환
    print ('Original:', string_address)
    print ('Packed :', binascii.hexlify(packed))
    print ('Unpacked:', socket.inet_ntoa(packed))
