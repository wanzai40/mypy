def str_reverse(str):
    """受传入字符串，将字符串反转返回"""
    return str[::-1]

def substr(s,x,y,z):
    '''按照下标x和y，对字符串s进行切片,步长为z'''
    return s[x:y:z]

if __name__ == '__main__':
    print(str_reverse("核对阿是对啊手打UI很大"))