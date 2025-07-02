from file_manager import write_to_json, read_from_json
import os


def add_new():
    product = input("Enter product: ")
    value = input("Enter value: ")

    data = {
        "product": product,
        "value": value
    }

    products = read_from_json(file="products.json")
    products.append(data)
    write_to_json(file="products.json", data=products)
    print("New product is added")


def view_list():
    products = read_from_json(file="products.json")
    for product in products:
        print(f"product: {product['product']}\t value: {product['value']}")


def delete_product():
    product_name = input("Enter product name: ")
    products = read_from_json(file="products.json")
    for index, product in enumerate(products):
        if product['product'] == product_name:
            products.pop(index)
            write_to_json(file="products.json", data=products)
            return
    print("product is not found")

def clear_all():
    if os.path.exists("products.json"):
        os.remove("products.json")
        print("products are deleted")
    else:
        print("products don't exist")
    
    
