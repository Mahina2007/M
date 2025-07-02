
def save_data_json():
    name = input("name: ")
    email = input("email: ")
    file_type = input("file type: ")

    users = {
        "name": name,
        "email" : email,
        "file_type": file_type
    }
    users = read_from_json(file="users.json")
    users.append(users)
    write_to_json(file="users.json", data=users)
    print("New data is saved")

def save_data_txt():
    with open(file = "users.txt", mode = "w") as file:
        print("data is saved")

def save_data_csv():
    with open(file= "users.csv", mode ="w", )




