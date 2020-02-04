my_list = [7, 5, 3, 3, 2]
number = int(input('Enter number: '))
index = 0
print('Init list: {}'.format(my_list))

while index < len(my_list):
    if number > my_list[index]:
        my_list.insert(index, number)
        break
    index += 1
else:
    my_list.append(number)

print('New list: ', my_list)
