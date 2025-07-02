"""
ValueError -> intni o'rniga str kiritib qo'ysa

"""
# try:
#     age = int(input("age: "))
#     print(age)
# except ValueError:
#     print("Wrong value, please enter int only")
# else:
#     print("Else is worked")
# # finally:
# #     print("finally")

# try:
#     pass
# except ValueError:
#     pass
# except ZeroDivisionError: -> 0ga bo'lish mumkinmasligi
#     pass
# else:
#     pass
# finally:
#     pass
#
#
# try:
#     age = int(input("Age: "))
#     print(age)
# except Exception as exc: -> bilmagan xatoligimizni shunaqa qilib ketamiz
#     print("what")
#     print(exc)
#
# try:
#     num1 = int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("You can not divide by zero")
# except ValueError:
#     print("Integer only")

# NameError
# name = "salom"
# print(age)

# RecursionError
# def hello():
#     print("Hello")
#     return hello()
#
#
# hello()

# KeyboardInterrupt
# while True:
#     name = input("Name: ")

# BaseException

# Exception

"""
4 types of errors:
1. Compile time errors (SyntaxError, IndentationError, TabError)
2. Runtime error (built-in exceptions)
3. Logical errors (bugs)
4. System errors (related to computer)

All exception types
ValueError
SyntaxError
TypeError
AttributeError
IndexError
IndentationError -> 
KeyboardInterrupt
KeyError
FileNotFoundError
ImportError
RecursionError
ZeroDivisionError
NameError
OverflowError
"""
"""
Foydalanuvchidan ismini va  yoshini input qilib olish va users.csvga yozish. Xatoliklarni oldini olish
"""
import csv
try:
    name = input("enter name: ")
    age = int(input("age: "))

    data = [name, age]
    with open(file = "users.csv", mode = "a+", encoding = "UTF-8", newline ="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

except ValueError:
    print("age can be only num")
except Exception as exc:
    print("something went wrong")
    print(exc)


