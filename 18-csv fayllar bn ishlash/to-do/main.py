from function import show_all
from function import add_task

def main():
    print("""
    1. Hamma tasklarni ko'rish
    2. Yangi task qo'shish
    3. Taskni o'chirish
    4. Taskni bajarildi qilish
    5. Kunlik tekshiruv ()
    6. Tasklarni tozalash
    7. Chiqish
    """)

    choice = input("Enter you choice: ")
    if choice == "1":
        show_all()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        tick_task()
    elif choice == "5":
        daily_check()
    elif choice == "6":
        clear_all()
    elif choice == "7":
        print("Hayr")
        return
    else:
        print("Noto'g'ri tanlov")
    return main()


if __name__ == "__main__":
    main()
