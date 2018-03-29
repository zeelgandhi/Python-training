#Client server architecture- socket programming

#Server side :
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(2)
while True:
    c,address= s.accept()   #c=client
    print ('yes thankyou I got connection')
    c.send("Thank you for your response on connection")
    c.close()
