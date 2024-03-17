"""
用户：
创建一个名为User的类，
其中包含属性first_name和last_name，
还有用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，
它打印用户信息摘要；
再定义一个名为greet_user()的方法，
它向用户发出个性化的问候。
创建多个表示不同用户的实例，
并对每个实例都调用上述两个方法。
"""
    
"""
分析：类-User(),__init__(self,first_name,last_name,sex,age)
     方法-describle_user(self),greet_user(self)
     describle_user(self):用户信息摘要
     greet_user(self):个性化问候，
     实例>=2
"""

class User():
    def __init__(self,first_name,last_name,sex,age):
        self.name = first_name +" "+last_name #python妙不可言的点
        self.sex = sex
        self.age = age
    def describle_user(self):
        print("user's name is "+self.name+"!")
        print("user's sex is "+self.sex+"!")
        print("user's age is "+str(self.age)+"!")
    def greet_user(self):
        print("Welcome!"+self.name+"!")
user_01 = User('liu','li','female',16)
user_01.describle_user()
user_01.greet_user()

user_02 = User('wang','er','male',19)
user_02.describle_user()
user_02.greet_user()