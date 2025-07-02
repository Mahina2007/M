
"""
1. create a base class Vehicle(type) with a method move(). Then, create two subclasses,
    Car(type,name) and Boat(type,name), each overriding the move() method. Write a function that takes
    a Vehicle object and calls its move() method.
"""


class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type

    def move(self):
        return f"Object type of {self.v_type} is moving"


class Car(Vehicle):
    def __init__(self, v_type, name):
        super().__init__(v_type)
        self.name = name

    def move(self):
        return f"{self.name} is moving"


class Boat(Vehicle):
    def __init__(self, v_type, name):
        super().__init__(v_type)
        self.name = name

    def move(self):
        return f"{self.name} is moving"


v = Vehicle(v_type="Cars")
car = Car(v_type="car", name="Malibu")
boat = Boat(v_type="boat", name="Titanic")

print(v.move())
print(car.move())
print(boat.move())

