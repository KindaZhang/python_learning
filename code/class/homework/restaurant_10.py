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
