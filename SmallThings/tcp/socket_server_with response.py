import socketserver


class ResponseTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        message = self.request.recv(1024).strip()
        print(f'{message.decode()} has just connected. Welcome!')
        response = f'Hello {message.decode()}. Welcome to our server!'
        self.request.sendall(response.encode())


if __name__ == '__main__':
    with socketserver.TCPServer(('', 8888), ResponseTCPHandler) as server:
        server.serve_forever()