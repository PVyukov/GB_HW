def mu_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


print(mu_func(3, 3, 9))