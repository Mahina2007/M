# import random

# com_guess = random.randint(a:1, b:100)
# attempts = 5

# while attempts > 0:
#     attempts -= 1
#     if attempts == 0:
#      break
 
# print("u lost")


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# if b > a:
#     for num in range(a, b + 1):
#         print(num)
#     print(f"Total nums between {a} and {b}: {b - a + 1}")
# else:
#     print("B should be greater than a")
    
    
n = int(input("Enter n: "))
m = int(input("Enter m: "))
if n > m:
    for num in range(m, n + 1):
        result = 0
        text = ""
        for digit in str(num):
            text += f"{digit},"
            result += int(digit)

        text = text.split(',')[:-1]
        text = " + ".join(text)
        print(f"{num} => {text} = {result}")

else:
    print("N should be greater than 10")


