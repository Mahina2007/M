
# days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
# day = input("Enter day: ").strip().lower()

# if day in days:
#     index = days.index(day)
#     prev_day = days[index - 1]
#     next_day = days[(index + 1) % 7]
#     print(prev_day, next_day)
# else:
#     print("Invalid day")

nums1 = {1, 1, 1, 1, 2, 3, 4, 'salom', 'ali'}
nums2 = {'a', 'b', 1, 2, 'c'}

# nums1.remove(1)
# num = nums1.pop()
# nums1.add(10)

# nums1.discard(100)
# nums1 = nums1.union(nums2)

# print(nums1.symmetric_difference(nums2))
# print(nums1.intersection(nums2))


# # 1. Ichida 10 element bor list yarating va uni ichida duplicate larini olib tashlang
# list =  {1, 2, 3, 3, 4, 5, 5, 6, 6, 7,}
# print(list)
# 2. Ikkita list yarating, birinchi listni ichidagi hamma
#    elementlar ikkinchi listni ichida bormi yo'qmi tekshiring
# nums1 = {1, 1, 1, 1, 2, 3, 4, 'salom', 'ali'}
# nums2 = {'a', 'b', 1, 2, 'c'}

# print(nums1.difference(nums2))
# 3. Sizda ikkita ro'yxat bor biri choy uchun ikkinchi cofe uchun
#    ro'yxatdan turgan odamlanri ismlarini saqlaydi, odam sizga ismini
#    kiritadi va sizni vazifangiz u ikkala ro'yxatda ham bormi
#    yo'qmi tekshirish


names_tea = {'ali', 'vali'}
names_coffee = {'ali', 'vali', 'gani'}
name = input("Name: ")

print(name in set(names_tea).intersection(names_coffee))
    
