import csv
import time

import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

# 这个网站价格每天都是一样的，无语
import json
'''
# 初始日期
date = datetime(2025, 4, 7)

head = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'cookie':'JSESSIONID=59F0A859481279B73BED3F11FBBC438B',
    'referer':'http://58.48.136.167:7500/priceComparison.html'
}
cook = {'JSESSIONID=59F0A859481279B73BED3F11FBBC438B'}
# 循环 20 次
for i in range(20):
    # 将日期格式化为字符串
    date_str = date.strftime('%Y-%m-%d')


    url = f'http://58.48.136.167:7500/price/priceStatistics/queryJBSJData?date={date_str}&areaCode=420100'
    resp = requests.post(url,headers=head)
    data_json = resp.json()
    data_list = []
    for i in range(40):
        data = data_json['data']['jbsjData']['data'][i]
        data_list=(list(data.values()))
        data_list =[data_list[3],data_list[1],data_list[4],data_list[2],data_list[0],data_list[5]]
        print(data_list)
        # 将日期往前推一天
    date -= timedelta(days=1)

'''


f = open('wuhan菜价.csv',mode='w',encoding='utf-8',newline='')
csvwrite = csv.writer(f)
def dowlode_one_page(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'cookie': 'JSESSIONID=59F0A859481279B73BED3F11FBBC438B',
        'referer': 'http://58.48.136.167:7500/priceComparison.html'
    }
    resp = requests.post(url, headers=head)
    data_json = resp.json()
    data_list = []
    for i in range(41):
        data = data_json['data']['jbsjData']['data'][i]
        data_list = (list(data.values()))
        data_list = [data_list[3], data_list[1], data_list[4], data_list[2], data_list[0], data_list[5]]
        # print(data_list)
        csvwrite.writerow(data_list)

if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:


        # 初始日期
        # date = datetime(2025, 4, 7)
        date = datetime.now()
        # 循环 20 次(天)
        for i in range(20):
            # 将日期格式化为字符串
            date_str = date.strftime('%Y-%m-%d')
            url = f'http://58.48.136.167:7500/price/priceStatistics/queryJBSJData?date={date_str}&areaCode=420100'
            t.submit(dowlode_one_page,url)
            print(url)
            # time.sleep(3)
            # 将日期往前推一天
            date -= timedelta(days=1)
            print(f'o{i}k')

f.close()