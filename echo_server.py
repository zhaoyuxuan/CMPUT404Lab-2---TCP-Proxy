import socket
import time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            full_data = conn.recv(BUFFER_SIZE)
            print("Connected by", addr)

            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

main()
