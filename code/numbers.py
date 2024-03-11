#for range
"""for value in range(1,5):
    print(value)"""
    
"""for value in range(1,6):
    print(value)"""
    
# list转换列表

"""numbers = list(range(1,6))
print(numbers)"""

#步长
"""even_numbers = list(range(2,11,2))
print(even_numbers)"""

#平方

"""squares =[]
for value in range(1,11):
    square =value**2
    squares.append(square)
print(squares)"""
"""
squares =[]
for value in range(1,11):
    squares.append(value**2)
print(squares)"""

squares = [value**2 for value in range(1,11)]
print(squares)