from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        for side in range(1,randint(1,self.sides)):
            print("The number is:"+str(side)+".")
die_01 = Die(6)
die_01.roll_die()
die_01 = Die(10)
die_01.roll_die()
die_01 = Die(20)
die_01.roll_die()
