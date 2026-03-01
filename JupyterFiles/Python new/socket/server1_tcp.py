import socket

s1=socket.socket()
host='127.0.0.1' 
port=5000

#print(socket.gethostname))
try:
 s1.bind((host, port))
except Exception as ex:
 print(ex)

s1.listen()
print("server listening...")

while True:
 con, address=s1.accept()     
 print("got connection from ,",address)
 con.send(b"hello i m TCP Server...") 
 data=con.recv(1024).decode()
 print(data)
 con.close()
 break
s1.close()