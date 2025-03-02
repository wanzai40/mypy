

# 列表利用集合去重
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
my_set = set()      #空集合用set(),集合其实是{}
for k in my_list:
    my_set.add(k)
print(f'{my_set}')
# 移除
my_set.remove('best')
print(my_set)

# pop随机取出一个

#比较2个集合,在集合1里去除在集合2 里重复的，得到一个新集合
set1 = {1,3,4}
set2 = {1,2,0}
set12 = set1.difference(set2)
print(set12)

# 比较2个集合,在集合1里删除在集合2 里重复的，会导致集合1改变
set1 = {1,3,4}
set2 = {2,3,4}
set1.difference_update(set2)
print(set1)

# 2个集合 合并
set1 = {1,3,4}
set2 = {2,3,4}
set12 = set1.union(set2)
print(set12)
