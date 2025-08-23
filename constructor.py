# class student:
     
#      #default constructors
#      def __init__(self):
#           pass

#      #parameterized construtors
#      def __init__(self, name, marks):
#           self.name = name
#           self.marks = marks
#           print("adding new student in Database..")


# s1 =  student("smit", 93) 
# print(s1.name, s1.marks)  

# s2 = student("harsh", 88)
# print(s2.name, s2.marks)

###############

# class student:
     
#      collage_name = "ABC Collage"
#      name = "anonymous" #class attr

#      def __init__(self, name, marks):
#           self.name = name #obj attr > class attr
#           self.marks = marks
#           print("adding new student in Database..")

# s1 = student("smit", 97)
# print(s1.name)

###################

# class student:
     
#      collage_name = "ABC Collage"
     

#      def __init__(self, name, marks):
#           self.name = name 
#           self.marks = marks
          
#      def welcome(self):
#           print("welocme student", self.name)

#      def get_marks(self):
#           return self.marks

# s1 = student("smit", 97)
# s1.welcome()
# print(s1.get_marks())

##########  practice 1 #########

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
         

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = student("tony stark", [99, 98, 97])
# s1.get_avg()

# s1.name = "ironman"
# s1.get_avg()

############# practice 2 ##############

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
         
    @staticmethod
    def hello():
       print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = student("tony stark", [99, 98, 97])
s1.get_avg()
s1.hello()

s1.name = "ironman"
s1.get_avg()
