import json
from base64 import b64encode

import requests
from Crypto.Cipher import AES


url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='


# 真实的参数
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    'rid': "R_SO_4_2083785152",
    'threadId': "R_SO_4_2083785152",

}

f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g= '0CoJUm6Qyw8W8jud'
e ='010001'
i = "nteDwqhUHNvAKvgS"      #固定的i

# 固定的encSecKey
def get_encSecKey():
    return "7b58a6467b971ac5778e5a621ffcf9ac91817b8ece0afbf08fe53d6e90d2639fafb6610adf9deed3330fa51342a9a010abc2f1d11fa93bee99e2f2f0a600327862b1c66b8488c55a05607f5a62ae97ca4821cbadfcfb7981adf99e4f48b9f20f7f563f729add9e24805c5baa4f2c840ee4330696f1cf5d54050145fc8ab9b1ab"

def get_params(data):
    first =enc_params(data,g)
    second = enc_params(first,i)
    return second       #返回 的是params


def to_16(data):
    pad = 16-len(data)%16
    data+= chr(pad)*pad
    return data

# 加密过程
def enc_params(data,key):
    IV="0102030405060708"
    data=to_16(data)
    aes =AES.new(key=key.encode('utf-8'),IV=IV.encode('utf-8'),mode=AES.MODE_CBC)  #创建加密器
    bs=aes.encrypt(data.encode('utf-8'))   #加密,加密的长度必须是16的倍数
    return  str(b64encode(bs),'utf-8')  #转化成字符串返回




# 处理加密过程
'''
  function a(a) {       #随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)      #循环16次
            e = Math.random() * b.length,       #随机数
            e = Math.floor(e),      #取整
            c += b.charAt(e);       #去（取）字符串中xxx的位置
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)      #b也就是秘钥了
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")     
          , e = CryptoJS.enc.Utf8.parse(a)  #e:数据
          , f = CryptoJS.AES.encrypt(e, c, {        #c:是加密的秘钥
            iv: d,  #偏移量
            mode: CryptoJS.mode.CBC     #模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {            #d:上面的data, e:bsi0x(["流泪", "强"])->'010001',  f:上面的f,  g:同理
        var h = {}
          , i = a(16);      #就是一个随机值，然后尝试让i固定，固定后encSecKey也就固定了
        return h.encText = b(d, g),     #g：也就是秘钥
        h.encText = b(h.encText, i),        #返回的就是params
        h.encSecKey = c(i, e, f),       #就是encSecKey
        h
    }'''

resp= requests.post(url, data={
    'params':get_params(json.dumps(data)),
    'encSecKey':get_encSecKey()
})

# print(resp.text)
resptext = resp.json()
comments =[]
for i in range(15):  # 添加循环，从0到14
    name = resptext['data']['hotComments'][i]['user']['nickname']  # 使用索引i获取每条评论的用户昵称
    content = resptext['data']['hotComments'][i]['content'].replace('\n', '')  # 使用索引i获取每条评论的内容并去掉换行符
    comments.append([name, content])  # 将昵称和内容添加到列表中
    print(name,':'+ content)

import csv  # 导入csv模块
with open('comments.csv', 'a', newline='', encoding='utf-8') as file:  # 创建一个CSV文件
    writer = csv.writer(file)  # 创建一个csv.writer对象
    writer.writerows(comments)  # 将评论数据写入CSV文件