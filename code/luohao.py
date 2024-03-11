""" a = int(input("第一个正整数："))
b = int(input("第二个正整数："))
for x in range(2,b+1):
    if a%x ==0:
        if b%x ==0:
            print("最小公约数"+x)
        else:
            print("最小公约数为1")
 """
 
 
""" x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break """
""" row = int(input("输入行数："))
for x in range(row):
    for _ in range(x+1):
        print('*',end=' ')
    print() """
    
row = int(input("输入行数："))
for x in range(row,-1):
    for _ in range(x):
        print('*',end=' ')
    print()
        
""" row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print() """