def positiv(num):
    if num > 0:
        return True
    else:
        False

num_list = [1, 2, 3, 4, 5, -1, -2, 0, 9, -4, 0, 1, -1]

no_0_list = list(filter(positiv, num_list))
print(no_0_list)