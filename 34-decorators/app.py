# import time
#
# def get_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         value = func(*args, **kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#         return value
#     return wrapper
#
# @get_time
# def add(a, b):
#     return a + b
# print(add(1, 2))

def my_outer_decorator(num: int):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num - 1):
                print(func(*args, **kwargs))
            return func(*args, **kwargs)
        return wrapper
    return my_decorator


@my_outer_decorator(5)
def add(a, b):
    return a + b

print(add(1, 2))


