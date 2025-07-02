# polymorphism - bir class boshqa class'dan voris olib turgan holatda, ota classni ichida mavjud bo'lgan
# methodlar bola class'da ham mavjud bo'lganda hech qanaqa muammo bo'lmasligi
# polymorphism - "many forms"
# 1- hodisa- overriding - ustidan yozish
# 2- hodisa - overloading - bitta classni ichida 2ta bir xil nom bilan method yaratish -> pythonda yo'q

class Add:
    def add(self, a, b, c=None, d=None):
        if c and d:
            return a + b + c + d
        elif c:
            return a + b + c
        elif d:
            return a + b + d
        return a + b


a = Add()
print(a.add(1, 2, 3, 4))


