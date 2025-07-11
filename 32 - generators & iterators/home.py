# 1. list qabul qiladigan itarator yarating va unga
# quyidagi 2 ta methodni ham qo'shing
#
# - start_from(index) -> bu methodni chaqirsam menga lisni
#   ichidagi elementlarni usha indexdan boshlab berishi kerak
# - random() -> buni chaqirsam usha listni ichidan
#   random son bersin, random kutubxonasini ishlatmang,
#   yangi random uchun algarithm o'ylab toping
#
# 2.  Cheksiz son generatorini yozib ber, u menga cheksiz son
#     qaytarib berib tursin, yani for bilan generatorni ishlatganimda
#     u hech qachon to'xtab qolmasin va sonni ochirib borsin.

# 1
class Iterator:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        return self

    def start_from(self, index):
        if not (0 <= index < len(self.list)):
            raise IndexError

        iterator = iter(self.list)
        result = []

        for element in range(index):
            next(iterator, None)

        for item in iterator:
            result.append(item)
        return result

    def random(self):
        if not self.list:
            return None

        random_id = input("press enter: ")
        index = id(random_id) % len(self.list)
        return self.list[index]


# list = [1, 2, 3, 4, 5]
# get_from_index = Iterator(list)
# print(get_from_index.start_from(3))
# print(get_from_index.random())

# 2
import time
def infinite_numbers():
    start = 0
    while True:
        yield start
        start += 1
#
# g = infinite_numbers()
# for num in g:
#     print(f"\r{num}", end='')
#     time.sleep(0.5)




