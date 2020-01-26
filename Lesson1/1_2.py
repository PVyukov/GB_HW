time = int(input('Enter time in second:'))
minutes, seconds = time // 60, time % 60
hours, minutes = minutes // 60, minutes % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
