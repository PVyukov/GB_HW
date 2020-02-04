my_sum = 0
flag = True
while flag:
    a = input('Enter numbers(Pres "F" to finish): ')
    my_list = a.split()
    if 'F' in my_list:
        flag = False
        my_list.remove('F')
    my_sum += sum(map(int, my_list))
    print(my_sum)




