"""
dunder method - maxsus method
"""
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.name
#
#     def __float__(self):
#         return float(self.age)
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __ge__(self, other):
#         return self.age >= other.age
#
#     def __call__(self, *args, **kwargs):
#         print("Hello world")
#
#     def __getitem__(self, item):
#         return self.name[item]
#
#     def __setitem__(self, key, value):
#         name = list(self.name)
#         name[key] = value
#         self.name = "".join(name)
#         return self.name
#
#
# ali = Student(name="Ali", age=21)
# vali = Student(name="Vali", age=20)
#
# # print(ali - vali)
#
# # print(ali >= vali)
#
# ali[0] = "W"
# print(ali.name)
# 1. __str__ va __repr__ — Kontaktlar ro‘yxati
# Vazifa: Telefon kontaktlarini saqlovchi klass yozing.
class Contacts:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.number

ali = Contacts(name="ali", number="123")
vali = Contacts(name="vali", number="124")

# print(ali, vali)
# contacts = [ali, vali]
# print(contacts)
# 2. __add__ — Savat (shopping cart)
# Vazifa: Ikkita savatdagi mahsulotlarni birlashtiring.
# class Shopping:
#     def __init__(self, products):
#         self.products = products
#
#     def __add__(self, other):
#         result = dict()
#         for name, quantity in self.products.items():
#             result[name] = quantity + other.products.get(name, 0)
#         return  result
# obj1 = Shopping(products={"a":1, "b": 2})
# obj2 = Shopping(products={"a":1, "b": 2})
# print(obj1 + obj2)

# print(obj1 + obj2)
# 3. __call__ — SMS yuboruvchi obyekt
# Vazifa: SMS yuboradigan obyekt yaratilsin.
# class SMS:
#
#     def __init__(self, message):
#         self.message = message
#
#     def __call__(self, *args, **kwargs):
#         print("hello")


# 4. __contains__ va __len__ — Ishchilar ro‘yxati
# Vazifa: Ishchilar ro‘yxatini tekshirish
#
# it_company = Company("TechSoft", ["Ali", "Laylo", "Bobur"])
# print("Ali" in it_company)    # True
# print(len(it_company))  # 3
#
# 5. _getitem__, __setitem__, __delitem__ — Elektron kundalik (dnevnik)
# Vazifa: O‘quvchining fanlar bo‘yicha baholarini boshqaradigan klass yozing.
#
# ali_diary = Diary()
# ali_diary["Matematika"] = 5
# ali_diary["Fizika"] = 4
#
# print(ali_diary["Matematika"])  # 5
# del ali_diary["Fizika"]
# print(ali_diary["Fizika"])      # Bahosi yo‘q
#
# 6. __eq__, __lt__, __gt__ — Narx solishtiruvchi mahsulotlar
# Vazifa: Mahsulotlar narxini solishtirish.
#
# p1 = Product("Pepsi", 12000)
# p2 = Product("Coca-Cola", 12000)
# p3 = Product("Fanta", 10000)
#
# print(p1 == p2)  # True
# print(p3 < p1)   # True

