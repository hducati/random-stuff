import ftplib
import argparse


def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(hostname, 'mee@your.com')
        print('\n[*] - Logon succeed!')
        ftp.quit()
        return True

    except Exception as e:
        print('\n[*] - Logon failed!')
        print('Exception: ' + str(e))
        return False


def main():
    parser = argparse.ArgumentParser(prog='Anon login', usage='Anon login -h <target host>')
    parser.add_argument('-h', dest='tgt_host', type=str, help='specify target host')

    args = parser.parse_args()

    tgt_host = args.tgt_host

    if tgt_host is None:
        print(parser.usage)
        exit(0)


if __name__ == '__main__':
    main()
