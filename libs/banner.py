#!/usr/bin/python
# ^_^ coding:utf8 ^_^

import sys

banner = '''
\033[0;32;40m
8""""8                     8""""8
8    8 e   e eeeee eeeee   8      eeeee  eeee
8eeee8 8   8   8   8  88   8eeeee 8   8  8  8
88   8 8e  8   8e  8   8       88 8eee8e 8e
88   8 88  8   88  8   8   e   88 88   8 88
88   8 88ee8   88  8eee8   8eee88 88   8 88e8
\033[0m
'''


def print_banner():
    sys.stderr.write(banner)


if __name__ == '__main__':
    print_banner()
