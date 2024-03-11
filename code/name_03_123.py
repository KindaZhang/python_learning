#3-1的课后练习题
"""names = ['zhang','wang','li','gao','sun']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])"""
#3-2的课后练习题
"""names = ['zhang','wang','li','gao','sun']
message = "Hello "+names[0]
message1 = "Hello "+names[1]
message2 = "Hello "+names[2]
message3 = "Hello "+names[3]
message4 = "Hello "+names[4]
print(message)
print(message1)
print(message2)
print(message3)
print(message4)"""

#这是3-3的课后练习题
"""run = ['motorcycle','bicycle','car','boat']
message = "I would like to own a Hoonda "+run[0]
message1 = "I would like to own a Hoonda "+run[1]
message2 = "I would like to own a Hoonda "+run[2]
message3 = "I would like to own a Hoonda "+run[3]

print(message)
print(message1)
print(message2)
print(message3)"""

#这是3-4的课后练习题
"""person_name = ['li','sun','zhang']
print(person_name)"""

#这是3-5的课后练习题
"""person_name = ['li','sun','zhang']
print(person_name)
person_no = person_name.pop()
print(person_no)
person_name.insert(2,'gao')
print(person_name)"""

#这是3-6的课后练习题
"""person_name = ['li','sun','zhang']
print(person_name)
person_no = person_name.pop()
print(person_no)
person_name.insert(2,'gao')
print(person_name)
print("find a new big table")
person_name.insert(0,'wang')
person_name.insert(2,'liu')
person_name.append('zhao')
print(person_name)"""

#3-7
"""person_name = ['li','sun','zhang']
print(person_name)
person_no = person_name.pop()
print(person_no)
person_name.insert(2,'gao')
print(person_name)
print("find a new big table")
person_name.insert(0,'wang')
person_name.insert(2,'liu')
person_name.append('zhao')
print(person_name)
print('only two person can be invent')
name_1=person_name.pop()
print(person_name)
print("sorry,can not invent you "+name_1)
name_2=person_name.pop()
print(person_name)
print("sorry,can not invent you "+name_2)
name_3=person_name.pop()
print(person_name)
print("sorry,can not invent you "+name_3)
name_4=person_name.pop()
print("sorry,can not invent you "+name_4)
print(person_name)
print(person_name[0]+",you are invented")
print(person_name[1]+",you are invented")
del person_name[0]
del person_name[0]
#person_name.del("li")
print(person_name)"""


#3-8
"""place = ['beijing','shanghai','taiyuan','fujian','qingdao']
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)"""

#3-9选的3-5

"""person_name = ['li','sun','zhang']
print(person_name)
person_no = person_name.pop()
print(person_no)
person_name.insert(2,'gao')
print(person_name)
print(len(person_name))
"""
#3-10
place = ['beijing','shanghai','taiyuan','fujian','qingdao']
print(place)
print("删除的两种展示：")
del place[4]
print(place)
place1=place.pop()
print(place)
print(place1)
print("增加的展示：")
place.append('qingdao')
print(place)
place.insert(3,'fujian')
print(place)
print("一种移除展示：")
place.remove('shanghai')
print(place)
print("翻转：")
place.reverse()
print(place)
print("翻转再一次：")
place.reverse()
print(place)
print("临时排序正反两次：")
print(sorted(place))
print(sorted(place,reverse=True))
print("排序正反两次：")
place.sort()
print(place)
place.sort(reverse=True)
print(place)
print(len(place))