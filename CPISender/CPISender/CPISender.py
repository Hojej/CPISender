import time
import socket

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    addr = ("127.0.0.1", 4000)

    fileName = ""

    try:
        f=open(file_name,"rb") 
        data = f.read()
        data, server = client_socket.recvfrom(1024)
        client_socket.sendto(data,addr)
        print("Sent")
    except socket.timeout:
        print('REQUEST TIMED OUT')

client_socket.close()
f.close()