money = int(input('设置开局游戏金额:'))
name = None
# 用户输入姓名
name = input('姓名：')
# 查询
def Inquire(flag):
    if flag:
        print('------------查询----------')
    print(f'余额：{money}')

# 存钱
def Saving(num):
    global money    #让money在函数中能全局变量
    money+=num
    print('------------存钱----------')
    print(f'存了{num}')
    Inquire(False)    #调用查询函数

#取
def take(num):
    global money
    if num > money:
        print('狂妄自大，没钱取')

    else:
        money-=num
        print('------------取----------')
        print(f'取{num}')
    Inquire(False)

# 菜单
def menu():
    print('-----------菜单----------')
    print('查询：\t1')
    print('存钱：\t2')
    print('取：\t\t3')
    print('滚：\t\t非1,2,3,')
    return input('》》》哪个？: ')

# 无限循环来一直运行
while True:
    keyboardInput =menu()
    if keyboardInput=='1':
        Inquire(True)
        continue
    elif keyboardInput == '2':
        num=int(input('存多少'))
        Saving(num)
        continue
    elif keyboardInput =='3':
        num =int(input('取多少？'))
        take(num)
        continue
    else:
        print('不玩，丨')
        break