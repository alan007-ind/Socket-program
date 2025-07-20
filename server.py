import socket as s
import sys
import select as sel

HOST = ''
PORT = 4444
SOCKET_LIST = []
RECV_BUFFER = 4096

def server_chat():
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    SOCKET_LIST.append(server_socket)
    print("LAHTP CHAT SERVER listening on port", PORT)

    while True:
        ready_read, _, _ = sel.select(SOCKET_LIST, [], [], 0)
        for sock in ready_read:
            if sock == server_socket:
                client_socket, addr = server_socket.accept()
                SOCKET_LIST.append(client_socket)
                print(f"Client {addr[0]}:{addr[1]} connected")
                broadcast(server_socket, client_socket, f"{addr} entered the chat\n".encode())
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        print(f"[{sock.getpeername()}]: {data.decode(errors='ignore').strip()}")
                        broadcast(server_socket, sock, data)
                    else:
                        disconnect(sock)
                except:
                    disconnect(sock)

def broadcast(server_socket, client_socket, message):
    for sock in SOCKET_LIST:
        if sock != server_socket and sock != client_socket:
            try:
                sock.send(message)
            except:
                sock.close()
                if sock in SOCKET_LIST:
                    SOCKET_LIST.remove(sock)

def disconnect(sock):
    try:
        peer = sock.getpeername()
        print(f"Client {peer} disconnected")
        if sock in SOCKET_LIST:
            SOCKET_LIST.remove(sock)
        broadcast(None, sock, f"{peer} left the chat\n".encode())
        sock.close()
    except:
        pass

if __name__ == '__main__':
    sys.exit(server_chat())
