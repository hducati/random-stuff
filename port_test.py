import socket

"""Função que faz uma busca nas redes através de um for loop e exibe-as"""


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return 'Error'


def checkVulns(banner):
    arq = open('vuln_banner.txt', 'r')
    for line in arq.readlines():
        if line.strip('\n') == banner:
            print('[+] Service is vulnerable: ' + banner.strip('\n'))


def main():
    portList = [21, 22, 25, 80, 110, 443]

    for x in range(1, 255):
        ip = '192.168.95.'+str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print('[+] ' + ip + ':' + str(port) + ' ' + banner)


if __name__ == '__main__':
    main()