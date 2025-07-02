"""

1. Add card (full_name, card_number, password)
2. Add money to card (card_number, amount)
3. Send money (from_card_number, password, to_card_number, amount)

"""
from file_manager import read_from_json, write_to_json
from utils import read, writerows

def add_card():
    try:
        full_name = input("full name: ")
        card_number = input("card number: ")
        password = int(input("password: "))

        user = {
            "name": full_name,
            "card number": card_number,
            "password": password
        }

        users = read_from_json(file="users.json")
        users.append(user)
        write_to_json(file="users.json", data=users)
        print("New card is added")

    except ValueError:
        print("Wrong value, please enter integer only")
    except Exception as exc:
        print("something went wrong")
        print(exc)



def add_money():
    card_number = int(input("Enter your card number: "))
    amount = int(input("Enter amount of money: "))

    money = {
        "card": card_number ,
        "amount" : amount,
    }
    money = read_from_json(file="money.json")
    money.append(amount)
    write_to_json(file="money.json", data=money)
    print("New money is added")



def transfer_money():
    from_card_number = int(input("Enter your card number: "))
    password = int(input("Enter your password: "))
    to_card_number = int(input("Enter receiver card number: "))
    amount = int(input("Enter amount of money: "))

    cards = read(filename = "card")
    from_card = None
    to_card = None

    for index, card in enumerate(cards):
        if card[1] == from_card_number:
            from_card = index
        elif card[1] == to_card_number:
            to_card = index

    if from_card is None:
        print("invalid from card number")
    elif to_card is None:
        print("invalid to card number")
    elif int(cards[from_card][2]) != password:
        print("invalid password")
    else:
        if int(cards[from_card][-1]) >= amount:
            cards[to_card][-1] = int(cards[to_card][-1]) + amount
            cards[from_card][-1] = int(cards[from_card][-1]) - amount
            writerows(filename="cards", data=cards)
        else:
            print("you dont have enough money")

