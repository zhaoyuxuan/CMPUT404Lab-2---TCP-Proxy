import socket, sys

def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except:
        print("Fail to create scoket")
        sys.exit()

    return s
def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except (socket.gaierror):
        sys.exit()

    return remote_ip

def main():
    try:
        host = "www.google.com"
        port = 80
        payload = "GET / HTTP/1.0\r\nHost:" + host + "\r\n\r\n"
        buffer_size = 4096

        s = create_tcp_socket()
        remote_ip = get_remote_ip(host)
        s.connect((remote_ip, port))

        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data+=data
        print(full_data)


    except:
        sys.exit()
    finally:
        s.close()
    




