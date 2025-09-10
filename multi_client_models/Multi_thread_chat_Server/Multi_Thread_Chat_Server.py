import threading
import socket

host = '10.11.180.29'
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen()
sock_list = []

print(f"Chat server is running on {host}:{port}...\n")

def broadcast(sender, data, sender_name):
    for client in sock_list:
        if client != sender:
            client.sendall(sender_name.encode() + b": " + data)
    print(sender_name + ": " + data.decode(errors='ignore').strip())

def client_thread(client_socket, name):
    while True:
        data = client_socket.recv(1024)
        if not data:
            sock_list.remove(client_socket)
            client_socket.close()
            for client in sock_list:
                client.sendall(f"{name} has left the chat\n".encode())
            print(f"{name} has left the chat")
            break
        broadcast(client_socket, data, name)

while True:
    conn, addr = sock.accept()
    conn.send(b"Welcome to Multi-Chat Server\nNow enter your nick name:\n")
    name = conn.recv(1024).decode().strip()
    sock_list.append(conn)
    conn.send(f"Welcome {name}, you are now connected!\n".encode())
    for client in sock_list:
        if client != conn:
            client.sendall(f"{name} has joined the chat\n".encode())
    print(f"{name} has joined the chat")

    t = threading.Thread(target=client_thread, args=(conn, name))
    t.start()
