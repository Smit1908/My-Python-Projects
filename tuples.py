tup = (2, 1, 3, 1)
print(tup[0])

# none tuple

tup = (1)
print(tup)
print(type(tup))

# siles 

tup = (1, 2, 3, 4)
print(tup[1:3])

# tuple inex 

tup = (1, 2, 3, 4)
print(tup.index(2))

# tuple count

tup = (1,2,4,2,4)
print(tup.count(4))

# practice
movies = []

mov1 = input("enter first movie: ")
mov2 = input("enter second movie: ")
mov3 = input("enter third movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

# print(movies)

# #or

movies = []
movies.append(input("enter 1st movies: "))
movies.append(input("enter 2nd movies: "))
movies.append(input("enter 3re movies: "))

# print(movies)

# prac 2 

list1 = [1, 2, 1, ]
list2 = [ 1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT pallindrome")

#  prac 

grade = ("C" , "A", "A", "B", "C")
print(grade.count("A"))

 # PRAC 

grade = ["C" , "A", "A", "B", "C"]
grade.sort()
print(grade)