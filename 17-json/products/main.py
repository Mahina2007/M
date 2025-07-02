import functions


def main():
    print("""
          Menu:
    1. Ro'yxatni ko'rish
    2. Yangi mahsulot qo'shish | nomi va qancha olish kerakligini kiritiadi
    3. O'chirib tashlash | mahsulotni nomini kiritadi va uni fayldan o'chirib tashlaysiz
    4. Butun faylni tozalash
    5. Chiqish
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        functions.view_list()
    elif choice == "2":
        functions.add_new()
    elif choice == "3":
        functions.delete_product()
    elif choice == "4":
        functions.clear_all()
    elif choice == "5":
        print("exit")
    else:
        print("Invalid choice")
    return main()


if __name__ == '__main__':
    main()