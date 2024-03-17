class Dog(): #定义类，类名为Dog，python中指出首字母大写是类，与函数不一样，且没有参数是因为从空白创建这个类
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):#这里在类里面的函数称为 方法。这个方法是特殊的，当调用类时会自动调用这个方法，
        #开头与末尾有两个下划线是一种约定，目的是避免python默认方法与普通方法发生名称冲突
        #self必不可少，且必须位于最前方。这个调用时自动传入，不需要提供值。每个与类相关的方法都自动传递，就相当于指向实例本身
        """初始化属性name和age"""
        self.name = name#这是实例的属性（可以通过实例访问的变量成为属性）
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+ " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")
my_dog = Dog('willie',6)#__init__()没有显式包含return语句，但py自动返回一个实例储存在my_dog中。大写开头为类，小写开头是实例
your_dog = Dog('lucy',3)#多个实例
print("My dog's name is "+my_dog.name.title()+".")#访问属性
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()#调用方法
print("\nYour dog's name is "+my_dog.name.title()+".")#访问属性
print("Your dog is "+str(my_dog.age)+" years old.")
your_dog.sit()