# kartadan kartaga
# o'zini kartasiga

from func_views import add_card
from func_views import transfer_money


def main():
    print("""
    1. Add card (full_name, card_number, password)
    2. Add money to card (card_number, amount)
    3. Send money (from_card_number, password, to_card_number, amount)
    4. Exit
    """)
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_card()
        elif choice == "2":
            add_money()
        elif choice == "3":
            transfer_money()
        elif choice == "4":
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



