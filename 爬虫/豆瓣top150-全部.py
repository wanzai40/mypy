import os

import requests
import re
import csv


url = 'https://movie.douban.com/top250'
head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
cook = {
    'cookie':'ll="118254"; bid=CzXlBY7iHdY; __utmc=30149280; __utmz=30149280.1742787332.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __utmz=223695111.1742787335.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=43be526c6a166183.1742787335.; __yadk_uid=jsfvd7lDM8kYPLyijcLICZY6KUuncuuN; _vwo_uuid_v2=DDB047BE67228423AB1AFBA3F769B5A90|9bdfe841a48ecef4e8db1dd28b1a8b97; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1742795571%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; __utma=30149280.739292639.1742787332.1742787332.1742795572.2; __utma=223695111.804065538.1742787335.1742787335.1742795572.2; ap_v=0,6.0'
}


file_path = '豆瓣250.csv'

if os.path.getsize(file_path) > 3:
    f = open(file_path, 'w')
    f.close()

for si in range(0, 251, 25):
    param = {
        'start':si,
        'filter':'',
    }


    resp = requests.get(url=url,headers=head,params=param)
    print(resp.text)
    page_content = resp.text
    obj = re.compile(r'<li>.*?<em>(?P<id>.*?)</em>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)

    iter_data = obj.finditer(page_content)

    f= open('豆瓣250.csv','a',newline='')

    csv_witer = csv.writer(f)
    for i in iter_data:
        # print(i.group('id'))
        # print(i.group('name'))
        # print(i.group('year').strip())
        # print(i.group('score'))
        dict = i.groupdict()            #把id，name等，全放到里面
        dict['year'] = dict['year'].strip()
        dict['score'] = dict['score']+'分'
        csv_witer.writerow(dict.values())
        f.flush()


f.close()
resp.close()