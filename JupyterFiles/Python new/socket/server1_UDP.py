import socket

s1=socket.socket(type=socket.SOCK_DGRAM)
host='127.0.0.1' 
port=5001

#print(socket.gethostname))
try:
 s1.bind((host, port))
except Exception as ex:
 print(ex)

print("server listening...")

while True:
 data, address=s1.recvfrom(1024)     
 print("got data from ,",address)
 print(data.decode())
 s1.sendto(b"hello i m UDP Server...",address) 
 break
s1.close()