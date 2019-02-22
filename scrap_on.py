import argparse
import requests
from bs4 import BeautifulSoup
from sys import exit


def page_finder(url):
    try:
        link = requests.get(url)

        if link.status_code == 200:
            print('[+]Getting HTML code...')
            soup = BeautifulSoup(link.content, 'html.parser')
            print('')

            print(soup.prettify())

        else:
            pass

    except ConnectionError as ce:
        print(str(ce))
        exit(0)


def main():
    parser = argparse.ArgumentParser(description='web scraping', usage='[-u] <target url>')
    parser.add_argument('-u', '--url', type=str, help='specify url')

    args = parser.parse_args()

    url = args.url

    if url is None:
        print(parser.usage)
        exit(0)

    else:
        page_finder(url)


if __name__ == '__main__':
    main()
