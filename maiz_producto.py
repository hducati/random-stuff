import requests
import argparse
import os
import getpass
from bs4 import BeautifulSoup


def web_manipulation(directory):
    url = 'https://dinem.agroindustria.gob.ar/dinem_fob.fob_consultaproductos.aspx#'
    page = requests.get(url, allow_redirects=True, stream=True)

    header = page.headers

    content_type = header.get('content-type')

    if 'text' in content_type.lower():
        return False

    if 'html' in content_type.lower():
        return False

    if page.encoding is None:
        page.encoding = 'utf-8'

    if url.find('/'):
        print(url.rsplit('/', 1)[1])
        filename = url.rsplit('/', 1)[1]
        file_path = os.path.join(directory, filename)

        if file_path:
            with open(file_path, 'wb') as f:
                for chunk in page.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                f.close()

    return True


def check_directory():
    directory = os.path.join(os.getcwd(), 'maiz_producto')

    if not os.path.exists(directory):
        print('[+]Creating folder...\n')
        os.makedirs(directory)

        print('[+]Done\n')
        web_manipulation(directory)

        return True
    else:
        directory = os.path.join(os.getcwd(), 'maiz_producto')
        web_manipulation(directory)

        return None


def main():
    parser = argparse.ArgumentParser(usage='')
    test = check_directory()
    print(test)


if __name__ == '__main__':
    main()
