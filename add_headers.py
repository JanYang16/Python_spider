#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan
@software: PyCharm Community Edition
"""

import urllib2


url = 'http://blog.csdn.net/wswzjdez/article/details/5694942'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'
}

request = urllib2.Request(url, headers=headers)       # 添加headers参数
response = urllib2.urlopen(request)
html = response.read().decode('gb18030')

print html
print response.getcode()
