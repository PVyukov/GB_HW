# def mu_func(x, y):
#     a = x
#     for i in range(abs(y)-1):
#         a *= x
#     if y < 0:
#         return 1/a
#     elif y > 0:
#         return a
#     else:
#         return 1


def mu_func(x, y):
    a_multiply = x
    a_power = x
    for i in range(abs(y) - 1):
        for j in range(x - 1):
            a_power += a_multiply
        a_multiply = a_power
    if y < 0:
        return 1 / a_power
    elif y > 0:
        return a_power
    else:
        return 1


print(mu_func(3, 3))
print(3 ** 3)


