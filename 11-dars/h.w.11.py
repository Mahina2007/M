cars = []

while input("do u want to buy a car? ").startswith("ye"):
    
    brand = input("what's ur desired brand? ")
    color = input("what's ur desired color? ")
    price = input("what's ur desired price? ")
    year = int(input("what's ur desired year? "))
    car = (brand, color, price, year)
    cars.append(car)
    
else:
    if input("do u want to see ur future car(s)? ").startswith("ye"):
        for car in cars:
            print(car)
    else:
        print("come back again")