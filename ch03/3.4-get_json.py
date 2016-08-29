#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
import json


def get_page_list(page):
    """将JSON格式字符串转字典，并获取对应的数据"""
    url = 'http://www.senseluxury.com/destinations_list/85'
    payload = {'page': page, 'callback': 'jsonp'}
    response = requests.get(url, params=payload)  # 发送请求
    # print response.text
    wb_data = json.loads(response.text[6:-1])  # 将JSON格式字符串转字典
    # print json.dumps(wb_data, encoding='utf-8', ensure_ascii=False)
    print(type(response.text), type(wb_data))  # 打印数据类型
    # print data['val']
    # 循环获取键值数据
    for i in wb_data['val']['data']:
        title = i['title']
        url = 'http://www.senseluxury.com' + i['url']  # 拼接URL链接
        print title, url


if __name__ == '__main__':
    get_page_list(1)
