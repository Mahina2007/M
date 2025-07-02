# Ushbu dasturni yaratish kerak.
#
# Harajatlarimni saqlab borishim uchun
# dastur kerak. Unda hohlagan paytim
# qancha pulni nimaga sarflagimni qo'shib bora
# olashim va o'chira olishim. Ko'ra olishim kerak.
# Undan tashqari bugungi harajatlarni ko'rish
# imkoniyati ham bo'lishi kerak.
from views import add_spendings

def main():
    print("""
    1. Add spendings 
    2. Delete spendings
    3. See spendings 
    4. today's spendings
    """)
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_spendings()
        elif choice == "2":
            delete_spendings()
        elif choice == "3":
            see_spendings()
        elif choice == "4":
            todays_spendings()
        elif choice == "5":
            print("Good bye")
            return None
        else:
            print("Invalid choice")
        return main()
    except KeyboardInterrupt:
        print("Good bye")
        return None


if __name__ == "__main__":
    main()