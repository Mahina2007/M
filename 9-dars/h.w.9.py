# 1. 17 ta ikki xonali sonlardan iborat massiv berilgan. Raqamlar yig'indisini hisoblang.

massiv = []

print("Iltimos, 17 ta ikki xonali son kiriting:")

s = 0
while s < 17:
    son = int(input(f"{s+1}-sonni kiriting: "))
    if 10 <= son <= 99:
        massiv.append(son)
        s += 1 
    else:
        print("ERROR: faqat 10 dan 99 gacha bolgan ikki xonali son kiriting!")


umumiy_yigindi = 0
for son in massiv:
    birlik = son % 10
    onlik = son // 10
    umumiy_yigindi += birlik + onlik

print("Raqamlar yig'indisi:", umumiy_yigindi)



# 2. 9 va 7 elementli ikkita haqiqiy sonlardan iborat massiv berilgan. Ularni o'sish tartibida yangi massiv hosil qiling.

massiv1 = [3.2, 7.1, 0.9, 5.5, 6.6, 1.1, 8.3, 2.4, 4.0]
massiv2 = [9.5, 2.2, 7.7, 3.5, 6.0, 1.9, 0.5]


massiv_total = massiv1 + massiv2


massiv_total.sort()

print(f"Yangi o'sish tartibidagi massiv: {massiv_total}")










# 3. 10 ta elementli butun sonli X va Y massivlari berilgan. Ikkisining bir xil elementlaridan yangi massiv hosil qiling.


X = []
Y = []


print("X massivining 10 ta elementini kiriting:")
for i in range(10):
    while True:
        try:
            son = int(input(f"{i+1}-elementini kiriting: "))
            X.append(son)  
            break  
        except ValueError:
            print("Faqat butun son kiriting!")


print("\nY massivining 10 ta elementini kiriting:")
for i in range(10):
    while True:
        try:
            son = int(input(f"{i+1}-elementini kiriting: "))
            Y.append(son)  
            break  
        except ValueError:
            print("Faqat butun son kiriting!")


bir_xil_elementlar = list(set(X) & set(Y))


print("Ikkala massivning bir xil elementlari:")
print(bir_xil_elementlar)



# 4. 16 ta haqiqiy sonli massiv berilgan. Juft indeksdagi elementlar yig'indisini va 3 ga karrali indeksdagi elementlar yig'indisini ayirmasini hisoblang.
massiv = [float(input(f"{i+1}-elementni kiriting: ")) for i in range(16)]


juft_indeks_yigindi = 0
for i in range(0, len(massiv), 2): 
    juft_indeks_yigindi += massiv[i]


karrali_indeks_yigindi = 0
for i in range(0, len(massiv), 3):  
    karrali_indeks_yigindi += massiv[i]


ayirma = juft_indeks_yigindi - karrali_indeks_yigindi


print(f"Juft indekslardagi elementlar yig'indisi: {juft_indeks_yigindi}")
print(f"3 ga karrali indekslardagi elementlar yig'indisi: {karrali_indeks_yigindi}")
print(f"Yig'indilar ayirmasi: {ayirma}")


# 5. 9 ta butun sonli massiv berilgan. Musbat toq sonlarning eng katta indeksini toping.
massiv = []

for son in range (9):
     while True:
        try:
            sonlar = int(input(f"{son+1}-elementini kiriting: "))
            massiv.append(sonlar)  
            break  
        except ValueError:
            print("Faqat butun son kiriting!")
            
eng_katta_indeks = -1  
for i in range(len(massiv)):
    if massiv[i] > 0 and massiv[i] % 2 != 0:
        eng_katta_indeks = i  

if eng_katta_indeks != -1:
    print(f"Musbat toq sonlarning eng katta indeksi: {eng_katta_indeks}")
else:
    print("Musbat toq sonlar mavjud emas.")


