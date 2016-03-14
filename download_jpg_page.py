#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan
@software: PyCharm Community Edition
"""

import urllib
import urllib2
import re
import time

start_url = 'http://tieba.baidu.com/p/3797994694?pn='


def download_jpg(url):
    """
    爬取贴吧的图片并下载到本地
    """
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')            # 读取相应的内容

    re_jpg = r'src="(http://imgsrc.baidu.com.+?\.jpg)" pic_ext="jpeg"'
    jpg_url = re.findall(re_jpg, html)                # 找出所有符合正则表达式的字符串
    # print jpg_url

    for jpg in jpg_url:                              # 循环打印所有url
        print jpg
        # urllib.urlretrieve(jpg, "%s.jpg" % x)       # 下载所有的图片，注意文件名称
        urllib.urlretrieve(jpg, jpg.split('/')[-1])

# download_jpg(url)


def get_all_pages(pages):
    """
    循环下载每个网页的图片
    """
    for i in range(1, pages):
        url = start_url + str(i)                      # 构造带有页码数的url链接

        download_jpg(url)
        time.sleep(2)                                 # 休息2秒钟


get_all_pages(5)
