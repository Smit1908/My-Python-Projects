######## Function in Python ##############

def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)

calc_sum(8, 9)

calc_sum(12, 17)

# # second type # function defination

def calc_sum(a, b): #parameters
    return a+b

sum = calc_sum(1,2) # FUNCTION CALL; ARGUMENT
print(sum)


# #example

def print_hello():
    print("hello")

output = print_hello()
print(output)

## average of 3 number 

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(98,97,95)
  
# print function built - in - function

print("smit", end = " ") # separate = ""
print("patel") #end = "\n"


#multi 

def cal_prod(a= 5, b = 1 ):
    print(a*b)
    return a * b

cal_prod() 

# practies

cities = ["delhi", "surat", "pune", "mumbai", "goa"]
heroes = ["thor", "captain america", "iron man", "hulk"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

## 2

heroes = ["thor", "captain america", "iron man", "hulk"]


def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end = " ")

print_list(heroes)

### 3

n =5 

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6) 

# 4

def converter(usd_val):
    inr_val = usd_val * 85.87
    print(usd_val, "USD =", inr_val, "INR")

converter(2)


######## Recursion Func  tion #######

def show(n):
    if (n == 0):
          return
    print(n)
    show(n-1) 
    print("END")

show(5)

# 2 

def fact(n):
    if (n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(4)) 

# practice

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(5)
print(sum)

# practice 2

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", 'banana', "charry", "avacado"]

print_list(fruits)