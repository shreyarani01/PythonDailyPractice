#customer details
class customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intro(self):
        print("I am", self.name,"and I am",self.age,"years old")

c1 = customer("Neha", 21)
c2 = customer("Ankit", 22)
c3 = customer("Jack", 45)

L = [c1,c2,c3]

for i in L:
    i.intro()