"""
餐馆：
创建一个名为Restaurant的类，
其方法__init__()设置两个属性：restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant的实例，
分别打印其两个属性，
再调用前述两个方法。
"""
#分析：类-Restaurant(self,restaurant_name,cuisine_type),方法-describle)restaurant(self),oprn_restaurant(self)
#describe_restaurant(self)打印restaurant_name+cuisine_type 
#open_restaurant(self)打印正在营业
class Resaurant():
    def  __init__(self,resaurant_name,cuisine_type):
      self.name = resaurant_name
      self.type1 = cuisine_type
    def describle_resaurant(self):
        print("Rsataurant's name is "+self.name+"!")
        print("Restaurant's type is "+self.type1+"!")
    def open_restaurant(self):
        print("Restaurant is opening!")
my_go = Resaurant('KFC','quick')
print("My favourite restaurant is :"+my_go.name+"!")
print("My favorite restaurant's type is:"+my_go.type1+"!")
my_go.describle_resaurant()
my_go.open_restaurant()

###错误Resaurant(self,resaurant_name,cuisine_type)，创建一个空白的类，不需要加参数