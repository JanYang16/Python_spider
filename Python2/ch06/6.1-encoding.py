#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup


# url = 'http://www.jsiq.net/hs.php?srchmem=&page=1'     # GBK编码的网站
url = 'http://www.w3school.com.cn/'                      # GB2312编码的网站

response = requests.get(url)
print response.encoding                                  # 打印response的编码方式
print response.request.headers
response.encoding = 'gb2312'                             # 方法一：设置response的编码方式
# soup = BeautifulSoup(response.text, 'lxml')
soup = BeautifulSoup(response.content, 'lxml')           # 方法二：使用原始的数据

print soup


