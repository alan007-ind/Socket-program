# Multi-Client Chat Server (Python)

This is a simple **multi-client chat server** written in Python using `socket` and `threading`.  
It allows multiple clients (like Telnet) to connect and chat with each other in real-time.  

---

## Features
- Supports multiple clients concurrently using threads.
- Nickname support: clients provide a name when they connect.
- Broadcasts join and leave messages to all clients.
- Server prints all chat activity in its console.

---

## How to Run

### 1. Start the server
```bash
python3 multi_thread.py
```
You should see:
```
[+] Chat server is running on 10.11.180.29:8080
```

### 2. Connect with Telnet (client)
From another terminal:
```bash
telnet 10.11.180.29 8080
```

Enter your nickname when prompted, then start chatting.  

---

## Example Session
**Server output:**
```
[+] Chat server is running on 10.11.180.29:8080
[+] alice has joined the chat
alice: hello everyone
bob: hi alice
[+] bob has disconnected
```

**Client 1 (alice):**
```
Welcome to Multi-Chat Server
Now enter your nick name:
alice
Welcome alice, you are now connected!
```

**Client 2 (bob):**
```
Welcome to Multi-Chat Server
Now enter your nick name:
bob
Welcome bob, you are now connected!
alice: hello everyone
bob: hi alice
```

---

## Requirements
- Python 3.8+
- Telnet (pre-installed on most Linux distros)

---

## Notes
- To disconnect in Telnet: press `Ctrl+]` then type `quit`.
- You can customize the host/port in the Python script.

---