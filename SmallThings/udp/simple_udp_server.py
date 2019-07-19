import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('', 8888))

    while True:
        message = sock.recv(1024)
        print(f"Message {message.decode('utf-8')}")
