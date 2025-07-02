import json
name = input("name: ")
birth_date= input("birth date: ")
age = int(input("age: "))

data = {
    "name" : name,
    "age" : age,
    "birthday" : birth_date
    
}

with open(file= "users.json", mode = "w") as file:
    json.dump(data, file, indent=4)