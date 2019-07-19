import socket
import subprocess


def get_uuid():
    cmd_command = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd_command))
    pos1 = uuid.find('\\n') + 2
    return uuid[pos1: -15]


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    uuid = get_uuid()
    message = f"Hi! I'm {uuid}."
    sock.sendto(bytes(message, encoding='utf-8'), ('localhost', 8888))
    