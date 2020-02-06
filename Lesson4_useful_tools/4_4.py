def exclude_el(tmp_list, i):
    new_list = tmp_list[:]
    new_list.pop(i)
    return new_list


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [my_list[i] for i in range(len(my_list)) if not my_list[i] in exclude_el(my_list, i)]

print(result)




