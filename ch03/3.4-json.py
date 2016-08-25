#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup
import json
import time


def get_page_list(page):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    url = 'http://www.senseluxury.com/destinations_list/85?page=%s' % page
    response = requests.get(url)  # 发送请求
    wb_data = json.loads(response.text[1:-1])  # 将JSON格式字符串转字典
    print(type(response.text), type(wb_data))  # 打印数据类型
    # print data['val']
    # 循环获取键值数据
    for i in wb_data['val']['data']:
        id = i['id']
        title = i['title']
        url = 'http://www.senseluxury.com' + i['url']  # 拼接URL链接
        print({'id': id, 'title': title, 'url': url, 'create_time': now})


if __name__ == '__main__':
    get_page_list(1)

