import requests


url  ='https://vip.lzcdn2.com/20220402/1945_f2f055d5/1200k/hls/mixed.m3u8'

head = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# resp = requests.get(url,headers=head)
# with open('fczlm.m3u8','wb') as f:
#     f.write(resp.content)

# 下载m3u8后，就可以不要上面的了


url_切 = url.rsplit('/',1)[0]
with open('fczlm.m3u8','r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        print(url_切+'/'+line)
        m3u8_url = url_切+'/'+line
        resp2 = requests.get(m3u8_url,headers=head)
        print(resp2.text)
        '''
        # f2= open(f'video/{line}','wb')
        # f2.write(resp2.content)
        # # f.close()
        # resp2.close()
        ############################
        with open(f'video/line.mp4','ab') as f2:
            f2.write(resp2.content)
        resp2.close()'''

        with open(f'video/{line}', 'ab') as f2:
            f2.write(resp2.content)
        resp2.close()

# 获取文件里的所有ts
import os

folder_path = 'video/'
file_list = []

# 遍历文件夹
for filename in os.listdir(folder_path):
    # 检查条目是否为文件
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_list.append(filename)

# 对列表进行排序
file_list_sorted = sorted(file_list)

print(file_list_sorted)

# 合并文件
# 定义输出文件名
output_file = '妇联4.mov'
# 打开输出文件
with open(output_file, 'wb') as outfile:
    # 遍历每个文件
    for ts_file in file_list_sorted:
        # 打开每个文件并读取内容
        with open(ts_file, 'rb') as infile:
            # 将内容写入输出文件
            outfile.write(infile.read())