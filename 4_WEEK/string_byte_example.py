import socket

a = 12345678
b = str(a)

# 정수 > 문자열 > byte
print("문자열 :", f"'{b}'")
c = b.encode()
print("Byte(문자열) :", c)

# byte > 문자열 > 숫자
d = c.decode()
print("문자열 :", f"'{d}'")
print("정수 :", int(d))