# 1
# def square_numbers(n):
#     for num in range(1, n+1):
#         yield num**2
#
# for num in square_numbers(10):
#     print(num)

# 2
# class ReverseString:
#     def __init__(self, txt: str):
#         self.txt = txt
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         reversed_text = ''
#         iterator = iter(self.txt)
#         for char in reversed(list(iterator)):
#             reversed_text += char
#         return reversed_text
#
# txt = "salom"
# teskari_txt = ReverseString(txt)
# print(teskari_txt.__next__())
