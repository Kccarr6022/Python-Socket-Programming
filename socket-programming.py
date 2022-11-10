import socket
import random

HOST = socket.gethostbyname('localhost')
PORT = 12345
print(f"Our localhost ip is {HOST} and our port is {PORT}")

def joke1(conn):
    conn.send("Boo".encode())
    print(conn.recv(1024).decode())

    conn.send("Don't cry, I just want to chat".encode())
    print(conn.recv(1024).decode())

def joke2(conn):
    conn.send("Auto".encode())
    print(conn.recv(1024).decode())

    conn.send("You auto know its me by now".encode())
    print(conn.recv(1024).decode())

def joke3(conn):
    conn.send("Kenya".encode())
    print(conn.recv(1024).decode())

    conn.send("Kenya stop with the jokes already?".encode())
    print(conn.recv(1024).decode())

def joke4(conn):
    conn.send("Arthur".encode())
    print(conn.recv(1024).decode())

    conn.send("Arthur any more knock-knock jokes".encode())
    print(conn.recv(1024).decode())

def joke5(conn):
    conn.send("Beak".encode())
    print(conn.recv(1024).decode())

    conn.send("Beak careful, that pan is hot!".encode())
    print(conn.recv(1024).decode())

def server_init():
        ## Create a socket "instance" (object)
    simple = socket.socket()
    print("Socket created successfully")

    ## Bind to a port
    simple.bind((HOST, PORT))
    print(f"Socket is binded to {PORT}")
    return simple

jokes = {
    1 : joke1,
    2 : joke2,
    3 : joke3,
    4 : joke4,
    5 : joke5,
}

## infinite loop - until interrupt or error
def server_listen(server):
    server.listen(5)
    while True:
        # Establish connection for our simple server
        conn, addr = server.accept()
        print(f"Connection accepted from {addr}")

        # Starts knock knock joke
        conn.send("Knock Knock!".encode())

        print(conn.recv(1024).decode())

        jokes[random.randint(1,5)](conn)

        ## We're closing after a single person (so no infinity looping process)
        conn.close()
        break

def main() -> int:
    server = server_init()
    server_listen(server)
    return 0

if __name__ == "__main__":
    main()