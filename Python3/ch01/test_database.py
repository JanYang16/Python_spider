#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan Yang
@software: PyCharm Community Edition
"""

import pymongo


def test_database():
    """测试Mongodb数据库代码"""
    client = pymongo.MongoClient('localhost', 27017)
    test_db = client['test_db']
    test_table = test_db['test_table']
    data = {'name': 'Jan Yang', 'software': 'pycharm'}

    test_table.insert(data)


if __name__ == '__main__':
    test_database()  # 调用测试程序
