import getpass


class Password:

    DEFAULT = 'Prompt if not specified'

    def __init__(self, value):
        if value == self.DEFAULT:
            value = getpass.getpass('LDAP Password: ')
        self.value = value

    def __str__(self):
        return self.value
