# 1
def square_numbers(n):
    for num in range(0, n+1):
        yield num**2

for num in square_numbers(10):
    print(num)

# 2
class ReverseString:
    def __init__(self, txt: str):
        self.txt = txt


    def __iter__(self):
        return self

    def __next__(self):
        for


my_string = "hello"