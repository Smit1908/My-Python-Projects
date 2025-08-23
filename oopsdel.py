# class student:  # del key word  
#     def __init__(self, name):
#         self.name = name

# s1 = student("smit")
# print(s1.name)
# del s1.name
# print(s1.name)


###########  public attribute

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


acc1 = account("12345", "abcd")

print(acc1.acc_no)
print(acc1.acc_pass) 

############ private attribute

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = account("12345", "abcd")

print(acc1.acc_no)
print(acc1.reset_pass()) 