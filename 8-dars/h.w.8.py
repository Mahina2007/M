# 1. Natural son n berilgan. Mersenn soni Mp dan kichik bo`lgan barcha
# sonlarni toping. Mersenn soni – bu oddiy son, u Mp=2p–1 ko`rinishida
# bo`lib, p – ham oddiy son

n = int(input("n: "))
    
def is_prime(num):
    if num < 2:
        return False 
    for d in range(2, int(num ** 0.5) + 1): 
        if num % d == 0: 
            return False
    return True

def find_mersen(n):
    result= []
    for p in range(2,n):
        if is_prime(p):
            mp = 2**p - 1
            if is_prime(mp):
                result.append(mp)
    return(result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_mersenne_numbers(n):
    result = []
    for p in range(2, n):
        if is_prime(p):  
            mp = 2**p - 1
            if is_prime(mp):  
                result.append(mp)
    return result
mersenne_numbers = find_mersenne_numbers(n)
print("result:", mersenne_numbers)


#2 Agar berilgan soni o`ngdan chapga va chapdan o`ngga bir xil o`qilsa
# palindrom deb ataymiz. 100 dan kichik palindrom sonlarni toping. 


def is_palindrome(n):
    return str(n) == str(n)[::-1]

for nums in range(1, 100):
    if is_palindrome(nums):
        print(nums, end=' ')
    
#3 Agar berilgan soni o`ngdan chapga va chapdan o`ngga bir xil o`qilsa
# palindrom deb ataymiz. 100 dan kichik bo`lgan, kvadratga oshirganda
# polindrom son bo`ladigan natural sonlarni toping. 
def is_palindrome(n):
    return str(n) == str(n)[::-1]

results = []

for num in range(1,100):
    square = num * num
    if is_palindrome(square):
        results.append(num)
        print(f"{num}**2 = {square}")
print(results)
    

#4 Haqiqiy son A va butun son N(>0) berilgan. A ning N chi darjasini 
# toping: AN = A·A··A(A soni N martta ko`paytiriladi).

a = float(input("a: ")) 
n = int(input("n: "))

if n > 0:
    print(int(a**n))
else:
    print("n should be greater than 0")
    
#5 Haqiqiy son A va butun son N(>0) berilgan. A ning barcha 1 dan N 
# gacha bo`lgan darajalarini toping. 
a = float(input("a: ")) 
n = int(input("n: "))

for power in range(1, n + 1):
    print(f"a^{power} = {a**power}")
    
#6
# Haqiqiy son A va butun son N(>0) berilgan. Chiqaring: 1+A+A2+A3+ 
# + AN.  
a = float(input("a: "))
n = int(input("n(n > 0): "))


s = 0
for p in range (n + 1):
    s += a**p
    
print(f"1 + a^1 + a^2...+ a^{n} = {s}")

# 7
# Haqiqiy son A(>1) berilgan. 1+1/2+1/3+…+1/N yig`indisi A dan katta 
# bo`ladigan, eng kichik N butun sonni va ushbu summani toping.

a = float(input("a: "))
sum = 0
n = 0

while sum <= a :
    n += 1
    sum += 1 / n
    
print(f"eng kichik n: {n}")
print(f"yig'indi: {sum}")

# 8
# Haqiqiy son N(>1) berilgan. 1∙2∙ ∙N ko`paytmasini toping.  
n = float(input("n(n> 1): "))
kopaytma = 1
butun_qismi = int(n)

for k in range(1, butun_qismi + 1):
    kopaytma *= k
    
print(f"1 * 2 * ...* {butun_qismi} = {kopaytma}")

# 9
# Haqiqiy son N(>1) berilgan. 2 ·1/(2) · 1/(3) ·…· 1/(N) ko`paytmasini 
# toping. 
n = float(input("n(n> 1): "))
kopaytma = 2
butun_qism = int(n)

for k in range (2, butun_qism + 1):
    kopaytma *= 1 / k
    
print(f"2 * 1/2 * 1/3*...* 1/{butun_qism} = {kopaytma}")

# 10
# Haqiqiy son X va butun son N(>0) berilgan. 1 + X+X2/2 +… + XN/N 
# qiymatini toping. 

x = float(input("x: "))
n = int(input("n: "))

S = 1
for i in range(1, n + 1):
    S += (x ** i) / i
    
print(f"qiymati:{S}")
    
    

    

