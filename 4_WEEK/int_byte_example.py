
# int 데이터 송신
byte1 = (1).to_bytes(length=4, byteorder="big")
byte2 = (1).to_bytes(length=2, byteorder="little")
print(byte1)
print(byte2)

# int 데이터 수신
int1 = int.from_bytes(bytes=byte1, byteorder="big")
int2 = int.from_bytes(bytes=byte2, byteorder="little")
print(int1)
print(int2)