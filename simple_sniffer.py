import socket


def sniff(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    while True:
        data = s.recvfrom(65565)
        try:
            if "HTTP" in data[0][54:]:
                print('[', '='*30, ']')
                raw = data[0][54:]

                if '\r\n\r\n' in raw:
                    line = raw.split('\r\n\r\n')[0]
                    print('Header captured')
                    print(line[line.find('HTTP'):])
                else:
                    print(raw)
            else:
                pass
        except:
            pass
