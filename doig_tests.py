import argparse
import os
import socket


# creating an INET, streaming socket
def scan(tgt_ip, tgt_port):
    try:
        socket.timeout(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((tgt_ip, tgt_port))
        banner = s.recv(1024)
        return banner

    except Exception as e:
        return e


def main():
    parser = argparse.ArgumentParser(usage='doing_tests.py -i <tgt_ip> -p <port>')
    parser.add_argument('-i', '--tgt_ip', type=str, help='specify target ip')
    parser.add_argument('-p', '--tgt_port', type=int, help='specify target port')

    args = parser.parse_args()

    tgt_ip = args.tgt_ip
    tgt_port = args.tgt_port

    if tgt_ip is None or tgt_port is None:
        print(parser.usage)
        exit(0)
    else:
        print(scan(tgt_ip, tgt_port))