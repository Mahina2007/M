# # 1
# link = input("type a link: ")

# if link.startswith("http://") or link.startswith("https://"):
#     print("It's a link")
# else:
#     print("it's not a link")
    
# # 2
# full_name = input("enter your full name: ")
# phone_num = input("enter your phone number: ")


# if len(full_name.split()) >= 2 and phone_num.startswith("+998") and len(phone_num) == 13 and phone_num[1:].isdigit():
#     print("Xush kelibsiz!")
# else:
#     print("Xato")

# 3
sentence = input("write a sentence: ")
word = input("write a word: ")

print(sentence.replace(word, " "))