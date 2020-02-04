# 1-st var of list initialisation
var_list = input("Enter numbers separated by ',':")
var_list = var_list.split(',')
print(f'Init list: {var_list}')

# 2-nd var of list initialisation
# var_list = []
# while True:
#     var = input('Enter number (if you finished just pres "Enter" without number): ')
#     if var:
#         var_list.append(int(var))
#     else:
#         break
# print(f'Init list: {var_list}')


index = 0
new_list = []
try:
    while index < len(var_list):
        new_list.append(var_list[index + 1])
        new_list.append(var_list[index])
        index += 2
except IndexError:
    new_list.append(var_list[index])
#
print(f'New list: {new_list}')
