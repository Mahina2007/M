"""
Ushbu built in funksiyalardan foydalanmang, max, min, sum, avg
1. Foydalanuvchidan so'z va belgi so'rab, o'sha belgi so'zda nechta marta uchraganini aniqlang.
word = input("word: ")
sign = input("sign: ")
counter = 0
index = 0

while index < len(word):
    sign_count = word.count(sign)
    count += sign_count
    index += 1
print(count)

while 
2. Ism ichida raqamlar bor yoki yo'qligini tekshiring.
3. So'zdagi barcha unli harflarni olib tashlang.
4. Foydalanuvchidan ism kiritishni so'rang va stop yozmaguncha ro'yxatga qo'shing.
5. Foydalanuvchidan ikki son va amal (+, -, *, /) kiritishni so'rang va natijani chiqarish.
   Agar amalga stop kiritsa to'xtang.

"""
# 1
# word = input("word: ")
# sign = input("sign: ")
# counter = 0
# index = 0

# while index < len(word):
#     if word[index] == sign:
#         counter += 1
#     index += 1
# print(counter)

# 2
name = input("name: ")
index = 0
has_digit = False

while index < len(name):
    if name[index].isdigit():
        has_digit = True
        break
    index += 1
if has_digit:
    print("it has digit")
else:
    print("doesn't have any digits") 
    
# 3
word = input("word: ")
index = 0

while index < len(word):
    if word[index] in "AOUIEaouie":
        
    