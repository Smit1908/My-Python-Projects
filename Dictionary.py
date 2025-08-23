info = {
    "name" : "smit",
    "subject" : ["python", "java", "c++"],
    "topics" : ("dict", "set"),
    "age" : 23,
    "is_adult" : True,
    "learning" : "coding"
}
print(type(info))
print(info)

# dfsdg

dict = {
    "name" : "smit",
    "subject" : ["python", "java", "c++"],
    "topics" : ("dict", "set"),
    "age" : 23,
    "is_adult" : True,
    "learning" : "coding"
}
print(info["name"])
print(info["topics"])
print(info["age"])
print(info["is_adult"])
print(info["learning"]) 

#CHANGE A VARIABLE


dict = {
    "name" : "smit",
    "subject" : ["python", "java", "c++"],
    "topics" : ("dict", "set"),
    "age" : 23,
    "is_adult" : True,
    "learning" : "coding"
}
print(info["name"])
print(info["topics"])
print(info["age"])
print(info["is_adult"])
print(info["learning"]) 

info["name"] = "monty"
info["surname"] = "patel"
print(info)

# nested dict 

student = {
    "name" : "smitm",
    "subject" : {
        "python" : 97,
        "c++" : 98,
        "java" : 89
     }
}
print(student["subject"]["java"])
print(student) 

# keys


student = {
    "name" : "smitm",
    "subject" : {
        "python" : 97,
        "c++" : 98,
        "java" : 89
     }
}

print(student.keys()) # print(list(student.keys())) list count karva and print(len(list(student.keys())))

# key values


student = {
    "name" : "smitm",
    "subject" : {
        "python" : 97,
        "c++" : 98,
        "java" : 89
     } 
}

print(student.values()) 

# return all key and valus # print (paris[0]) particular show karva


student = {
    "name" : "smitm",
    "subject" : {
        "python" : 97,
        "c++" : 98,
        "java" : 89
     } 
}

print(student.items()) 

# return the key accoring to valuse

student = {
    "name" : "smitm",
    "subject" : {
        "python" : 97,
        "c++" : 98,
        "java" : 89
     } 
}

print(student.get("name"))

# update methods

student = {
    "name" : "smitm",
    "subject" : {
        "python" : 97,
        "c++" : 98,
        "java" : 89
     } 
}

new_student = {"city" : "surat"}
student.update(new_student)
print(student)