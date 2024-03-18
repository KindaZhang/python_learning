class Car():#这是父类的定义，它必须包含在当前文件中，且位于子类前
    """一次模拟骑车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" milese on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):#这是子类的定义，括号内指定父类的名称
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):#这个方法接受创建Car实例所需的信息
        """初始化父类的属性"""
        super().__init__(make, model, year)#super函数，是一个特殊函数。帮助父类和子类关联起来
        #上述代码就可以调用父类的同名方法可以让子类实例包含父类的所有属性，此时父类可以成为超类
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
