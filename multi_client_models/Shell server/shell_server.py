import socket
import subprocess

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print(f"{addr[0]} Connected with back port: {addr[1]}")
while True:
    data = conn.recv(1024)
    if not data:
        break
    else:
        data = data.decode()
        data = data.strip()
        print(f"cmd > {data}")
        if data == "quit":
            break
        else:
            separator = ("\n" + "=" * 99 + "\n")
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            print(stderr)
            data = "\n" + stdout.decode(errors='replace') + stderr.decode(errors='ignore')
            conn.sendall((data + separator + "\r\n$ ").encode())

s.close()


