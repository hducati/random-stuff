from selenium import webdriver
import argparse
from sys import exit, argv
import time


def url_browser():
    browser = webdriver.Chrome("C:/Users/henrique.miranda/webdriver/chromedriver.exe")
    url = argv[2]

    try:
        browser.get(url)
        time.sleep(1)

    except ConnectionError as ce:
        print('[!] Connection error. ' + str(ce))
        exit(0)


def main():
    parser = argparse.ArgumentParser(usage='[-u] <url> ')

    parser.add_argument('-u', '--url', type=str, help='specify url')

    args = parser.parse_args()

    url = args.url

    if url is None:
        print(parser.usage)
        exit(0)

    else:
        url_browser()


if __name__ == '__main__':
    main()
