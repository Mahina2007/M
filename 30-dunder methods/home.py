class Students:
    def __init__(self, full_name, age, birthday, gender):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = []

    def __call__(self, other):
        self.courses.append(other)
        return f'{other} is added to {self.full_name} courses: {self.courses}'

    def __repr__(self):
        pass

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("other should be integer")
        elif isinstance(other, Students):
            self.age += other.age
        else:
            raise TypeError("other must be int or Students instance")
        return self

    def __imul__(self, other):
        self.age *= other.age
        return self

    def __isub__(self, other):
        self.age -= other.age
        return self

    def __itruediv__(self, other):
        self.age /= other.age
        return self

    def __pow__(self, power, modulo=None):
        return self.age ** power


    def __len__(self):
        return len(self.courses)

    def __contains__(self, course):
        return course in self.courses

    def __iter__(self):
        return iter(self.courses)
    # def __add__(self, other):
    #     return self.age + other.age
    #
    # def __sub__(self, other):
    #     return self.age - other.age
    #
    # def __mul__(self, other):
    #     return self.age * other.age
    #
    # def __truediv__(self, other):
    #     return self.age / other.age

obj1 = Students(full_name="mahina", age=18, birthday="19-feb", gender="female")
obj2 = Students(full_name="habiba", age=19, birthday="12", gender="female")

# print(obj1 + obj2)
# # print(obj1 - obj2)
# print(obj1 * obj2)
# print(obj1 / obj2)
# print(obj1("math"))
# print(obj1.courses)
# print(obj1("English"))
# print(obj1("math"))
# print(obj1.courses)
# print(len(obj1))
# obj1.age += obj2.age
# print(obj1.age)
# obj1.age *= obj2.age
# print(obj1.age)
# obj2.age -= obj1.age
# print(obj2.age)
# obj2.age /= obj1.age
# # print(obj2.age)
# print(obj1.age ** obj2.age)
# print(obj1("math"))
# print("python" in obj1)
# print(obj1("English"))
# print(obj1("math"))
# for course in obj1:
#     print(course)