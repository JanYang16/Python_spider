#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan
@software: PyCharm Community Edition
"""


import urllib2
import re
import json

# url = 'http://bj.xiaozhu.com/'
url = 'http://bj.xiaozhu.com/search-duanzufang-p2-0/'

def url_open(url):
    """
    打开url获取网页内容
    """
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    return html


def get_house_url(url):
    """
    从列表页获取详情页的url地址
    """
    html = url_open(url).decode('utf-8')
    re_url = r'href="(.+?\.html)" class="resule_img_a"'
    re_compile = re.compile(re_url)           # 编译正则表达式
    house_url = re.findall(re_compile, html)  # 找出所有符合正则表达式的字符串
    return house_url


# print get_house_url(url)

def get_house_info(url):
    """
    从详情页获得相关数据
    """
    house_list = get_house_url(url)
    for i in house_list:
        html = url_open(i).decode('utf-8')
        try:
            re_title = r'div class="pho_info".+?em\>(.+?)\</em'    # 注意 < 前面要加 \ 转义
            re_rent = r'div class="day_l.+?\<span\>(\d{3,4})\</span'
            re_title_compile = re.compile(re_title, re.S)
            re_rent_compile = re.compile(re_rent)
            title = re.search(re_title_compile, html)  # 查找符合正则表达式的字符串
            rent = re.search(re_rent_compile, html)

            print title.group(1), rent.group(1)        # group(1)字符串的第一个分组
        except Exception, e:
            print Exception, ":", e             # 处理可能产生的异常并打印出来



get_house_info(url)
