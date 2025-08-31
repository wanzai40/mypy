import time
import random
import requests
import csv
from concurrent.futures import ThreadPoolExecutor
from json import JSONDecodeError
import threading

data_list = []
lock = threading.Lock()


def download_page(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'Referer': 'http://www.xinfadi.com.cn/priceDetail.html',
        'Accept': 'application/json'
    }
    try:
        time.sleep(random.uniform(0.5, 1.5))
        resp = requests.post(url, headers=head, timeout=10)

        # 检查状态码
        if resp.status_code != 200:
            print(f"请求失败，状态码: {resp.status_code}, URL: {url}")
            return

        # 捕获 JSON 解析错误
        try:
            page_data = resp.json().get('list', [])
        except JSONDecodeError:
            print(f"响应内容不是有效的 JSON: {resp.text[:200]}...")
            return

        # 解析数据
        current_page_rows = []
        for item in page_data:
            row = [
                item.get('prodCat', ''),
                item.get('prodName', ''),
                item.get('avgPrice', ''),
                item.get('unitInfo', ''),
                item.get('place', ''),
                item.get('pubDate', ''),
                item.get('specInfo', '')
            ]
            current_page_rows.append(row)

        # 线程安全写入全局列表
        with lock:
            data_list.extend(current_page_rows)

        print(f"成功解析 {url}，获取到 {len(current_page_rows)} 条数据")

    except Exception as e:
        print(f"请求 {url} 异常: {e}")


if __name__ == '__main__':
    # 控制并发数和请求间隔
    with ThreadPoolExecutor(max_workers=20) as executor:
        for page in range(1, 200):
            url = f'http://www.xinfadi.com.cn/getPriceData.html?current={page}'
            executor.submit(download_page, url)
            time.sleep(random.uniform(0.2, 0.5))  # 降低请求频率

    # 写入文件
    with open('线程池爬test-2.csv', 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['一级分类', '品名', '平均价', '单位', '产地', '发布日期', '规格'])
        csv_writer.writerows(data_list)

    print(f"数据保存完成，总计 {len(data_list)} 条记录")