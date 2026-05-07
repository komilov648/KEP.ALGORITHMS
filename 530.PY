def map(func, sequence):
    new_lst = []
    for n in sequence:
        new_lst.append(func(n))

    return new_lst
print(list(map(lambda x: x + 2, [-5, 0, 5, ]))) # [ -3, 2, 7]
print(list(map(lambda y: y % 3, [-5, 5, 8, 6,]))) # [1, 2, 2, 0]