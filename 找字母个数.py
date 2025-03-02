# 定义字符串变量name，内容为:"itheimais abrand ofitcast'
# 通过for循环，遍历此字符串，统计有多少个英文字母:"a

name='itheimais abrand ofitcast'
y: int=0
for x in name:
    if x == 'a':
        y+=1
print(f'a的个数为{y}')