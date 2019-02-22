"""Script que verifica quais portas estão abertas em um determinado IP.
    conn_scan vai fazer a conexão com o IP e a PORTA dada."""

import argparse
from socket import *
from threading import Thread, Semaphore


# impedindo que as Threads printem toda vez que seja executada.
# caso essa variável não existisse, toda vez que criasse uma Thread, o print seria exibido de maneira desordenada.
screen_lock = Semaphore(value=1)


def conn_scan(tgt_host, tgt_port):
    try:
        conn_skt = socket(AF_INET, SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send('Violent Python\r\n')

        results = conn_skt.recv(100)
        screen_lock.acquire()

        print('[+]{}/TCP OPEN'.format(tgt_port))
        print('[+] ' + str(results))

    except ConnectionRefusedError:
        screen_lock.acquire()
        print('{}/TCP CLOSED'.format(tgt_port))
    finally:
        screen_lock.release()
        conn_skt.close()


def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except ConnectionRefusedError:
        print('[-] {} - Unknown host'.format(tgt_host))
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print('\n[+] Scan results: {}'.format(tgt_name[0]))

    except IndexError:
        print('\n[-] Scan results: {}'.format(tgt_ip))

    setdefaulttimeout(1)

    for tgt_port in tgt_ports:
        t = Thread(target=conn_scan, args=(tgt_host, int(tgt_port)))
        t.start()


def main():
    parser = argparse.ArgumentParser(prog='TCP SCAN', usage='PROG -H <target host> -p <target port>')
    parser.add_argument('-H', '--tgt_host', help='specify target host')
    parser.add_argument('-p', '--tgt_ports', help='specify target port')

    args = parser.parse_args()
    tgt_host = args.tgt_host
    tgt_ports = str(args.tgt_ports).split(',')

    if (tgt_host is None) | (tgt_ports[0] is None):
        print(parser.usage)
        exit(0)
    port_scan(tgt_host, tgt_ports)


if __name__ == '__main__':
    main()