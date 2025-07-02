from basket import Basket

def main():
    print("""
    Menu:
    1. Show all products
    2. Add to basket(id,quantity)
    3. Show basket
    4. Create order from basket(name, phone)
    5. Clear the basket
    6. Show orders
    """)

    choice = input("Enter you choice: ")
    basket = Basket(filename="filename")
    if choice == "1":
        basket.show_products()
    elif choice == "2":
        basket.add(p_id=0, quantity=0)
    elif choice == "3":
        basket.show()
    elif choice == "4":
        pass
    elif choice == "5":
        basket.clear()
    elif choice == "6":
        pass
    else:
        print("invalid choice")

    return main()

if __name__ == '__main__':
    main()