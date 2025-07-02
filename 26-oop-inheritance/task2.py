import csv
import json


class FileHandler:
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type

    def read(self):
        return open(file=f"{self.filename}.{self.file_type}", mode="r")


class TextFileHandler(FileHandler):
    def __init__(self, filename, file_type):
        super().__init__(filename, file_type)

    def read(self):
        file = super().read()
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

