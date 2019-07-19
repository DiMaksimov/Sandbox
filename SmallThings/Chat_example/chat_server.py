import socket
from threading import Thread

clients = {}

MAX_CONNECTIONS = 10
HOST = '127.0.0.1'
PORT = 65432


class ChatServer:
    max_connections = 0
    host = ''
    port = 0
    clients = {}
    sock = None
    accept_thread = None

