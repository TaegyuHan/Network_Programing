a = 1
zero = 0
data = zero.to_bytes(4, "big")*3
print(data[:4], data[4:8], data[8:])
