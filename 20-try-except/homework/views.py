from file_manager import read_from_json, write_to_json

def add_spendings():
    try:
        money = int(input("add how much u spent: "))

        spending = {
            "spending" : money,
        }

        spendings = read_from_json(file="spendings.json")
        spendings.append(spending)
        write_to_json(file="spendings.json", data=spendings)
        print("New spending is added")

    except ValueError:
        print("insert only number")
    except Exception as exc:
        print("something went wrong")
        print(exc)
