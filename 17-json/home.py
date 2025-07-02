
from func import add_nums
from func import subtract
from func import divide
from func import multiply
from func import show_all


def main():
    print("""
    Menu:
    1. Add
        num1, num2
    2. Subtract
    3. Multiply
    4. Divide
    5. Show all results
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        add_nums()
    elif choice == "2":
        subtract()
    elif choice == "3":
        multiply()
    elif choice == "4":
        divide()
    elif choice == "5":
        show_all()
    else:
        print("Invalid choice")
    return main()


if __name__ == "__main__":
    main()