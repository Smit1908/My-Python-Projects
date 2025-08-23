#arithmetic operators
a = 5
b = 2 

print(a + b)
print(a - b) 
print(a * b)
print(a /  b)
print(a % b) #remindrs
print(a ** b) #a^b  

#relational value 

a = 50
b = 20

print(a==b) #False
print(a !=b ) #True
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)
 
#assignment operators
num = 10
num = num + 10 #10+10=>20
num +=10 #same value

print("num :", num)
num = 10
num **= 5
print("num :", num)

#logical operators
a = 50
b = 30
print(not False)
print(not (a > b)) 
 
val1  = True 
val2 = False
print("and operators:", val1 and val2) 
print("or operators:", a == b or (a > b))  

# type conversion
  
a = 2
b = 4.25

sum = a + b # b  2.0 + 4.25
print(sum)

# type casting 

a = int("2")
b = 4.25
print(type(a))
print(a + b)