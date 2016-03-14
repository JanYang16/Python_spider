#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan
@software: PyCharm Community Edition
"""

import urllib2

# url = 'https://www.baidu.com/'
url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'

proxy_handler = urllib2.ProxyHandler({"http": "203.195.162.96:8080"})   # 添加proxy对象，在http://cn-proxy.com/查找
opener = urllib2.build_opener(proxy_handler)                # 创建opener
urllib2.install_opener(opener)                              # 安装opener

request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()


print html
print response.getcode()              # 打印状态码
