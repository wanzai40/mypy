r'''from DrissionPage import ChromiumOptions
path=r'C:\Program Files\Google\Chrome\Application\chrome.exe' #请改为你电脑内Chrome可执行文件路径
ChromiumOptions().set_browser_path(path).save()'''

from DrissionPage import ChromiumPage
from pprint import pprint
import csv




f= open('酒店.csv', 'w', encoding='utf-8', newline='')
# 字典写入方法
csv_writer = csv.DictWriter(f, fieldnames=['名称', '价格', '地址', '评分','评论数','照片'])
# 表头
csv_writer.writeheader()

dp = ChromiumPage()

# 监听数据包
dp.listen.start('HotelSearch')

dp.get('https://cube.meituan.com/cube/block/ae43f238d3fe25cced30/251405/index.html?hotelchannel=BsFdBdBbHfJ&appkey=eada18a6c600f1077cc3da724e89cf6f:jdzx1000&mtlm=cps%3Ahotel%3A1719938602%3AgwU4wIzn15YS-lujcqBMnx-i_iB4fEHOhJuIPcc9e9IOuEXnFmQoPrezjWrgVi4uF29m4nb-DbXJ8dT3CQ5N1uc')
# dp.get('https://ihotel.meituan.com/coresearch/HotelSearch?externalRequestSource=Cube-251405&mysteryBoxCrossActivityId=251405&sourceType=hotelSearch&limit=20&offset=0&startDay=20250619&endDay=20250619&sort=smart&gps_cityid=57&ci=57&q=%E6%B1%9F%E6%B1%89%E8%B7%AF%E6%AD%A5%E8%A1%8C%E8%A1%97&ste=_b300201&attr_28=129&cateId=20&discount_type_poi=544342&mypos=undefined%2Cundefined&cityId=57&cityid=57&platformid=1&utm_medium=touch&version_name=999.9&yodaReady=h5&csecplatform=4&csecversion=3.2.0&mtgsig=%7B%22a1%22%3A%221.2%22%2C%22a2%22%3A1750306854861%2C%22a3%22%3A%22743yxxvuvuw3523z0026wu5271385zyz802133240x597958y9v6v49w%22%2C%22a5%22%3A%2246y06zjR49AQ5edAht9ZoZZV7lySp1O8sA%2F2v9MX8WpP5VN%2F0B7hGYmIXdH9XO1qqOD%3D%22%2C%22a6%22%3A%22hs1.67%2F%2BNvEuAyD6IvcOo7aCwSlZugrdNrqs6Wik6raGUYoOIwYe3VC6UH7RmaYDLw%2B36QzkzVQ4kZYY4Z2nlOT%2B%2BLHtGYEflEGkpWNwVUIb3AB7%2FwPhn1u11ymQq0Odqs12m94yAm0IEeXjPkIR4fGvU95TbFq69yykzgtrpqAVmuFA%3D%22%2C%22a8%22%3A%22cea758796d15b72ae74b37e206e10ac9%22%2C%22a9%22%3A%223.2.0%2C7%2C141%22%2C%22a10%22%3A%2206%22%2C%22x0%22%3A4%2C%22d1%22%3A%22e150a4086212d30cc493917b8342770b%22%7D')

# 等待数据包加载
r = dp.listen.wait()

# 获取数据
json_data= r.response.body

# print(json_data)

# 先提取到酒店列表存放在哪一层
hotel_list = json_data['data']['searchresult']
# 遍历酒店列表
for hotel in hotel_list:
    img = hotel['frontImg'].split('w.h/')  # 使用 split() 方法切分字符串
    # print(img)
    img2 = ''.join(map(str, img)) # 将列表转换为字符串
    # print(img2)

    img4 = img2+'@240w_286h_1e_1c'

    # 在循环中提取每个酒店的具体信息 并放在字典里
    dic = {
        '名称': hotel['name'], # 酒店名称
        '价格': hotel['originalPrice'], # 酒店价格
        '地址': hotel['addr'],  # 酒店dizi
        '评分': hotel['avgScore'], # 酒店评分
        '评论数': hotel['commentsCountDesc'], # 酒店评论数
        '照片':img4
    }

    # 写入csv文件
    csv_writer.writerow(dic)
    print(dic)




