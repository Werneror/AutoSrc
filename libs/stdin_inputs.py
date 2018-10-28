#!/usr/bin/python
# ^_^ coding:utf8 ^_^

import sys
import select


def inputs_from_stdin():
    targets = list()
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line:
            if line != '\n':
                targets.append(line.rstrip('\n'))
        else:
            break
    return targets



if __name__ == '__main__':
    for target in inputs_from_stdin():
        print('inputline: {}'.format(target))
