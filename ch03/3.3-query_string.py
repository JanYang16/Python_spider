#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup
import time


def get_search_list():
    '''
    获取买粮网搜索列表数据，并写入文本文件
    '''
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    url = 'http://www.mailiangwang.com/biz/list'
    payload = {'keyword': u'玉米', 'pageid': 1}  # 构建查询字符串参数字典
    response = requests.get(url, params=payload)  # 关键字参数
    print(response.url)                      # 打印请求URL
    soup = BeautifulSoup(response.text, 'lxml')  # 解析响应的内容
    names = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n1 > a')  # 公司名称
    capitals = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n3')  # 注册资本
    adds = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n5')  # 公司地址
    categorys = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n6')  # 主营品类

    with open('data.txt', 'w') as f:
        f.write('公司名称|注册资本|公司地址|主营品类|创建时间\n')  # 写入标题行

        for name, capital, add, category in zip(names, capitals, adds, categorys):
            # print(name.get('title').strip(), capital.text, add.text, category.text)
            name = name.get('title').strip()  # 获取属性值文本
            capital = capital.text  # 获取标签文本
            add = add.text
            category = category.text
            data = [name, capital, add, category, now, '\n']  # 创建数据列表
            f.write('|'.join(data))  # 写入文本文件
            print(now, '写入成功！')


if __name__ == '__main__':
    get_search_list()

