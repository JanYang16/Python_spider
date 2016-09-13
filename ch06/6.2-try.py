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
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)              # 连接Mongodb数据库
sense = client['sense']                                       # 创建数据库
url_list = sense['url_list']                                  # 创建数据表
item_info = sense['item_info']                                # 同上


def get_city_urls():
    """获取首页所有城市的url列表"""
    try:
        with open('six.html') as f:
            response = f.read()                               # 读取本地html文件
        soup = BeautifulSoup(response, 'lxml')
        urls = soup.select('#destination_nav > div > div > div > dl.dl-list > dt > a')
        return [url.get('href') for url in urls]              # 列表解析式，存储各城市URL链接
    except Exception, e:
        print Exception, ':', e


def get_page_list(city, page=1):
    """获取列表页数据"""
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 创建时间
    url = 'http://www.senseluxury.com/destinations_list/%s?page=%s' % (city.split('/')[-1], page)
    try:
        response = requests.get(url)                          # 发送请求
        wb_data = json.loads(response.text[1:-1])             # 将JSON字符串转换为字典
        # print wb_data['val']

        # 循环获取键值数据
        for i in wb_data['val']['data']:
            title = i['title']
            url = 'http://www.senseluxury.com' + i['url']      # 拼接链接
            server = i['server'].replace('&nbsp;', ' ').split()  # 数据清理，替换脏数据
            img = i['imageUrl']
            memo = i['memo']
            price = i['price']
            address = i['address'].split()                     # 按空格分割成列表
            subject = i['subject']
            data = {'title': title, 'url': url, 'server': server, 'img': img, 'memo': memo,
                    'price': price, 'adderss': address, 'subject': subject, 'create_time': now}
            url_list.insert_one(data)                          # 将数据插入数据库
            print data
    except Exception, e:
        print Exception, ':', e


def get_all_list(city):
    """获取所有的列表页数据"""
    for page in range(1, 30):
        get_page_list(city, page)


def get_item_info(url):
    """获取详情页的数据"""
    print url
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 404:                        # 处理404页面
            print '404Error'
        else:
            scenery = list(soup.select('body > div.wp.Lcfx.save-data-info > div.jg-left.Lfll > div.de-ssfw.floor-index > ul > li:nth-of-type(1) > table > tr')[0].stripped_strings)
            theme = list(soup.select('body > div.wp.Lcfx.save-data-info > div.jg-left.Lfll > div.de-ssfw.floor-index > ul > li:nth-of-type(2) > table > tr')[0].stripped_strings)
            data = {'scenery': scenery, 'theme': theme, 'url': url}
            item_info.insert_one(data)
    except Exception, e:
        print Exception, ':', e


def func(x):
    """测试错误的临时函数"""
    try:
        return 1/x
    except ZeroDivisionError, e:
        print ZeroDivisionError, e
    except TypeError, e:
        print TypeError, e


if __name__ == '__main__':
    # listing = [i['url'] for i in url_list.find()]
    # city_urls = get_city_urls()
    # pool = Pool(processes=3)                               # 设置进程池中的进程数
    # pool.map(get_all_list, city_urls)                      # 多进程爬取列表页数据
    # pool.map(get_item_info, listing)                       # 多进程爬取详情页数据
    # pool.close()                                           # 等待进程池中的进程执行结束后再关闭pool
    # pool.join()                                            # 防止主进程在子进程结束前提前关闭
    # get_item_info('http://www.senseluxury.com/villa/2539_levelfurnishedlivingapartment3bedroom')  # 调试详情页爬虫
    get_item_info('http://www.senseluxury.com/villa/100000_hillsidevillageyufangshouse')  # 调试404错误页面

