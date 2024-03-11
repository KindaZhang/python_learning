#7-1
""" car = input("which car do you want?")
print("Let me see if i can find you a "+car) """


#7-2

""" number = input("How many people?")
number = int(number)
if number > 8:
    print("no table")
else:
    print("have table.")
 """

#7-3

""" number = input("a number:")
number = int(number)
if number % 10 == 0:
    print("是十的倍数。")
else:
    print("不是时的倍数。") """

#7-4

#choose = input("输入选择：")
""" while True:
    choose = input("输入选择：")
    if choose == 'quit':
        break
    else:
        print(choose)
 """

#7-5


""" age ="你所少岁？"
while True:
    message = int(input(age))
    if message <=3:
        print("free")
    elif message >12:
        print("15元")
    else:
        print("10元")
 """

#6-6

""" age ="你所少岁？"
active = True
while active:
    message = int(input(age))
    message2 = str(input(age))
    if message2 =='quit':
        break
    if message <=3:
        print("free")
        active =False
    elif message >12:
        print("15元")
        active =False
    else:
        print("10元")
        active =False """


#7-7



#7-8
""" sandwich_orders = ['one','teo','three']
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("\nI made "+sandwich_order+" sandwich")
    finished_sandwiches.append(sandwich_order)
for sandwich in finished_sandwiches:
    print(sandwich) """

#7-9
""" sandwich_orders = ['one','pastrami','teo','pastrami','three','pastrami']
print("\n五香牛肉买完了！")
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("\nI made "+sandwich_order+" sandwich")
    finished_sandwiches.append(sandwich_order)
for sandwich in finished_sandwiches:
    print(sandwich)  """

#7-10


place = {}
vac = True
while vac:
    user = input("who?")
    place_1 = input("Where tog go?\n")
    place[user] = place_1
    print("lll")
    repeat = input("yes or no")
    if repeat == 'no':
        vac = False
for user,place_1 in place.items():
    print(user+":"+place_1)
print(place)




































