# while loop

count = 1 
while count <= 5 :
    print("hello")
    count += 1

  
i =1 
while i <= 5 :
    print("world" , i)
    i +=1

# print number from 1to 5 

i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop Ended")

# practice

i = 1
while i <=100:
    print(i)
    i +=1

# 2 

i = 100
while i >= 1:
    print(i)
    i -= 1

# 3
# n = int(input("enter the value : "))
i = 1 
while i <= 10:
    print(3*i) # enter the valuve print(n*i)
    i += 1

# 4

nums = [1,4,9,16,25,36,49,64,81,100]
print(nums[0])
idx = 0
while idx < len(nums) :
    print(nums[idx]) 
    idx +=1

# 5 

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0 # initiliation
while i < len(nums):
    if(nums[i] == x):
      print("FOUND at idx", i)
    else:
        print("finding...")
    i +=1   


# breack loops

i = 1 

while i<=5 :
    print (i)
    if (i==3):
        break
    i += 1

print ("end of loop")

############


nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0 # initiliation
while i < len(nums):
    if(nums[i] == x):
      print("FOUND at idx", i)
      break
    else:
        print("finding...")
    i +=1   

print("end of loop")

# continue loop

i = 0 
while i <= 5:
    if(i==3):
        i +=1
        continue
    print(i)
    i += 1 

# odd number print 

i = 1 
while i <= 10:
    if(i%2 == 0):
        i +=1
        continue
    print(i)
    i += 1 

# even number 

i = 1
while i <= 10:
    if(i%2 !=0):
        i +=1
        continue
    print(i)
    i += 1 

# for loop

nums = [1,2,3,4,5]

for val in nums:
    print(val)

# 2nd example

veggies = ["potato", "brinjal", "ladyfinger","cucumber"]

for val in veggies:
    print(val)

# tupple

tup = (1,2,3,4,5,7,8,9,10)

for num in tup:
    print(num)

 # break code inloop

str = "smitking"

for char in str:
    if(char == 't'):
        print("t found")
        break
print(char)

print("END")


# practice 

i = [1,4,9,16,25,36,49,64,81,100]

for el in i:
    print(el)

# practice 2 # linear search

num = (1,4,9,16,25,36,49,64,81,100)
x = 64

idx = 0
for el in num:
    if(el == x):
        print("number found at idx", idx )
    idx += 1 

# range function

seq = range(10)

for i in seq:
    print(i)

#2nd type

for i in range(10): # range(stop)
    print(i)

for i in range(2,10): # range (start,stop)
    print(i)

for i in range(2,10,2): # range (start,stop,step)
    print(i)

# even print

for i in range(2,100,2):
    print(i)

# odd number

for i in range(1,100,2):
    print(i)

# practice

for i in range(1,101):
    print(i)

# 2 

for i in range(100,0,-1):
    print (i)

# 3 

n = int(input("enter number :"))

for i in range (1,11):
    print(n*i)

#pass sta

for i in range(5):
    pass

print("some useful work")

# 2ns\

for i in range(5):
    pass
if i > 5:
    pass

print("some useful work")

# practice que

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    
print("total sum =", sum )

# 2nd

n = 5
fact = 1
i = 1
while i<=n:
    fact*= i 
    i += 1

print("factorial =", fact)

# for   

n = 5
fact = 1 

for i in range(1, n+1):
    fact *= i 

print("factorial = ", fact)

