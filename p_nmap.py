import nmap
import argparse


def nmap_scan(tgt_host, tgt_port):
    np_scan = nmap.PortScanner()
    np_scan.scan(tgt_host, tgt_port)
    state=np_scan[tgt_host]['TCP'][int(tgt_port)]['state']

    print('[*] {} - TCP/{} - {}'.format(tgt_host, tgt_port, state))


def main():
    parser = argparse.ArgumentParser(prog='nmap scan', usage='PROG -H <target host> -p <target port>')
    parser.add_argument('-H', dest='tgt_host', help='specify target host', type=str)
    parser.add_argument('-p', dest='tgt_port', help='specify target port', type=int)
    args = parser.parse_args()

    tgt_host = args.tgt_host
    tgt_port = str(args.tgt_port).split(',')

    if (tgt_host is None) or (tgt_port[0] is None):
        print(parser.usage)
        exit(0)

    for port in tgt_port:
        nmap_scan(tgt_host, port)


if __name__ == '__main__':
    main()
