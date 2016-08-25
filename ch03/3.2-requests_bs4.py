#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup
import urllib
import time
import xlwt


def download_jpg(url):
    '''
    使用requests和BeautifulSoup，具体文档如下：
    http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    http://beautifulsoup.readthedocs.io/zh_CN/latest/
    '''
    response = requests.get(url)  # 请求url链接
    print response.status_code  # 获取状态码
    soup = BeautifulSoup(response.text, 'lxml')  # 解析response并创建BeautifulSoup对象
    urls = soup.select('img.BDE_Image')  # CSS选择器获取标签

    for url in urls:
        url = url.get('src')  # 获取标签属性值
        print url
        urllib.urlretrieve(url, 'img/%s' % url.split('/')[-1])  # 下载图片


def get_all_jpg(url, pages):
    '''
    爬取多页码图片数据
    '''
    for page in range(1, pages + 1):
        new_url = url + '?pn=' + str(page)  # 创建带页码的新页面链接
        download_jpg(new_url)  # 调用函数
        time.sleep(2)  # 休息2秒钟


if __name__ == '__main__':
    # get_jpg_url(url)
    get_all_jpg('http://tieba.baidu.com/p/3797994694', 5)
