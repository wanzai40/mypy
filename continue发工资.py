import random
# 公司财务10000元，20个员工
gs_money = 10000
for yuangong in range(1,21):
    if gs_money == 0:
        print(f'公司没钱了')
        break

    if random.randint(1,10)<5:
        print(f'员工{yuangong}：绩效分《5，滚')
        continue
    else:
        gs_money-=1000
        print(f'员工{yuangong}：给1000 ，公司余额：{gs_money}')
def add(a ,b):
    '''
    
    :param a:
    :param b:
    :return:
    '''
    ab= a+b
    print(f'{ab}')
    return ab
add(4,5)