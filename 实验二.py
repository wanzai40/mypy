#1、从键盘输入父母的身高，并使用 eval()或 float()转换输入的数据类型。计算公式：儿子身 高=(父亲身高+母亲身高)*0.54。
father = float(input('父，身高（cm）'))
mather = float(input('母，身高（cm）'))
son = (father + mather) * 0.54
print(f'儿子：{son:.2f}')


# 2、从键盘获取一个4 位整数，分别输出个位、十位、百位、千位上的数字。

number = int(input("请输入一个4位整数："))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10
print(f"千位数字：{thousands}")
print(f"百位数字：{hundreds}")
print(f"十位数字：{tens}")
print(f"个位数字：{units}")

# 3、输入圆的半径，计算周长和面积（提示：PI用 math 中的 PI)
import math
r = float(input('半径：'))
c = 2 * math.pi * r
s = math.pi * r * r
print(f'周长：{c:.2f}  面积：{s:.2f}')

# 4、要求用户一次性输入姓名、年龄、婚否、身高，分别用字符串、整数、布尔、小数表示 (提示：用“,”分开）
user = input('输入姓名、年龄、婚否、身高（cm）(提示：用“,”分开 中文的）')
name, age, married, height = user.split('，')
age = int(age)
married = True if married == '是' else False if married == '否' else None
height = float(height)
print(f'姓名：{name}  年龄：{age}  婚否：{married}  身高：{height}')
print(type(name), type(age), type(married), type(height))