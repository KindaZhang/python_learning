#列表元素修改
"""motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)"""

#列表元素末尾增加append(),以及空列表用append()增加元素
"""motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)"""

"""motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)"""


#插入元素：insert()
"""motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)"""

#删除元素 知道位置：del()
"""motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)"""

#有记录的删除：pop()
"""motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)"""

"""motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")"""

"""motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+".")
"""
#根据值来删除：remove()
"""motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)"""
"""
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too exopensive for me.")
"""
#排序

"""cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)"""

"""cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)"""


#反转列表
"""cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)"""

#列表长度
cars = ['bmw','audi','toyota','subaru']
print(len(cars))


