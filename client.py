import socket, sys

def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print("Failed to create socket")
        sys.exit()
    
    print("Socket created successfully")
    return s

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except (socket.gaierror): 
        print("Host name cannot be resolved")
        sys.exit()
    
    print('IP address of' + host + "is" + remote_ip)
    return remote_ip
    
def send_data(serversocket, payload):
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("Send Failed")
        sys.exit()
    
    print("Payload sent successfully")

def main():
    try:
        host = "www.google.com"
        port = 80

        payload = 'GET / HTTP/1.0\r\nHost: '+host+'\r\n\r\n'
        buffer_size = 4096

        s = create_tcp_socket()
        remote_ip = get_remote_ip(host)

        s.connect((remote_ip, port))
        print('Socket connected to' + host + 'on IP' + remote_ip)

        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

main()