# 1
workers = {
    "Ali": {"yosh": 30, "maosh": 500, "lavozim": "Dasturchi"},
    "Vali": {"yosh": 25, "maosh": 450, "lavozim": "Dizayner"},
    "Sardor": {"yosh": 28, "maosh": 600, "lavozim": "Muhandis"},
}

max_salary = None
average = 0

for name, salary in workers.items():
    average += salary["maosh"]/3
    if max_salary is None:
        max_salary = (name, salary)
    elif salary["maosh"] > max_salary[1]["maosh"]:
        max_salary = (name, salary,)
        
print(max_salary[0], max_salary[1])
print(average)
# 2
books = {
    "Python asoslari": {"muallif": "Aliyev", "narx": 120000, "sotildi": 30},
    "Django": {"muallif": "Valiyev", "narx": 150000, "sotildi": 20},
    "Algoritmlar": {"muallif": "Karimov", "narx": 180000, "sotildi": 15},
}

best_sold = None
total_money = 0

for name, sold in books.items():
    total_money += sold["narx"] * sold["sotildi"]
    if best_sold is None:
        best_sold = (name, sold)
    elif sold["sotildi"] > best_sold[1]["sotildi"]:
        best_sold = (name, sold)
        
print(best_sold[0], best_sold[1])
print(total_money)

# 3
students = {
    "Aziz": {"Matematika": 4, "Fizika": 5, "Ingliz tili": 3},
    "Bekzod": {"Matematika": 5, "Fizika": 4, "Ingliz tili": 5},
    "Gulnoza": {"Matematika": 3, "Fizika": 4, "Ingliz tili": 4},
}

top_math = None

for name, grades in students.items():
    if top_math is None:
        top_math = (name, grades) 
    elif grades["Matematika"] > top_math[1]["Matematika"]:
        top_math = (name, grades)
print(top_math[0], top_math[1])

top_physic = None

for name, grades in students.items():
    if top_physic is None:
        top_physic = (name, grades) 
    elif grades["Fizika"] > top_physic[1]["Fizika"]:
        top_physic = (name, grades)
print(top_physic[0], top_physic[1])

top_english = None

for name, grades in students.items():
    if top_english is None:
        top_english = (name, grades) 
    elif grades["Ingliz tili"] > top_english[1]["Ingliz tili"]:
        top_english = (name, grades)
print(top_english[0], top_physic[1])
