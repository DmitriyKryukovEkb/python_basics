from functools import reduce


def multiplication_for_list(a, b):
    return a * b


list_1 = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multiplication_for_list, list_1))
