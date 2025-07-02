# 1
# list = []
# n = int(input("n: "))

# for num in range(1, n + 1):
#     if num % 2 == 1:
#         list.append(num)

# 2
# unique_words = []

# while True:
#     word = input("word: ").lower()
#     if word == "exit":
#         break
#     if word not in unique_words:
#         unique_words.append(word)
# print(unique_words)

# 3
# import math
# number = int(input("number: "))

# prime_numbers = []

# for num in range(2, number + 1):
#     is_prime = True
#     # for n2 in range(2, num//2):
#     for n2 in range(2, int(math.sqrt(num))+ 1):
#         if num % n2 == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_numbers.append(num)
        
# print(prime_numbers)

# 4
population = []

# while True:
#     choice = input('odam qoshasizmi? ')
#     if choice == 'yoq':
#         break
while input("do u wanna add someone? ").startswith("y"):
    
    full_name = input("enter ur full name: ")
    age = int(input("enter ur age: "))
    address = input("enter ur address: ")
    phone = input("enter ur phone num: ")
    citizen = (full_name, age, address, phone)
    population.append(citizen)
else:
    choice = input("do u wanna see population list? ")
    if choice == "yes":
        for citizen in population:
            print(citizen)
    else:
        print("come back again")
        
# print(population)
    
    

