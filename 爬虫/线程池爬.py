import csv
from concurrent.futures import ThreadPoolExecutor
import time
import requests
from lxml import etree
# url = 'http://58.48.136.167:7500/price/priceStatistics/queryJBSJData'



f = open('菜价.csv',mode='w',encoding='utf-8',newline='')
csvwrite = csv.writer(f)

def dowlode_one_page(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'referer': 'https://www.cnhnb.com/'

    }
    resp = requests.get(url,headers=head)
    # print(resp.text)
    html = etree.HTML(resp.text)
    div_quotation_content_list=html.xpath('//*[@id="__layout"]/div/div/div[2]/div[1]/div[3]/div/div[1]/div/div[1]/div[2]')[0]
    lis = div_quotation_content_list.xpath('./ul/li')
    # print(lis[0])
    time = html.xpath('//*[@id="__layout"]/div/div/div[2]/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/span[1]/text()')
    print(time)
    csvwrite.writerow(time)

    for li in lis:
        span = li.xpath('./a/span/text()')
        span = (item.replace('\n','').replace(' ','').replace('-','').replace('','') for item in span)
        # print(list(span))
        csvwrite.writerow(span)  # 将提取的数据写入CSV文件
    print(url,'ok')






if __name__ == '__main__':
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'referer':'https://www.cnhnb.com/'

    }

    # dowlode_one_page(url='https://www.cnhnb.com/hangqing/cdlist-2003192-0-17-0-0-1/'   ,head=head)
    with ThreadPoolExecutor(2) as t :
        for i in range(1,6):
            t.submit(dowlode_one_page,f'https://www.cnhnb.com/hangqing/cdlist-2003192-0-17-0-0-{i}/')
            time.sleep(3)
    f.close()
