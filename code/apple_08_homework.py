#实践检验环节
#8-6
"""编写一个名为city_country()的函数，
   它接受城市的名称及其所属的国家。
   这个函数应返回一个格式类似于下面这样的字符串：
   "Santiago,Chile"
   至少使用三个城市-国家对调用这个函数，并打印它返回的值。
"""
#分析：1用到title（）函数，2 用到return函数进行返回，3 函数里面应设置2个参数，和一个变量
def city_country(city,country):
    full_address = city+','+country #满足分析3
    return full_address.title() #满足分析1,2
full_name = city_country('tai wan','china')
print(full_name)
full_name = city_country('hong kong','china')
print(full_name)
full_name = city_country('macao','china')
print(full_name)
"""city_country('tai wan','china')
   print(city_country) 
   这是一个错误的行为，函数不是变量，不可以直接print
"""

#8-7
    
"""
编写一个名为make_album()的函数，
它创建一个描述音乐专辑的字典。
这个函数应接受歌手的名字和专辑名，
并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，
并打印每个返回的值，
以核实字典正确地存储了专辑的信息。
给函数make_album()添加一个可选形参，
以便能够存储专辑包含的歌曲数。
如果调用这个函数时指定了歌曲数，
就将这个值添加到表示专辑的字典中。
调用这个函数，
并至少在一次调用中指定专辑包含的歌曲数。
"""

#分析 1 函数包含字典｛'singer':singger_name,'sing':dong_name｝,参数为（singger_name,song_name,num='0'）
# 2 return调用 创建函数调用3次

def make_album(singger_name,song_name,num=''):
    album = {'singger':singger_name,'song':song_name}
    if num:
        album['num'] = num#字典添加元素
    return album
album = make_album('赵雷','赵小雷')
print(album)
album = make_album('赵雷','无法长大','10')
print(album)
album = make_album('赵雷','暑前街少年')
print(album) 
"""迷茫点：字典的调用与字典添加 函数内的参数与字典元素之间弄错
   复习点：1 字典的创建，2 字典遍历， 3 增删改查
   创建：1 dict = {key:value}
        2 dict = {}
          dict[key] = value
        3 list = [(key,value)]
          dist = dist(list)
    遍历：key(),values(),items()
    key()是键值 values()是字典值 items()是字典整体
    都不是直接输出字典
    增删改查：增加： dict{key1:value1}
                    dict[key2] = value2
              删除： pop() dict{key1:value1} 从后往前弹出元素 可以调用此元素
                           dict.pop("key")
                     del   dict{key1:value1}
                           del dict[key]
                     popitem() 随机一个元素，与pop函数一样用法
                     clear() 清空字典
              修改：与增加雷同
              
"""

#8-8
"""
在为完成练习8-7编写的程序中，
编写一个while循环，
让用户输入一个专辑的歌手和名称。
获取这些信息后，
使用它们来调用函数make_album()，
并将创建的字典打印出来。
在这个while循环中，
务必要提供退出途径。
"""

def make_album(singger_name,song_name):
    album = {'singger':singger_name,'song':song_name}
    return album
while True:
    print("(退出输入q)")
    singger_name = input("请输入歌手名：")
    #print("(退出输入q)")
    if singger_name == 'q':
        break
    song_name = input("请输入专辑名：")
    if singger_name == 'q':
        break
    album1 = make_album(singger_name,song_name)
    print(album1)
    
"""关于函数的形参在主体中用 同样的命名是否会有不妥呢？"""

#8-9
"""创建一个包含魔术师名字的列表，
并将其传递给一个名为show_magicians()的函数，
这个函数打印列表中每个魔术师的名字。"""

magicians = ['刘谦','周星驰']
#magicians1 = []

def show_magicians(magicians):
    for magician in magicians:
        print("魔术师的名字是："+magician)
show_magicians(magicians)
#调用函数时带参数，则一开始定义事就应该带参数

#8-10
"""
在你为完成练习8-9而编写的程序中，
编写一个名为make_great()的函数，
对魔术师列表进行修改，
在每个魔术师的名字中都加入字样“the Great”。
调用函数show_magicians()，确认魔术师列表确实变了。
"""
#分析： 1添加一个函数，带有一个参数
magicians = ['刘谦','周星驰']
#magicians1 = []
def make_great(magicians):
    for magician in range(len(magicians)):
        msg = "the Great "+str(magicians[magician])
        magicians[magician] = msg
def show_magicians(magicians):
    for magician in magicians:
        print("魔术师的名字是："+magician)
make_great(magicians)
show_magicians(magicians)
"""总结：这一题让我意识到还得要努力，加油"""


#8-11

"""修改你为完成练习8-10而编写的程序，
在调用函数make_great()时，
向它传递魔术师列表的副本。
由于不想修改原始列表，
请返回修改后的列表，
并将其存储到另一个列表中。
分别使用这两个列表来调用show_magicians()，
确认一个列表包含的是原来的魔术师名字，
而另一个列表包含的是添加了字样“the Great”的魔术师名字。"""

magicians = ['刘谦','周星驰']
magicians1 = []
def make_great(magicians,magicians1):
    for magician in range(len(magicians)):
        msg = "the Great "+str(magicians[magician])
        magicians1.append(msg)
def show_magicians(magicians,magicians1):
    for magician in magicians:
        print("魔术师的名字是："+magician)
    for magician in magicians1:
        print("改变后的魔术师："+magician)
make_great(magicians[:],magicians1)
show_magicians(magicians,magicians1)


#8=12
"""
编写一个函数，
它接受顾客要在三明治中添加的一系列食材。
这个函数只有一个形参（它收集函数调用中提供的所有食材），
并打印一条消息，
对顾客点的三明治进行概述。
调用这个函数三次，
每次都提供不同数量的实参
。"""


"""make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')"""

def sandwich(*toppings):
    for topping in toppings:
        print("顾客点的是: "+topping+"三明治")
        
sandwich('沙拉')
sandwich('沙拉','芝士')
sandwich('沙拉','芝士','起司')


#8-13


"""复制前面的程序user_profile.py，
在其中调用build_profile()来创建有关你的简介；
调用这个函数时，
指定你的名和姓，
以及三个描述你的键-值对。"""

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile =build_profile('张','三',location = '中国',field = '科学')
print(user_profile)

"""
编写一个函数，
将一辆汽车的信息存储在一个字典中。
这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
这样调用这个函数：提供必不可少的信息，以及两个名称—值对，
如颜色和选装配件。这个函数必须能够像下面这样进行调用：
car = make_car('subaru','outback',color='blue',tow_package=True)
打印返回的字典，
确认正确地处理了所有的信息"""

def make_car(maker,size,**toppings):
    cars = {}
    cars['制造商'] = maker
    cars['型号'] = size
    for key,value in toppings.items():#zhey9bu必不可少，虽然**是穿件了一个空字典，但这个字典不属于刚创建的另一个字典
        cars[key] = value
    return  cars
cars1 = make_car('大众','辉腾',color='black',tow_package=True)
print(cars1)


