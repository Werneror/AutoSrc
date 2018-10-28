#!/usr/bin/python
# ^_^ coding:utf8 ^_^

import sys

class Logger:

    close = False

    def close_log(self):
        self.close = True

    def success(self, msg):
        if not self.close:
            sys.stderr.write('\033[0;32;40m[+] {}\033[0m\n'.format(msg))

    def info(self, msg):
        if not self.close:
            sys.stderr.write('\033[0;36;40m[*] {}\033[0m\n'.format(msg))

    def warning(self, msg):
        if not self.close:
            sys.stderr.write('\033[0;33;40m[!] {}\033[0m\n'.format(msg))

    def error(self, msg):
        if not self.close:
            sys.stderr.write('\033[0;31;40m[-] {}\033[0m\n'.format(msg))


logger = Logger()


if __name__ == '__main__':
    logger.success('success')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
