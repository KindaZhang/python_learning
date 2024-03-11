"""requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")"""
    
    
    #
"""requested_toppings = ['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")"""


#

"""requested_toppings = ['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are ot of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")"""



#


"""requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
"""

#

"""available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza!")
"""

#5-8
"""users = [ 'aaa','bbb','ccc','ddd','admin']
for user in users:
    if users == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+user+",thank you for logging in again")

"""
#5-9

"""users = [ 'aaa','bbb','ccc','ddd','admin']
if users != []:
    for user in users:
        if users == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello "+user+",thank you for logging in again")
else:
    print("We need to find some users!")
print("exit "+users.pop())
print("exit "+users.pop())
print("exit "+users.pop())
print("exit "+users.pop())
print("exit "+users.pop())"""


#5-10
"""current_users = [ 'aaa','bbb','ccc','ddd','admin']
new_users = [ 'aaa','Bbb','www','fff','admin']
for current_user in current_users:
    current_user.lower()
for new_user in new_users:
    if new_user.lower() in current_users:
        print("used,need to use other username")
    else:
        print("Not used")"""


#5-11
"""numbers = []
for value in range(1,10):
    numbers.append(value)
print(numbers)"""
numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == '1':
        print(str(number)+"st")
    elif number == '2':
        print(str(number)+"nd")
    elif number == '3':
        print(str(number)+"rd")
    else:
        print(str(number)+"th")



#5-12



#5-13





