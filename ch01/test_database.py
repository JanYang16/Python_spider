#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Jan Yang
@software: PyCharm Community Edition
"""

import pymongo

# 测试Mongodb数据库代码
client = pymongo.MongoClient('localhost', 27017)
test = client['test']
test_table = test['test_table']
data = {'name': 'Jan Yang', 'software': 'pycharm'}

test_table.insert(data)
