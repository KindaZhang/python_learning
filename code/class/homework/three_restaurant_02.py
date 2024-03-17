"""
三家餐馆：
根据你为完成练习9-1而编写的类创建三个实例，
并对每个实例调用方法describe_restaurant()。
"""
class Resaurant():
    def  __init__(self,resaurant_name,cuisine_type):
      self.name = resaurant_name
      self.type1 = cuisine_type
    def describle_resaurant(self):
        print("Rsataurant's name is "+self.name+"!")
        print("Restaurant's type is "+self.type1+"!")
    def open_restaurant(self):
        print("Restaurant is opening!")
resaurant_01 = Resaurant('KFC','quick')
resaurant_02 = Resaurant('McDonald','slow')
resaurant_03 = Resaurant('Starbucks','drink')
resaurant_01.describle_resaurant()
resaurant_02.describle_resaurant()
resaurant_03.describle_resaurant()