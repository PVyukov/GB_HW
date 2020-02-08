new_list = []
with open('5_4_in_data', encoding='utf-8') as f:
    conv_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for i in f:
        numeric = i.split(' ')[0]
        line = i.replace(numeric, conv_dic[numeric])
        new_list.extend(line)
with open('5_4_out_data', 'w',  encoding='utf-8') as f:
    f.writelines(new_list)



