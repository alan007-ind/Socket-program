# 🔌 Socket Command Server (Python)

This is a simple socket-based command execution server written in Python. It allows a remote client to send shell commands to a host machine and receive output via a TCP connection.

> ⚠️ **Ethical use only**: This script is meant for controlled experiments, learning socket programming, and building awareness of how reverse/backdoor shells work. **Do not use on unauthorized systems.**

---

## 🧠 Features

- Accepts TCP connections on `localhost:8000`
- Receives shell commands from the connected client
- Executes them using `subprocess`
- Sends back both `stdout` and `stderr` output
- Recognizes `quit` to safely close the connection

---

## 🚀 How It Works

1. Server listens on port `8000`.
2. When a client connects, it prints the IP and port.
3. For every command received:
   - It runs the command in a subprocess.
   - Returns the command output (or error) back to the client.

---

## 🧪 Usage

### ▶️ Run the server:

```bash
python socket_server.py
