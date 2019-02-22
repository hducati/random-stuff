from robobrowser import RoboBrowser
import requests
from bs4 import BeautifulSoup

post_paragram = {
    
}


def form_manipulation():
    site = requests.get('https://dinem.agroindustria.gob.ar/PublicTempStorage/ConsultaDiaria-5619.xlsx')
    info = site.content

    current_page = []
    hidden_list = []

    # browser = BeautifulSoup(info)

    """hidden_tags = browser.find('input', {'name': 'GXState'}).attrs['value']

    for val in hidden_tags.split(','):

        if "vGRIDCURRENTPAGE" in val:

            next_page = val.replace("1", "2")
            # print(next_page)

        hidden_list.append(val)
        print(val + '\n')"""


form_manipulation()
