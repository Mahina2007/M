"""
Foydalanuvchini shaxsiy ma'lutlarini saqlash uchun programma yasash kerak. Qanday faylda sqlash kerakligini ham
foydalanuvchi tanlaydi.

Menu:
    1: Save personal data: name, email, file_type(csv, json, txt)
    2: Read personal data: email
    3: Delete personal data: email
    4: Exit

Hohlasangiz har bitta foydanuvchini malumoti uchun alohida fayl ochishingiz mumkin.
Yoki barcha foydalanuvchilar uchun 3 ta turgani csv, txt, json turdagi fayl ochib
shuni ichiga saqlab ketsangiz ham bo'ladi.

Barcha malumotlar bitta users nomli papkani ichida bo'lishi kerak. Papka mavjud yoki mavjud
emasligini tekshirib olish va yo'q bo'lsa yaratib qo'ying.
"""

def main():
    print("""
    Menu:
    1. save personal data: name, email, file_type(txt, json, csv)
    2. read personal data: email
    3: Delete personal data: email
    4: Exit
    """)

    choice = input("Enter you choice: ")
    if choice == "1":
        save_data()
    elif choice == "2":
        read_data()
    elif choice == "3":
        delete_data()
    elif choice == "4":
        print("exit")
    else:
        print("invalid choice")
    return main()

if __name__ = __main__" :
    main()
