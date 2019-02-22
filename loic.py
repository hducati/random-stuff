import dpkt
import socket
import argparse
import os
THRESH = 10000


def find_download(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)

            if http.method == 'GET':
                url = http.url.lower()

                if '.zip' in url and 'loic' in url:
                    print('[+] Source {} downloaded LOIC'.format(src))

        except Exception as e:
            pass


def find_hivemind(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data

            dport = tcp.dport
            sport = tcp.sport

            if dport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDos Hivemind issued by: ' + src)
                    print('[+] Target cmd: ' + tcp.data)

            if sport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDos Hivemind issued to: ' + src)
                    print('[+] Target cmd: ' + tcp.data)

        except Exception as e:
            pass


def find_attack(pcap):
    pkt_count = []
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport

            if dport == 80:
                stream = src + ':' + dst

                if pkt_count.has_key(stream):
                    pkt_count[stream] = pkt_count[stream] + 1
                else:
                    pkt_count[stream] = 1

        except Exception as e:
            pass

        for stream in pkt_count:
            pkt_sent = pkt_count[stream]
            if pkt_sent > THRESH:
                src = stream.split(':')[0]
                dst = stream.split(':')[1]

                print(' {} source attacked {} with {} pkts'.format(src, dst, str(pkt_sent)))


def main():
    parser = argparse.ArgumentParser(usage='python loic.py -p <pcap filename>')
    parser.add_argument('-p', '--pcap_filename', type=str, help='specify pcap filename')

    args = parser.parse_args()

    if args.pcap_filename is None:
        print(parser.usage)
        exit(0)

    elif not os.path.isdir(args.pcap_filename):
        print('[!] Path not found')
        exit(0)

    else:
        print('Reading pcap file...\n')
        file = open(args.pcap_filename)
        pcap = dpkt.pcap.Reader(file)
        print('Executing find download...\n')
        find_download(pcap)
        print('Searching for HIVE...\n')
        find_hivemind(pcap)
        print('Searching for an attack...\n')
        find_attack(pcap)


if __name__ == '__main__':
    main()
