my_keys = ('название', 'цена', 'количество', 'eд')

# test data
# goods = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'})
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
# print(goods)

# Init goods
goods = []
dic = {}
gods_number = int(input('Enter number of goods: '))
for i in range(gods_number):
    for my_key in my_keys:
        dic[my_key] = input(f'Введите {my_key} {i+1}-го элемента: ')
    goods.append((i+1, dic))
    dic = {}
print(goods)

# Processing goods
analytics = {}
my_list = []
for my_key in my_keys:
    for good in goods:
        my_list.append(good[1][my_key])
    analytics[my_key] = my_list
    my_list = []
print(analytics)
