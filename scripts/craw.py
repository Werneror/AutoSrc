#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = Werner
# 该脚本从一个url开始，以广度优先的队列爬取网页中同域名下的链接，默认爬取３级网页，可修改LEVEL参数

from bs4 import BeautifulSoup
import requests
import urlparse
import urllib
import Queue

LEVEL = 3


class spiderMain(object):

    def __init__(self, url):
        self.SIMILAR_SET = set()
        self.link = url
        self.domain = self.get_domain(url)
        self.proto = urllib.splittype(url)[0]

    def get_domain(self, url):
        return urllib.splithost(urllib.splittype(url)[1])[0]

    def judge(self, url):
        if url.startswith('javascript'):
            return False
        if url.startswith('http://') or url.startswith('https://') or url.startswith('//'):
            domain = self.get_domain(url)
            if domain != self.domain:
                return False
            if url.startswith('//'):
                url = self.proto + ':' + url
        elif url.startswith('/'):
            url = urlparse.urljoin(self.proto + '://' + self.domain, url)
        else:
            url = urlparse.urljoin(self.url, url)
        return url

    def run(self):
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Referer"] = "http://www.baidu.com/"
        new_urls = set()
        try:
            r = requests.get(self.link, headers=header, timeout=5)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                a_tags = soup.find_all('a')
                for a_tag in a_tags:
                    new_url = a_tag.get('href')
                    full_url = self.judge(new_url)
                    if full_url:
                        new_urls.add(full_url)
        except Exception:
            pass
        return new_urls


def poc(url):
    if '://' not in url:
        url = 'http://' + url

    urls = set()
    urls.add(url)

    url_queue = Queue.Queue()
    url_queue.put((0, url))
    while not url_queue.empty():
        level, url = url_queue.get()
        if level > LEVEL:
            break
        s = spiderMain(url)
        new_urls = s.run()
        for url in new_urls:
            urls.add(url)
            url_queue.put((level+1, url))

    return urls


if __name__ == '__main__':
    domain = 'http://asset.pingan.com/gongkaixinxi/jiben.shtml'
    urls = poc(domain)
    if urls:
        for url in urls:
            print(url)
    else:
        print('None')
