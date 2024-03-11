#4-1
"""pizzas = ['one','two','three']
for pizza in pizzas:
    print(pizza)
    print("I like "+pizza+" pizza")
print("I really love pizza!")"""
#4-2

"""animals = ['cat','dog','zebra']
for animal in animals:
    print(animal)
    print("A "+animal+" would make a great pet.")
print("Any of these animals would make a great pet!")"""


#4-3
"""numbers = [value for value in range(1,21)]
print(numbers)"""

#4-4
"""numbers = [value for value in range(1,100001)]
print(numbers)"""

#4-5
"""numbers = [value for value in range(1,100001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))"""


#4-6
"""numbers = [value for value in range(1,21,2)]
print(numbers)"""

#4-7
"""numbers = [value for value in range(3,31,3)]
print(numbers)"""

#4-8 4-9
"""numbers = [value**3 for value in range(1,11)]
print(numbers)"""

#4-10

"""my_foods = ['pizza','falafel','carrot cake','fruit cake','cholocate cake']
print("The first three items in the list are:")
for foods in my_foods[:3]:
    print(foods)
print("Three items from the middle of the list are:")
for foods in my_foods[1:4]:
    print(foods)
print("The last three items in the list are:")
for foods in my_foods[-3:]:
    print(foods)"""
    
#4-11

"""my_foods = ['pizza','falafel','carrot cake','fruit cake','cholocate cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('hambur')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)"""
#4-12
"""my_foods = ['pizza','falafel','carrot cake','fruit cake','cholocate cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('hambur')
for food in my_foods:
    print(food)
for food in friend_foods:
    print(food)
"""

#4-13

my_foods = ('pizza','falafel','carrot cake','fruit cake','cholocate cake')
for food in my_foods:
    print(food)
print("#######")
my_foods[0]='cake'
my_foods = ('pizza','falafel','carrot','fruit cake','cholocate')
for food in my_foods:
    print(food)
print("#######")

#4-14
阅读

#4-15

"""
my_foods = ['pizza','falafel','carrot cake','fruit cake','cholocate cake']
print("The first three items in the list are:")
for foods in my_foods[:3]:
    print(foods)
print("Three items from the middle of the list are:")
for foods in my_foods[1:4]:
    print(foods)
print("The last three items in the list are:")
for foods in my_foods[-3:]:
    print(foods)
"""

"""
my_foods = ['pizza','falafel','carrot cake','fruit cake','cholocate cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('hambur')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)
"""

"""
my_foods = ['pizza','falafel','carrot cake','fruit cake','cholocate cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('hambur')
for food in my_foods:
    print(food)
for food in friend_foods:
    print(food)
"""

my_foods = ('pizza','falafel','carrot cake','fruit cake','cholocate cake')
for food in my_foods:
    print(food)
print("#######")
my_foods[0]='cake'
my_foods = ('pizza','falafel','carrot','fruit cake','cholocate')
for food in my_foods:
    print(food)
print("#######")