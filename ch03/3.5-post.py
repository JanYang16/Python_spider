#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Jan Yang
@software: PyCharm Community Edition
"""

import requests
import json


def get_translate_date(word=None):
    """获取有道翻译翻译结果"""
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 创建数据字典
    payload = {'type': 'AUTO', 'i': word, 'doctype': 'json', 'xmlVersion': '1.8',
               'keyfron': 'fanyi.web', 'ue': 'UTF-8', 'action': 'FY_BY_CLICKBUTTON',
               'typoResult': 'true'}
    response = requests.post(url, data=payload)                # 请求表单数据
    content = json.loads(response.text)                        # 将JSON格式字符串转字典

    print(content['translateResult'][0][0]['tgt'])             # 打印翻译后的数据


if __name__ == '__main__':
    get_translate_date('苹果')
