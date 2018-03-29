import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))  #s=server
print (s.recv(1024))  #1024bytes
s.close()
