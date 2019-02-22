from robobrowser import RoboBrowser
import requests
from bs4 import BeautifulSoup


def form_manipulation():
    site = requests.get('https://dinem.agroindustria.gob.ar/dinem_fob.fob_consultaproductos.aspx')
    info = site.content

    current_page = []
    hidden_list = []

    browser = BeautifulSoup(info)

    hidden_tags = browser.find('input', {'name': 'GXState'}).attrs['value']

    for val in hidden_tags.split(','):

        if "vGRIDCURRENTPAGE" in val:

            next_page = val.replace("1", "2")
            print(next_page)

        hidden_list.append(val)
        print(val + '\n')

    # for tag in hidden_tags:
        # print(tag.value)
    # print(str(browser.text))
    """list_order = []

    order = soup.find_all('span')

    for value in order:
        list_order.append(value.string)
    print(soup.text)"""


form_manipulation()
