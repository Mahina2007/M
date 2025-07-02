# 1. PaymentProcessor nomli abstract class yozing va uni process_payment
#    nomli method bor bo'lsin va u amount qabul qilsin
#    Undan 3 ta subclass yarating, click, payme, uzum nomli
#    method ni ichida shunchaki string qaytarib qo'ysangiz bo'ladi
from abc import abstractmethod
# class PaymentProcessor:
#     @abstractmethod
#     def process_payment(self):
#         pass
# class Click(PaymentProcessor):
#     def process_payment(self):
#         return ""
# class Payme(PaymentProcessor):
#     def process_payment(self):
#         return ""
# class Uzum(PaymentProcessor):
#     def process_payment(self):
#         return ""

import json
import os
import csv
class FileHandler:
    @abstractmethod
    def write(self):
        pass

    def read(self):
        pass

# class FileHandler:
#     def __init__(self, filename, file_type):
#         self.filename = filename
#         self.file_type = file_type

    # def read(self):
    #     return open(file=f"{self.filename}.{self.file_type}", mode="r")


class TextFileHandler(FileHandler):
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type

    def read(self):
        open(file=f"{self.filename}.{self.file_type}", mode="r")
        data = file.read()
        file.close()
        return data


class CSVFileHandler(FileHandler):
    def __init__(self, filename, file_type):
        super().__init__(filename, file_type)

    def read(self):
        file = super().read()
        reader = csv.reader(file)
        # file.close()
        return list(reader)


class JSONFileHandler(FileHandler):
    def __init__(self, filename, file_type):
        super().__init__(filename, file_type)

    def read(self):
        file = super().read()
        # file.close()
        return json.load(file)


object1 = TextFileHandler(filename="data", file_type="txt")
object2 = CSVFileHandler(filename="data", file_type="csv")
object3 = JSONFileHandler(filename="data", file_type="json")

# # print(object1.read())
# print(object2.read())
print(object3.read())



