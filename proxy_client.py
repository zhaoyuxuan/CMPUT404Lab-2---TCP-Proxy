import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024
payload = ""

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)

        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect(('127.0.0.1',8001))

main()

