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

class Privileges():

    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        #self.privileges = ['can add post','can delete post','can ban user']
        for privileges in self.privileges:
            print("This admin "+privileges)
class Admin(User):
    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()