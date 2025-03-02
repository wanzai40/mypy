print('hello')

#9 9 乘法表
i=1
while i<=9 :
    j= 1
    while j<=i:
        print(f'{i} * {j} = {i*j}\t',end='')
        j+=1
    i+=1
    print()

print()
# 用for循环
for x in range(1,10):
    for y in range(1,x+1):
        print(f'{x} * {y} = {x * y}\t', end='---')
    print()

s = '学习'
s= '赋'+s[1:]
print(s)