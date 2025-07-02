class RentCar:
    def __init__(self, car_name, model):
        self.car_name = car_name
        self.model = model
        self.__is_rented = False

    def rent_car(self):
        if not self.__is_rented:
            self.__is_rented = True
            return "car is rented"
        return "car is already rented"
    @property
    def is_rented(self):
        return self.__is_rented


    def get(self):
        return self.__is_rented

    def return_car(self):
        if self.__is_rented:
            self.__is_rented = True
            return "car is returned"
        return "car is not rented yet"

car1 = RentCar(car_name="BYD", model="champion")
# print(car1.rent_car())
print(car1.is_rented)
# print(car1.get())
# print(car1.return_car())