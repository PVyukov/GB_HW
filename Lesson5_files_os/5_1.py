data = input('Enter string: ').split()
with open('5_1_out_data', 'w') as f:
    for i in data:
        print(f'{i}', file=f)
        # f.write(i)



