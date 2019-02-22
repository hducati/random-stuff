import pygeoip
import socket
import dpkt
import argparse
import os


gi = pygeoip.GeoIP('GeoIP.dat')


def print_pcap(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Source: {} - Destiny: {]'.format(ret_geo_str(src), ret_geo_str(dst)))

        except Exception as e:
            pass


def print_record(target):
    rec = gi.record_by_name(target)
    city = rec['city']
    region = rec['region_name']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']

    print('[*] Target: ' + target)
    print('\n[*] Geo Location: City {} - Region {} - Country {}'.format(city, region, country))
    print('\n[*] Longitude: {} - Latitude {}'.format(long, lat))


def ret_geo_str(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']

        if city != '':
            geo_loc = city + ", " + country
        else:
            geo_loc = country

        return geo_loc

    except IndexError:
        return "Unregistered"


def main():
    parser = argparse.ArgumentParser(usage='python geo_location.py -p <pcap_filename>')

    parser.add_argument('-p', '--pcap_file', help='specify pcap file', type=str)

    args = parser.parse_args()

    pcap_filename = args.pcap_file

    if pcap_filename is None:
        print(parser.usage)
        exit(0)

    elif not os.path.isdir(pcap_filename):
        print('Path not found')
        exit(0)

    else:
        f = open(pcap_filename)
        pcap = dpkt.pcap.Reader(f)
        print_pcap(pcap)


if __name__ == '__main__':
    main()
