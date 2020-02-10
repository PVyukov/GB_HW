with open('data_for_parsing.txt', encoding='utf-8') as f:
    str_cnt = 0
    word_cnt = 0
    for i in f:
        str_cnt += 1
        word_cnt += len(i.split(' '))

print('Total strings are {}, total words are {}'.format(str_cnt, word_cnt))
