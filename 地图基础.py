from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()

data = [
    ('湖北省',33),
    ('湖南省',56),
    ('陕西省',12),
    ('山西省',88)
]

map.add('测试',data,'china')

# 设置全局选项
# 设置全局选项
map.set_global_opts(
    # 设置视觉映射选项
    visualmap_opts=VisualMapOpts(
        # 是否显示
        is_show=True,
        # 是否分段显示
        is_piecewise=True,
        # 分段显示的参数
        pieces=[
            # 第一段
            {'min':1,'max':12,'label':'1-12','color':'#456'},
            # 第二段
            {'min':13,'max':33,'label':'13-33','color':'#9hg'},
            # 第三段
            {'min':34,'max':56,'label':'34-56','color':'#5q1'},
            # 第四段
            {'min':57,'max':100,'label':'57-100','color':'#9c5'}
        ]

    )
)

map.render()