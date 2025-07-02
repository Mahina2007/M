# 1
age = int(input("enter ur age: "))

if 0 < age <6 :
    print("it's free")
elif 6 <= age < 18:
    print("It's 20k sum")
elif 18 <= age:
    print("it's 40k sum")
else:
    print("invalid age")
    
# 2
battery = int(input("enter ur battery %: "))

if 0 <= battery <= 20:
    print("charge ur phone!")
elif 21 <= battery <= 50:
    print ("ur battery is normal, but it should be charged.")
elif 51 <= battery <= 100:
    print ("ur phone is fully charged!")
else:
    print("invalid percentage")
    
# 3
a = int(input("number: "))

if a > 0 and a % 2 == 0 or a % 10 == 3:
    print("Either the number is even or ends with 3")
elif a > 0 and a % 2 != 0 or a % 10 == 3:
    print("neither it's even, nor ends with 3 ")
else:
    print("it's not natural number")

