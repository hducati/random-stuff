from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {}: {}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()

    # return True if resp.status_code == 20 and content_type is not None and content_type.find('html') > -1 else False

    return (resp.status_code == 20
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)