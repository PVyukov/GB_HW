from functools import reduce


def power(a, b):
    return a * b


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(power, my_list))
