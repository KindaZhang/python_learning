#6-1
""" 
friend = {
    'first_name':'wang',
    'last_name':'miaoyan',
    'sex':'girl',
    'hobby':'man',
    'age':'24',
    'city':'taiyuan',
}

print(friend['age'])
print(friend['city'])
print(friend['first_name'])
print(friend['last_name'])
print(friend['hobby'])
print(friend['sex']) 
"""


#6-2

"""
number_like = {
    'wang':1,
    'li':2,
    'xiao':3,
    'zhao':4,
    'lie':5,
}
for key,value in number_like.items():
    print(key+":"+str(value)) 
"""


#6-3
""" number_learned = {
    'num1':'C',
    'num2':'Python',
    'num3':'Java',
    'num4':'C#',
    'num5':'Go',
}

for num,value in number_learned.items():
    print(num+':'+value+'\n') """


#6-4
""" number_learned = {
    'num1':'C',
    'num2':'Python',
    'num3':'Java',
    'num4':'C#',
    'num5':'Go',
}

for num,value in number_learned.items():
    print(num+':'+value+'\n') """


#6-5


""" rivers = {
    'nile':'egypt',
    'amazon river':'brazil',
    'mississippi river':'america',
}
for river,country in rivers.items():
    print("The "+river.title()+" runs through "+country.title()+".")
    
for river in rivers.values():
    print(river)
for country in rivers.keys():
    print(country) """
    
    
#6-6

""" favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    } 
friends = ['phil','zhang']
for friend in favorite_languages.keys():
    print(friend.title())
    if friend in friends:
        print("Thank you"+friend.title())
    if friend not in friends:
        print("invent you "+friend.title())
 """

#6-7

""" friend = {
    'first_name':'wang',
    'last_name':'miaoyan',
    'sex':'girl',
    'hobby':'man',
    'age':'24',
    'city':'taiyuan',
}
friend1 = {
    'first_name':'wang',
    'last_name':'miaoyan',
    'sex':'girl',
    'hobby':'man',
    'age':'24',
    'city':'taiyuan',
}
friend2 = {
    'first_name':'wang',
    'last_name':'miaoyan',
    'sex':'girl',
    'hobby':'man',
    'age':'24',
    'city':'taiyuan',
}

friend3 = ['friend','friend1','friend2']

for friend123 in friend3[:3]:
    print(friend)
 """

#6-8
""" pets = []
li = {
    'name':'li',
    'master':'wang',
    'kind':'dog',
}
pets.append(li)
lie = {
    'name':'lie',
    'master':'wa',
    'kind':'cat',
}
pets.append(lie)
lin = {
    'name':'lin',
    'master':'wen',
    'kind':'bird',
}
pets.append(lin)
for pet in pets[0:3]:
   print(pet) """


#6-9
""" favorite_places = {
    'li':['1','2','3'],
    'lie':['4','5','6'],
    'lin':['7','8','9'],
}

for name,place in favorite_places.items():
    print(name)
    print(place) """


#6-10

""" 
number_like = {
    'wang':[1,2,3],
    'li':2,
    'xiao':3,
    'zhao':4,
    'lie':[5,7,6],
}
for name,number in number_like.items():
    print(name)
    print(number) """
#6-11




cities = {
    'nj':{
        'country':'c',
        'population':110,
        'fact':333,
    },
    'nj1':{
        'country':'cc',
        'population':1101,
        'fact':3331,
    },
    'nj2':{
        'country':'ccc',
        'population':1102,
        'fact':3333,
    },
}
for coun,value in cities.items():
    print(coun)
    print(value)

#6-12















