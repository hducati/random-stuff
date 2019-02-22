import socket


def get_ip():
    ip1 = socket.gethostbyname(socket.gethostname())
    ip2 =