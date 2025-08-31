import time

import requests
import csv
from concurrent.futures import ThreadPoolExecutor


# url = 'http://www.xinfadi.com.cn/getPriceData.html'
f = open('线程池爬test-2.csv','w',encoding='utf-8',newline='')

csv_writer = csv.writer(f)
csv_writer.writerow(['一级分类','品名','平均价','单位','产地','发布日期','规格'])
def dowlode_1_page(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'referer': 'http://www.xinfadi.com.cn/priceDetail.html'

    }
    # time.sleep(1)
    resp = requests.post(url,headers=head,timeout=10)
    # print(resp.json())
    print(f'提取{url}中')

    # time.sleep(1)

    for i in range (len(resp.json()['list'])):
        list_21=[]
        # list = resp.json()['list'][i]
        prodCat = resp.json()['list'][i]['prodCat']    #一级分类
        prodName = resp.json()['list'][i]['prodName']    #品名
        print(prodName)
        avgPrice = resp.json()['list'][i]['avgPrice']    #平均价
        place = resp.json()['list'][i]['place']    #	产地
        unitInfo = resp.json()['list'][i]['unitInfo']    #单位
        pubDate = list['pubDate']    #发布日期
        specInfo= resp.json()['list'][i]['specInfo']    #规格
        list_21.extend( [prodCat,prodName,avgPrice,unitInfo,place,specInfo])
        # print(list_21)
        # time.sleep(4)
        csv_writer.writerow(list_21)


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t :
        for a in range(1,200):
            # print(i)
            # time.sleep(1)
            future= t.submit(dowlode_1_page,f'http://www.xinfadi.com.cn/getPriceData.html?current={a}')
            # result = future.result(timeout=None)


            # print(f'http://www.xinfadi.com.cn/getPriceData.html?current={a}&pubDateStartTime=2023/01/01')

            # print(f'当前活动线程数量：{threading.active_count()}')
    print(f'当前线程池中正在使用的线程数量：{t._work_queue.qsize()}')
# 多线程访问新发地过快会报错，有时请求不到数据，还不如单线程能拿到数据