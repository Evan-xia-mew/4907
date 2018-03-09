import socket
s=socket.socket()
s.connect(('192.168.0.17',2000))   
data=s.recv(512)
print ('the data received\n')
s.send('hihi I am client')


s.close()
