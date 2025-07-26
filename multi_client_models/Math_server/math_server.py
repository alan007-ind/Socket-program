from subprocess import Popen, PIPE, STDOUT
import socket
import threading
import time




def StartNewMathServer(conn, addr):
    t = MathServerCommunicationThread(conn, addr)
    t.start()


class MathServerCommunicationThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        p = Popen(['bc', '-q'], stdout=PIPE, stderr=STDOUT, stdin=PIPE, shell=False)

        output = ProcessOutputThread(p, conn)
        output.start()
        conn.send("Welcome To The Math Server :) \n".encode())
        conn.send("To exit the server type exit or quit \n".encode())
        while not p.stdout.closed:
            conn.send("\nEnter the math expression > ".encode())
            user = conn.recv(1024).decode().strip()

            if user == "exit":
                p.terminate()
                p.stdout.close()
                p.stdin.close()
                output.join()
                conn.sendall("Thank you for using Math server :)\n".encode())
                conn.close()
                break

            else:

                data = (user + "\n").encode()
                p.stdin.write(data)
                p.stdin.flush()
                time.sleep(0.1)


class ProcessOutputThread(threading.Thread):
    def __init__(self, process, conn):
        super().__init__()
        self.process = process
        self.conn = conn

    def run(self):
        while not self.process.stdin.closed:
            message = ("=" * 30 + '\n').encode()
            answer = ('The answer is > ').encode()
            self.conn.sendall(answer + self.process.stdout.readline() + ("\n").encode() + message)


HOST = 'localhost'
PORT = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print("Math server is running")
try:
    while True:
        conn, addr = s.accept()
        StartNewMathServer(conn, addr)

except KeyboardInterrupt:
    print("\n[!] Server shutting down gracefully...")
    s.close()  # This frees the port
    exit(0)

