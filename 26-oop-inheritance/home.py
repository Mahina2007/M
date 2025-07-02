import json
import os

class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        self.product_type = product_type

    def calculate_total_price(self):
        total = 0
        if os.path.exists("products.json"):
            with open("products.json", "r") as file:
                products = json.load(file)
            for product in products:
                total += int(product.get('price', 0))
        return total

    def show_data(self):
        with open(file="products.json", mode="r") as file:
            products = json.load(file)
            return products

class Books(Product):
    def __init__(self, name, price, pages):
        super().__init__(name, price, product_type= "book")
        self.pages = pages


    def add_to_file(self):
        new_product = {
            "product_type": self.product_type,
            "name": self.name,
            "price": self.price,
            "pages": self.pages
        }

        path = "products.json"
        if os.path.exists(path):
            with open(path, "r") as file:
                products = json.load(file)
                products.append(new_product)
                with open(path, "w") as file:
                    json.dump(products, file, indent=4)

        return "book is added"

    def calculate_total_book(self):
         total = 0
         if os.path.exists("products.json"):
             with open("products.json", "r") as file:
                 products = json.load(file)

             for product in products:
                 if product.get("type") == self.product_type:
                     total += int(product.get('price', 0))
         return total

    def show_data_books(self):
        books = []
        with open("products.json", "r") as file:
            products = json.load(file)

        for product in products:
            if product.get("type") == "book":
                books.append(product)
        return books

class Electronics(Product):
    def __init__(self, name, price, made_in, year ):
        super().__init__(name, price, product_type="electronics")
        self.made_in = made_in
        self.year = year


    def add_to_file(self):
        new_product = {
            "product_type": self.product_type,
            "name": self.name,
            "made_in": self.made_in,
            "year": self.year,
            "price": self.price
        }

        path = "products.json"
        if os.path.exists(path):
            with open(path, "r") as file:
                products = json.load(file)
                products.append(new_product)
                with open(path, "w") as file:
                    json.dump(products, file, indent=4)

        return "electronics is added"

    def calculate_electronics_total(self):
        total = 0
        if os.path.exists("products.json"):
            with open("products.json", "r") as file:
                products = json.load(file)

            for product in products:
                if product.get("type") == self.product_type:
                    total += int(product.get('price', 0))
        return total

    def show_data_electronics(self):
        electronics = []
        with open("products.json", "r") as file:
            products = json.load(file)

        for product in products:
            if product.get("type") == "electronics":
                electronics.append(product)
        return electronics

class Clothing(Product):
    def __init__(self, name, price, color ):
        super().__init__(name, price, product_type="cloth")
        self.color = color



    def add_to_file(self):
        new_product = {
            "product_type": self.product_type,
            "name": self.name,
            "price": self.price,
            "color": self.color
        }

        path = "products.json"
        if os.path.exists(path):
            with open(path, "r") as file:
                products = json.load(file)
                products.append(new_product)
                with open(path, "w") as file:
                    json.dump(products, file, indent=4)

        return "cloth is added"

    def calculate_clothing_total(self):
        total = 0
        if os.path.exists("products.json"):
            with open("products.json", "r") as file:
                products = json.load(file)

            for product in products:
                if product.get("type") == self.product_type:
                    total += int(product.get('price', 0))
        return total

    def show_data_cloth(self):
        clothes = []
        with open("products.json", "r") as file:
            products = json.load(file)

        for product in products:
            if product.get("type") == "cloth":
                clothes.append(product)
        return clothes


# book1 = Books(product_type="book", name="Iffat va hayo", price= 100000, pages= 120)
# electronics1 = Electronics(product_type="electronics", name="headphone", price=200000, made_in="Korea", year=2025)
# cloth2= Clothing(name="Wakiki", price= 1000000, color="white")
# print(cloth2.add_to_file())

# product = Books(name="name", price="price", pages="pages")
# total_book_price = product.calculate_total_book()
# print(total_book_price)

# product = Electronics(name="name", price="price", made_in="made_in", year="year")
# total_electronics_price = product.calculate_electronics_total()
# print(total_electronics_price)

# product = Clothing(name="name", price="price", color="color")
# total_clothing_price = product.calculate_clothing_total()
# print(total_clothing_price)

# product = Product(name="name", product_type="product_type", price="price")
# total_product = product.calculate_total_price()
# print(total_product)


