"""
x -> create
w -> write
a -> eskini saqlab qo'shish yonidan
r -> o'qish terminalda


    
"""
# open(file= "mahina.txt", mode="x")

# file = open(file= "mahina.txt", mode= "w")
# file.write("\nnimadir")

# file = open(file= "mahina.txt", mode= "a")
# file.write("\nnimadir")

# file = open(file= "mahina.txt", mode= "r")
# print(file.read())
# print(file.readline())
# print(file.readlines())
# file = open(file= "mahina.txt", mode= "r+")
# file.close()



# 1-mashq
# file = open(file="names.txt", mode="a")
# counter = 1
# while counter <= 3:
#     name = input("Name: ")
#     file.write(f"{name}\n")
#     counter += 1
# file.close()

# 2-mashq
# with open(file = "fruits.1.txt", mode = "r") as file:
#     fruits1 = set()
# for fruit in file.readlines():
#     fruits1.add(fruit)
    
# with open(file = "fruits2.txt", mode = "r") as file:
#     fruits2 = set()
# for fruit in file.readlines():
#     fruits2.add(fruit)
# with open(file="fruits1.txt", mode="r") as f1, open(file="fruits1.txt", mode="r") as f2:
#     meva1 = set(f1.read().splitlines())
#     meva2 = set(f2.read().splitlines())
    
#     umumiy_mevalar = meva1.intersection(meva2)
    
#     with open(file="fruits3.txt", mode="w") as file:
#         for meva in umumiy_mevalar:
#             file.write(meva)



# with open(file= "fruits3.txt", mode = "w") as file:
#     fruits3 = fruits1.intersection(fruits2)
#     file.writelines(fruits3)
# from functions import create_file

# import os
"""
papka yaratish -> os.mkdir
papka o'chirish -> os.rmdir
papka tekshirish -> os.path.exists(path="klskd")

"""
# os.mkdir(path='../../17-json-file')
# os.rmdir(path='../../17-json-file')



# def main():
#     print("""
#     1. Create file
#     2. Delete file
#     3. Check file
#     4. Write to file
#     5. Append to file
#     6. Read file
#     """)

#     choice = input("Enter your choice: ")
#     if choice == "1":
#         create_file()
#     elif choice == "2":
#         pass
#     elif choice == "3":
#         pass
#     elif choice == "4":
#         pass
#     elif choice == "5":
#         pass
#     elif choice == "6":
#         pass
#     else:
#         print("Invalid choice")
#     return main()


# if __name__ == "__main__":
#     main()
import os
from functions import create_file
from functions import delete_file
from functions import check_file
from functions import write_into_file
from functions import append_file
from functions import read_file


def main():
    print("""
    1. Create file
    2. Delete file
    3. Check file
    4. Write to file
    5. Append to file
    6. Read file
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        create_file()
    elif choice == "2":
        delete_file()
    elif choice == "3":
        check_file()
    elif choice == "4":
        write_into_file()
    elif choice == "5":
        append_file()
    elif choice == "6":
        read_file()
    else:
        print("Invalid choice")
    return main()


if __name__ == "__main__":
    main()
