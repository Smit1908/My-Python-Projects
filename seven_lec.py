# f = open("demo.txt", "r")
# data = f.read(5)
# print(data)
# print(type(data))
# f.close()


##### written method ######## 

# f = open("demo.txt", "w")

# f.write("I want to learn JavaScript tomorrow. 123")

# f.close()


##### written method "A" ########

# f = open("demo.txt", "a")

# f.write("\nThen i will move to ReactJs")

# f.close()

 #### written override mode r+ ####

# f = open("demo.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()


#### with open file code ####

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# with open("demo.txt", "w") as f:
#     f.write("new data")


####### create  a file ######### 

# f = open("sample.txt", "w")
# f.close 

####### removing a file ####

import os 

os.remove("sample.txt")