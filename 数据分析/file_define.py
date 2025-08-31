"""
和文件相关的类定义
"""
import json

import data_define

# 先定义一个抽象类，确定有哪些功能需要实现
class FileRead:
    """" 读取文件的数据，读掉的每一条数据都转换成Record对象，然后将他们封装到list里返回"""
    def read_data(self) -> list[data_define.Record]:
        pass

class txtFileRead(FileRead):
    #定义成员变量，，记录文件的路径
    def __init__(self,path):
        self.path = path

    #复写（实现抽象方法）父类的方法
    def read_data(self) -> list[data_define.Record]:
        with open(self.path,'r',encoding='UTF-8')as f:         #在方法内部使用成员变量 要注意self
            record_list = []
            for line in f.readlines():
                line = line.strip()        #处理前后空格，换行符
                data_list = line.split(',')
                # print(data_list)
                record = data_define.Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
                record_list.append(record)
        return record_list


class jsonFileRead(FileRead):
    # 定义成员变量，，记录文件的路径
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[data_define.Record]:
        with open(self.path, 'r', encoding='UTF-8') as f:  # 在方法内部使用成员变量 要注意self
            record_list = []
            for line in f.readlines():
                data_dict = json.loads(line)
                record = data_define.Record(data_dict['date'],data_dict['order_id'],int(data_dict['money']),data_dict['province'])
                record_list.append(record)
        return record_list


if __name__ == '__main__':
    text_file_read = txtFileRead('./2011年1月销售数据.txt')
    list_txt = text_file_read.read_data()


# print(list_txt)
#     for l in list_txt:
#         print(l)