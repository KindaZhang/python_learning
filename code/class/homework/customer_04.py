"""
就餐人数：
在为完成练习9-1而编写的程序中，
添加一个名为number_served的属性，
并将其默认值设置为0。
根据这个类创建一个名为restaurant的实例；
打印有多少人在这家餐馆就餐过，
然后修改这个值并再次打印它。
添加一个名为set_number_served()的方法，
它让你能够设置就餐人数。
调用这个方法并向它传递一个值，
然后再次打印这个值。
添加一个名为increment_number_served()的方法，
它让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：
你认为这家餐馆每天可能接待的就餐人数。
"""
"""
分析：属性增加-number_served ，默认值为0
      方法增加-set_number_served(self,num),num为就餐人数
      方法增加-increment_number_served(self,num_all)
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
my_go.number_served_print()