import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPADDRESS=s.getsockname()[0]
print(IPADDRESS)
s.close()
