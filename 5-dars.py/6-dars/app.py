# for num in range(0,100,3):
#     print(num)

# sum = 0
# for num in range(1,100):
#     if num % 4 == 0 and num % 3 == 0:
#         sum += num
# print(sum)
        
# a = int(input("enter 1st number: "))
# b = int(input("enter 2nd number: "))
# sum = 0

# for num in range(a,b):
#     sum += num
# print(sum)

# num = input("enter a number: ")
# if num.isdigit():
#     sum = 0
#     for digit in num:
#         sum +=int(digit)
#     print(sum)
# else:
#     print("invalid number")

# 8. 1 dan 100 gacha toq sonlarni yig'indisini toping
# 9. 12 dan 80 gacha bo`lgan sonlarni kvadratini yig`indisini chiqaring.
# 10.11 dan 99 gacha bo`lgan sonlarni kvadratini chiqaring.

sum = 0
for num in range(1,100):
    if num % 2 != 0:
        sum += num
print(sum)

sum = 0
for num in range(12, 80):
    num = num ** 2
    sum += num
print(sum)
    

    
for power in range(11,99):
    print(power**2)
    

