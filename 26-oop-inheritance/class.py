class A:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def greeting(self):
        return f"Hello, {self.name}"

class B(A):
    def __init__(self, name, year, age):
        super().__init__(name, year)
        self.age = age

object1= A(name= "Ali", year= 1900)
object2= B(name= "li", year= 2000, age=25)

print(object1.greeting())