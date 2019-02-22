"""Script que consiste basicamente em pegar informações(contatos,mensagens, etc) de usuários que usam/usaram o skype
    através de tabelas, fazendo uma consulta SQL"""

import sqlite3
import os
import argparse


def print_messages(skype_db):
    conn = sqlite3.connect(skype_db)
    c  = conn.cursor()
    c.execute("SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM messages")

    for row in c:
        try:
            if 'parlist' not in str(row[3]):
                if str(row[1]) != str(row[2]):
                    msg_direction = 'To ' + str(row[1]) +': '
                else:
                    msg_direction = 'From: ' + str(row[2]) + ': '
                print('Time: ' + str(row[0]) + ' ' + str(row[3]))

        except Exception as e:
            pass


def print_calllog(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity from calls, conversations where"
              " calls.conv_dbid = conversation.id")

    for row in c:
        print('--Found Calls--\n')
        print('[+] Time: ' + str(row[0]) + '\n[+] Partner: ' + str(row[1]))


def print_contacts(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts")

    for row in c:
        print('[*] Found contact: ')
        print('[+] User: ' + str(row[0]))
        print('[+] Skype Name: ' + str(row[1]))

        if str(row[2]) != '' and str(row[2]) is not None:
            print('[+] Location: ' + str(row[2]) + ' ' + str(row[3]))

        if str(row[4]) is not None:
            print('[+] Phone mobile: ' + str(row[4]))

        if str(row[5]) is not None:
            print('[+] Birthday: ' + str(row[5]))


def print_profile(skype_db):
    conn = sqlite3.connect(skype_db)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch' from ACCOUNTS")

    for row in c:
        print('[+] -- Found account -- ')
        print('[+] User: ' + str(row[0]))
        print('[+] Skype username: ' + str(row[1]))
        print('[+] Location: ' + str(row[2]))
        print('[+] Profile date: ' + str(row[3]))


# main.db é onde fica as tabelas para procurar as informações do skype
def main():
    parser = argparse.ArgumentParser(usage='auto_skype_process.py -p <profile path>')
    parser.add_argument('-p', '--path_name', type=str, help='specify profile path')

    args = parser.parse_args()

    path_name = args.path_name

    if path_name is None:
        print(parser.usage)
        exit(0)

    elif not os.path.isdir(path_name):
        print('Path not found.\nExiting...')
        exit(0)

    else:
        skype_db = os.path.join(path_name, 'main.db')

        if os.path.isfile(skype_db):
            print_profile(skype_db)
            print_contacts(skype_db)
            print_calllog(skype_db)
            print_messages(skype_db)
        else:
            print('[-] Skype database does not exist! ' + str(skype_db))


if __name__ == '__main__':
    main()
