def print_file_info(file_name):
    """传入文件的路径，打印文件的全部内容"""
    f = None
    try:
        f = open(file_name,'r',encoding='utf-8')
        print(f'内容：\n{f.read()}')
    except Exception as e:
        print(f'{file_name}文件不存在')
    finally:
        if f:            #如果变量是None，表示False，如果有任何内容，就是True
            f.close()

def append_to_file(file_name,data):
    """接收文件路径以及传入数据，将内容追加写入到文件中"""
    f = open(file_name,'a',encoding='utf-8') #追加模式
    f.write(data)
    f.write("\n")
    f.close()