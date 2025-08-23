my_set = {1,2,3}
print(my_set)
print(type(my_set)) 


# charaterstics of set
#1. unique values/item
#2. unordered - no indexing
#3. mutable - add/remove elements
#4. immuttable elements - replace/modify existing elements

# create set using set constructor

my_set2 = set([4,5,6])
print(my_set2)

# set operations
# ADDDING ELEMENTSz 

num = {1,2,3,4}
num.add(5)
print(num)

# remove method  # error show thay chhe

fruits = {"apple", "mango", "banana"}
fruits.remove("apple")
print(fruits)

# discard method # error show nahi hota

fruits = {"apple", "mango", "banana"}
fruits.discard("mango")
print(fruits)

# set method

# union 

set_a = {1,2,3}
set_b = {3,4,5}
union_set = set_a.union(set_b)  # union_set = set_a | set_b
print(union_set)

# intersection

set1 = {1,2,3,4}
set2 = {3,4,5}
intersection_set = set1.intersection(set2) # intersection_set = set1 & set2
print(intersection_set) 

# difference 

set1 = {1,2,3,4}
set2 = {3,4,5}
diff_set = set1.difference(set2) # diff_set = set1 - set2
print(diff_set)

# symmetric

set1 = {1,2,3,4}
set2 = {3,4,5,6}
sym_set = set1.symmetric_difference(set2) #sym_set = set1 ^ set2
print(sym_set)

# set iteration # for loop

numbers = {1,2,3,4,5}
for i in numbers :
    print(i)

# while loop - does not support

# set compreshesion

squares = {x**2 for x in range(1,6)}
print(squares)

