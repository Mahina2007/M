"""
1. Valyuta kurslari

exchange_rates = {
    "USD": 12500,
    "EUR": 13500,
    "RUB": 150,
}
Berilgan so'mni foydalanuvchi tanlagan valyutaga o'giradigan funksiya yozing.

2. Mashinalar ro'yxati

cars = {
    "Cobalt": {"narx": 12000, "yil": 2022},
    "Malibu": {"narx": 25000, "yil": 2023},
    "Damas": {"narx": 9000, "yil": 2021},
}
Eng arzon mashinani toping.
Eng yangi mashinani toping.



3.Supermarket kassasi

cart = {
    "Olma": 3,
    "Banan": 2,
    "Uzum": 5,
}
prices = {
    "Olma": 12000,
    "Banan": 18000,
    "Uzum": 15000,
}
Jami xarid narxini hisoblang.
--------------------------------------------------------------------------------
"""
# 1
exchange_rates = {
    "USD": 12500,
    "EUR": 13500,
    "RUB": 150,
}

def sum_usd(sum):
    return sum / exchange_rates["USD"]
    
    
def sum_eur(sum):
    return sum / exchange_rates["EUR"]
    
def sum_rub(sum):
    return sum / exchange_rates["RUB"]



# som = int(input("how much som? "))
# exchange = int(input("which one do you want to choose:  1.USD   2.EUR   3.RUB "))

# if exchange == 1:
#     print(sum_usd(som))
# elif exchange == 2:
#     print(sum_eur(som))
# elif exchange == 3:
#     print(sum_rub(som))
# else:
#     print("invalid choice")

# 2
# cars = {
#     "Cobalt": {"narx": 12000, "yil": 2022},
#     "Malibu": {"narx": 25000, "yil": 2023},
#     "Damas": {"narx": 9000, "yil": 2021},
# }

# cheapest = None
# newest = None

# for name, values in cars.items():
#     if cheapest is None:
#        cheapest = (name, values) 
#     elif values["narx"] < cheapest[1]["narx"]:
#         cheapest = (name, values)
        
# print(cheapest[0], cheapest[1])
        
# for name, values in cars.items():
#     if newest is None:
#        newest = (name, values) 
#     elif values["yil"] > newest[1]["yil"]:
#         newest = (name, values)
           
# print(newest[0] , newest [1])



    
# 3
# cart = {
#     "Olma": 3,
#     "Banan": 2,
#     "Uzum": 5,
# }
# prices = {
#     "Olma": 12000,
#     "Banan": 18000,
#     "Uzum": 15000,
# }

# total_price = 0

# for name, value in cart.items():
#     total_price += prices[name] * value
    
# print(total_price)
    