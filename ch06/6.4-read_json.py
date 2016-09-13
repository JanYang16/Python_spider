#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
import pandas as pd
import numpy as np


# 读取json数据删除'_id'字段，建议用jupyter notebook打开.ipynb文件
url_list = pd.DataFrame([json.loads(i) for i in open('url_list.json')]).drop(['_id'], axis=1)
item_info = pd.DataFrame([json.loads(i) for i in open('item_info.json')]).drop(['_id'], axis=1)
data = pd.merge(url_list, item_info, on='url')         # 合并DataFrame

print np.mean(data['price'])                           # 计算均值