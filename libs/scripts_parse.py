#!/usr/bin/python
# ^_^ coding:utf8 ^_^

import os 


def isfileexists(path):
    if not (path.endswith('.py') or path.endswith('.pys')):
        path += '.py'
    if os.path.exists(path) and os.path.isfile(path):
        return path
    else:
        return False


def isfolderexists(path):
    if os.path.exists(path) and not os.path.isfile(path):
        file_paths = list()
        for dir, folder, files in os.walk(path):
            for file in files:
                if file.endswith('.py') or file.endswith('.pyc'):
                    file_paths.append(os.path.join(dir, file))
        return file_paths
    else:
        return list()


def scripts_parse(script_name):
    path = os.path.join('scripts', script_name)
    file_path = isfileexists(path)
    if file_path:
        return [file_path]
    return isfolderexists(path)
    


if __name__ == '__main__':
    print(scripts_parse('findsub'))

