list = [21,25,21,23,22,20]

print(list)

#查找下标
q = list.index(25)
print(q)

# 追加一个数字31到尾部
list.append(31)
print(list)
# 指定插入
list.insert(0,11)
print(list)

# 追加一个新列表[29,33,30]，到列表的尾部
list.extend([29,33,30])
print(list)

# 删除
del list[0]
print(list)

# 取出
num = list[-1]
print(f'取出{num}')

#取出并删除,可以被赋给变量
b = list.pop(3)
print(list,b)

# 删除第一个匹配的元素
list.remove(21)
print(list)

# 统计这个元素的个数
c = list.count(25)
print(c)

# 统计列表有几个元素
d = len(list)
print(d)

# 遍历列表
liebiao = [1,2,3,4,5,6,7,8,9,10]
oushu =[]
for i in liebiao:
    if i %2 ==0:
        oushu.append(i)
print(f'for偶数的列表：{oushu}')

# while
liebiao2 = [1,2,3,4,5,6,7,8,9,10]

oushu2 =[]
index = 0

while index < len(liebiao2):
    b = liebiao2[index]
    if b%2 ==0:
        oushu2.append(b)
    index+=1
print(f'偶数的列表：{oushu2}')
