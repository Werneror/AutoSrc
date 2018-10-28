#!/usr/bin/python
# ^_^ coding:utf8 ^_^

import argparse 


def argv_parse():
    parser = argparse.ArgumentParser('auto_src.py')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False, help='Do not export redundant information.') 
    parser.add_argument('-t', metavar='THREAD', dest='thread', type=int, default=1, help='Number of threads') 
    parser.add_argument('-s', metavar='SCRIPT', dest='script', required=True, help='Script to execute') 
    parser.add_argument('-i', metavar='INPUT', dest='inputs', action='append', help='Input, can be many times.')

    return parser.parse_args()

if __name__ == '__main__':
    argv_parse()

