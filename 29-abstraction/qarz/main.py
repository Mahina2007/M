"""
Ushbu muommoga yechim topish kerak, qanday holatda daastur yasash o'zingizga bog'liq.

Masala:
Bir kichik do'kon egasi do'kondagi ba'zi bir narsalarni qarzga ham berib turadi.
Va kimga qancha narsani necha puli va qachon qarzga berganini daftarga yozib boradi.
Sizni vazifangiz uni ishini osonlashtirish. Ya'ni unga qarzga bergan narsalari ro'yxatini
boshqarishga yordam berish."""

from views import Debt


def main():
    print("""
    Menu:
    1. Show all debts
    2. Give to debt
    3. Show someone's debt
    4. delete all debts
    5. delete by phone number
    6. Exit
    """)

    choice = input("Enter you choice: ")
    d = Debt()
    if choice == "1":
        d.show_all_debts()
    elif choice == "2":
        d.give_to_debt()
    elif choice == "3":
        d.show_debt_by_num()
    elif choice == "4":
        d.delete_debts()
    elif choice == "5":
        d.delete_debt()
    elif choice == "6":
        print("good bye!")
    else:
        print("invalid choice")

    return main()

if __name__ == '__main__':
    main()

