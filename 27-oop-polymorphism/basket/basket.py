from file_manager import FileManager

class Basket:
    basket = list()
    def __init__(self, filename):
        self.filename = filename
        self.product_manager = FileManager(filename="products")
        self.order_manager = FileManager(filename="order")

    def show_products(self):
        products = self.product_manager.read_file()

        for p in products:
            print(f"ID: {p["id"]}\t{p["name"]}\t{p["price"]}\t{p["quantity"]}")

    def add(self, p_id, quantity):
        self.show_products()
        p_id = int(input("enter product id: "))
        quantity = int(input("enter quantity: "))

        products = self.product_manager.read_file()
        for index, p in enumerate(products):
            if p['id'] == p_id:
                if p['quantity'] >= quantity:
                    self.basket.append({
                        "id": p_id, "quantity": quantity,
                        "name": p['name'], "price": p['price'],
                    })
                    products[index]['quantity'] = products[index]['quantity'] - quantity
                    self.product_manager.write_file(data=products)
                    print("product is added")
                    return
                else:
                    print("There is not enough products")
                    return
        print("product is not found")

    def show(self):
        for p in self.basket:
            print(f"ID: {p["id"]}\t{p["name"]}\t{p["price"]}\t{p["quantity"]}")

    def create_order(self):
        pass

    def clear(self):
        self.basket.clear()
    def show_orders(self):
        pass

