# Multi-Client Chat Server (Python)

A simple multi-client chat server written in Python using **socket** and **threading**.  
It allows multiple clients (e.g., Telnet) to connect and chat with each other in real-time.

---

## Features

- Supports multiple clients concurrently using threads.
- Nickname support: clients provide a name when they connect.
- Broadcasts join and leave messages to all clients.
- Server prints all chat activity in its console.

---

## Requirements

- Python 3.8+  
- Telnet (pre-installed on most Linux distributions)

---

## How to Run

### 1. Start the server

```bash
python3 multi_thread.py
You should see:

text
Copy code
[+] Chat server is running on 10.11.180.29:8080
2. Connect with Telnet (client)
From another terminal:

bash
Copy code
telnet 10.11.180.29 8080
Enter your nickname when prompted.

Start chatting with other connected clients.

Example Session
Server Output
text
Copy code
[+] Chat server is running on 10.11.180.29:8080
[+] alice has joined the chat
alice: hello everyone
bob: hi alice
[+] bob has disconnected
Client 1 (alice)
text
Copy code
Welcome to Multi-Chat Server
Now enter your nick name:
alice
System: Welcome alice, you are now connected!
Client 2 (bob)
text
Copy code
Welcome to Multi-Chat Server
Now enter your nick name:
bob
System: Welcome bob, you are now connected!
alice: hello everyone
bob: hi alice
Disconnecting
To disconnect in Telnet:
Press Ctrl+] then type quit.

Notes
You can customize the host and port in the Python script.

Server logs all chat messages and system events (join/leave) to the console.