
import socket, time, sys

HOST = ""
PORT = 8001
BUFFERSIZE = 1024

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except (socket.gaierror):
        sys.exit()

    return remote_ip

def main():

    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = get_remote_ip(host)

                proxy_end.connect((remote_ip,port))
                send_full_data = conn.recv(BUFFERSIZE)

                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)
                data = proxy_end.recv(BUFFERSIZE)
                print(data)

                conn.send(data)
            
            conn.close()
    
main()


        