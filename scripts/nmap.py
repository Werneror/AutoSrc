#!/usr/bin/python
# ^_^ coding:utf8 ^_^

def poc(domain):
    return 'sudo nmap -Pn -sV -sS -script auth,brute,fuzzer,malware,vuln,vulners {} -oX {}.xml'.format(domain, domain)
