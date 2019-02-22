from bs4 import BeautifulSoup
import re
import requests
import requests.exceptions
import argparse
import os
from urllib.parse import urlsplit
from collections import deque
from user_agent import generate_user_agent
from multiprocessing import Queue
from sys import exit

# setting a user-agent
headers = {
    'User-Agent': generate_user_agent()
    }


def web_crawler(url, path_file):
    new_urls = deque([url])

    arq = open(path_file, 'w')

    # arq_return = check_if_arq_has_values(arq)

    # if arq_return is None:
        # exit(0)

    # else:
       # arq = arq_return

    processed_urls = set()

    emails = set()

    while len(new_urls):
        url = new_urls.popleft()
        processed_urls.add(url)

        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/') + 1] if '/' in parts.path else url

        print('[+] Processing %s' % url)

        try:
            response = requests.get(url, timeout=5, headers=headers)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError) as e:
            print(str(e))
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, 'html.parser')

        for anchor in soup.find_all("a"):

            link = anchor.attrs["href"] if "href" in anchor.attrs else ''

            if link.startswith('/'):
                link = base_url + link
                arq.write('Link: ' + link)
            elif not link.startswith('http'):
                link = path + link
                arq.write('Link: ' + link)

            if link not in new_urls and link not in processed_urls:
                new_urls.append(link)


def check_if_arq_has_values(arq):
    cont = 0

    for line in arq.readlines():
        if re.findall(r'\w\.', line):
            print('[!] Already has values in this file.\n')
            resp = input('Wanna rewrite?[y/N] ')
            arq.close()

            if resp.strip().lower().startswith('y'):
                arq = open(arq, 'w')

                return arq

            elif resp.strip().upper().startswith('N'):
                return None

            else:
                print('Incorrect value\n.')
                exit(0)
        else:
            cont += 1
            continue


def main():
    parser = argparse.ArgumentParser(usage='REQUIRED: python scrapy_int.py [-u] <url> [-p] <path>\n'
                                     'OPTIONAL: python scrapy_int.py [-u] <url> [-p] <path> [-o] <file_output>')

    parser.add_argument('-u', '--url', type=str, help='specify url')
    parser.add_argument('-p', '--path', type=str, help='specify file path')
    parser.add_argument('-o', '--output', type=str, help='specify output file')

    args = parser.parse_args()

    url = args.url
    path = args.path
    file = args.output

    if url is None:
        print(parser.usage)
        exit(0)

    if path is None:
        print(parser.usage)
        exit(0)

    elif file.split('.')[-1] != 'txt':
        print('[!] Missing .txt extension after the {}.\n'.format(file))
        exit(0)

    elif not os.path.isdir(path):
        print('[!] Path not found. ' + str(path) + '\n')
        exit(0)

    else:
        path_file = os.path.join(path, file)

        if os.path.isfile(path_file) and os.access(path_file, os.R_OK):
            web_crawler(url, path_file)

        elif not os.path.isfile(path_file):
            print('[!] File path not found. ' + path_file)
            response = input('\nCreate a new one? [y/N]')

            if response.lower().strip().split(' ')[0][0] == 'y':
                arq = open(path_file, 'w+')
                arq.close()

            elif response.upper().strip().split(' ')[0][0] == 'N':
                exit(0)

            else:
                print('[!] Incorrect value.\n')
                exit(0)

        else:
            print('[!] Error.\n')
            exit(0)


if __name__ == '__main__':
    main()
