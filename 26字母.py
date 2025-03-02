import time
# text = 'hello word python'
text = input('输入要流星的内容--(仅支持大小写26字母，数字，中英文逗号，感叹号，空格)\n')
keydown = input('输入“1”后3秒后开始：')
en26 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789，,! '
kong = ''

if keydown == '1':
    time.sleep(3)
    for char in text:
        for letter in en26:
            print(kong + letter)
            time.sleep(0.05)
            if letter == char:
                kong += letter
                # print(kong)
                break
print('完成,30秒自动关闭')
time.sleep(30)



'''
import time
text = 'hello word'
en26 = ' abcdefghijklmnopqrstuvwxyz'
kong = ''
for char in text:
    for letter in en26:
        if letter == char:
            kong += letter
            print(kong)
            time.sleep(0.001)
            break
        else:
            print(kong + letter)
            time.sleep(0.001)
'''