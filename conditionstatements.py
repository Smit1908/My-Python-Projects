age = 24

if (age >= 18 ):
    print("can vote & apply for license")
    print("can drive")


# # elif

light = "yellow"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

print("end of code")

# else
 
light = "pink"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken ")

print("end of code")

 # if else 

age = 24

if(age >= 18):
    print("can vote")
else:
    print("CANNOT vote") 


# marks system

marks = int(input("enter the student marks :"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the students ->", grade)

 # nesting

age = 95

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# practice

num = int(input("enter number : ")) 
 
if (num % 2  == 0):
    print("EVEN")
else:
    print("ODD")

# PRACTICE 2 

a = int(input("enter first number : ")) 
b = int(input("enter second number : ")) 
c = int(input("enter third number : ")) 
d = int(input("enter fourth number: "))


if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest", c)
else:
    print("fourth number is largest", d)

# practice 3

x = int(input("enter number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a mulitple")