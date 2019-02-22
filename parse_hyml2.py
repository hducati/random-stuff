from bs4 import BeautifulSoup
import requests


def web_scrap(url):
    session_request = requests.Session()

    browser = session_request.get(url)
    data = browser.content

    bs = BeautifulSoup()
    links = bs.find_all()

    for link in links:
        if 'href' in link:
            print(link['href'])

    # print(bs.prettify(data))


url = 'https://stackoverflow.com/'
