name = input('姓名：')
gender = input('性别：')
CLASS = input('班级：')
studentID = input('学号：')

print(f'我叫{name}，{gender}，我的班级是{CLASS}，我的学号是：{studentID}')

#
edgeLength1 = int(input('第一条边长为：'))
edgeLength2 = int(input('第二条边长为：'))
edgeLength3 = int(input('第三条边长为：'))
girth = edgeLength1 + edgeLength2 + edgeLength3
print(f'周长为：{girth}')