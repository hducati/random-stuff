from winreg import *
import robobrowser
import urllib.parse
import urllib
import re
import argparse


def wigle_print(username, password, netid):
    browser = robobrowser.RoboBrowser(history=True)
    browser.open('http://wigle.net')
    req_data = urllib.parse.urlencode({'credential_0': username, 'credential_1': password})
    browser.open('https://wigle.net/gps/gps/main/login', req_data)

    params = {}
    params['netid'] = netid

    req_param = urllib.parse.urlencode(params)
    resp_url =  'http://wigle.net/gps/gps/main/confirmquery/'
    resp = browser.open(resp_url, req_param).read()
    map_lat = 'N/A'
    map_lon = 'N/A'
    r_lat = re.findall(r'maplat=.*\&', resp)

    if r_lat:
        map_lat = r_lat[0].split('&')[0].split('=')[1]
    r_lon = re.findall(r'maplon=.*\&', resp)

    if r_lon:
        map_lon = r_lon[0].split
    print('[-] Lat: {} Long: {}'.format(map_lat, map_lon))


def val_address(val):
    addrs = ""
    for ch in val:
        addrs += ("%02x" % ord(ch))
    addrs = addrs.strip(" ").replace(" ", ":")[0:17]
    return addrs


def print_net(username, password):
    net = '\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged'
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print('[+] Networks you have joined: ')

    for i in range(100):
        try:
            guid = EnumKey(key, 1)
            net_key = OpenKey(key, str(guid))
            (n, addrs, t) = EnumValue(net_key, 5)
            (n, name, t) = EnumValue(net_key, 4)

            mac_addrs = val_address(addrs)
            net_name = str(name)

            print('[+] {} {} '.format(net_name, mac_addrs))
            wigle_print(username, password, mac_addrs)
            CloseKey(net_key)

        except Exception:
            break


def main():
    parser = argparse.ArgumentParser(prog='wd_registry', usage='PROG -u <wigle username> -p <wigle password>')
    parser.add_argument('-u', dest='username', type=str)
    parser.add_argument('-p', dest='password', type=str)

    args = parser.parse_args()

    username = args.username
    password = args.password

    if username is None or password is None:
        print(parser.usage)
        exit(0)
    else:
        print_net(username, password)


if __name__ == '__main__':
    main()
