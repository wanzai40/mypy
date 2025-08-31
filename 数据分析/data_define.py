"""
数据定义的类
"""
# 记录数据的基本信息
class Record:
    def __init__(self,date,order_id,money,province):
        self.date = date            #订单日期
        self.order_id = order_id    #订单id
        self.money = money          #订单金额
        self.province = province    #销售省份


    #通过魔术方法。把打印的内存地址转成字符串
    def __str__(self):
        return f'{self.date},{self.order_id},{self.money},{ self.province}'