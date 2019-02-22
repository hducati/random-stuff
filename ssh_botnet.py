import argparse
import pxssh


class Client:
    def __init__(self, host, user,  password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def bot_command(command):
    for client in bot:
        output = client.send_command(command)
        print('Output from: {]'.format(client.host))
        print('[+] Output: ' + output)


def add_client(host, user, password):
    client = Client(host, user, password)
    bot.append(client)


bot = []

add_client('10.10.10.110', 'root', 'toor')
add_client('10.10.10.120', 'root', 'toor')
add_client('10.10.10.130', 'root', 'toor')