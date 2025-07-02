from datetime import datetime
from filemanager import JsonManager
class Debt:
    def __init__(self):
        self.debts_manager = JsonManager(filename="debts")


    def give_to_debt(self):
        product_name = input("name: ")
        price = int(input("price: "))
        phone_num = input("phone number: ")
        date = datetime.now().isoformat()
        new_id = self.debts_manager.generate_new_id()

        debt = {
            "name": product_name,
            "price": price,
            "phone_num": phone_num,
            "date": date,
            "id": new_id
        }
        debts = self.debts_manager.read_file()
        debts.append(debt)
        self.debts_manager.write_file(data=debts)
        print("new debt is added")

    def delete_debt(self):
        phone_num = input("phone number: ")
        debts = self.debts_manager.read_file()
        for d in debts:
            if d["phone_num"] == phone_num:
                debts.remove(d)
                self.debts_manager.write_file(debts)
                print("debt is deleted")
                return

        print("no person with this phone number")

    def show_all_debts(self):
        debts = self.debts_manager.read_file()
        for d in debts:
            print(f"ID: {d["id"]}\t{d["name"]}\t{d["phone_num"]}\t{d["price"]}\t{d["date"]}")

    def show_debt_by_num(self):
        phone_num = input("Phone number: ")
        debts = self.debts_manager.read_file()
        total_debts = []

        found = False
        for d in debts:
            if d["phone_num"] == phone_num:
                print(f'{d["name"]}, your debt is {d["price"]}, date: {d["date"]}')
                found = True
                if found:


        if not found:
            print("You don't have any debts.")

    def delete_debts(self):
        debts = self.debts_manager.read_file()
        debts.clear()
        self.debts_manager.write_file(debts)
        print("all debts are deleted")
        return []


    def update_debt(self):
        pass














