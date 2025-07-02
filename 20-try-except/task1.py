# ism
# yosh
# users,csv
# try-except

import csv

path = f"data/{filename}.csv"
    with open(file=path, mode="a", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    try:
        user = input("name: ")
        age = int(input("age"))
        print(user, age)
    except ValueError:
        print("Wrong value, please enter integer only")
