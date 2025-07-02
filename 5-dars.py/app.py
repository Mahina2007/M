name = input("what's ur name: ")
age = input("how old r u: ")

if name.isalpha():
   if age.isnumeric() and 0 < int(age) < 200:
      print(f"{name} was born in {2025 - int(age)}")    
   else:
      print("invalid age")
else:
   print("invalid name, only letters should be")
   
# name = input("what's ur name: ")
# age = input("how old r u: ")

# if name.isalpha():
#     if age.isnumeric():
#         age = int(age)  # convert once
#         if 0 < age < 200:
#             print(f"{name} was born in {2025 - age}")    
#         else:
#             print("invalid age")
#     else:
#         print("invalid age")
# else:
#     print("invalid name, only letters should be")

text = "ozbeKisTon mening Vatanim"
text = text.replace('asas', '--')


print(text)

"""
title() -> har bitta so'zni boshini katta qilish
upper() -> har bir harfni katta qilish
lower() -> hammasini kichik qilish
capitalize() -> birinchisini katta qolgan hamasini kichik 

count('nimadir') -> berilgan belgilarni nechtaligini sanaydi
endswith('nimadir) -> oxiri nima bilan tugaganini tekshirish
startwith('nimadir) -> boshi nima bilan boshlanishini tekshirish

find('nimadir') -> boshlanish indexini topadi topilmasa -1
index('nimadir') -> boshlanish indexini topadi topilmasa xato

strip() -> boshi va oxiridagi bo'sh joylarni kesib beradi
lstrip() -> faqat chap taradini bo'sh joylarni kesib beradi
rstrip() -> faqat o'ng tarafini bo'sh joylarni kesib beradi

split('nimadir') -> berilgan belgi bo'yicha kesish
join() -> berilgan beli bo'yicha birlashtirish
replace('eski', 'yangi') -> berilgan narsalarni alishtirib beradi



"""


