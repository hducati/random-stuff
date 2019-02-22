import sqlite3
import re
import argparse
import os


def print_download(firefox_db):
    conn = sqlite3.connect(firefox_db)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endtime/1000000, \\'unixepoch') FROM moz_downloads")

    print('-- Files found --')

    for row in c:
        print('File name {} - source {} - date {}'.format(str(row[0]), str(row[1]), str(row[2])))


def print_cookies(cookies_db):
    try:
        conn = sqlite3.connect(cookies_db)
        c = conn.cursor()
        c.execute("SELECT host, name, value FROM moz_cookies")
        print('-- Found cookies --')

        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])

            print('Host {} - name {} - value {}'.format(host, name, value))

    except Exception as e:
            if 'encrypted' in str(e):
                print('Error reading your cookies')
                print('[*]Upgrade your python sqlite3 library')
                exit(0)


def print_history(history_db):
    try:
        conn = sqlite3.connect(history_db)
        c = conn.cursor()
        c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') from moz_places inner join moz_historyvisits "
                  "on moz_places.id == historyvisits.place_id where visit_count > 0")
        print('-- Found History --')

        for row in c:
            url = str(row[0])
            datetime = str(row[1])
            print('[+] Date: {} - visited: {]'.format(datetime, url))

    except Exception as e:
        if 'encrypted' in str(e):
            print('Error reading your history')
            print('[*]Upgrade your python sqlite3 library')
            exit(0)


def print_google(history_db):
    try:
        conn = sqlite3.connect(history_db)
        c = conn.cursor()
        c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits"
                  " where visit_count > 0 and moz_places.id == historyvisits.place_id;")
        print('-- Found google history --')

        for row in c:
            url = str(row[0])
            date = str(row[1])

            if 'google' in url.lower():
                r = re.findall(r'q=.*\&', url)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').replace('+', ' ')

                    print('Date searched: {} - search: {]'.format(date, search))

    except Exception as e:
        if 'encrypted' in str(e):
            print('Error reading your history')
            print('[*]Upgrade your python sqlite3 library')
            exit(0)


def main():
    parser = argparse.ArgumentParser(usage='parse_firefox.py -p <pathName>')

    parser.add_argument('-p', '--firefox_path', help='specify firefox path', type=str)

    args = parser.parse_args()

    firefox_db = args.firefox_path
    print(firefox_db)

    if firefox_db is None:
        print(parser.usage)
        exit(0)

    elif not os.path.isdir(firefox_db):
        print('Path does not exist ' + str(firefox_db))
        exit(0)

    else:
        download_db = os.path.join(firefox_db, 'downloads.sqlite')

        if os.path.isfile(download_db):
            print_download(download_db)
        else:
            print('File not founded! (Download)')

        cookies_db = os.path.join(firefox_db, 'cookies.sqlite')

        if os.path.isfile(cookies_db):
            print_cookies(cookies_db)
        else:
            print('File not founded! (Cookies)')

        history_db = os.path.join(firefox_db, 'places.sqlite')
        if os.path.isfile(history_db):
            print_history(history_db)
        else:
            print('File not founded! (Places)')


if __name__ == '__main__':
    main()
