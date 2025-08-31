import re

import requests
domain = 'https://www.dygod.net/html/gndy/index.html'

head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

resp = requests.get(domain,verify=False,headers=head)
resp.encoding = 'gb2312'

# print(resp.text)

# 拿到ul里的li
obj1 = re.compile(r'<div class="title_all"><p>2013精品专区.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile("<a href='(?P<herf>.*?)'",re.S)

child_href_list = []

result1 = obj1.finditer(resp.text)
for i in result1:
        ul = i.group('ul')
        print(ul)

        # 提取子页面链接
        result2 = obj2.finditer(ul)
        for ii in result2:
                child_href = domain.replace('/html/gndy/index.html','') + ii.group('herf')#.lstrip('/html/gndy/')
                print(ii.group('herf'))
                print(child_href)
                child_href_list.append(child_href)


#
obj3 = re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1>.*?<li><a href="(?P<movie>.*?)">',re.S)
for href in child_href_list:
        child_resp = requests.get(href,verify=False,headers=head)
        child_resp.encoding='gbk'
        result3 = obj3.search(child_resp.text)
        print(result3.group('name'))
        print(result3.group('movie'))


resp.close()