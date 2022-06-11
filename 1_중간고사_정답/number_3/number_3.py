import socket

ip = "220.69.189.125"
port = 443

url = socket.getfqdn(ip)
https_string = socket.getservbyport(port)

# A
print(url)

# B
print(https_string)

# C
print(f"{https_string}://{url}")

# D
print(bytes(ip.encode()))