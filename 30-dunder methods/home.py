"""
Student nomli class yarating va unda quyidagi amallarni bajara olishim uchun dunder methodlar yozing
undan quyidagicha attributelar bo'lishi kerak:
full_name, age, birthday, gender, courses=[]

biror bir objectni chaqarib unga yangi object ni berib yuborsam o'zini ichidagi
courses listiga shu objectni qo'shib qo'ysin


+, -, *, /,  +=, -=, /=, *=, **

object ni uzunligini o'lchasam jami courselarni sonini chiqarib bersin
object ni for bilan aylansam kurslarini birma bir bersin -> __repr__
object ni in bilan tekshirsam kurslarini ro'yxatini ichida bormi yo'qmi tekshirsin

qolgan tepadagi amallarga o'zingiz mantiq yozing

heh qanday menyu yasash kerak emas shunchaki har bir methodni tekshirib ko'rish kerak

"""
class Students:
    def __init__(self, full_name, age, birthday, gender):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = []

    def __call__(self, other):
        if isinstance(other, Students):
            return other.courses.append(other)

    def __repr__(self):
        for s in self.courses:
         return f"(full_name='{self.full_name}', courses={[s.full_name]})"

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
# obj3 = Students(full_name="habib", age=20, birthday="13", gender="male")
# print(obj1 + obj2)
# # print(obj1 - obj2)
# print(obj1 * obj2)
# print(obj1 / obj2)

obj1(obj2)
print(obj1)










