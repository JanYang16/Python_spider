#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan Yang
@software: PyCharm Community Edition
"""

import urllib.request
import re


def download_jpg(url):
    """爬取贴吧的图片并下载到本地"""
    request = urllib.request.Request(url)               # 创建request对象
    response = urllib.request.urlopen(request)          # 请求request对象

    print(response.getcode())                     # 打印状态码

    html = response.read().decode('utf-8')       # 读取相应的内容,decode是根据网页编码方式进行解码
    string = r'src="(http://imgsrc\.baidu\.com.+?\.jpg)" pic_ext="jpeg"'  # 正则表达式字符串
    urls = re.findall(string, html)              # 找出所有符合正则表达式的字符串，返回的是列表
    # prin(jpg_url)

    x = 0
    for url in urls:                             # 循环打印所有url
        urllib.request.urlretrieve(url, "%s.jpg" % x)    # 下载所有的图片，注意文件名称带.jpg
        x += 1
        print(url)


if __name__ == '__main__':
    download_jpg('http://tieba.baidu.com/p/3797994694')
