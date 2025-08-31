import requests
import re
import csv

url = 'https://movie.douban.com/top250'
head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}

resp = requests.get(url=url,headers=head)
# print(resp.text)
page_content = resp.text
obj = re.compile(r'<li>.*?<em>(?P<id>.*?)</em>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)

result = obj.finditer(page_content)
f= open('豆瓣250.csv','w',newline='')
csv_witer = csv.writer(f)
for i in result:
    # print(i.group('id'))
    # print(i.group('name'))
    # print(i.group('year').strip())
    # print(i.group('score'))
    dict = i.groupdict()            #把id，name等，全放到里面
    dict['year'] = dict['year'].strip()
    csv_witer.writerow(dict.values())

f.close()
resp.close()