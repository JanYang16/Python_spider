#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup


def get_proxy_ip(url):
    '''
    获取访问IP，使用代理访问
    http://www.kuaidaili.com/
    '''

    proxies = {'http': '218.56.132.154:8080'}
    response = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')
    ip = soup.select('body > p')[0].text

    print(ip)


if __name__ == '__main__':
    get_proxy_ip('http://icanhazip.com/')

