import subprocess

from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType



import file_define
from data_define import Record

txt_file_read = file_define.txtFileRead('./2011年1月销售数据.txt')
json_file_read = file_define.jsonFileRead('./2011年2月销售数据JSON.txt')

# 通过txt_file_read里面的read_data的方法来去获取数据了
jan_data = txt_file_read.read_data()    #一月数据   #jan_data ： list类型，里面存放的是record对象   #......这个read_data是TextFileReader类里定义的一个函数，其返回值类型为list[Record]
feb_data = json_file_read.read_data()    #二月数据

# 将2个月份的数据合并一个
all_data = jan_data + feb_data

data_dict ={}
for record in all_data:
    # print(type(record) ,record)
    if record.date in data_dict.keys():
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date] = record.money
print(data_dict)

# 可视化图表开发
bar =Bar(init_opts=InitOpts(theme=ThemeType.DARK))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额',list(data_dict.values()),label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)

bar.render('销售.html')

subprocess.run(["start", "Google Chrome", "销售.html"], shell=True)