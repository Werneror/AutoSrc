#!/usr/bin/python
# ^_^ coding:utf8 ^_^

from libs.argv_parse import argv_parse
from libs.stdin_inputs import inputs_from_stdin
from libs.scripts_parse import scripts_parse
from libs.check_parse import check_parse
from libs.exploit import run


if __name__ == '__main__':
    argvs = argv_parse()
    argvs.inputs += inputs_from_stdin()

    scripts = scripts_parse(argvs.script)
    targets = argvs.inputs
    threads = argvs.thread
    quiet = argvs.quiet

    run(*check_parse(scripts, targets, threads, quiet))
