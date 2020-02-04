def first_letter_up(word):
    """"will change first letter in word"""
    word_list = list(word)
    first_letter_int = ord(word_list[0])
    if first_letter_int < 97:
        first_letter_int += 32
    else:
        first_letter_int -= 32
    word_list[0] = chr(first_letter_int)
    return ''.join(word_list)


def first_letter_string(my_str):
    """"will change first letter in every word"""
    my_str_list = my_str.split()
    my_str_list = map(first_letter_up, my_str_list)
    return ' '.join(my_str_list)


new_str = input('Input sting: ')
print(f'Your init str is: \t\t"{new_str}"')
print(f'Your updated str is: \t"{first_letter_string(new_str)}"')

