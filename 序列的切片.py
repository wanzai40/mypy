my_str = '万过薪月,员序程马黑来,nohtyP学'

# 倒序字符串，切片取出或切片取出，然后倒序
my_str1 = my_str[::-1]
my_str2 =my_str1[9:14]
print(my_str2)

# 1.2
# my_str1 = my_str[::-1][9:14]


# split分隔"，"replace替换"来"为空，倒序字符串
my_str11 = my_str.split(',')
print(my_str11)
# my_str22 = my_str11[1]    #split后是列表，通过下标取出列表的第二个元素，员序程马黑来
my_str22 = my_str11[1].replace('来','')[::-1]
print(my_str22)