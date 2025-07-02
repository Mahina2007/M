"""
1. Sizda bir foydalanuvchi sotib olgan mahsulotlar ro'yxati bor,
   va hozirda bozorda bor mahsulotlar ham ro'yxati bor
   sizni vazifangiz foydalanuvchi sotib olmagan 3 ta boshqa mahsulotni unga ko'rsatadigan funksiya yozish
2. Sizda ikki kun ichida do'konga kirgan insonlarni ismlar ro'yxati ikkita ro'yxat ko'rinishida berilgan,
   ikkala kun ichida do'konga faqat bir martta kirga foydalanuvchilarni sonini toping
3. Bitta tuple yarating va uni teskariga o'girib bering
4. Bitta tuple yararing u sonlardan tashkil topgan bo'lsin. Juft va toq sonlarni alohida chiqaring
5. Ikkita do'stning qiziqishlari berilgan. Ikkala do'st ham qiziqadigan narsalarni topib bering
"""
# 1
# customer_product = {"apple", "banana", "grapes", "kiwi", "strawberry"}
# shopping_product = {"onion", "tomato", "potato", "strawberry"}

# print(shopping_product.difference(customer_product))

# 2
# day1 = {"mahina", "madina", "maftuna"}
# day2 = {"mahina", "madina", "zebo"}
# print(len(day1.symmetric_difference(day2)))

# 3
# tuple = (1, 2, 3, 4, 5)

# length = len(tuple)

# new_tuple = ()
    
# for num in range(length):
#     new_tuple += (tuple[length - num - 1],)
# print(new_tuple)

# 4
# tup = (1, 2, 3, 4, 5, 6,)

# even = ()
# odd = ()

# for num in tup:
#     if num % 2 == 0:
#         even += (num,)
#     else:
#         odd += (num,)
# print(f"even numbers: {even}")
# print(f"odd nums: {odd}")

# 5
# friend1 = {"art", "chemistry","football"}
# friend2 = {"language", "art", "football"}

# print(friend1.intersection(friend2))
    