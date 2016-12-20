# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
from bs4 import BeautifulSoup


def get_search_list(keyword=None, page=1):
    """获取买粮网搜索列表数据，并写入文本文件"""
    url = 'http://www.mailiangwang.com/biz/list'
    payload = {'keyword': keyword, 'pageid': page}              # 构建查询字符串参数字典
    response = requests.get(url, params=payload)                # 关键字参数
    print response.url                                          # 打印请求URL
    print response.status_code                                  # 打印状态码
    soup = BeautifulSoup(response.text, 'lxml')                 # 解析响应的内容
    names = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n1 > a')  # 公司名称
    capitals = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n3')   # 注册资本
    adds = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n5')       # 公司地址
    categorys = soup.select('body > div.wrap > div.merchantList > div.p_dataList > div.p_dataItem > span.n6')  # 主营品类

    # 提取数据并写入文本文件
    with open('data.txt', 'w') as f:
        f.write('公司名称|注册资本|公司地址|主营品类|创建时间\n')     # 写入标题行

        for name, capital, add, category in zip(names, capitals, adds, categorys):    # zip是同时迭代多个对象
            name = name.get('title').strip()                     # 获取属性值文本，并删除空格
            capital = capital.text                               # 获取标签文本
            add = add.text
            category = category.text
            data = [name, capital, add, category, '\n']          # 创建数据列表，注意添加'\n'进行换行
            f.write('|'.join(data).encode('utf-8'))              # 写入文本文件
            print '写入成功！'


if __name__ == '__main__':
    get_search_list(u'玉米', page=1)
