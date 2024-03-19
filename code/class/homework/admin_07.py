"""
    管理员：管理员是一种特殊的用户。
    编写一个名为Admin的类，
    让它继承你为完成练习9-3或练习9-5而编写的User类。
    添加一个名为privileges的属性，
    用于存储一个由字符串
    （如"can add post"、"can delete post"、
    "can ban user"等）组成的列表。
    编写一个名为show_privileges()的方法，
    它显示管理员的权限。
    创建一个Admin实例，
    并调用这个方法。
"""
"""
    分析：类新增Admin,包含一个方法show_privis加一个属性priviles
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
        
class Admin(User):
    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        for privileges in self.privileges:
            print("This admin "+privileges)
user_01 = Admin('liu','li','female',16)
user_01.describle_user()
user_01.show_privileges()
"""
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
"""