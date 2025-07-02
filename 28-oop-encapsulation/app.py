# encapsulation - method va attributelarga murojaat qilish darajasini belgilash
# 1.private - o'sha method yoki attribute'ni o'sha classdan boshqa classda ishlaatib bo'lmaydi
# 2.protected - o'zini ichida va "bolalari"da ishlatsa bo'ladi
# 3.public - hammasida ishlatsa bo'ladi
# client - boshqa class
# @property - decorator ; methodni attribute'da ishlatish imkonini beradi




# 1-vazifa: Oddiy inkapsulyatsiya
# Book klassini yarating, unda private atribut __title bo‘lsin.
# get_title() va set_title() metodlari orqali o‘qish va o‘zgartirish imkonini yarating.

# 2-vazifa: Pythonic getter/setter
# Yuqoridagi Book klassida @property va @setter orqali title ni boshqaring.

# 3-vazifa: Setterda tekshiruv
# Book klassiga __pages atributini qo‘shing.
# Setter ichida pages butun son va 0 dan katta bo‘lishini tekshiring. Aks holda xatolik chiqarsin.
#1
# class Book:
#     def __init__(self, pages):
#         self.__pages = pages
#
#     @property
#     def pages(self):
#         return self.__pages
#
#     @pages.setter
#     def pages(self, new_pages):
#         if new_pages > 0 and isinstance(new_pages, int):
#             self.__pages = new_pages
#         else:
#             raise ValueError('wrong data')
#
# a1 = Book(pages=100)
# a1.pages = 10
# print(a1.pages)
#     def get_title(self):
#         return self.__title
#
#     def set_title(self, new_title):
#         self.__title = new_title
#
# a = Book(title="men")
# print(a.title)
# 2

# 4-vazifa: Protected atribut
# Car klassini yarating, unda _mileage protected atribut bo‘lsin.
# Uni tashqaridan o‘qib bo‘lishini ko‘rsating, lekin nima uchun bu noto‘g‘ri amaliyot ekanini tushuntiring.
# class Car:
#     def __init__(self, mileage):
#         self._mileage = mileage
#
# car1 = Car(mileage="mileage")
#
# print(car1._mileage)

# 5-vazifa: Private metod
# Robot klassini yarating va unda __boot_sequence() private metodini yozing.
# Uni tashqaridan chaqirishga harakat qiling (xatolik chiqadi), keyin esa _ClassName__method shaklida chaqirib ko‘ring.
# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     def __boot_sequence(self):
#         return  f"{self.name} is booting up..."
#
#
# r1 = Robot("Robo-1")
# print(r1._Robot__boot_sequence())


# 6-vazifa: Faqat yozish (write-only) xossasi
# PasswordManager klassini yarating va unda private __password atributini belgilang.
# Faqat setter yozing, getterda AttributeError chiqarilsin.
# class PasswordManager:
#     def __init__(self, password):
#         self.__password = password
#
#     def get(self):
#         return AttributeError
#
#     def set(self, new_password):
#         self.__password = new_password
#         return new_password
#
# user = PasswordManager(password=123)
# print(user.set(new_password=321))

# 7-vazifa: Metod orqali boshqarish
# Employee klassini yarating, __salary private atributi bo‘lsin.
# # increase_salary(percent) metodi orqali maoshni faqat 1-100 oralig‘ida oshirishga ruxsat bering.
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary
#
#     def get(self):
#         return self.__salary
#
#     def increase_salary(self, percent):
#         if 1 <= percent <= 100:
#             increase = self.__salary * (percent/100)
#             self.__salary += increase
#             return self.__salary
#         else:
#             raise ValueError("percentage must be between 1 and 100")
#
# emp1= Employee(salary=1000000)
# print(emp1.get())
# print(emp1.increase_salary(percent=10))

# 8-vazifa: Kalit so‘z bilan to‘qnashuvdan qochish
# class_ nomli atributga ega Course klassini yarating (class kalit so‘zidan farqli).
# class_ qiymatini belgilang va uni chop eting.
# class Course:
#     def __init__(self, class_):
#         self.class_ = class_
# obj = Course(class_ = 1)
# print(obj.class_)

# 9-vazifa: Vorislik va protected metod
# Animal klassini yarating va unda _speak() protected metodi bo‘lsin.
# Dog klassi Animal dan voris bo‘lsin va _speak() metodini ichida chaqirsin.
# Tashqaridan ham chaqirib bo‘lishini ko‘rsating.

# class Animal:
#     def __init__(self):
#         pass
#
#     def _speak(self, animal_name):
#         self.animal_name = animal_name
#         return f"{animal_name}"
#
# class Dog(Animal):
#     pass
#
# animal = Dog()
# print(animal._speak(animal_name="haski"))

