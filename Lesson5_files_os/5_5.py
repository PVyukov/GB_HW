list_numbers = [2, 0, 212, 1, 0]
with open('5_5_out_data', 'w') as f:
    new_str = ' '.join(map(str, list_numbers))
    # new_str = ' '.join(str(i) for i in list_numbers)
    f.write(new_str)

with open('5_5_out_data') as f:
    my_list = f.readline().split(' ')
    my_list = [int(x) for x in my_list]
    print(sum(my_list))
