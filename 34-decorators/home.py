"""
Log decorator yozish kerak, uning vazifa funksiya qanday parametrlar bilan
ishlatilgani va natijasi nima bo'lganini faylga yozib ketsin.
"""
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(file = "info.txt", mode="a") as file:
            file.write(f"parameters : {args}, {kwargs} result : {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(1, 2))