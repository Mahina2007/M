#task 1
import csv
# with open(file= "users,csv", mode= "r+", encoding= "UTF-8", newline= "" ) as file:
#     counter = 1
#     while counter <=3:
#         name = input("name: ")
#         age = input("age: ")
#         gender = input("gender: ")
#         counter += 1
#         headers = ['name', 'age', 'gender']
#     writer = csv.writerow(headers)


users = [
    ['name', 'age', 'gender'],
    ['ali', 12, 'male'],
    ['vali', 123, 'male'],
    ['dona', 11, 'female']
]

headers = ['name', 'age', 'gender']

with open(file="users.csv", mode="w+", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
#     writer.writerows(users)


# with open(file="users.csv", mode="r+", encoding="UTF-8", newline="") as file:
#     # reader = csv.reader(file)
#     # print(list(reader))
#     # for line in reader:
#     #     print(line)
# 
#     dict_reader = csv.DictReader(file)
#     print(list(dict_reader))
#     # for line in dict_reader:
#     #     print(dict(line))

#task 1
# import csv

# counter = 0
# users = list()
# while counter < 3:
#     name = input("Name: ")
#     age = int(input("Age: "))
#     gender = input("Gender: ")
#     user = [name, age, gender]
#     users.append(user)

#     counter += 1
# else:
#     users.insert(0, ['name', 'age', 'gender'])

# with open(file="users.csv", mode="w+", encoding="UTF-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)

