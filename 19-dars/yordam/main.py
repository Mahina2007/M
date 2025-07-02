
"""
Ushbu muommoga yechim topish kerak.

Bir kompaniya egasi ishga kech qolgan ishchilarni
har bir daqiqasi uchun 1000 so'mdan jarima bilan
jazolaydi. Hozirda u bu ishlardi qog'ozda olib
bormoqda. Siz unda yordam berishingiz kerak.
Kichik bir dastur yaratin, unda quyidagi
imkoniyatlar bor bo'lsin, ishni qo'shish, o'chirish,
har bir ishchi uchun login unda keyin esa ishni boshlash
va o'zining barcha jarimalar miqdorini ko'rish
qaysi kuni necha daqiqa kech qolgani bilan birga.
"""

from functions import  add_worker
from functions import calculate
from functions import clear_all
from functions import calculate_all


def main():
    print("""
    Menu:
    1. Ishchi qo'shish
    2. hisoblash (ismini)
    3. hammani hisoblash
    4: Tozalash
    """)

    choice = input("Enter you choice: ")
    if choice == "1":
        add_worker()
    elif choice == "2":
        calculate()
    elif choice == "3":
        calculate_all()
    elif choice == "4":
        clear_all()
    else:
        print("invalid choice")

    return main()

if __name__ == '__main__':
    main()