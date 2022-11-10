import socket

# create a socket object
sclient = socket.socket()

## cross-platofrm, telnet-ish connection

PORT = 12345
HOST = socket.gethostbyname("localhost")

# In order to "connect to a server - I must connect" to its socket
sclient.connect((HOST, PORT))

# Recieve somedata from our connected client (decode that string)
print(sclient.recv(1024).decode())

sclient.send("Who's there?".encode())

name = sclient.recv(1024).decode()
print(name)

sclient.send(f"{name} who?".encode())

print(sclient.recv(1024).decode())

sclient.send("Groan.".encode())

#close connection
sclient.close()