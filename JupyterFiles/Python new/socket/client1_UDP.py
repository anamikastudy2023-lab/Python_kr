import socket

s1=socket.socket(type=socket.SOCK_DGRAM)
host='127.0.0.1' 
port=5001

s1.sendto(b"hello i m UDP Client...",(host, port))
data,address=s1.recvfrom(1024)
print("got data from ",address)
print(data.decode())
s1.close()