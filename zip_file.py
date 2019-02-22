"""-----------------------------------------------------
    Alterar library optparse para argparse"""

import zipfile
import argparse
from threading import Thread


def extract_file(z_file, password):
    try:
        guess = z_file.extractall(pwrd=password)
        if guess:
            print('[+] Password: ' + guess)
            exit(0)
        else:
            pass
    except NameError:
        return


def main():

    parser = argparse.ArgumentParser(description='Input values', usage='%(prog)[-H]')

    parser.add_argument(metavar='-f', dest='zname', type=str, help='specify zipfile')
    parser.add_argument(metavar='-d', dest='dname', type=str, help='specify dictionary')
    args = parser.parse_args()

    if (args.zname is None) | (args.dname is None):
        print(parser.usage)
        exit(0)
    else:
        zname = args.zname
        dname = args.dname

        z_file = zipfile.ZipFile(zname)
        pass_file = open(dname, 'r')

        for line in pass_file.readlines():
            password = line.strip('\n')
            t = Thread(target=extract_file(z_file, password))
            t.start()


if __name__ == '__main__':
    main()