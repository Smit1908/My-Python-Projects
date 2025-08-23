# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")

#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return complex(newReal, newImg)

# num1 = complex(1,3)
# num1.showNumber()

# num2 = complex(4, 6)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

### practice

# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius **2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = circle(21)
# print(c1.area())
# print(c1.perimeter())

###########practice 2

# class employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class engineer(employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("engineer", "IT", "75000")


# engg1 = engineer("smit", 23)
# engg1.showDetails()

##### practice 3 

class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
    
ord1 = order("chips", 20)
ord2 = order("tea", 15)

print(ord1 > ord2)  
