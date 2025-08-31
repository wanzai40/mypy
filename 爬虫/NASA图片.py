'''
用bs4 来爬
'''
import time

import requests
from bs4 import BeautifulSoup

url = 'https://www.nasachina.cn/astronomy-picture-of-the-day'

head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

resp = requests.get(url,headers=head)
# print(resp.text)

#用BeautifulSoup打开网页
main_page = BeautifulSoup(resp.text,'html.parser')
#先拿到图片集的大div，再找里面的a标签       也就是子页面
a_list = main_page.find('div',class_='elementor-posts-container elementor-posts elementor-posts--skin-cards elementor-grid').find_all('a',class_='elementor-post__thumbnail__link')
# print(a_list)





for a in a_list:
    print(a.get('href'))
    #请求到子页面
    href = a.get('href')
    child_page_resp = requests.get(href,headers=head)
    #子页面的源代码
    child_page_text = child_page_resp.text
    #用BeautifulSoup打开
    child_page = BeautifulSoup(child_page_text,'html.parser')
    #找子页面中图片的父级div
    try:
        div_img = child_page.find('div',class_='entry-content single-content')
        #在大div里面找到img标签
        img = div_img.find('img')
        #在img标签里面找src属性
        src = img.get('src')
        #请求图片的链接
        img_resp = requests.get(src,headers=head)
        #定义图片的名字
        img_name = src.split('/')[-1]
        with open('img/' + img_name, mode='wb') as f:
            f.write(img_resp.content)  # img_resp.content  拿到的是图片的字节
        pass

    except  Exception:
        div_video = child_page.find('video',class_='wp-video-shortcode')
        video = div_video.find('source')
        video_src = video.get('src')
        video_src_resp = requests.get(video_src,headers=head)
        video_name_yichuqianmian = video_src.split('/')[-1]         #移除前面的，只要最后一个 / 后面的作为文件名
        video_name_yichuwenhaohoumian = video_name_yichuqianmian.split('?')[0].split('/')[-1]    #  移除名字后面的？开始的内容
        with open('img/'+video_name_yichuwenhaohoumian,mode='wb') as f:
            f.write(video_src_resp.content)
        pass


    print('下载ing  ',img_name)
    time.sleep(3)



print('完成')
resp.close()