
from auth import register, login

def main():
    print("""
    1. Register
    2. Login
    3. Log out
    4. Exit
    """)



    try:

        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                print("you can log in now")
            else:
                print("try again")
        elif choice == "2":
            pass
        elif choice == "3":
            pass
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
