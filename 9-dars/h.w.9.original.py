"""
1. 17 ta ikki xonali sonlardan iborat massiv berilgan. Raqamlar yig'indisini hisoblang.
2. 9 va 7 elementli ikkita haqiqiy sonlardan iborat massiv berilgan. Ularni o'sish tartibida yangi massiv hosil qiling.
3. 10 ta elementli butun sonli X va Y massivlari berilgan. Ikkisining bir xil elementlaridan yangi massiv hosil qiling.
4. 16 ta haqiqiy sonli massiv berilgan. Juft indeksdagi elementlar yig'indisini va 3 ga karrali indeksdagi elementlar yig'indisini ayirmasini hisoblang.
5. 9 ta butun sonli massiv berilgan. Musbat toq sonlarning eng katta indeksini toping.
"""

#1
# nums = [12, 34, 55, 66, 77, 88, 58, 78, 96, 86, 33, 45, 77, 94, 52, 41, 14]

# for num in nums:
#     summa = 0
#     for digit in str(num):
#         summa += int(digit)
#     print(summa)

# 2
# nums1 = [12, 34, 5, 6, 7, 8, 10, 5, 23]
# nums2 = [1, 34, 55, 66, 25, 48, 8]

# nums3 = nums1 + nums2
# nums3.sort()
# print(nums3)

#3
# nums1 = [1, 34, 5, 66, 77, 8, 9, 4, 1, 22]
# nums2 = [1, 34, 55, 66, 4, 7, 2, 5, 10, 99]

# nums3 = []

# for num in nums1:
#     if num in nums2:
#         nums3.append(num)

# print(nums3)

# 4
# nums1 = [1, 3, 4, 3, 10, 5, 7, 8, 5, 9, 11, 52, 6, 7, 15, 16]
# # 59- 42 = 17

# two_summa = 0
# three_summa = 0

# for index in range(len(nums1)):
#     if index % 2 == 0:
#         two_summa += nums1[index]
#     if index % 3 == 0:
#         three_summa += nums1[index]

# print(two_summa - three_summa)

#5
# nums = [1, 3, 4, 3, 11, 50, -7, -8, -9]

# index = len(nums) - 1
# while index >= 0:
#     if nums[index] > 0 and nums[index] % 2 == 1:
#         print(index)
#         break
#     index -= 1
