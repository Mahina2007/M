def create_file():
    name = input("Enter file name: ")
    with open(file=name, mode="x") as file:
        print("File is created")
    return name

import os
def delete_file():

    name = input("Enter file name: ")
    os.remove(name)
    print("File is deleted")
    return name

def check_file():
    name = input("Enter file name: ")
    os.path.exists(path={name})
    print("file is checked")
    
def write_into_file():
    name = input("enter file name: ")
    with open(file= name, mode= "w") as file:
        print("file is written")
        
def append_file():
    name = input("enter file name: ")
    with open(file= name, mode= "a") as file:
        print("file is appended")
    
def read_file():
    name = input("enter file name: ")
    with open(file = name, mode= "r") as file:
        print("file is read")
    
    
    

    

