names = []
while True:
    print(names)
    name = input("name: ")
    names.append(name)
    if name.lower() == "break":
        break
    elif name not in names:
        names.append(name)
        pass
    else:
        
