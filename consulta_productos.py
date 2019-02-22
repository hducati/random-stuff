from robobrowser import RoboBrowser
import requests


def form_manipulation():
    site = requests.get('https://dinem.agroindustria.gob.ar/dinem_fob.fob_consultaproductos.aspx')
    browser = RoboBrowser(site, 'lxml')

    browser.open()

    soup = browser.parsed
    list_order = []

    order = soup.find_all('span')

    for value in order:
        list_order.append(value.string)
    print(soup.text)


form_manipulation()
