# 1
# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))

# print(a + b)
# print(a - b)
# print(a / b)
# print(a * b)
# 2.

# ur_name = input("insert ur name: ")
# ur_letter = input("insert a letter: ")



# if ur_name.isalpha() and len(ur_name) >= 2 and ur_letter.isalpha() and len(ur_letter) == 1:
#         counter = ur_name.count(ur_letter)
#         print(counter)
# else:
#     print ("come back again")

# 3.
# grades = [45, 78, 90, 65, 88, 55, 92, 70]
# index = 0
# new = []
# summa = 0

# for index in grades:
#     if index >= 70:
#         new.append(index)
#         index += 1
# print(new)

# for index in grades:
#     summa += index
#     index += 1
# print(summa / 8)

# print(max(grades))
# print(min(grades))




4.
text = input("write sth: ")
words = text.split()
count = []

for word in words:
    if word not in count:
        word_count = words.count(word)
        print(f"{word}- {word_count}")
        count.append(word)
    
# 5.Masala. 


# numbers = [8, 78, 90, 16, 88, 55, 1024, 70]
# inp = int(input("input a num: "))
# power = 0

# for num in numbers:
#     power = 0
#     result = 1
#     while result < num:
#         power += 1
#         result = inp ** power
#     if result == num:
#         print(f"{num} -> {inp}** {power}")

