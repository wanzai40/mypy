import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
f_jp = open("E:\\日本.txt",'r',encoding='UTF-8')
jp_data = f_jp.read()      #拿到全部内容
f_us = open("E:\\美国.txt",'r',encoding='UTF-8')
us_data = f_us.read()      #拿到全部内容
f_in = open("E:\\印度.txt",'r',encoding='UTF-8')
in_data = f_in.read()      #拿到全部内容

# 去掉不符合JSON规范的内容：
# 获取us_data中第一个'{'的索引
a = us_data.index('{')
b = jp_data.index('{')
c = in_data.index('{')
print(a)
print(b)
print(c)
# 从第26个元素开始，到倒数第2个元素结束，将us_data中的数据切片,不包括-2
us_data = us_data[26:-2]
jp_data = jp_data[26:-2]
in_data = in_data[26:-2]

# JSON转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)


"""
Us dict这个字典，下面中有一个叫data的键，Data是个列表，所以第一个元素为0，这个0这是一个字典，它里面有一个trend这个键,然后tr_data的内容是trend这个键的值
"""
# 先获取到trend这个key
tr_data = us_dict['data'][0]['trend']
jp_data = jp_dict['data'][0]['trend']
in_data = in_dict['data'][0]['trend']


"""
根据上面取到的那个trend，这个key的值，也就是tr data的内容就是那个键的里面的value，这个value的内容有两个列表，然后x data取到的就是第一个列表里面的内容
"""
# 取日期数据，用于x轴，只取到12.31号
us_x_data = tr_data['updateDate'][:314]
jp_x_data = jp_data['updateDate'][:314]
in_x_data = in_data['updateDate'][:314]

# 取感染数据，用于y，只取到12.31号
us_y_data = tr_data['list'][0]['data'][:314]
jp_y_data = jp_data['list'][0]['data'][:314]
in_y_data = in_data['list'][0]['data'][:314]

line =  Line()

line.add_xaxis(us_x_data)

line.add_yaxis('us',us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('jp',jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('in',in_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title='疫情折线图',pos_left='center',pos_bottom='1%')
)

line.render()

f_us.close()
f_jp.close()
f_in.close()