import socket as s
import sys
import select as sel

from server import SOCKET_LIST

SOCKET_LIST = [sys.stdin]

def chat_client():
        if(len(sys.argv) < 3):
            print("usage : python chat_client.py <ip> <port>")
        host = sys.argv[1]
        port = int(sys.argv[2])

        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        soc.settimeout(5)

        try:
            soc.connect((host, port))
        except:
            print("failed to connect to server")
            sys.exit(-1)
        print("connected to server")
        sys.stdout.write("> ")
        sys.stdout.flush( )
        while True:
            read_ready, _, _ = sel.select(SOCKET_LIST, [], [])
            for sock in read_ready:
                if sock == soc:
                    data = sock.recv(4096)
                    if not data:
                        print("disconnected from server")
                        sys.exit()
                    else:
                        sys.stdout.write(data)
                        sys.stdout.write("> ")
                        sys.stdout.flush()
                else:
                    msg = sys.stdin.readline()
                    soc.send(msg.encode())
                    sys.stdout.write("> ")
                    sys.stdout.flush()

if __name__ == "__main__":
    sys.exit(chat_client())

