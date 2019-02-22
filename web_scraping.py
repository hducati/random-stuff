from bs4 import BeautifulSoup
import requests
import argparse
import os
from googlesearch import search


def email_finder(url, archive):
    try:
        page_response = requests.get(url, timeout=5)

        email_content = []

        arq = open(archive, 'w')

        if page_response.status_code == 200:
            page_content = BeautifulSoup(page_response.content, 'html.parser')

            for email in page_content.find_all('p'):
                if email.find('@.com'):
                    email_content.append(email.find)
                    arq.write('email: ' + str(email.find('@.com') + '\n'))
                else:
                    pass
        else:
            print('Connection failed.')
            exit(0)

    except ConnectionError as ce:
        print(str(ce))
        exit(0)


def link_finder(url, archive):
    try:
        print('link finder ' + archive)
        page_response = requests.get(url, timeout=5)

        link_content = []

        arq = open(archive, 'w')

        if page_response.status_code == 200:
            page_content = BeautifulSoup(page_response.content, 'html.parser')

            for link in page_content.find_all('a'):

                if link.get('href'):
                    link_content.append(link.get('href'))
                    arq.write('url: ' + str(url) + '\nlink: ' + link.get('href') + '\n')
                    arq.write('-------------------------------------------------------------------------------------\n')

                else:
                    pass
        else:
            print('Connection Failed.')
            exit(0)

        arq.close()

    except ConnectionError as ce:
        print('[!] Error: ' + str(ce))
        exit(0)


def web_parser(url, archive):
    try:
        print('web parser: ' + archive)
        page_response = requests.get(url, timeout=5)

        page_content = BeautifulSoup(page_response.content, "html.parser")
        text_content = []

        arq = open(archive, 'w')

        for i in range(0, 20):
            paragraphs = page_content.find_all('p')[i].text
            text_content.append(paragraphs)

            arq.write(paragraphs + '\n')

        arq.close()

    except ConnectionError as ce:
        print('[!] Connection Error: ' + str(ce))
        exit(0)


def google_search(query, archive):
    for gs in search(query, 'com', 'pt-br', num=10, stop=1, pause=2):
        link_finder(gs, archive)
        email_finder(gs, archive)
        print(gs)


def main():
    parser = argparse.ArgumentParser(usage='python web_scraping.py -u <target_url> -p <archive path> -a <archive name>')

    parser.add_argument('-u', '--target_url', type=str, help='specify target url')
    parser.add_argument('-p', '--path', type=str, help='specify path')
    parser.add_argument('-a', '--archive', type=str, help='specify archive name')
    # parser.add_argument('-e', '--email', type=str, help='get emails')

    args = parser.parse_args()
    tgt_url = args.target_url
    path = args.path
    archive = args.archive
    # email = args.email

    if tgt_url is None:
        print(parser.usage)
        exit(0)

    if path is None:
        print(parser.usage)
        exit(0)

    if archive is None:
        print(parser.usage)
        exit(0)

    elif not os.path.isdir(path):
        print('[!] Path not found\nExiting...')
        exit(0)

    else:
        # archive_name = path.split("'\'")[-1]
        archive_txt = os.path.join(path + archive)

        if not os.path.isfile(archive_txt):
            print('[!] File doesnt exist.')
            response = input(' Create a new one [y/N]? '.strip())

            if response.lower().split(' ')[0][0] == 'y':
                arq = open(archive_txt, 'w+')
                arq.close()

            elif response.upper().split(' ')[0][0] == 'N':
                print('Exiting...\n')
                exit(0)

            else:
                print('Incorrect Value.\nExiting...')
                exit(0)

        elif tgt_url == 'http://www.google.com' or 'https://www.google.com':
            search_query = input('Search for: ')
            google_search(search_query, archive_txt)

        else:
            # web_parser(tgt_url, archive_txt)
            link_finder(tgt_url, archive_txt)


if __name__ == '__main__':
    main()
