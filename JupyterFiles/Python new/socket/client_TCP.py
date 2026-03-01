import socket

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1' 
port=5000
s1.connect((host, port))

data=s1.recv(1024).decode()
print(data)
s1.send(b"hello i m TCP Client...")

s1.close()