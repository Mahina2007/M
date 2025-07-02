# 1

n = int(input("n = "))
for even in range (n, 1, -2):
    if even % 2 == 0:
        print(even)
        
# 2

n = int(input("n = "))
for odd in range (n, 1, -2):
    if odd % 2 == 1:
        print(odd)

# 3

num = (input("number: "))

for digit in num [::-1]:
    print (digit)



# 4

name = input("name: ")
sum = 0

for vowel in name:
    if vowel in "AOUIEaouie":
      sum += 1
print(sum)




# 5

tags = input("insert some tags: ")
result=[]

for word in tags.split():
    if not word.startswith("#"):
        word = "#" + word
    result.append(word)
        
print(" ".join(result))
