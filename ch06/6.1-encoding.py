#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup


# url = 'http://www.jsiq.net/hs.php?srchmem=&page=1'
url = 'http://www.w3school.com.cn/'


response = requests.get(url)
print response.encoding
print response.request.headers
# response.encoding = 'gb2312'
# soup = BeautifulSoup(response.text, 'lxml')
soup = BeautifulSoup(response.content, 'lxml')

print soup


