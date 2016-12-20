#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""


import requests
from bs4 import BeautifulSoup


def test_webpage(url):
    """测试网页访问情况，添加headers模拟浏览器"""
    # 创建请求头部信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
    response = requests.get(url, headers=headers)         # 添加headers进行请求
    # response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    print response.status_code                            # 打印状态码
    print response.request.headers                        # 打印请求请求头部
    print soup.head.title.text                            # 打印网页标题


if __name__ == '__main__':
    test_webpage('http://blog.csdn.net/wswzjdez/article/details/5694942')
    # test_webpage('http://www.cec.com.cn/')
