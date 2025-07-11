def add_nums():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    num3 = str(num1 + num2)
    text = f"{num1},{num2},{num3}\n"
    with open(file="results.txt", mode="a") as file:
        file.write(text)
    return file


def subtract():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    num3 = str(num1 - num2)
    with open(file="results.txt", mode="a") as file:
        file.write("\n" + num3)
    return


def multiply():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    num3 = str(num1 * num2)
    text = f"{num1},{num2},{num3}\n"
    with open(file="results.txt", mode="a") as file:
        file.write(text)
    return


def divide():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    num3 = str(num1 / num2)
    with open(file="results.txt", mode="a") as file:
        file.write("\n" + num3)
    return


def show_all():
    with open(file="results.txt", mode="r") as file:
        print(file.readlines())