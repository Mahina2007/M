# 1. Internet tezligi - Foydalanuvchi uchun eng yaxshi tarifni tanlash.
#     foydalanuvchidan qancha puli borligini so'raysiz, usha puli yetadigan
#     eng yaxshi tarifni chiqarib berasiz


# def find_appropriate_tarif(trafik: list) -> dict:
#     money = int(input("enter your money: "))
#     best_tarif = None
#     for tarif in trafik:
#         if money >= tarif["narxi"]:
#                 best_tarif = tarif
#     if best_tarif is None:
#         print('money is not enough')
#     return best_tarif
    
# Tariflar = [
#     {
#         "tarif": "barakali 33 ",
#         "narxi" : 33000
#     },
#     {    
#         "tarif": "barakali 44",
#         "narxi": 44000
#     },
#     {   
#         "tarif": "barakali 55 ",
#         "narxi" : 55000   
#     }
# ]

# result = find_appropriate_tarif(trafik = Tariflar)
# print(result)
# 2. Mahsulot zaxiralari - Ombordagi kam qolgan mahsulotlarni chiqarish.


# def find_min_product(products : list) -> dict | None:
#     collected_products = dict()
#     for product in products:
#         if product['name'] in collected_products.keys():
#             collected_products[product['name']] += product["value"]
#         else:
#             collected_products[product['name']] = product["value"]

#     min_product = None
#     for name, quantity in collected_products.items():
#         if min_product is None:
#             min_product = (name, quantity)
#         elif quantity < min_product[1]:
#             min_product = (name, quantity)
#     return min_product

# ombor = [
#     {
#         "name": "potato",
#         "value": 4
#     },
#     {
#         "name": "tomato",
#         "value": 20
#     },
#     {
#         "name": "onion",
#         "value": 10
#     },
#     {
#         "name": "cucumber",
#         "value": 10
#     },
#     {
#         "name" : "potato",
#         "value" : 1
#     }    
# ]
# result = find_min_product(products = ombor)
# print(result)

# 3. Ishchilar ma'lumoti - Eng tajribali ishchini topish.
# def find_most_experienced_person(people: list) -> dict | None:
#     """
#     This function helps to find experienced employer and return as a dict
#     or None if there is no any employer
#     :param groups: list of employers as a dict
#     :return: employer dict or None
#     """
#     most_experienced = None
#     for person in people:
#         if most_experienced is None:
#             most_experienced = person
#         else:
#             if person['years'] > most_experienced['years']:
#                 most_experienced = person
#     return most_experienced

# employers = [
#     {
#         "name": "Madina",
#         "years": 10
#     },
#     {
#         "name": "Ikrom",
#         "years": 13
#     },
#     {
#         "name": "Zilola",
#         "years": 12
#     }
# ]

# result = find_most_experienced_person(people=employers)
# print(result)
