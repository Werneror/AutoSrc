#!/usr/bin/python
# ^_^ coding:utf8 ^_^

from sys import exit
from libs.log import logger
from .banner import print_banner


def check_parse(scripts, targets, threads, quiet):
    if quiet:
        logger.close_log()
    else:
        print_banner()
    if threads < 1:
        logger.error('The number of threads must be no less than one.')
        exit(-1)
    scripts = list(set(scripts))
    if len(scripts) == 0:
        logger.error('The specified script does not exist.')
        exit(-1)
    targets = list(set(targets))
    if len(targets) == 0:
        logger.warning('The target entered is empty.')
        exit(0)
    logger.info('Script(s): {}'.format(len(scripts)))
    logger.info('Target(s): {}'.format(len(targets)))
    logger.info('Thread(s): {}'.format(threads))
    return scripts, targets, threads


if __name__ == '__main__':
    pass
