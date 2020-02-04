string = input('Enter string:')
cnt = 0
for word_full in string.split():
    cnt += 1
    word = word_full[:10]
    print(f'{cnt}: {word}')
