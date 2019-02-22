import requests
from bs4 import BeautifulSoup


def web_parser():
    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'

    page_response = requests.get(url, timeout=5)

    page_content = BeautifulSoup(page_response.content, 'html.parser')
    text_content = []

    for i in range(0,20):
        paragraphs = page_content.find_all('a')[i]
        print(paragraphs.get('href'))
        if paragraphs.find('href'):
            print(paragraphs)


web_parser()
