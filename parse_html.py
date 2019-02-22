from bs4 import BeautifulSoup
import requests
from http import cookiejar


def print_cook(url):
    # browser = requests.Session()

    cookie_jar = cookiejar.LWPCookieJar()
    page = requests.get(url, cookies=cookie_jar)

    for cook in cookie_jar:
        print(cook)


def test_useragent(url, useragent):
    session_request = requests.Session()

    browser = session_request.get(url)
    browser.headers = useragent

    data = browser.content

    print(data)


def test_proxy(url, proxies):
    request_session = requests.Session()

    page_request = request_session.get(url, proxies=proxies)
    data = page_request.content

    bs = BeautifulSoup(data, features='lxml')

    print(bs.prettify())


url = 'https://stackoverflow.com/'

proxy = {"http": "https://10.10.1.10:1080",
         }

user_agent = [('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 '
               '(KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')]

# test_proxy(url, proxy)
# test_useragent(url, user_agent)
print_cook(url)
