import re
from robobrowser import RoboBrowser
import argparse
import getpass
from sys import exit


def form_manipulation(username, password):

    """Após instanciar a classe RoboBrowser, a url é aberta e então vai realizar a busca pelo form.
    Após encontrar o form desejado, ocorre o preenchimento do formulário pelo name que está no código HTML.
    E por fim, vai realizar o envio das informações."""

    browser = RoboBrowser(history=True)
    browser.open('http://192.168.10.24/inventario/login.php')

    signup_form = browser.get_form(class_='form-signin')

    signup_form["username"].value = username
    signup_form["password"].value = password

    browser.submit_form(signup_form)

    # print(str(browser.select))
    print(str(browser.select))


def main():
    parser = argparse.ArgumentParser(
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                    usage='[-u] <username> [-p] <password>'
    )

    parser.add_argument('-u', '--username', type=str, help='Enter your username.')

    args = parser.parse_args()

    username = args.username

    if username is None:
        print(parser.usage)
        exit(0)

    try:
        p = getpass.getpass()

    except Exception as e:
        print(str(e))

    else:
        form_manipulation(username, p)


if __name__ == '__main__':
    main()
