#返回简单值

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title() #title()开头首字母大写
musician = get_formatted_name('jimi','hendrix')
print(musician)


#可选实参

def get_formatted_name(first_name,middle_name,last_name):
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)

"""区别在于给middle_name一个默认值，if真，打印三个，if假，打印2个"""
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)
musician = get_formatted_name('jimi','hendrix')
print(musician)

#返回字典
""""""
def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)


def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)

#while与函数相结合

"""利用input函数惊醒用户输入，进行人机交互，但是这个while函数是一个无限循环不可取"""
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title() #title()开头首字母大写
"""while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    l_name = input("Last name:")
    formatted_name = get_formatted_name(f_name,l_name)#调用def
    print("\nHello, "+formatted_name+"!")"""
    
"""使用break结束循环，是否可以将break封装成函数呢？可以，但是有点得不偿失"""    
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title() #title()开头首字母大写
"""while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name =='q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)#调用def
    print("\nHello, "+formatted_name+"!")
"""
#实践检验成果环节 apple_08_homework.py

#传递列表

def greet_users(names):
    """想列表中的美味用户都发出简单的问候"""
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)
usernames = ['hannah','ty','margot']
greet_users(usernames)

#在函数中修改列表


#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
#模拟打印每个设计，知道没有未打印的设计为止
#打印每个涉及后，都将其移到列表copleted——models中
while unprinted_designs:
    current_design = unprinted_designs.pop()#这个就是列表弹出最后一个元素
#模拟根据涉及制作3D打印模型的过程
    print("Printing model:"+current_design)
    completed_models.append(current_design)#添加列表元素append()
#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
    



def print_models(unprinted_designs,completed_models):
#模拟打印每个设计，直到没有未打印的设计为止
#打印每个涉及后，都将其移到列表copleted——models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()#这个就是列表弹出最后一个元素
    #模拟根据涉及制作3D打印模型的过程
        print("Printing model:"+current_design)
        completed_models.append(current_design)#添加列表元素append()
def show_completed_models(completed_models):
    #显示打印好的所有模型
    print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)      
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#传递实参
def make_pizza(*toppings):#*就是创建一个空元组
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the followiong toppongs:")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#位置实参和任意实参
def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print("\nMaking a "+str(size)+"-inch pizza with the followiong toppongs:")
    for topping in toppings:
        print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile =build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)


#将函数创建模块

def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)