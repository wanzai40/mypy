from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线对象,通过调用Line()函数创建一个折线图对象，并将其赋值给变量line。
line = Line()
line.add_xaxis(['的','啊','人'])
line.add_yaxis('GDP',[30,50,10])

# 设置全局配置项，还要再import
line.set_global_opts(
#     标题
    title_opts=TitleOpts(title='标题',pos_left='center',pos_bottom='80%'),
#     控制图例
    legend_opts=LegendOpts(is_show=True),
#     工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
#     视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)

)

# 生成网页
line.render()