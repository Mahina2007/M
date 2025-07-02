import json
# datani jsonga o'girish
# data = {'name': 'ali', 'age': 12, 'grade': 4.5, 'is_male': True, 'hobby': None}
# print(json.dumps(data))

# datani jsondan filega o'girish
# json_data = '{"name": "ali", "age": 12, "grade": 4.5, "is_male": true, "hobby": null}'
# print(json.loads(json_data))

# dump(data, file, indent=(joy tashash) -> datani json file qilib yozish
data = {'name': 'ali', 'age': 12, 'grade': 4.5, 'is_male': True, 'hobby': None,
        "data": {
            "a": 1
        }}
with open(file="data.json", mode="w") as file:
    json.dump(data, file, indent=4)

# load-datani json filedan terminalda o'qish
# with open(file="data.json", mode="r") as file:
#     data = json.load(file)
#     print(data)

# r+: read and append
# w+: write and read
# a+ : append and read
# x+: create, append, write
