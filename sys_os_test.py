""" Verificando se o usuário tem acesso ao(s) arquivo(s) e se ele existe, caso uma das opções sejam inválidas,
    o programa exibe uma mensagem de erro.
    Verifica a conexão de um ip e uma porta e checa se o serviço está vulnerável ou não."""


import sys
import os
import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return None


def checkVulns(banner, filename):
    f = open(filename, 'r')
    for file in f.readlines():
        if file.strip('\n') in banner:
            print('[+] Service is vulnerable: ' + \
                  banner.strip('\n'))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] File ' + filename + ' does not exist.')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] You dont have permission to access the file ' + filename + '.' )
            exit(0)
        print('[+] Reading file: ' + filename)
    else:
        filename = sys.argv[0]
        print('[-] Usage: ' + str(sys.argv[0]) + \
              '<vuln filename>')
        exit(0)
        port_list = [21, 22, 25, 80, 110, 443]

        for x in range(147, 155):
            ip = '192.168.48.' + str(x)
            for port in port_list:
                banner = retBanner(ip, port)
                if banner:
                    print('[+] ' + ip + ':' + str(port) + '  ' + banner)
                    checkVulns(banner, filename)


if __name__ == '__main__':
    main()