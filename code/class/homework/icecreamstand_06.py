"""
冰淇淋小店：
冰淇淋小店是一种特殊的餐馆。
编写一个名为IceCreamStand的类，
让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。
这两个版本的Restaurant类都可以，
挑选你更喜欢的那个即可。
添加一个名为flavors的属性，
用于存储一个由各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。
创建一个IceCreamStand实例，
并调用这个方法。
"""


class Resaurant():
    def  __init__(self,resaurant_name,cuisine_type):
      self.name = resaurant_name
      self.type1 = cuisine_type
      self.number_served = 0
    def describle_resaurant(self):
        print("Rsataurant's name is "+self.name+"!")
        print("Restaurant's type is "+self.type1+"!")
    def open_restaurant(self):
        print("Restaurant is opening!")
    def number_served_print(self):
        """打印人数"""
        print("the number of customers now is "+str(self.number_served)+".")
    def set_number_served(self,num):
        """就餐人数修改"""
        self.number_served = num
        #print("the number of cutomers are: "+str(self.number_served)+".")
    def increment_number_served(self,num_all):
        """统计总的就餐人数"""
        if num_all>=0:
            self.number_served+=num_all
        else:
            print("total is not changed")
        #print("Today the number of customers total are:"+str(self.number_served)+".")

"""
class Flavors():
    def __init__(self,flavors):
        self.flavors = flavors
    def describle_flaver(self):
        print("The flaver is "+self.flavors+"!")
"""
class IceCreanStand(Resaurant):
    def __init__(self, resaurant_name, cuisine_type):
        super().__init__(resaurant_name, cuisine_type)
        self.flavors = ['oreo','apple','banana']
        # self.flavors = Flavors()
    def describle_flavers(self):
        for flaver in self.flavors:
            print("The flaver is "+flaver.title()+"!")

my_go = IceCreanStand('KFC','quick')
my_go.describle_flavers()

"""
my_go = Resaurant('KFC','quick')
print("My favourite restaurant is :"+my_go.name+"!")
print("My favorite restaurant's type is:"+my_go.type1+"!")
my_go.describle_resaurant()
my_go.open_restaurant()
my_go.number_served = 10
my_go.number_served_print()
my_go.set_number_served(23)
my_go.number_served_print()
my_go.increment_number_served(100)
my_go.number_served_print()"""
