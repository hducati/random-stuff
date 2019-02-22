import sqlite3
import os
import argparse


def print_tables(iphone_db):
    try:
        conn = sqlite3.connect(iphone_db)
        c = conn.cursor()
        c.execute("SELECT tbl_name from sqlite_master WHERE type==\'table\';")
        print('DATABASE: ' + iphone_db)

        for row in c:
            print('[+] Table: ' + str(row))

    except Exception as e:
        pass

    conn.close()


def is_message_table(iphone_db):
    try:
        conn = sqlite3.connect(iphone_db)
        c = conn.cursor()
        c.execute("SELECT tbl_name FROM sqlite_master WHERE type==\'table\';")

        for row in c:
            if 'message' in str(row):
                return True

    except Exception as e:
        print(e)
        return False


def print_message(msg_db):
    try:
        conn = sqlite3.connect(msg_db)
        c = conn.cursor()
        c.execute('select datetime(date, \'unixepoch\', address, text from message WHERE address>0')

        for row in c:
            date = str(row[0])
            addr = str(row[1])
            text = row[2]
            print('\n Date: {} - Address {} - Text {]'.format(date, addr, text))

    except Exception as e:
        pass


def main():
    parser = argparse.ArgumentParser(usage='python ios_device.py -p <iphone backup directoy>')

    parser.add_argument('-p', '--iphone_path', type=str, help='specify iphone backup directory')

    args = parser.parse_args()

    iphone_path = args.iphone_path

    if iphone_path is None:
        print(parser.usage)
        exit(0)

    elif not os.path.isdir(iphone_path):
        print('Path not found.\nExiting...')
        exit(0)

    else:
        dir_list = os.listdir(os.getcwd())

        for file_name in dir_list:
            final_path = os.path.join(iphone_path, file_name)
            if is_message_table(final_path):
                try:
                    print('-- Found messages -- ')
                    print_message(final_path)

                except Exception as e:
                    pass


if __name__ == '__main__':
    main()
