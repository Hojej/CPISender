import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = ("127.0.0.1", 4000)

file_name = "/home/ubuntu/workspace/CPISender/CPISender/CPISender/15_09_00.0347.bin"

try:
	f=open(file_name,"rb") 
	data = f.read()
	#data, server = client_socket.recvfrom(1024)
	client_socket.sendto(data,addr)
	print("Sent")
except socket.timeout:
        print('REQUEST TIMED OUT')

client_socket.close()
f.close()
