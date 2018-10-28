#!/usr/bin/python
# ^_^ coding:utf8 ^_^

import os
import imp
from sys import exit
from libs.log import logger


def get_module_name(module_path):
    return os.path.splitext(os.path.split(module_path)[1])[0]


def load_module(module_name, module_path):
    try:
        module = imp.load_source(module_name, module_path)
    except IOError:
        module = None
    return module


def load_modules(scripts):
    logger.info('Start loading module ...')
    modules = dict()
    for script in scripts:
        module_name = get_module_name(script)
        module = load_module(module_name, script)
        if module:
            modules.update({script: module})
            logger.success('The module {} successfully loaded from {}.'.format(module_name, script))
        else:
            logger.error('Failed to load {}.'.format(script))
            exit(-1)
    return modules


if __name__ == '__main__':
    load_module('findsub', 'scripts/findsub.py')
