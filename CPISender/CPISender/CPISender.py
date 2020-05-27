import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = ("127.0.0.1", 4000)

file_name = "/home/ubuntu/workspace/CPISender/CPISender/CPISender/15_09_00.0347.bin"

count = 0
with open(file_name,"rb") as f:
	data = f.read(6162)
	#data, server = client_socket.recvfrom(1024)
	while(data):
		if(client_socket.sendto(data,addr)):
			data = f.read(6162)
			print("Sending..")
			count = count + 1
print(count)

client_socket.close()
f.close()
print("Closing")
