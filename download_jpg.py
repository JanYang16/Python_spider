#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan
@software: PyCharm Community Edition
"""

import urllib
import urllib2
import re

url = 'http://tieba.baidu.com/p/3797994694'


def download_jpg(url):
    """
    爬取贴吧的图片并下载到本地
    """
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')            # 读取相应的内容,decode是根据网页编码方式进行解码

    re_jpg = r'src="(http://imgsrc.baidu.com.+?\.jpg)" pic_ext="jpeg"'
    jpg_url = re.findall(re_jpg, html)                # 找出所有符合正则表达式的字符串
    # print jpg_url

    x = 0
    for jpg in jpg_url:                              # 循环打印所有url
        print jpg
        # urllib.urlretrieve(jpg, "%s.jpg" % x)       # 下载所有的图片，注意文件名称
        urllib.urlretrieve(jpg, "{}.jpg".format(x))   # 同上，但推荐用这种方式
        x += 1


download_jpg(url)
# help(urllib.urlretrieve)