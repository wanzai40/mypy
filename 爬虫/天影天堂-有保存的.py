import csv
import re

import requests


'''
爬的是精品电影专区
'''
domain = 'https://www.dytt8899.com/html/gndy/dyzz/index.html'

head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

resp = requests.get(domain,verify=False,headers=head)
resp.encoding = 'gb2312'

# print(resp.text)

# 
obj1 = re.compile(r'<b>(?P<b>.*?)</b>',re.S)
obj2 = re.compile('<a href="(?P<herf>.*?)"',re.S)

child_href_list = []

result1 = obj1.finditer(resp.text)

for i in result1:
        # print(i)
        b = i.group('b')
        print(b)

        result2 = obj2.finditer(b)
        for ii in result2:
            print(ii)
            child_href = domain.replace('/html/gndy/dyzz/index.html', '') + ii.group('herf')
            child_href_list.append(child_href)



print(child_href_list)



        # 提取子页面链接
        # result2 = obj2.finditer(ul)
        # for ii in result2:
        #         child_href = domain.replace('/html/gndy/dyzz/index.html','') + ii.group('herf')#.lstrip('/html/gndy/')
        #         print(ii.group('herf'))
        #         print(child_href)
        #         child_href_list.append(child_href)


#
obj3 = re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1>.*?<li><a href="(?P<movie>.*?)">',re.S)
with open('最新电影专区.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['最新电影专区'])  # 修改为列表格式
    writer.writerow(['[播放器自己下：https://softdl.rinhome.com/jianpian_4.2.3.48_0828_Full.exe]'])  # 修改为列表格式

    writer.writerow(['Name', 'Movie Link'])  # 写入表头
    for href in child_href_list:
            child_resp = requests.get(href,verify=False,headers=head)
            child_resp.encoding='gbk'
            result3 = obj3.search(child_resp.text)
            print(result3.group('name'))
            print(result3.group('movie'))
            if result3:  # [新增] 检查是否找到匹配
                writer.writerow([result3.group('name')+'\t\t\t'   ,'\t\t\t\t\t\t' +   result3.group('movie')])  # 写入数据



'''
obj3 = re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1>.*?<li><a href="(?P<movie>.*?)">',re.S)
for href in child_href_list:
        child_resp = requests.get(href,verify=False,headers=head)
        child_resp.encoding='gbk'
        result3 = obj3.search(child_resp.text)
        print(result3.group('name'))
        print(result3.group('movie'))
'''

resp.close()