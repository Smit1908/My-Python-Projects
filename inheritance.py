# class car:   ##inherit property
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started...")

    
#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Toyotacar(car):
#     def __init__(self, name):
#         self.name = name
    
# car1 = Toyotacar("fortuner")
# car2 = Toyotacar("polo")

# print(car1.name) 
# print(car1.start())
# print(car1.color)

#########

# class car:       
   
#     @staticmethod
#     def start():
#         print("car started...")

    
#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Toyotacar(car):
#     def __init__(self, brand):
#         self.brand = brand

# class fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type = type

# car1 = fortuner("diesel")
# car1.start()

#################

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welocme to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varA)
# print(c1.varB)

######################
 
# class car:       #super method
    
#     def __init__(self, type):
#         self.type = type
         
#     @staticmethod
#     def start():
#         print("car started...")

    
#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Toyotacar(car):
#     def __init__(self, name, type): 
#         super().__init__(type) 
#         self.name = name
#         super().start()

# car1 = Toyotacar("virtus", "eletric")
# print(car1.type)
  

#########


# class person:
#     name = "anonymouse"

#     def changeName(self, name):
#         self.name = name

# p1 = person()
# p1.changeName("smit patel")
# print(p1.name)
# print(person.name)


###########

# class person:
#     name = "anonymouse"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = person()
# p1.changeName("smit patel")
# print(p1.name)
# print(person.name)
 

############

# class student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.chem +self.phy + self.math) / 3) + "%"
    
#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage()
# print(stu1.percentage)

########### 2nd type

class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)