#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup


def get_proxy_ip(url):
    """使用代理访问并获取访问IP
    西刺免费代理：http://www.xicidaili.com/
    """
    proxies = {'http': '123.56.218.131:8080'}             # 创建代理字典，键是协议，值是IP和端口号，代理经常失效要去用新的测试
    response = requests.get(url, proxies=proxies)         # 使用代理访问
    soup = BeautifulSoup(response.text, 'lxml')           # 解析response.text
    ip = soup.select('body > p')[0].text                  # 获取访问IP

    print(ip)


if __name__ == '__main__':
    get_proxy_ip('http://icanhazip.com/')
