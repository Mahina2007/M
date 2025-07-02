class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self):
        return self.price

    def to_dict(self):
        return {
            "type": "product",
            "name": self.name,
            "price": self.price
        }

    def add_to_file(self):
        data = self.to_dict()
        filename = "products.json"
        if os.path.exists(filename):
            with open(file=filename, mode="r") as file:
                products = json.load(file)
        else:
            products = []

        products.append(data)

        with open(file=filename, mode="w") as file:
            json.dump(products, file, indent=4)

    def show_data(self):
        print(self.to_dict())
