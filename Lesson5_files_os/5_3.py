with open('5_3_in_data', encoding='utf-8') as f:
    cnt = 0
    sum_salary = 0
    for i in f:
        cnt += 1
        my_str = i.strip().split(' ')
        name = my_str[0]
        salary = float(my_str[1])
        sum_salary += salary
        if salary > 20000:
            print(name)

print("Average salary: {:.2f}".format(sum_salary/cnt))
