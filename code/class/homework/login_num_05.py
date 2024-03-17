"""
尝试登录次数：
在为完成练习9-3而编写的User类中，
添加一个名为login_attempts的属性。
编写一个名为increment_login_attempts()的方法，
它将属性login_attempts的值加1。
再编写一个名为reset_login_attempts()的方法，
它将属性login_attempts的值重置为0。
根据User类创建一个实例，
再调用方法increment_login_attempts()多次。
打印属性login_attempts的值，
确认它被正确地递增；
然后，调用方法reset_login_attempts()，
并再次打印属性login_attempts的值，
确认它被重置为0。
"""
"""
分析：属性增加-login_attempets
      方法增加-increment_login_attempts(self)
      方法增加-reset_login_attempts(self)
"""
class User():
    def __init__(self,first_name,last_name,sex,age):
        self.name = first_name +" "+last_name #python妙不可言的点
        self.sex = sex
        self.age = age
        self.login_attempts = 0
    def describle_user(self):
        print("user's name is "+self.name+"!")
        print("user's sex is "+self.sex+"!")
        print("user's age is "+str(self.age)+"!")
    def greet_user(self):
        print("Welcome!"+self.name+"!")
    def increment_login_attempts(self):
        """登陆次数加1"""
        self.login_attempts+=1
    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
    def num_total(self):
        """打印登录次数"""
        print("The numbers of login are:"+str(self.login_attempts)+".")
user_01 = User('liu','li','female',16)
user_01.describle_user()
user_01.greet_user()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.increment_login_attempts()
user_01.num_total()
user_01.reset_login_attempts()
user_01.num_total()