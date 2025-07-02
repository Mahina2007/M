grade = int(input("Enter your score: "))

if grade >= 90:
    print('A')
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")