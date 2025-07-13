# Raw TCP Client-Server in Python

This project demonstrates a basic TCP client-server communication using Python's built-in `socket` module — without any external libraries or frameworks. Nothing Fancy, but a start!
## Files

- `server.py`: Starts a TCP server that listens on `127.0.0.1:8080`, accepts a client connection, and prints the data received.
- `client.py`: Connects to the server and sends a message.
- `config.py`: Contains the shared server address used by both client and server.

## How It Works

1. The server binds to `127.0.0.1:8080` and starts listening.
2. The client connects to the server on the same address and port.
3. The client sends a UTF-8 encoded message.
4. The server accepts the connection and prints the decoded message.

## Usage

### 1. Start the server:

```bash
python server.py
````

### 2. In a new terminal, run the client:

```bash
python client.py
```

## 📄 Example Output (on server side)

```
0123456789
```

## 🛠 Requirements

* Python 3.x
* No external dependencies
