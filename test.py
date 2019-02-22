"""
    a_list = [2, 4, 5, 6, 7, 8, 'arroz', 'mandioca', 4, 122]

    square = [e*2 for e in a_list if type(e) is int]

    print(square)

    print([[1 if item_idx == row_idx else 0 for item_idx in range(0, 3)]for row_idx in range(0, 3)])

"""

import argparse
import os

parser = argparse.ArgumentParser(usage='python test.py [-v] value')
parser.add_argument('-v', '--value', type=int, help='specify number')

args = parser.parse_args()

if args.value is None:
    print(parser.usage)
    exit(0)

else:
    if args.value == 4:
        dic = os.environ
        print(type(dic))
    else:
        print(args.value * 2)
    exit(0)
