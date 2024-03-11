#字典 外星人
"""
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
"""

#外星人2

"""
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")
print(alien_0['color'])
print(alien_0['points'])
"""


#外星人3

"""
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#print(alien_0['color'])
#print(alien_0['points'])
# """

#创建空字典

"""
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points']=5
print(alien_0)
"""

#修改字典

""" 
alien_0 = {'color':'green'}
print("The alien is "+alien_0['color']+".")
alien_0['color'] = 'yellow'
print("The alien is now "+alien_0['color']+".") 
"""

#外星人移动

""" 
alien_0 = {'x_poisiton':0,'y_poisition':25,'speed':"medium"}
print("Original  x-poisition:"+str(alien_0['x_poisiton']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_poisiton'] = alien_0['x_poisiton']+x_increment
print("New xp-poisition:"+str(alien_0['x_poisiton']))

 """
#删除

""" 
alien_0 ={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0) 
"""

#喜欢语言类型

""" 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

print("Sarah's favorite language is "+favorite_languages['sarah'].title()+".")
 """
 
 #遍历字典
 
"""
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print("\nKey:"+key)
    print("Value:"+value)
 """
#遍历2
""" 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")
"""
 
 
 #key()
 
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }  
for name in favorite_languages.keys():
    print(name.title())
 """
#个值推荐
""" 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }  
friend = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friend:
        print(" Hi "+name.title()+",I see your favorite language is "+
              favorite_languages[name].title()+"!")
if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!") 
"""

""" favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    } 
for name in sorted(favorite_languages.keys()):
    print(name.title()+",thank you for taking the poll!") """
""" 
print("The folowing languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
"""
    
""" print("The folowing languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title()) """
    
    
    
    
    
    
    
    
#外星人

""" alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien) """
    
    
""" aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','pointss':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens:"+str(len(aliens))) """


"""aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','pointss':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:5]:
    print(alien)
print("...")"""

#pizza

""" pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print("You ordered a "+pizza['crust']+"-crust pizza "+"with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping) """


#语言


""" favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title()) """
        
        
#多用户


users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marle',
        'last':'curie',
        'location':'paris',
    },
}
for username,user_info in users.items():
    print("\nUsername:"+username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print("\tFull name:"+full_name.title())
    print("\tLocation:"+location.title())