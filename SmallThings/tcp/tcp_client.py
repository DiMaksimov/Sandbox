import socket
from subprocess import check_output


def get_uuid():
    cmd_command = 'wmic csproduct get uuid'
    uuid = str(check_output(cmd_command))
    pos1 = uuid.find('\\n') + 2
    return uuid[pos1: -15]


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 8888))
        message = f"{get_uuid()}"
        client.send(bytes(message, encoding='utf-8'))

        while True:
            try:
                response = client.recv(1024)
            except:
                pass
            else:
                print(response.decode('utf-8'))
                break
